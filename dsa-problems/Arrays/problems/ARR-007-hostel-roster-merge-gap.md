---
problem_id: ARR_MERGE_PRIORITY_TIE__6153
display_id: ARR-007
slug: hostel-roster-merge-gap
title: "Hostel Roster Merge With Gap"
difficulty: Medium
difficulty_score: 42
topics:
  - Arrays
  - Two Pointers
  - Merge
tags:
  - arrays
  - two-pointers
  - merge
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-007: Hostel Roster Merge With Gap

## Problem Statement

Merge two sorted arrays A and B into a single sorted array. If two equal elements appear from different arrays, place the element from A before the one from B.

![Problem Illustration](../images/ARR-007/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers A[i]
- Third line: integer m
- Fourth line: m space-separated integers B[i]

## Output Format

Print the merged array, space-separated.

## Constraints

- `0 <= n, m <= 100000`
- `-1000000000 <= A[i], B[i] <= 1000000000`

## Example

**Input:**

```
3
1 3 3
2
3 4
```

**Output:**

```
1 3 3 3 4
```

**Explanation:**

On ties, elements from A are placed before elements from B.

![Example Visualization](../images/ARR-007/example-1.png)

## Notes

- This is a stable merge with a tie-breaker for A.
- If one array is empty, return the other.

## Related Topics

Arrays, Two Pointers, Merge

---

## Solution Template

### Java


### Python


### C++


### JavaScript

