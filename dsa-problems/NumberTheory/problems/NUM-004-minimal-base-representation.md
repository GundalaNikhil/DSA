---
problem_id: NUM_MINIMAL_BASE_REPRESENTATION__6628
display_id: NUM-004
slug: minimal-base-representation
title: "Minimal Base Representation"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Bases
  - Optimization
tags:
  - number-theory
  - bases
  - optimization
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-004: Minimal Base Representation

## Problem Statement

Given an integer `x` (>= 2), find the smallest base `b` (2 <= b <= 36) such that the sum of digits of `x` in base `b` is minimized. If multiple bases yield the same minimal digit sum, choose the smallest base. Output `b` and the minimal digit sum.

![Problem Illustration](../images/NUM-004/problem-illustration.png)

## Input Format

- Single line: integer `x`

## Output Format

- Two integers: `b` and `digitSum`

## Constraints

- `2 <= x <= 10^12`
- `2 <= b <= 36`

## Example

**Input:**

```
31
```

**Output:**

```
5 3
```

**Explanation:**

31 in base 5 is 111, digit sum = 3. No smaller base gives a smaller digit sum.

![Example Visualization](../images/NUM-004/example-1.png)

## Notes

- Try all bases from 2 to 36
- Convert by repeated division and sum digits
- Time complexity: O(36 * log_b(x))
- Space complexity: O(1)

## Related Topics

Number Bases, Digit Sum, Search

---

## Solution Template

### Java


### Python


### C++


### JavaScript

