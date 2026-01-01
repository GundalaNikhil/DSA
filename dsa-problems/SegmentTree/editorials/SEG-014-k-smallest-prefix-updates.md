---
title: K Smallest Prefix Updates
slug: k-smallest-prefix-updates
difficulty: Medium
difficulty_score: 50
tags:
- Segment Tree
- Range Assignment
- Prefix Updates
problem_id: SEG_K_SMALLEST_PREFIX_UPDATES__9461
display_id: SEG-014
topics:
- Segment Tree
- Range Assignment
- Prefix Updates
---
# K Smallest Prefix Updates - Editorial

## Problem Summary

You are given an array `a`. You need to support:
1.  **SETPREFIX k x**: Set `a[0..k-1] = x`.
2.  **SUM l r**: Calculate the sum of `a[l..r]`.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= k <= n`
## Real-World Scenario

Imagine a **Budget Allocation System**.
-   You have a list of departments or projects.
-   **SETPREFIX**: The CEO decides to reset the budget for the top `k` priority projects to a fixed amount `x`.
-   **SUM**: You need to calculate the total budget for a range of projects (e.g., a specific division).

## Problem Exploration

### 1. Range Assignment
This is a standard **Range Assignment** problem, but restricted to prefixes.
-   Prefix assignment is just `update(0, k-1, x)`.
-   Range Sum is standard.

### 2. Segment Tree with Lazy Propagation
-   We need a Segment Tree that supports range set updates and range sum queries.
-   **Lazy Tag**: `lazy_set`.
    -   If `lazy_set != -1` (or some sentinel), it means all elements in this range are set to `lazy_set`.
    -   When pushing down, update children's values and lazy tags.
    -   Sum of a range `[L, R]` with set value `v` is `(R - L + 1) * v`.

### 3. Sentinel Value
-   Since values can be anything (including negative), we need a robust sentinel.
-   Or use a boolean flag `has_lazy`.

## Approaches

### Approach 1: Segment Tree with Lazy Propagation
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
`3 2`
`1 2 3`
`SETPREFIX 2 5`
`SUM 0 2`

1.  **Initial**: `[1, 2, 3]`. Sum = 6.
2.  **SETPREFIX 2 5**: Set `a[0..1]` to 5.
    -   Array becomes `[5, 5, 3]`.
    -   Segment tree updates range `[0, 1]`.
3.  **SUM 0 2**:
    -   Sum `5 + 5 + 3 = 13`.

## Proof of Correctness

-   **Lazy Propagation**: Ensures updates are efficient (`O(log N)`) and correctly applied to sub-ranges when queried.
-   **Prefix as Range**: Treating prefix update as `[0, k-1]` update maps problem to standard Range Assignment.

## Interview Extensions

1.  **Range Add + Range Set?**
    -   Need two lazy tags. Order matters (Set overrides Add).
2.  **History Sum?**
    -   Persistent Segment Tree or specialized tags.

### Common Mistakes

-   **Lazy Flag**: Forgetting `hasLazy` and assuming `lazy=0` means no update (0 is a valid value to set).
-   **Push Order**: Push before recursing children in both update and query.
