---
title: Range GCD with Skip Zones
slug: range-gcd-skip-zones
difficulty: Medium
difficulty_score: 54
tags:
- Segment Tree
- GCD
- Dynamic Sets
problem_id: SEG_RANGE_GCD_SKIP_ZONES__6230
display_id: SEG-010
topics:
- Segment Tree
- GCD
- Dynamic Sets
---
# Range GCD with Skip Zones - Editorial

## Problem Summary

You are given an array `a` and a set of **forbidden indices**.
You need to support:
1.  **TOGGLE i**: Flip whether index `i` is forbidden.
2.  **SET i x**: Update `a[i] = x`.
3.  **GCD l r**: Calculate the GCD of all elements in `a[l..r]` that are **not** forbidden. If no allowed elements exist, return 0.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based
## Real-World Scenario

Imagine a **Cluster Health Monitoring System**.
-   You have a cluster of servers, each reporting a "heartbeat" interval or a version number.
-   You want to find the greatest common divisor of these values to synchronize them or find a common compatible protocol version.
-   However, some servers might be **down** (forbidden) or in maintenance mode. You need to ignore them dynamically.
-   Servers can come back online (TOGGLE) or change their config (SET).

## Problem Exploration

### 1. GCD Properties
-   `gcd(0, x) = x`.
-   `gcd(a, b, c) = gcd(a, gcd(b, c))`.
-   This associativity allows Segment Trees.

### 2. Handling Forbidden Indices
-   If an index `i` is forbidden, we can treat its value as `0` for GCD purposes.
-   Since `gcd(0, x) = x`, a `0` effectively contributes nothing to the GCD calculation, which is exactly what we want (ignoring the element).
-   If all elements in a range are forbidden (all 0), the result is 0.

### 3. Segment Tree Approach
-   Maintain a Segment Tree where each leaf `i` stores:
    -   `a[i]` if `i` is allowed.
    -   `0` if `i` is forbidden.
-   **TOGGLE i**: Update leaf `i`. If it was `a[i]`, make it `0`. If `0`, make it `a[i]`.
-   **SET i x**: Update `a[i]`. If `i` is allowed, update leaf to `x`. If forbidden, just update the stored `a[i]` but keep leaf as `0`.
-   **GCD l r**: Standard range GCD query.

## Approaches

### Approach 1: Segment Tree with Zero-Masking
-   Store actual values in an auxiliary array `vals`.
-   Store `active` boolean array.
-   Segment Tree stores the effective values.
-   **Update**: `O(log N + log (max_val))`. GCD takes logarithmic time.
-   **Query**: `O(log N + log (max_val))`.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3 3`
`6 9 3`
`1` (forbidden count)
`1` (index 1 is forbidden)
`GCD 0 2`
`TOGGLE 1`
`GCD 0 2`

1.  **Initial State**:
    -   `vals = [6, 9, 3]`.
    -   `active = [T, F, T]`.
    -   Leaves: `6`, `0`, `3`.
    -   Root: `gcd(6, 0, 3) = gcd(6, 3) = 3`.
2.  **Query 1**: `GCD 0 2`. Returns 3.
3.  **Toggle 1**:
    -   `active[1]` becomes `T`.
    -   Leaf 1 becomes `9`.
    -   Root: `gcd(6, 9, 3) = 3`.
4.  **Query 2**: `GCD 0 2`. Returns 3.

## Proof of Correctness

-   **Zero Identity**: `gcd(0, x) = x` ensures that setting forbidden elements to 0 effectively removes them from the calculation without affecting the result of other elements.
-   **Segment Tree**: Correctly maintains range GCDs under point updates.

## Interview Extensions

1.  **Range Toggle?**
    -   Lazy propagation with boolean flip?
    -   If we flip a range, we need to swap "active GCD" and "inactive GCD"?
    -   We can maintain `gcd_active` and `gcd_inactive` in each node.
    -   Flip swaps them.
2.  **Number of Active Elements?**
    -   Maintain count sum in segment tree.

### Common Mistakes

-   **GCD(0, 0)**: Should be 0.
-   **Negative Numbers**: GCD is usually defined on non-negative integers. If input has negatives, take `abs()`.
