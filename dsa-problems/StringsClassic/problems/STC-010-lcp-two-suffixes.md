---
problem_id: STC_LCP_TWO_SUFFIXES__5381
display_id: STC-010
slug: lcp-two-suffixes
title: "Longest Common Prefix of Two Suffixes"
difficulty: Medium
difficulty_score: 52
topics:
  - Strings
  - Suffix Array
  - RMQ
tags:
  - strings
  - suffix-array
  - lcp
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-010: Longest Common Prefix of Two Suffixes

## Problem Statement

You are given a string `s`. For each query `(i, j)`, return the length of the longest common prefix of the two suffixes `s[i..]` and `s[j..]`.

You must preprocess once and answer all queries efficiently.

![Problem Illustration](../images/STC-010/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: integer `q`, the number of queries
- Next `q` lines: two integers `i` and `j` (0-based indices)

## Output Format

- Print `q` lines, each the LCP length for the corresponding query

## Constraints

- `1 <= |s| <= 100000`
- `1 <= q <= 100000`
- `0 <= i, j < |s|`
- `s` contains lowercase English letters

## Example

**Input:**

```
banana
2
1 3
0 2
```

**Output:**

```
3
0
```

**Explanation:**

Suffix at 1 is "anana" and suffix at 3 is "ana". Their LCP is "ana" with length 3.
Suffix at 0 is "banana" and suffix at 2 is "nana". Their LCP length is 0.

![Example Visualization](../images/STC-010/example-1.png)

## Notes

- Build a suffix array and the LCP array.
- LCP of suffixes at positions `i` and `j` is the minimum LCP between their ranks.
- Use RMQ (sparse table or segment tree) over the LCP array.
- Each query can be answered in O(1) or O(log n) after preprocessing.

## Related Topics

Suffix Array, LCP, RMQ

---

## Solution Template

### Java


### Python


### C++


### JavaScript

