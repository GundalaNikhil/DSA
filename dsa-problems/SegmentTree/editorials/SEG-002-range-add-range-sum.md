---
title: Range Add, Range Sum
slug: range-add-range-sum
difficulty: Medium
difficulty_score: 46
tags:
- Segment Tree
- Lazy Propagation
- Range Updates
problem_id: SEG_RANGE_ADD_RANGE_SUM__6841
display_id: SEG-002
topics:
- Segment Tree
- Lazy Propagation
- Range Updates
---
# Range Add, Range Sum - Editorial

## Problem Summary

You are given an array and need to support two operations:
1.  **ADD l r x**: Add value `x` to all elements in the range `[l, r]`.
2.  **SUM l r**: Calculate the sum of elements in the range `[l, r]`.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based
## Real-World Scenario

Imagine a **Mass Salary Adjustment System**.
-   **Range Add**: The company decides to give a bonus of $500 to all employees with IDs from 100 to 200.
-   **Range Sum**: The finance department needs to calculate the total salary expenditure for employees in department range 150-250 to budget for the next month.
Updating each employee individually is too slow (`O(N)`). We need a way to update the whole group instantly (`O(log N)`).

## Problem Exploration

### 1. The Challenge of Range Updates
A standard Segment Tree handles point updates in `O(log N)`. However, a range update naively requires updating every leaf node in the range, which takes `O(N)` in the worst case.
To achieve `O(log N)` for range updates, we need **Lazy Propagation**.

### 2. Lazy Propagation Logic
Instead of updating all children immediately, we update the current node and "flag" it to indicate that its children need to be updated later.
-   **Node Structure**: Each node stores `sum` (total value of its range) and `lazy` (pending addition value).
-   **Update**: When updating a range `[L, R]` that fully covers a node's range `[start, end]`:
    -   Update the node's `sum`: `sum += (end - start + 1) * x`.
    -   Update the node's `lazy`: `lazy += x`.
    -   Stop recursing.
-   **Push (Propagate)**: Before visiting children (for a query or partial update), we "push" the `lazy` value down:
    -   Add `lazy` to left child's `sum` and `lazy`.
    -   Add `lazy` to right child's `sum` and `lazy`.
    -   Reset current node's `lazy` to 0.

### 3. Data Structures
-   **Segment Tree with Lazy Propagation**: Ideal for this problem.
-   **Fenwick Tree (BIT)**: Can also handle Range Add + Range Sum using two BITs (one for `d[i]` and one for `i * d[i]`), but Segment Tree is more intuitive for general range operations.

## Approaches

### Approach 1: Segment Tree with Lazy Propagation
We build a tree where each node represents a range `[start, end]`.
-   **Build**: `O(N)`.
-   **Update**: `O(log N)`.
-   **Query**: `O(log N)`.
-   **Space**: `O(4N)`.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3 3`
`0 0 0`
1.  `ADD 0 1 5`:
    -   Update range `[0, 1]` with +5.
    -   Node `[0, 2]` (root): partial overlap. Push.
    -   Node `[0, 1]`: full overlap. `sum` += 5*2=10. `lazy` += 5.
    -   Node `[2, 2]`: no overlap.
    -   Root sum becomes 10.
2.  `ADD 1 2 2`:
    -   Update range `[1, 2]` with +2.
    -   Node `[0, 2]`: partial. Push.
    -   Node `[0, 1]`: partial. Push `lazy=5`.
        -   Node `[0, 0]`: `sum`=5, `lazy`=5.
        -   Node `[1, 1]`: `sum`=5, `lazy`=5.
    -   Node `[0, 0]`: no overlap with `[1, 2]`.
    -   Node `[1, 1]`: full overlap. `sum` += 2*1 = 7. `lazy` += 2 = 7.
    -   Node `[2, 2]`: full overlap. `sum` += 2*1 = 2. `lazy` += 2.
    -   Root sum becomes 5 + 7 + 2 = 14.
3.  `SUM 0 2`:
    -   Query `[0, 2]`. Full overlap with root. Return 14.

**Output:**
14

## Proof of Correctness

-   **Lazy Propagation**: Ensures that we only visit `O(log N)` nodes per update. By pushing the lazy value down only when necessary, we maintain the invariant that a node's `sum` is correct relative to its subtree's pending updates.
-   **Sum Calculation**: `tree[node] += val * (end - start + 1)` correctly updates the sum of a range by adding `val` to every element.

## Interview Extensions

1.  **Range Set to Value?**
    -   Instead of `+=`, we do `=`. We need a boolean flag `hasLazy` to distinguish "set to 0" from "no update".
2.  **Range Mul?**
    -   Maintain `mulLazy` and `addLazy`. Order of operations matters (usually multiply then add).
3.  **Max instead of Sum?**
    -   `tree[node] += val` works for max too. `push` adds to children.

### Common Mistakes

-   **Array Size**: Segment tree array should be `4 * N`.
-   **Push Logic**: Forgetting to multiply `lazy` by range length when updating `sum` for children.
-   **Index Bounds**: Ensure `l` and `r` are within `[0, n-1]`.
