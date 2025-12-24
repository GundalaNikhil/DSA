# Greedy Editorials Directory

Place editorial files here following the format:

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
---
```

**Note:** NO `time_limit` or `memory_limit` in editorial frontmatter.

## Structure Requirements

- 500-750 lines total
- Emojis: 📋 🌍 ✅ 🧪 💡
- Real-world scenario (3-4 paragraphs)
- ASCII diagrams
- Naive → Optimal progression
- All 4 implementations
- Test walkthrough with table
- 3-5 Common Mistakes (❌ ✅)
- Related concepts

See `UNIVERSAL_DSA_GENERATION_PROMPT.md` for complete template.
