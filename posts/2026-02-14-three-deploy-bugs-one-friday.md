---
title: "Three Deploy Bugs, One Friday: What Broke Between Local and Production"
tags: deployment, docker, devops, fastapi, nginx, lessons-learned
---

# Three Deploy Bugs, One Friday: What Broke Between Local and Production

*Everything worked locally. Then I deployed and learned three lessons about the gap between `docker compose up` and production.*

---

## Context

I'm building [AI Workshop CS](https://aiworkshop.edinfinite.com), a platform for Maryland CS educators to create AI-aligned lessons mapped to state standards. The stack is SvelteKit + FastAPI + PostgreSQL, deployed to an OrbStack VM via a custom zero-downtime deploy script.

Last week I built a feedback loop: a modal in the nav, a FastAPI endpoint with five layers of spam prevention, PII redaction (emails, phone numbers, SSNs get scrubbed before storage), and automatic BEADS issue file creation. Everything committed, frontend builds clean, local Docker test passes.

Time to ship.

## Bug 1: The Invisible File

**Symptom:** API container starts, immediately crashes. `ModuleNotFoundError: No module named 'deps'`.

**Root cause:** My deploy script syncs files to the remote box using an explicit tar file list:

```bash
tar -cf - \
    backend/Dockerfile \
    backend/main.py \
    backend/config.py \
    backend/routers/ \
    backend/services/ \
    | orb sh -c "tar -xf - -C ${REMOTE_DIR}"
```

The Dockerfile uses `COPY . .`, which grabs everything in the build context. Locally, `deps.py` is right there. But the deploy script never included it in the tar, so it never made it to the remote box.

**Fix:** Add `backend/deps.py` to the list.

**Lesson:** Explicit-include file lists are safe (no accidental secrets or `.env` files get synced), but they're also brittle. Every new file needs to be manually added. The failure mode is silent until runtime. If you use this pattern, consider a smoke test that imports your app module after deploy.

## Bug 2: Wrong Filesystem

**Symptom:** Migration script runs, `psql` reports "No such file or directory."

**Root cause:** The migration runner syncs SQL files to the host filesystem on the remote box, then runs:

```bash
docker exec ai-workshop-pgvector psql -U workshop -d ai_workshop \
    -f /home/demo/apps/ai-workshop-cs/backend/migrations/001_feedback.sql
```

The `-f` flag tells psql to read a file. But `docker exec` runs inside the container, where that host path doesn't exist. The container has its own filesystem.

**Fix:** Pipe via stdin instead:

```bash
cat /host/path/to/migration.sql | docker exec -i container psql -U user -d db
```

The `-i` flag keeps stdin open so psql can read from the pipe.

**Lesson:** `docker exec` drops you inside the container. File paths that work on the host mean nothing there. Either mount the directory as a volume, or pipe content through stdin. I chose stdin because it requires zero changes to the container configuration.

## Bug 3: The Protocol Betrayal

**Symptom:** Click "Send Feedback" on the live HTTPS site. Browser blocks the request. Console says: `Mixed Content: requested an insecure resource 'http://aiworkshop.edinfinite.com/api/feedback/'`.

**Root cause:** Three things conspired:

1. FastAPI has `redirect_slashes` enabled by default. The client sends `POST /api/feedback`, the route is `/api/feedback/`, so FastAPI returns a 307 redirect.
2. Nginx proxies to the backend over plain HTTP internally (`proxy_pass http://api:8000`). FastAPI sees an HTTP request and generates an HTTP redirect URL.
3. The browser sees an HTTPS page trying to follow an HTTP redirect and blocks it as mixed content.

The standard fix is to pass `X-Forwarded-Proto` from nginx so the backend knows the original scheme was HTTPS. But that alone wasn't enough because uvicorn's `--forwarded-allow-ips` defaults to `127.0.0.1`, and nginx's requests come from the Docker bridge network (something like `172.18.0.x`). Uvicorn sees an untrusted IP and ignores the forwarded headers entirely.

**Fix (belt and suspenders):**

```nginx
# nginx.conf
proxy_set_header X-Forwarded-Proto $scheme;
```

```dockerfile
# Dockerfile
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", \
     "--forwarded-allow-ips", "*"]
```

```javascript
// api.js - avoid the redirect entirely
fetch(`/api/feedback/`, { method: 'POST', ... })
//                   ^ trailing slash = no redirect needed
```

**Lesson:** Behind a reverse proxy, every redirect is a potential protocol mismatch. The redirect itself is invisible to users. It worked locally because there's no HTTPS in dev. Three things need to align: nginx forwarding the scheme, uvicorn trusting the source IP, and ideally your client URLs matching the canonical route to avoid redirects altogether.

## The Pattern

All three bugs share a root cause: **things that are implicit locally become explicit in production**.

- Locally, all files exist in the build context. In production, only what you sync exists.
- Locally, there's one filesystem. In production, every container has its own.
- Locally, there's no TLS termination. In production, the protocol changes between every hop.

None of these bugs showed up in `docker compose up -d` on my laptop. They only appeared when the same code hit the real deployment pipeline with a reverse proxy, a remote VM, and HTTPS.

## What's Next

The feedback loop is live. Maryland CS educators can now click "Feedback" in the nav, pick a type (suggestion, bug, question), and submit. Their message gets spam-checked, PII-scrubbed, stored in PostgreSQL, and turned into a BEADS issue file for triage. All running on a single OrbStack VM with zero-downtime deploys.

Next up: making the AI lesson agent actually generate full lesson plans from the standards crosswalk data.

---

*February 2026. Built with SvelteKit, FastAPI, and a healthy respect for production environments.*
