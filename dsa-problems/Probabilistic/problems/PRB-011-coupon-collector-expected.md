---
problem_id: PRB_COUPON_COLLECTOR_EXPECTED__1148
display_id: PRB-011
slug: coupon-collector-expected
title: "Coupon Collector Expected Trials"
difficulty: Medium
difficulty_score: 40
topics:
  - Probability
  - Expected Value
  - Harmonic Numbers
tags:
  - probability
  - expectation
  - harmonic
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-011: Coupon Collector Expected Trials

## Problem Statement

With `N` equally likely coupons, compute the expected number of draws to collect all coupons:

```
E = N * (1 + 1/2 + 1/3 + ... + 1/N)
```

![Problem Illustration](../images/PRB-011/problem-illustration.png)

## Input Format

- Single line: integer `N`

## Output Format

- Single floating-point number: expected draws

## Constraints

- `1 <= N <= 10^6`

## Example

**Input:**

```
3
```

**Output:**

```
5.500000
```

**Explanation:**

E = 3 * (1 + 1/2 + 1/3) = 5.5.

![Example Visualization](../images/PRB-011/example-1.png)

## Notes

- Compute harmonic sum with double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(N)

## Related Topics

Coupon Collector, Harmonic Numbers, Expectation

---

## Solution Template

### Java


### Python


### C++


### JavaScript

