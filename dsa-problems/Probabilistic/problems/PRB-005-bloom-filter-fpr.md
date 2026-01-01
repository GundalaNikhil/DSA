---
problem_id: PRB_BLOOM_FILTER_FPR__4972
display_id: PRB-005
slug: bloom-filter-fpr
title: "Bloom Filter False Positive Rate"
difficulty: Medium
difficulty_score: 48
topics:
  - Probability
  - Data Structures
  - Hashing
tags:
  - probability
  - bloom-filter
  - hashing
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-005: Bloom Filter False Positive Rate

## Problem Statement

Given a Bloom filter with `m` bits, `k` hash functions, and `n` inserted items, compute the false positive probability using the standard approximation:

```
P = (1 - exp(-k * n / m))^k
```

![Problem Illustration](../images/PRB-005/problem-illustration.png)

## Input Format

- Single line: integers `m`, `k`, `n`

## Output Format

- Single floating-point number: false positive probability

## Constraints

- `1 <= m, n <= 10^6`
- `1 <= k <= 20`

## Example

**Input:**

```
1000 3 100
```

**Output:**

```
0.017411
```

**Explanation:**

Using the approximation, the false positive rate is about 0.01741.

![Example Visualization](../images/PRB-005/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(1)

## Related Topics

Bloom Filters, False Positives, Probabilistic Data Structures

---

## Solution Template

### Java


### Python


### C++


### JavaScript

