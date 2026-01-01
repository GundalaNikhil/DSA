---
problem_id: ARR_SHUTTLE_SHIFT_BLACKOUT__2845
display_id: ARR-003
slug: shuttle-shift-blackout
title: "Shuttle Shift With Blackout"
difficulty: Easy-Medium
difficulty_score: 32
topics:
  - Arrays
  - Rotation
  - Simulation
tags:
  - arrays
  - rotation
  - simulation
  - easy-medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# ARR-003: Shuttle Shift With Blackout

## Problem Statement

Rotate the array to the left by k positions, but indices listed in the blackout
set must stay fixed. Only the elements at non-blackout indices rotate among
themselves in order.

![Problem Illustration](../images/ARR-003/problem-illustration.png)

## Input Format

- First line: integer n
- Second line: n space-separated integers arr[i]
- Third line: integer k
- Fourth line: integer b, the number of blackout indices
- Fifth line: b space-separated indices (0-based); if b = 0, this line is omitted

## Output Format

Print the resulting array, space-separated.

## Constraints

- `1 <= n <= 200000`
- `0 <= k <= 1000000000`
- `0 <= b <= n`
- `Blackout indices are in range 0..n-1`

## Example

**Input:**
```
5
1 2 3 4 5
2
2
1 3
```

**Output:**
```
3 2 5 4 1
```

**Explanation:**

Indices 1 and 3 stay fixed (values 2 and 4). The remaining elements [1, 3, 5]
rotate left by 2 to [5, 1, 3], yielding [3, 2, 5, 4, 1].

![Example Visualization](../images/ARR-003/example-1.png)

## Notes

- If there are no movable indices, the array is unchanged.
- Use k % movable_count to avoid full rotations.

## Related Topics

Arrays, Rotation, Simulation

---

## Solution Template

### Java



### Python



### C++



### JavaScript


