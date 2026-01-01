---
problem_id: NUM_CRT_EXISTENCE_VALUE__5186
display_id: NUM-015
slug: crt-existence-value
title: "CRT Existence and Value"
difficulty: Medium
difficulty_score: 58
topics:
  - Number Theory
  - Chinese Remainder Theorem
  - GCD
tags:
  - number-theory
  - crt
  - gcd
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-015: CRT Existence and Value

## Problem Statement

You are given `k` congruences:

```
x ≡ a_i (mod m_i)
```

Determine if a solution exists. If it does, output the smallest non-negative solution. Moduli are not guaranteed to be coprime.

![Problem Illustration](../images/NUM-015/problem-illustration.png)

## Input Format

- First line: integer `k`
- Next `k` lines: two integers `a_i` and `m_i`

## Output Format

- If no solution exists, print `NO`
- Otherwise, print the smallest non-negative solution

## Constraints

- `1 <= k <= 10`
- `1 <= m_i <= 10^9`
- `0 <= a_i < m_i`

## Example

**Input:**

```
2
2 6
5 9
```

**Output:**

```
14
```

**Explanation:**

The smallest x such that x%6=2 and x%9=5 is 14.

![Example Visualization](../images/NUM-015/example-1.png)

## Notes

- Use generalized CRT with gcd checks
- Combine congruences iteratively
- Time complexity: O(k log M)
- Space complexity: O(1)

## Related Topics

CRT, Extended GCD, Number Theory

---

## Solution Template

### Java


### Python


### C++


### JavaScript

