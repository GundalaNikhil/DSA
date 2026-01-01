---
problem_id: REC_LAB_ID_PERMUTATIONS_NO_TWINS__9064
display_id: REC-002
slug: lab-id-permutations-no-twins
title: "Lab ID Permutations With No Adjacent Twins"
difficulty: Easy
difficulty_score: 30
topics:
  - Recursion
  - Backtracking
  - Strings
tags:
  - recursion
  - backtracking
  - permutations
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-002: Lab ID Permutations With No Adjacent Twins

## Problem Statement

Given a string `s` (may contain duplicate characters), generate all unique permutations such that no two identical characters are adjacent. Output permutations in lexicographic order.

![Problem Illustration](../images/REC-002/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Each valid permutation on its own line, in lexicographic order
- If no permutation exists, output `NONE`

## Constraints

- `1 <= |s| <= 8`
- `s` contains lowercase English letters

## Example

**Input:**

```
aab
```

**Output:**

```
aba
```

**Explanation:**

The permutations are `aab`, `aba`, `baa`. Only `aba` avoids adjacent identical letters.

![Example Visualization](../images/REC-002/example-1.png)

## Notes

- Sort the characters and use a visited array for lexicographic order
- Skip duplicates by checking previous identical characters
- Track the last placed character to avoid twins
- Time complexity is bounded by O(n! ) for `n <= 8`

## Related Topics

Backtracking, Permutations, Pruning

---

## Solution Template
### Java


### Python


### C++


### JavaScript

