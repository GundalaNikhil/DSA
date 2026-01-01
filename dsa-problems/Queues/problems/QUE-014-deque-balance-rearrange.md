---
problem_id: QUE_DEQUE_BALANCE_REARRANGE__5142
display_id: QUE-014
slug: deque-balance-rearrange
title: "Deque Balance Rearrange"
difficulty: Medium
difficulty_score: 41
topics:
  - Deque
  - Two Pointers
  - Simulation
tags:
  - deque
  - two-pointers
  - rearrangement
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-014: Deque Balance Rearrange

## Problem Statement

You are given an array of values. Build a new deque by alternately taking from the front and back of the array, starting with the front. Output the deque from front to back.

For example, `[2, 4, 6, 8]` becomes `[2, 8, 4, 6]`.

![Problem Illustration](../images/QUE-014/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers

## Output Format

- Single line: deque contents from front to back, space-separated

## Constraints

- `1 <= n <= 100000`
- Values fit in 32-bit signed integer

## Example

**Input:**

```
4
2 4 6 8
```

**Output:**

```
2 8 4 6
```

**Explanation:**

Take alternately from the ends:

- Take front 2
- Take back 8
- Take front 4
- Take back 6

![Example Visualization](../images/QUE-014/example-1.png)

## Notes

- Use two pointers `l` and `r`
- Append elements to the output in the chosen order
- Time complexity: O(n)
- Space complexity: O(n) for the output

## Related Topics

Deque, Two Pointers, Simulation

---

## Solution Template

### Java


### Python


### C++


### JavaScript

