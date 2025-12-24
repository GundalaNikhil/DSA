# Greedy Problems Directory

Place problem statement files here following the format:

**Filename:** `GRD-XXX-[slug].md`

**Example:** `GRD-001-activity-selection.md`

## Required Frontmatter

```yaml
---
problem_id: GRD_[DESCRIPTION_CAPS]__[4_DIGITS]
display_id: GRD-XXX
slug: [kebab-case]
title: "[Problem Title]"
difficulty: [Easy|Medium|Hard]
difficulty_score: [10-90]
topics:
  - Greedy
  - [Secondary Topic]
tags:
  - greedy
  - [additional-tags]
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
```

## Structure Requirements

- 150-250 lines total
- 1 example only
- All 4 language templates (Java, Python, C++, JavaScript)
- Clear constraints
- Image references
- Notes section

See `UNIVERSAL_DSA_GENERATION_PROMPT.md` for complete template.
