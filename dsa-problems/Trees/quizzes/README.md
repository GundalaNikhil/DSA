# Trees Quizzes Directory

Place quiz YAML files here following the format:

**Filename:** `TRE-XXX-[slug].yaml`

**Example:** `TRE-001-binary-tree-inorder.yaml`

## Required Structure

```yaml
---
problem_id: TRE_[DESCRIPTION_CAPS]__[4_DIGITS]
display_id: TRE-XXX
slug: [kebab-case]
title: "[Problem Title] - Quiz"
---

# Problem-Related Questions (PRQ)

problem_questions:
  - quiz_id: "PRQ-XXX-Q001"
    category: "problem"
    type: single_choice
    question: "[Question]"
    options:
      - option_id: "A"
        text: "[Option A]"
        correct: false
      - option_id: "B"
        text: "[Option B]"
        correct: true
      - option_id: "C"
        text: "[Option C]"
        correct: false
      - option_id: "D"
        text: "[Option D]"
        correct: false
    explanation: "[Why correct]"
    difficulty: easy
    points: 10

# Editorial/Algorithm Questions (EDQ)

editorial_questions:
  - quiz_id: "EDQ-XXX-Q001"
    category: "editorial"
    type: single_choice
    question: "[Question]"
    options:
      - option_id: "A"
        text: "[Option A]"
        correct: true
      - option_id: "B"
        text: "[Option B]"
        correct: false
      - option_id: "C"
        text: "[Option C]"
        correct: false
      - option_id: "D"
        text: "[Option D]"
        correct: false
    explanation: "[Why correct]"
    difficulty: medium
    points: 15
```

## Requirements

- 5-7 PRQ questions
- 6-8 EDQ questions
- Types: single_choice, multiple_choice, scenario
- Difficulty: 40% easy (10pts), 40% medium (15pts), 20% hard (20pts)

See `UNIVERSAL_DSA_GENERATION_PROMPT.md` for complete template.
