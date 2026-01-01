---
title: Range Sum of Multiple Powers
slug: range-sum-multiple-powers
difficulty: Medium
difficulty_score: 55
tags:
- Segment Tree
- Modular Arithmetic
- Range Sum
problem_id: SEG_RANGE_SUM_MULTIPLE_POWERS__4175
display_id: SEG-013
topics:
- Segment Tree
- Modular Arithmetic
- Range Sum
---
# Range Sum of Multiple Powers - Editorial

## Problem Summary

You are given an array `a`. You need to support:
1.  **SET i x**: Update `a[i] = x`.
2.  **SUM l r p**: Calculate `sum_i=l^r (a[i]^p) +/-od10^9+7` for `p in 1, 2, 3`.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- `p` is in `{1,2,3}`
## Real-World Scenario

Imagine a **Statistical Analysis Tool**.
-   You have a dataset of measurements.
-   To calculate variance, skewness, or kurtosis, you need sums of powers (moments).
-   Mean requires sum of `x^1`.
-   Variance requires sum of `x^2`.
-   Skewness requires sum of `x^3`.
-   As data updates, you need to recompute these moments efficiently for any subset of the data.

## Problem Exploration

### 1. Segment Tree Node Structure
Each node in the Segment Tree will store three values:
-   `sum1`: `sum a[i]^1`
-   `sum2`: `sum a[i]^2`
-   `sum3`: `sum a[i]^3`

### 2. Merge Logic
When merging two nodes `left` and `right`:
-   `node.sum1 = (left.sum1 + right.sum1) % MOD`
-   `node.sum2 = (left.sum2 + right.sum2) % MOD`
-   `node.sum3 = (left.sum3 + right.sum3) % MOD`

### 3. Update Logic
When updating `a[i] = x`:
-   Leaf `i` updates its sums: `x`, `x^2`, `x^3`.
-   Path to root updates by re-merging.

### 4. Query Logic
-   Standard range sum query.
-   Return the specific sum requested by `p`.

## Approaches

### Approach 1: Segment Tree
-   **Build**: `O(N)`.
-   **Update**: `O(log N)`.
-   **Query**: `O(log N)`.
-   Space: `O(N)`.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`2 2`
`2 3`
`SUM 0 1 2`
`SUM 0 1 3`

1.  **Build**:
    -   Leaf 0: `(2, 4, 8)`.
    -   Leaf 1: `(3, 9, 27)`.
    -   Root: `(5, 13, 35)`.
2.  **Query 1**: `SUM 0 1 2`.
    -   Returns `sum2` from root: 13.
3.  **Query 2**: `SUM 0 1 3`.
    -   Returns `sum3` from root: 35.

## Proof of Correctness

-   **Linearity of Sum**: `sum (a_i^p) = (sum_left a_i^p) + (sum_right a_i^p)`.
-   **Modular Arithmetic**: `(A + B) +/-od M = (A +/-od M + B +/-od M) +/-od M`.
-   **Segment Tree**: Correctly aggregates these independent sums.

## Interview Extensions

1.  **Range Add Updates?**
    -   If we add `x` to range:
    -   New sum1: `sum (a_i+x) = sum a_i + N * x`.
    -   New sum2: `sum (a_i+x)^2 = sum (a_i^2 + 2a_ix + x^2) = sum a_i^2 + 2xsum a_i + N * x^2`.
    -   New sum3: `sum (a_i+x)^3 = sum (a_i^3 + 3a_i^2x + 3a_ix^2 + x^3)`.
    -   We can maintain this with lazy propagation!
2.  **Higher Powers?**
    -   Binomial expansion works for any `p`, but complexity grows with `p`.

### Common Mistakes

-   **Modulo Negative Numbers**: Ensure `val % MOD` handles negatives correctly (add MOD if negative).
-   **Overflow**: Intermediate calculations like `v * v` can exceed 64-bit if not careful, though with MOD `10^9+7`, `v^2` fits in `long long`. `v^3` requires step-by-step modulo.
