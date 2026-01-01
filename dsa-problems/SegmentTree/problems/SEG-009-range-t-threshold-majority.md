---
problem_id: SEG_RANGE_T_THRESHOLD_MAJORITY__7412
display_id: SEG-009
slug: range-t-threshold-majority
title: "Range T-Threshold Majority Check"
difficulty: Medium
difficulty_score: 62
topics:
  - Segment Tree
  - Frequency Counting
  - Range Queries
tags:
  - segment-tree
  - frequency
  - range-query
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SEG-009: Range T-Threshold Majority Check

## Problem Statement

Given an array `a`, answer queries `MAJ l r T`: determine whether there exists a value that appears at least `T` times in the subarray `a[l..r]`.

If such a value exists, output the value with the highest frequency; if multiple have the same frequency, output the smallest value. Otherwise output `-1`.

![Problem Illustration](../images/SEG-009/problem-illustration.png)

## Input Format

- First line: integers `n` and `q`
- Second line: `n` space-separated integers
- Next `q` lines: `MAJ l r T`

## Output Format

- For each query, print the selected value or `-1`

## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i] <= 10^9`
- `1 <= T <= r - l + 1`

## Example

**Input:**

```
5 1
1 1 2 3 1
MAJ 0 4 3
```

**Output:**

```
1
```

**Explanation:**

Value 1 appears 3 times in the range, meeting the threshold.

![Example Visualization](../images/SEG-009/example-1.png)

## Notes

- Store a small candidate frequency map per segment
- Merge nodes by keeping top candidates only
- Verify the candidate frequency in the query range
- Time complexity is around O(log n * K)

## Related Topics

Segment Tree, Majority, Range Queries

---

## Solution Template
### Java


### Python


### C++


### JavaScript

