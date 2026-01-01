---
problem_id: NUM_SUM_DIVISORS_RANGE__4175
display_id: NUM-010
slug: sum-divisors-range
title: "Sum of Divisors in Range"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Divisors
  - Prefix Sums
tags:
  - number-theory
  - divisors
  - prefix
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-010: Sum of Divisors in Range

## Problem Statement

For each integer `n`, let `sigma(n)` be the sum of its positive divisors. Given `L` and `R`, compute:

```
Sigma = sum_{n=L..R} sigma(n) mod 1000000007
```

![Problem Illustration](../images/NUM-010/problem-illustration.png)

## Input Format

- Single line: two integers `L` and `R`

## Output Format

- Single integer: the range sum modulo `1000000007`

## Constraints

- `1 <= L <= R <= 1000000`
- Modulus is fixed at `1000000007`

## Example

**Input:**

```
2 4
```

**Output:**

```
14
```

**Explanation:**

sigma(2)=3, sigma(3)=4, sigma(4)=7, total = 14.

![Example Visualization](../images/NUM-010/example-1.png)

## Notes

- Precompute sigma values using a sieve-like method
- Use prefix sums for fast range queries
- Time complexity: O(R log R)
- Space complexity: O(R)

## Related Topics

Divisor Sums, Sieve, Prefix Sums

---

## Solution Template

### Java


### Python


### C++


### JavaScript

