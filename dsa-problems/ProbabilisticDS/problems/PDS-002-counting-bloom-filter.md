---
problem_id: PDS_COUNTING_BLOOM_FILTER__5830
display_id: PDS-002
slug: counting-bloom-filter
title: "Counting Bloom Filter"
difficulty: Medium
difficulty_score: 55
topics:
  - Probabilistic Data Structures
  - Bloom Filter
  - Poisson Approximation
tags:
  - probabilistic-ds
  - bloom-filter
  - poisson
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-002: Counting Bloom Filter

## Problem Statement

A counting Bloom filter uses counters instead of bits. With `m` counters, `k` hash functions, and `n` insertions, approximate the overflow probability of a counter of `c` bits using a Poisson model.

Let `lambda = k * n / m`, and the counter maximum be `MAX = 2^c - 1`. Then:

```
P_overflow = 1 - sum_{i=0..MAX} (e^{-lambda} * lambda^i / i!)
```

Compute `P_overflow`.

![Problem Illustration](../images/PDS-002/problem-illustration.png)

## Input Format

- Single line: integers `m`, `k`, `c`, and `n`

## Output Format

- Single floating-point number: overflow probability

## Constraints

- `1 <= m <= 10^6`
- `1 <= k <= 20`
- `1 <= c <= 10`
- `1 <= n <= 10^6`

## Example

**Input:**

```
1000 3 4 500
```

**Output:**

```
0.000000000007679
```

**Explanation:**

lambda = 1.5, MAX = 15, overflow probability is about 7.679e-12.

![Example Visualization](../images/PDS-002/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-12
- Time complexity: O(2^c)

## Related Topics

Counting Bloom Filters, Poisson Approximation

---

## Solution Template

### Java


### Python


### C++


### JavaScript

