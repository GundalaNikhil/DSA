---
problem_id: STK_ASSEMBLY_PREVIOUS_GREATER_PARITY__6802
display_id: STK-006
slug: assembly-previous-greater-parity
title: "Assembly Previous Greater with Parity"
difficulty: Medium
difficulty_score: 46
topics:
  - Stack
  - Monotonic Stack
  - Parity
tags:
  - stack
  - monotonic
  - parity
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# STK-006: Assembly Previous Greater with Parity

## Problem Statement

For each element `a[i]`, find the nearest element to its left that is strictly greater and has opposite parity (one even, one odd). If no such element exists, output `-1` for that position.

![Problem Illustration](../images/STK-006/problem-illustration.png)

## Input Format

- First line: integer `n`
- Second line: `n` space-separated integers

## Output Format

- Single line: `n` integers, the previous greater with opposite parity or `-1`

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a[i] <= 10^9`

## Example

**Input:**

```
5
2 9 5 7 3
```

**Output:**

```
-1 2 9 9 9
```

**Explanation:**

For 9 (odd), previous greater with opposite parity is 2. For 5 (odd), previous greater even is 9.

![Example Visualization](../images/STK-006/example-1.png)

## Notes

- Maintain separate monotonic stacks for even and odd values
- Pop smaller values while searching for a greater element
- Each element is pushed and popped at most once
- Time complexity: O(n)

## Related Topics

Monotonic Stack, Parity, Previous Greater Element

---

## Solution Template
### Java


### Python


### C++


### JavaScript

