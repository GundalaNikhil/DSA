---
problem_id: NUM_LCM_OF_RANGES__8402
display_id: NUM-007
slug: lcm-of-ranges
title: "LCM of Ranges"
difficulty: Medium
difficulty_score: 52
topics:
  - Number Theory
  - LCM
  - Prime Factorization
tags:
  - number-theory
  - lcm
  - queries
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-007: LCM of Ranges

## Problem Statement

Given an array `a`, answer queries asking for `lcm(a[l..r])` modulo `MOD`. Each query has `r - l <= 20`, so ranges are short.

![Problem Illustration](../images/NUM-007/problem-illustration.png)

## Input Format

- First line: integers `n`, `q`, and `MOD`
- Second line: `n` integers `a[i]`
- Next `q` lines: two integers `l` and `r` (0-based, inclusive)

## Output Format

- For each query, print `lcm(a[l..r]) mod MOD`

## Constraints

- `1 <= n <= 200000`
- `1 <= q <= 100000`
- `1 <= a[i] <= 10^9`
- `1 <= MOD <= 10^9+7`
- `0 <= l <= r < n`, and `r - l <= 20`

## Example

**Input:**

```
3 1 1000000007
2 6 3
0 1
```

**Output:**

```
6
```

**Explanation:**

lcm(2, 6) = 6.

![Example Visualization](../images/NUM-007/example-1.png)

## Notes

- Factorize numbers in the short range
- Track max exponent per prime for the LCM
- Time complexity per query: O((r-l+1) log a[i])
- Space complexity: O(number of primes in range)

## Related Topics

LCM, Prime Factorization, Range Queries

---

## Solution Template

### Java


### Python


### C++


### JavaScript

