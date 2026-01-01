---
problem_id: SRT_LOCATE_PEAK_LIMITED_QUERIES__1358
display_id: SRT-016
slug: locate-peak-limited-queries
title: "Locate Peak with Limited Queries"
difficulty: Medium
difficulty_score: 55
topics:
  - Searching
  - Binary Search
  - Peaks
tags:
  - binary-search
  - peak
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-016: Locate Peak with Limited Queries

## Problem Statement

An array has at least one peak (an index `i` such that `a[i] > a[i-1]` and `a[i] > a[i+1]`, when neighbors exist). You may query array values by index at most `q` times. Devise a strategy that finds any peak index within the query budget.

For this task, the full array is given as input, but your algorithm should still respect the query limit conceptually.

![Problem Illustration](../images/SRT-016/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers

## Output Format

- Single integer: an index of a peak

## Constraints

- `1 <= n <= 100000`
- `1 <= q <= 20`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
5 5
1 3 2 4 1
```

**Output:**

```
1
```

**Explanation:**

Index 1 is a peak since 3 is greater than its neighbors 1 and 2.

![Example Visualization](../images/SRT-016/example-1.png)

## Notes

- A binary-search-like strategy finds a peak in O(log n) queries
- Any valid peak index is acceptable
- Peaks can exist at boundaries if they are greater than their only neighbor
- The query limit is a conceptual constraint

## Related Topics

Binary Search, Peak Finding, Searching

---

## Solution Template
### Java


### Python


### C++


### JavaScript

