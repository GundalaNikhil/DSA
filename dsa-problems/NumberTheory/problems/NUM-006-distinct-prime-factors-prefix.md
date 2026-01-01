---
problem_id: NUM_DISTINCT_PRIME_FACTORS_PREFIX__5173
display_id: NUM-006
slug: distinct-prime-factors-prefix
title: "Distinct Prime Factors Count Prefix"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Sieve
  - Prefix Sums
tags:
  - number-theory
  - sieve
  - prefix
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-006: Distinct Prime Factors Count Prefix

## Problem Statement

For each integer `x`, let `f(x)` be the number of distinct prime factors of `x`. Precompute `f(1..N)` and answer range sum queries:

```
sum_{x=l..r} f(x)
```

![Problem Illustration](../images/NUM-006/problem-illustration.png)

## Input Format

- First line: integers `N` and `q`
- Next `q` lines: two integers `l` and `r` (1-based, inclusive)

## Output Format

- For each query, print the range sum on its own line

## Constraints

- `1 <= N <= 1000000`
- `1 <= q <= 100000`
- `1 <= l <= r <= N`

## Example

**Input:**

```
6 1
2 5
```

**Output:**

```
4
```

**Explanation:**

f(2)=1, f(3)=1, f(4)=1, f(5)=1, sum = 4.

![Example Visualization](../images/NUM-006/example-1.png)

## Notes

- Use a modified sieve to count distinct primes
- Build a prefix sum array over f(x)
- Time complexity: O(N log log N + q)
- Space complexity: O(N)

## Related Topics

Sieve of Eratosthenes, Prefix Sums, Number Theory

---

## Solution Template

### Java


### Python


### C++


### JavaScript

