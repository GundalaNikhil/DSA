---
title: Range Add, K-th Order
slug: range-add-kth-order
difficulty: Hard
difficulty_score: 70
tags:
- Segment Tree
- Order Statistics
- Range Updates
problem_id: SEG_RANGE_ADD_KTH_ORDER__8059
display_id: SEG-012
topics:
- Segment Tree
- Order Statistics
- Range Updates
---
# Range Add, K-th Order - Editorial

## Problem Summary

You need to maintain an array `a` under two operations:
1.  **ADD l r x**: Add `x` to all elements in `a[l..r]`.
2.  **KTH l r k**: Find the `k`-th smallest value in `a[l..r]`.


## Constraints

- `1 <= n, q <= 100000`
- `-10^9 <= a[i], x <= 10^9`
- `1 <= k <= r - l + 1`
## Real-World Scenario

Imagine a **Salary Adjustment System**.
-   You have a list of employees and their salaries.
-   **ADD**: You give a raise of $X to everyone in a specific department (range of IDs).
-   **KTH**: You want to know the median salary (or 10th percentile) for a group of employees to analyze pay equity.
-   Since salaries change dynamically and you query arbitrary ranges, this is complex.

## Problem Exploration

### 1. Difficulty
This is a classic "Hard" problem.
-   Static array, K-th order: Merge Sort Tree or Persistent Segment Tree (`O(log N)`).
-   Point updates, K-th order: Fenwick Tree of Segment Trees or SQRT Decomposition (`O(log^2 N)` or `O(sqrtN log N)`).
-   **Range updates**, K-th order: Very hard.
    -   Persistent Segment Tree doesn't support range updates easily (lazy propagation breaks persistence structure usually).
    -   SQRT Decomposition is the most viable "standard" approach.

### 2. SQRT Decomposition Approach
Divide array into blocks of size `B ~= sqrtN log N`.
-   Maintain each block in **sorted order**.
-   **ADD l r x**:
    -   Partial blocks: Brute force update, then re-sort (`O(B log B)` or `O(B)` with merge).
    -   Full blocks: Maintain a `lazy_add` tag.
-   **KTH l r k**:
    -   Binary search for the answer `V`.
    -   Check `count(l, r, V)`: how many elements in `[l, r]` are `<= V`.
    -   `count` function:
        -   Partial blocks: Brute force check (`O(B)`).
        -   Full blocks: Binary search (upper bound) on sorted block, adjusting for `lazy_add` (`O(log B)`).
    -   Total check time: `O(fracNB log B + B)`.
    -   Total query time: `O(log(Range) * (fracNB log B + B))`.

With `N=100,000` and block size `B ~= 1000`:
- Query time estimate: `30 x (100 x 10 + 1000) ~= 60,000` operations per query.
- Total operations: `10^5 x 6 x 10^4 = 6 x 10^9`.

Alternative block size `B ~= sqrtN` yields `O(sqrtN log N)` per check:
- Total: `O(Q log(Range) sqrtN log N)`.
- `10^5 x 30 x 300 x 17 ~= 1.5 x 10^10` operations.

**Optimization strategies:**
- **Randomized Quickselect**: Pick random pivot from `[l, r]`, count elements smaller than pivot, recurse. Similar complexity but better constants.
- **Block size tuning**: Smaller blocks make `upper_bound` faster; larger blocks reduce the number of blocks to process.
- **Optimal block size**: `B ~= sqrtN log N` balances update and query costs.

**SQRT Decomposition** provides a robust, implementable solution:
- Binary search on answer range `[-10^14, 10^14]` (approximately 60 iterations).
- For each candidate value, use `count(l, r, val)`:
  - Full blocks: `upper_bound` on sorted vector.
  - Partial blocks: linear iteration.
- ADD operation: `O(B)` (update lazy tags for full blocks, rebuild sorted array for partial blocks).

## Approaches

### Approach 1: SQRT Decomposition
-   Block size `B ~= 400-500`.
-   Each block stores:
    -   `original`: values in original order (for partial updates).
    -   `sorted`: values in sorted order (for binary search).
    -   `lazy`: lazy add value.
-   **ADD**:
    -   Update `original` and `sorted` for partial blocks. Re-sort `sorted`.
    -   Update `lazy` for full blocks.
-   **KTH**:
    -   Binary search for value `v` in range `[min_possible, max_possible]`.
    -   `count_less_equal(l, r, v)`:
        -   Sum `upper_bound` in full blocks (adjusting for lazy).
        -   Brute force in partial blocks.
    -   If count `>= k`, try smaller `v`. Else larger.

**Range of values**:
Initial values `+/- 10^9`. Updates can add up.
Max value can be around `10^14` (if `10^5` updates of `10^9`).
Binary search range: roughly 60 iterations.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3 2`
`1 2 3`
`ADD 0 2 1`
`KTH 0 2 2`

1.  **Initial**: `[1, 2, 3]`. Blocks depend on size.
2.  **ADD 0 2 1**:
    -   Array becomes `[2, 3, 4]`.
    -   Blocks updated (lazy or direct).
3.  **KTH 0 2 2**:
    -   Binary search for answer.
    -   Try `mid = 3`. `count(<=3)` in `[2, 3, 4]` is 2. `2 >= 2`. Ans = 3. High = 2.
    -   Try `mid = 2`. `count(<=2)` is 1. `1 < 2`. Low = 3.
    -   Loop ends. Return 3.

## Proof of Correctness

-   **SQRT Decomposition**: Correctly handles updates by rebuilding partial blocks and tagging full blocks.
-   **Binary Search on Answer**: Monotonicity of `count(<= val)` allows finding the k-th smallest.
-   **Complexity**: `O(Q * log(Range) * sqrtN log N)` (worst case with small blocks) or optimized. Given constraints and typical test cases, this passes.

## Interview Extensions

1.  **Range Rank?**
    -   This is exactly the `countLessEqual` function we implemented.
2.  **Point Update?**
    -   Special case of range update. Faster (`O(sqrtN)` or `O(log N)` with Segment Tree).

### Common Mistakes

-   **Block Size**: Too small = slow query. Too large = slow update. `sqrtN log N` is a good balance.
-   **Lazy Propagation**: Don't forget to push lazy values to the array before partial updates.
-   **Binary Search Range**: Ensure it covers all possible values after many additions.
