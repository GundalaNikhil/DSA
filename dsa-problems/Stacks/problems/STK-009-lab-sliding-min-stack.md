---
problem_id: STK_LAB_SLIDING_MIN_STACK__5027
display_id: STK-009
slug: lab-sliding-min-stack
title: "Lab Sliding-Min Stack"
difficulty: Medium
difficulty_score: 52
topics:
  - Stack
  - Range Minimum
  - Data Structures
tags:
  - stack
  - min-stack
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-009: Lab Sliding-Min Stack

## Problem Statement

Maintain a stack with operations:

- `PUSH x`
- `POP`: remove and output top value
- `MIN k`: output the minimum among the top `k` elements (top counts as 1)

If `POP` is called on an empty stack, output `EMPTY`. If `MIN k` is requested with fewer than `k` elements, output `NA`.

![Problem Illustration](../images/STK-009/problem-illustration.png)

## Input Format

- First line: integer `m`
- Next `m` lines: commands as above

## Output Format

- For each `POP` and `MIN`, output one line with the result

## Constraints

- `1 <= m <= 100000`
- `-10^9 <= x <= 10^9`
- `1 <= k <= 100000`

## Example

**Input:**

```
6
PUSH 5
PUSH 1
PUSH 3
MIN 2
POP
MIN 2
```

**Output:**

```
1
3
1
```

**Explanation:**

Top 2 elements are [1,3], min is 1. POP removes 3. Top 2 are [5,1], min is 1.

![Example Visualization](../images/STK-009/example-1.png)

## Notes

- Store prefix mins to answer `MIN` quickly
- Use an auxiliary stack of minimums with counts
- Keep size to validate `MIN k`
- Time complexity per operation: O(1) amortized

## Related Topics

Stack, Min Stack, Range Queries

---

## Solution Template
### Java


### Python


### C++


### JavaScript

