---
problem_id: STC_DIFF_SUBSTRINGS_TWO_STRINGS__6174
display_id: STC-012
slug: diff-substrings-two-strings
title: "Number of Different Substrings of Two Strings"
difficulty: Medium
difficulty_score: 58
topics:
  - Strings
  - Suffix Array
  - Counting
tags:
  - strings
  - suffix-array
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-012: Number of Different Substrings of Two Strings

## Problem Statement

You are given two strings `a` and `b`. Count how many substrings of `a` do not appear anywhere in `b`.

Return the total number of distinct substrings of `a` that are absent from `b`.

![Problem Illustration](../images/STC-012/problem-illustration.png)

## Input Format

- First line: string `a`
- Second line: string `b`

## Output Format

- Single integer: number of distinct substrings of `a` not present in `b`

## Constraints

- `1 <= |a|, |b| <= 100000`
- `|a| + |b| <= 200000`
- Strings contain lowercase English letters

## Example

**Input:**

```
ab
b
```

**Output:**

```
2
```

**Explanation:**

Substrings of `a` are "a", "b", and "ab". Only "b" appears in `b`, so the answer is 2.

![Example Visualization](../images/STC-012/example-1.png)

## Notes

- The answer can be large; use 64-bit integers.
- With suffix array and LCP, subtract the longest overlap with `b` for each suffix of `a`.
- A suffix automaton of `b` can also provide longest matches in O(n).
- Time complexity: O(n log n) or O(n) depending on approach.

## Related Topics

Suffix Array, Suffix Automaton, Distinct Substrings

---

## Solution Template

### Java


### Python


### C++


### JavaScript

