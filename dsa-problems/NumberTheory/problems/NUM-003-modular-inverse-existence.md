---
problem_id: NUM_MODULAR_INVERSE_EXISTENCE__3507
display_id: NUM-003
slug: modular-inverse-existence
title: "Modular Inverse Existence"
difficulty: Easy
difficulty_score: 22
topics:
  - Number Theory
  - GCD
  - Modular Arithmetic
tags:
  - number-theory
  - gcd
  - modular
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-003: Modular Inverse Existence

## Problem Statement

For each query `(a, m)`, determine whether `a` has a modular inverse modulo `m`. An inverse exists if and only if `gcd(a, m) = 1`.

![Problem Illustration](../images/NUM-003/problem-illustration.png)

## Input Format

- First line: integer `q`
- Next `q` lines: two integers `a` and `m`

## Output Format

- For each query, print `true` if an inverse exists, otherwise `false`

## Constraints

- `1 <= q <= 100000`
- `1 <= a, m <= 10^9`

## Example

**Input:**

```
1
4 7
```

**Output:**

```
true
```

**Explanation:**

`gcd(4, 7) = 1`, so the inverse exists.

![Example Visualization](../images/NUM-003/example-1.png)

## Notes

- Use the Euclidean algorithm for gcd
- Time complexity: O(q log max(a,m))
- Space complexity: O(1)

## Related Topics

Modular Arithmetic, GCD, Euclid Algorithm

---

## Solution Template

### Java


### Python


### C++


### JavaScript

