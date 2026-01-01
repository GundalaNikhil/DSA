---
problem_id: SRT_SEARCH_ROTATED_DUPLICATES_PARITY__9062
display_id: SRT-007
slug: search-rotated-duplicates-parity
title: "Search Rotated With Duplicates Parity Count"
difficulty: Medium
difficulty_score: 52
topics:
  - Sorting
  - Binary Search
  - Rotated Arrays
tags:
  - binary-search
  - rotated-array
  - duplicates
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-007: Search Rotated With Duplicates Parity Count

## Problem Statement

Given a rotated sorted array that may contain duplicates, count how many occurrences of a value `x` appear at even indices.

Indices are 0-based.

![Problem Illustration](../images/SRT-007/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers
- Third line: integer `x`

## Output Format

- Single integer: count of occurrences of `x` at even indices

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i], x <= 10^9`

## Example

**Input:**

```
6
4 5 5 1 2 3
5
```

**Output:**

```
1
```

**Explanation:**

Value 5 appears at indices 1 and 2; only index 2 is even.

![Example Visualization](../images/SRT-007/example-1.png)

## Notes

- Find the rotation pivot to map to a sorted order
- Use binary search to locate the range of `x`
- Count how many indices in the occurrence range are even
- Time complexity: O(log n)

## Related Topics

Binary Search, Rotated Array, Counting

---

## Solution Template
### Java


### Python


### C++


### JavaScript

