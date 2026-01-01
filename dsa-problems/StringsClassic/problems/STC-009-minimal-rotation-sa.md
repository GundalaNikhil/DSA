---
problem_id: STC_MINIMAL_ROTATION_SA__6042
display_id: STC-009
slug: minimal-rotation-sa
title: "Lexicographically Minimal Rotation (SA)"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
  - Suffix Array
  - Rotation
tags:
  - strings
  - suffix-array
  - rotation
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-009: Lexicographically Minimal Rotation (SA)

## Problem Statement

Given a string `s`, consider all its cyclic rotations. Return the starting index (0-based) of the lexicographically smallest rotation. If multiple rotations are identical, return the smallest index.

![Problem Illustration](../images/STC-009/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single integer: index of the minimal rotation

## Constraints

- `1 <= |s| <= 100000`
- `s` contains lowercase English letters

## Example

**Input:**

```
bba
```

**Output:**

```
2
```

**Explanation:**

Rotations: index 0 -> "bba", index 1 -> "bab", index 2 -> "abb". The smallest is "abb" at index 2.

![Example Visualization](../images/STC-009/example-1.png)

## Notes

- Build suffix array for `s + s`
- The first suffix with start < n gives the answer
- Time complexity: O(n log n)
- Space complexity: O(n)

## Related Topics

Suffix Array, Rotations, String Algorithms

---

## Solution Template
### Java


### Python


### C++


### JavaScript

