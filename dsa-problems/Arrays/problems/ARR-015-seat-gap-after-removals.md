---
problem_id: ARR_SEAT_GAP_REMOVALS__6037
display_id: ARR-015
slug: seat-gap-after-removals
title: "Seat Gap After Removals"
difficulty: Medium
difficulty_score: 33
topics:
  - Arrays
  - Simulation
  - Greedy
tags:
  - arrays
  - simulation
  - greedy
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-015: Seat Gap After Removals

## Problem Statement

You are given sorted seat positions and a list of indices to remove (indices refer to the original array). After removals, compute the maximum gap between remaining consecutive seats.

![Problem Illustration](../images/ARR-015/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers seats[i] (sorted)
- Third line: integer r, the number of removals
- Fourth line: r space-separated indices to remove

## Output Format

Print the maximum gap between remaining consecutive seats.

## Constraints

- `2 <= n <= 200000`
- `0 <= seats[i] <= 1000000000`
- `1 <= r <= n - 2`

## Example

**Input:**
```
4
2 5 9 10
1
1
```

**Output:**
```
7
```

**Explanation:**

Seat at index 1 (value 5) is removed. Remaining seats are [2, 9, 10], so the
maximum gap is 7.

![Example Visualization](../images/ARR-015/example-1.png)

## Notes

- Removal indices refer to the original array positions.
- At least two seats remain after removals.

## Related Topics

Simulation, Greedy, Arrays

---

## Solution Template

### Java



### Python



### C++



### JavaScript


