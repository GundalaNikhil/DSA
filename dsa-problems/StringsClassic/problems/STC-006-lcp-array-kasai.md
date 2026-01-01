---
problem_id: STC_LCP_ARRAY_KASAI__6109
display_id: STC-006
slug: lcp-array-kasai
title: "LCP Array (Kasai)"
difficulty: Medium
difficulty_score: 46
topics:
  - Strings
  - Suffix Array
  - LCP
tags:
  - strings
  - lcp
  - kasai
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-006: LCP Array (Kasai)

## Problem Statement

Given a string `s` and its suffix array, compute the LCP array where `lcp[i]` is the longest common prefix length of the suffixes at `sa[i]` and `sa[i+1]`.

![Problem Illustration](../images/STC-006/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `n` (length of `s`)
- Third line: `n` space-separated integers (suffix array)

## Output Format

- Single line: `n-1` integers (LCP array)

## Constraints

- `1 <= |s| <= 100000`
- `s` contains lowercase English letters

## Example

**Input:**

```
cababa
6
5 3 1 4 2 0
```

**Output:**

```
1 3 0 2 0
```

**Explanation:**

Adjacent suffix pairs share prefixes of lengths 1, 3, 0, 2, 0.

![Example Visualization](../images/STC-006/example-1.png)

## Notes

- Use Kasai's algorithm for O(n)
- Build inverse rank array from suffix array
- LCP array length is `n-1`
- Output values are 0-based lengths

## Related Topics

Kasai Algorithm, Suffix Array, LCP

---

## Solution Template
### Java


### Python


### C++


### JavaScript

