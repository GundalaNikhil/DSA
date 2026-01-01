---
title: Range Min After Additive Toggles
slug: range-min-after-toggles
difficulty: Medium
difficulty_score: 60
tags:
- Segment Tree
- Lazy Propagation
- Range Minimum
problem_id: SEG_RANGE_MIN_AFTER_TOGGLES__5728
display_id: SEG-015
topics:
- Segment Tree
- Lazy Propagation
- Range Queries
---
# Range Min After Additive Toggles - Editorial

## Problem Summary

You need to maintain an array `a` under two operations:
1.  **ADD l r x**: Add `x` to all elements in `a[l..r]`.
2.  **FLIP l r**: Multiply all elements in `a[l..r]` by `-1`.
3.  **MIN l r**: Find the minimum value in `a[l..r]`.


## Constraints

- `1 <= n, q <= 100000`
- `-10^9 <= a[i], x <= 10^9`
## Real-World Scenario

Imagine a **Financial Portfolio Tracker**.
-   **ADD**: Deposit or withdraw a fixed amount from a group of accounts.
-   **FLIP**: Convert debts to credits or vice versa (e.g., reversing a transaction type view).
-   **MIN**: Find the account with the lowest balance (or highest debt).

## Problem Exploration

### 1. Handling Flip
-   When we multiply a range by `-1`, the minimum value becomes `-1 * maximum`.
-   The maximum value becomes `-1 * minimum`.
-   So, we need to track both `min` and `max` in each Segment Tree node.

### 2. Lazy Propagation
-   We have two types of lazy tags: `lazy_add` and `lazy_flip`.
-   **Order matters**:
    -   Usually, we can apply `flip` then `add` or `add` then `flip`.
    -   Let's say a node has pending `lazy_add` and then receives a `flip`.
    -   Current state: `val + lazy_add`.
    -   New state: `-(val + lazy_add) = -val - lazy_add`.
    -   This means `flip` negates both the current values AND the pending `lazy_add`.
    -   So, when pushing `flip`, we negate `lazy_add` of children and toggle their `lazy_flip`.

### 3. Node Structure
-   `minVal`: Minimum in range.
-   `maxVal`: Maximum in range.
-   `lazyAdd`: Pending addition.
-   `lazyFlip`: Pending negation (boolean).

## Approaches

### Approach 1: Segment Tree with Two Lazy Tags
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
`3 3`
`1 -2 3`
`FLIP 0 2`
`ADD 1 2 1`
`MIN 0 2`

1.  **Initial**: `[1, -2, 3]`. Min -2, Max 3.
2.  **FLIP 0 2**:
    -   Array effectively `[-1, 2, -3]`.
    -   Segment tree root: Min -3, Max -1.
3.  **ADD 1 2 1**:
    -   Array effectively `[-1, 3, -2]`.
    -   Segment tree updates range `[1, 2]`.
4.  **MIN 0 2**:
    -   Returns -2.

## Proof of Correctness

-   **Dual Tracking**: Maintaining both Min and Max allows correct updates under sign flip.
-   **Lazy Composition**: Correctly handling interaction between `add` and `flip` (negating `lazy_add` on flip) ensures consistency.

## Interview Extensions

1.  **Range Multiply by Positive X?**
    -   Just multiply min, max, and lazy_add.
2.  **Range Absolute Value?**
    -   Harder. Segment Tree Beats.

### Common Mistakes

-   **Lazy Order**: Applying `flip` without negating `lazy_add` is a common bug.
-   **Min/Max Swap**: Forgetting to swap min and max when flipping.
