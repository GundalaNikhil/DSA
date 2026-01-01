---
problem_id: ARR_PREFIX_AVG__4252
display_id: ARR-001
slug: snack-restock-snapshot
title: "Snack Restock Snapshot"
difficulty: Easy
difficulty_score: 18
topics:
  - Arrays
  - Prefix Sum
  - Math
tags:
  - arrays
  - prefix-sum
  - math
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-001: Snack Restock Snapshot

## Problem Statement

You are given an array of daily deliveries. For each day i, compute the average of all deliveries from day 0 to day i (inclusive), rounded down to an integer. 
Return the list of prefix averages in order.

![Problem Illustration](../images/ARR-001/problem-illustration.png)

## Input Format

- First line: integer n, the number of days
- Second line: n space-separated integers arr[i]

## Output Format

Print n integers: the prefix averages, in order, space-separated.

## Constraints

- `1 <= n <= 100000`
- `0 <= arr[i] <= 1000000`

## Example

**Input:**
```
4
4 6 6 0
```

**Output:**
```
4 5 5 4
```

**Explanation:**

Running sums are 4, 10, 16, 16. Dividing by 1, 2, 3, 4 and rounding down gives
4, 5, 5, 4.

![Example Visualization](../images/ARR-001/example-1.png)

## Notes

- Use 64-bit arithmetic for the running sum.
- Output values are integers using floor division.

## Related Topics

Arrays, Prefix Sum, Math

---

## Solution Template

### Java



### Python



### C++



### JavaScript


