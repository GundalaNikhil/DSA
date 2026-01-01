---
problem_id: STC_SUFFIX_ARRAY_DOUBLING__3726
display_id: STC-005
slug: suffix-array-doubling
title: "Suffix Array (Doubling) Construction"
difficulty: Medium
difficulty_score: 48
topics:
  - Strings
  - Suffix Array
  - Sorting
tags:
  - strings
  - suffix-array
  - doubling
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STC-005: Suffix Array (Doubling) Construction

## Problem Statement

Given a string `s`, build its suffix array using the O(n log n) doubling algorithm. Output the starting indices of suffixes in lexicographic order.

![Problem Illustration](../images/STC-005/problem-illustration.png)

## Input Format

- First line: string `s`

## Output Format

- Single line: `n` integers, the suffix array indices

## Constraints

- `1 <= |s| <= 100000`
- `s` contains lowercase English letters

## Example

**Input:**

```
cababa
```

**Output:**

```
5 3 1 4 2 0
```

**Explanation:**

The suffixes in order are: a, aba, ababa, ba, baba, cababa.

![Example Visualization](../images/STC-005/example-1.png)

## Notes

- Doubling sorts by pairs of ranks (2^k length)
- Use counting sort or std::sort on tuples
- Output indices are 0-based
- Time complexity: O(n log n)

## Related Topics

Suffix Array, Sorting, String Algorithms

---

## Solution Template
### Java


### Python


### C++


### JavaScript

