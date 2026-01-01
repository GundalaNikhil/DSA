---
problem_id: STK_CONVEYOR_WEIGHTED_DEDUPLICATION__5318
display_id: STK-003
slug: conveyor-weighted-deduplication
title: "Conveyor Weighted Deduplication"
difficulty: Easy
difficulty_score: 36
topics:
  - Stack
  - Simulation
  - Strings
tags:
  - stack
  - simulation
  - strings
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-003: Conveyor Weighted Deduplication

## Problem Statement

You are given a string `s` and an array of weights `w` of the same length. Process characters from left to right. When the current character matches the top of the stack, you may remove the pair only if the sum of their weights is even. The removed sum is added to a running total. The remaining characters form the reduced string.

Output the reduced string and the total removed weight.

![Problem Illustration](../images/STK-003/problem-illustration.png)

## Input Format

- First line: string `s`
- Second line: `n` space-separated integers `w[i]` (where `n = |s|`)

## Output Format

- First line: reduced string
- Second line: total removed weight

## Constraints

- `1 <= |s| <= 200000`
- `1 <= w[i] <= 1000`

## Example

**Input:**

```
xxyyz
1 3 2 2 5
```

**Output:**

```
xyz
4
```

**Explanation:**

The pair `y` with weights 2 and 2 is removed, contributing 4 to the total.

![Example Visualization](../images/STK-003/example-1.png)

## Notes

- Use a stack of (char, weight)
- Only adjacent equal characters can be removed
- Each character is pushed and popped at most once
- Time complexity: O(n)

## Related Topics

Stack, Simulation, String Processing

---

## Solution Template
### Java


### Python


### C++


### JavaScript

