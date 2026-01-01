---
title: Range Sum with Point Updates and Undo
slug: range-sum-point-updates-undo
difficulty: Medium
difficulty_score: 52
tags:
- Segment Tree
- Fenwick Tree
- Rollback
problem_id: SEG_RANGE_SUM_POINT_UPDATES_UNDO__5472
display_id: SEG-001
topics:
- Segment Tree
- Fenwick Tree
- Rollback
---
# Range Sum with Point Updates and Undo - Editorial

## Problem Summary

You are given an array of integers and need to support three operations:
1.  **UPDATE**: Change the value at a specific index.
2.  **QUERY**: Calculate the sum of elements in a range `[L, R]` modulo `M`.
3.  **UNDO**: Revert the last `k` updates.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= M <= 10^9+7`
- `0 <= k <= 100`
## Real-World Scenario

Imagine a **Financial Ledger System**.
-   **Update**: A transaction modifies an account balance.
-   **Query**: An auditor checks the total assets across a range of accounts.
-   **Undo**: A batch of erroneous transactions needs to be rolled back quickly.

## Problem Exploration

### 1. Operations Analysis
-   **Point Update**: Standard operation supported by Segment Trees or Fenwick Trees in `O(log N)`.
-   **Range Sum**: Standard operation supported by Segment Trees or Fenwick Trees in `O(log N)`.
-   **Undo**: This is the tricky part. We need to revert the state of the array to what it was before the last `k` updates.

### 2. Handling Undo
Since we need to undo *updates*, we must store the history of changes.
For every `UPDATE i x`, we should record:
-   The index `i`.
-   The *previous* value at `a[i]` (so we can restore it).

When we receive `UNDO k`, we pop the last `k` updates from our history stack and apply the reverse operation: set `a[i] = prev_value`.

### 3. Data Structures
-   **Fenwick Tree (Binary Indexed Tree)**: Easier to implement for point updates and prefix sums. Range sum `[L, R]` is `query(R) - query(L-1)`.
-   **Segment Tree**: Also works, slightly more code but more flexible if operations get complex (e.g., range max). Since we only need sum, Fenwick is sufficient and faster.

## Approaches

### Approach 1: Fenwick Tree with History Stack
1.  Build a Fenwick Tree from the initial array.
2.  Maintain a stack `history` storing tuples `(index, old_value)`.
3.  **UPDATE i x**:
    -   Get current value `old_val = a[i]`.
    -   Update Fenwick Tree: `add(i, x - old_val)`.
    -   Update array: `a[i] = x`.
    -   Push `(i, old_val)` to `history`.
4.  **QUERY l r**:
    -   Return `(query(r) - query(l-1)) % M`. Handle negative results by adding `M`.
5.  **UNDO k**:
    -   Repeat `k` times:
        -   Pop `(idx, val)` from `history`.
        -   Current value is `a[idx]`.
        -   Update Fenwick: `add(idx, val - a[idx])`.
        -   Restore array: `a[idx] = val`.

**Complexity**:
-   Update: `O(log N)`
-   Query: `O(log N)`
-   Undo: `O(k log N)`
-   Total: `O((N + Q) log N)` since total undos are bounded or proportional to updates.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`5 5 1000`
`1 2 3 4 5`
1.  `QUERY 1 3`: Sum indices 1, 2, 3 (values 2, 3, 4). Sum = 9. Output 9.
2.  `UPDATE 2 10`: `a[2]` changes from 3 to 10. History: `[(2, 3)]`. Array: `1 2 10 4 5`.
3.  `QUERY 0 4`: Sum all. `1+2+10+4+5 = 22`. Output 22.
4.  `UNDO 1`: Pop `(2, 3)`. Restore `a[2]` to 3. Array: `1 2 3 4 5`.
5.  `QUERY 0 4`: Sum all. `1+2+3+4+5 = 15`. Output 15.

**Output:**
9
22
15

## Proof of Correctness

-   **Fenwick Tree**: Correctly maintains prefix sums under point updates.
-   **Undo Logic**: By storing the exact previous value, we can compute the difference `old_val - current_val` and apply it to the Fenwick Tree, effectively reversing the update. Since updates are processed sequentially, a stack correctly reverses the order.
-   **Modulo Arithmetic**: All additions and subtractions are modulo `M`, handling negative results correctly.

## Interview Extensions

1.  **Range Updates?**
    -   If we had Range Updates and Point Queries, we could use a BIT on the difference array.
    -   If Range Updates and Range Queries, we need Segment Tree with Lazy Propagation. Undo becomes more complex (store old node states or reverse operations).
2.  **Persistent Segment Tree?**
    -   We could use a Persistent Segment Tree to access *any* previous version, not just undoing the last `k`. This would be `O(log N)` per update/query but use `O(Q log N)` space.

### Common Mistakes

-   **0-based vs 1-based Indexing**: Fenwick Trees are naturally 1-based. Input is usually 0-based. Be careful with conversions.
-   **Modulo Negative Numbers**: In languages like Java/C++, `%` can return negative numbers. Always add `mod` before taking modulo again.
-   **History Stack**: Ensure you push *before* updating the array.
