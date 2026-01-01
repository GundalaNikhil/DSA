---
problem_id: STC_Z_FUNCTION__9307
display_id: STC-003
slug: z-function
title: "Z-Function Construction"
difficulty: Easy
difficulty_score: 24
topics:
  - Strings
  - Z-Algorithm
  - Prefix Matching
tags:
  - strings
  - z-function
  - prefix
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-003: Z-Function Construction

## Problem Statement

Given a string `s`, compute its Z-array. `Z[i]` is the length of the longest substring starting at `i` that matches the prefix of `s`. By convention, `Z[0] = |s|`.

![Problem Illustration](../images/STC-003/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single line: `n` integers `Z[0..n-1]`, space-separated

## Constraints

- `1 <= |s| <= 200000`
- `s` contains lowercase English letters

## Example

**Input:**

```
aabxaabx
```

**Output:**

```
8 1 0 0 4 1 0 0
```

**Explanation:**

The prefix matches at positions 1 and 4 with lengths 1 and 4.

![Example Visualization](../images/STC-003/example-1.png)

## Notes

- Use the linear Z-algorithm
- Maintain a window [l, r] of the current Z-box
- Time complexity: O(n)
- Space complexity: O(n)

## Related Topics

Z-Algorithm, String Matching, Prefixes

---

## Solution Template
### Java


### Python


### C++


### JavaScript

