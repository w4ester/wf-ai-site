# Accessibility & Inclusive Language Standards

This hook ensures all blog posts meet accessibility standards and use inclusive language.

## Inclusive Language Guidelines

### Family Terminology

**Use these inclusive terms:**
- "Caregivers" (most inclusive - covers all caring adults)
- "Parents, guardians, and caregivers" (when you want to be explicit)
- "Caring adults" or "trusted adults"
- "Families" (includes all family structures)
- "Grown-ups" (casual contexts)

**Instead of:**
- "Parents" alone (excludes grandparents raising grandchildren, foster families, kinship care, etc.)
- "Mom and Dad" (excludes single parents, same-sex parents, non-binary parents)
- "Your parents" (assumes traditional family structure)

**Why this matters:**
- 2.7 million children in the US are raised by grandparents or other relatives ([kinship care](https://cwig-prod-prod-drupal-s3fs-us-east-1.s3.amazonaws.com/public/documents/f_kinshi.pdf))
- 400,000+ children are in foster care
- Many children have guardians, step-parents, or "fictive kin" (chosen family)
- Research shows inclusive language helps children feel seen and included

### Young People Terminology

**Preferred:**
- "Young people" (respectful, acknowledges agency)
- "Children" (appropriate for younger ages)
- "Kids" (casual, friendly)
- "Students" (educational contexts)
- "Youth" (formal contexts)

**Avoid:**
- Diminishing language that removes agency
- Assuming all children have the same family structure

---

## Accessibility Standards (WCAG 2.2 Level AA)

### Heading Structure

- Use proper heading hierarchy: H1 → H2 → H3 (never skip levels)
- One H1 per page (the title)
- Headings should describe content, not just look nice
- Screen readers use headings for navigation

### Plain Language

**Target: 5th-8th grade reading level** (helps everyone, required for accessibility)

- Use short sentences (under 25 words when possible)
- Use short paragraphs (3-4 sentences max)
- Avoid jargon; if you must use it, define it
- Avoid idioms and metaphors (challenging for neurodivergent readers and non-native speakers)
- Left-align text (no justified text - creates irregular spacing)

### Diagrams and ASCII Art

**All ASCII diagrams need a text description** for screen reader users.

Format:
```markdown
<!-- Diagram: [Brief title] -->
<!-- Description: [What the diagram shows in plain text] -->
```

Example:
```markdown
<!-- Diagram: Trust Layers -->
<!-- Description: A hierarchy showing trust from highest to lowest:
     1. Home (full trust), 2. Your infrastructure (high trust),
     3. Open source (medium trust), 4. Companies with aligned incentives (lower trust),
     5. Companies with misaligned incentives (no trust) -->
```

### Links

- Use descriptive link text (not "click here")
- Good: "Read the [WCAG guidelines](url)"
- Bad: "[Click here](url) to read the guidelines"

### Color and Contrast

- Don't convey information by color alone
- Ensure sufficient contrast (4.5:1 for normal text)
- Our dark theme should handle this, but check any custom colors

### Lists and Structure

- Use actual list markup (-, *, 1.) not just visual formatting
- Break up long content with headings
- Use bullet points for scannable information

---

## Neurodivergent-Friendly Content

These practices help readers with ADHD, autism, dyslexia, and other conditions:

1. **Clear structure** - Predictable layout, consistent formatting
2. **Scannable content** - Headings, bullets, bold key points
3. **Plain language** - Avoid figurative language and idioms
4. **Whitespace** - Don't crowd the page
5. **Consistent navigation** - Same structure across posts

**Avoid:**
- Walls of text
- Justified text alignment
- Overly decorative fonts
- Flashing or auto-playing media
- Unexpected popups or changes

---

## Pre-Publish Checklist

Before publishing any post, verify:

### Inclusive Language
- [ ] "Parents" → "Caregivers" or "parents, guardians, and caregivers"
- [ ] Family diversity acknowledged
- [ ] No assumptions about family structure
- [ ] Young people referred to respectfully

### Accessibility
- [ ] Heading hierarchy is correct (H1 → H2 → H3)
- [ ] All diagrams have text descriptions
- [ ] Links have descriptive text
- [ ] Reading level is appropriate (5th-8th grade target)
- [ ] Short paragraphs (3-4 sentences)
- [ ] Lists use proper markup

### Neurodivergent-Friendly
- [ ] Clear structure and formatting
- [ ] No idioms without explanation
- [ ] Scannable with headings and bullets
- [ ] No walls of text

---

## Resources

### Inclusive Language
- [APA Inclusive Language Guide](https://www.apa.org/about/apa/equity-diversity-inclusion/language-guidelines)
- [Coalition for Diversity: Family and Relationship Status](https://c4disc.pubpub.org/pub/v176q7xc)
- [IES: Inclusive Language for Kinship Caregivers](https://ies.ed.gov/rel-appalachia/2025/01/handout-inclusive-language-caregivers)

### Accessibility
- [W3C WCAG 2.2](https://www.w3.org/WAI/standards-guidelines/wcag/)
- [WebAIM WCAG Checklist](https://webaim.org/standards/wcag/checklist)
- [W3C Accessibility Statement Generator](https://www.w3.org/WAI/planning/statements/)

### Neurodiversity
- [Intuit: Readability Guidelines](https://contentdesign.intuit.com/accessibility-and-inclusion/readability/)
- [Design for Neurodiversity](https://adchitects.co/blog/design-for-neurodiversity)
- [WCAG and Neurodiversity](https://www.wcag.com/blog/digital-accessibility-and-neurodiversity/)

---

*This guide is a living document. Update as we learn more.*
