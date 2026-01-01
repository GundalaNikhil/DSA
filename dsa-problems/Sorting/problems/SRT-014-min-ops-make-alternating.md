---
problem_id: SRT_MIN_OPS_MAKE_ALTERNATING__4621
display_id: SRT-014
slug: min-ops-make-alternating
title: "Minimum Operations to Make Array Alternating"
difficulty: Medium
difficulty_score: 51
topics:
  - Sorting
  - Counting
  - Greedy
tags:
  - counting
  - greedy
  - arrays
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# SRT-014: Minimum Operations to Make Array Alternating

## Problem Statement

You want the array to alternate between two distinct values `x` and `y`, i.e., `x, y, x, y, ...` or `y, x, y, x, ...`. You may change any element to any value.

Compute the minimum number of changes required.

![Problem Illustration](../images/SRT-014/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers

## Output Format

- Single integer: minimum changes to make the array alternating

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
4
1 1 1 2
```

**Output:**

```
1
```

**Explanation:**

Change the second element to 2 to get `[1,2,1,2]`.

![Example Visualization](../images/SRT-014/example-1.png)

## Notes

- Count frequencies separately on even and odd indices
- Choose the best pair of values to maximize already-correct positions
- `x` and `y` must be different
- Time complexity: O(n)

## Related Topics

Greedy, Frequency Counting, Arrays

---

## Solution Template
### Java


### Python


### C++


### JavaScript

