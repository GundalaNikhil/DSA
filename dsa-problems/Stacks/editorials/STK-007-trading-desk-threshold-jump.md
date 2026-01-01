---
title: Trading Desk Threshold Jump
slug: trading-desk-threshold-jump
difficulty: Medium
difficulty_score: 48
tags:
- Stack
- Monotonic Stack
- Next Greater Element
problem_id: STK_TRADING_DESK_THRESHOLD_JUMP__2549
display_id: STK-007
topics:
- Stack
- Monotonic Stack
- Arrays
---
# Trading Desk Threshold Jump - Editorial

## Problem Summary

For each price `p[i]` in an array, find the number of steps forward (distance) to the nearest future price `p[j]` (where `j > i`) such that `p[j] >= p[i] + t`. If no such price exists, output `0`.


## Constraints

- `1 <= n <= 200000`
- `0 <= p[i], t <= 10^9`
## Real-World Scenario

Imagine you are an **Algorithmic Trader**.
-   You buy a stock at price `P`.
-   You have a strict rule: you only sell if the price rises by at least `T` dollars (i.e., reaches `P + T`).
-   You want to know, for every possible buying moment in history, how long you would have had to wait to trigger a sell.
-   If the price never rose by `T` after that point, you would have been stuck holding the bag forever (wait time 0 or infinity).

## Problem Exploration

### 1. Next Greater Element Variation
-   This is very similar to the "Next Greater Element" problem.
-   Standard NGE: Find nearest `j > i` such that `p[j] > p[i]`.
-   Our Problem: Find nearest `j > i` such that `p[j] >= p[i] + t`.
-   The condition `p[j] >= p[i] + t` depends on both `p[i]` and `p[j]`.

### 2. Segment Tree Approach
-   This problem requires finding the nearest future index with a value threshold.
-   We use **Coordinate Compression** with a **Segment Tree** to efficiently query minimum indices.
-   The approach:
    1. Map all values to ranks using coordinate compression.
    2. Build a Segment Tree that stores minimum indices for value ranges.
    3. Process prices from right to left.
    4. For each position, query for the nearest future price meeting the threshold.
-   **Complexity**: `O(N log N)` for both coordinate compression and segment tree operations.

## Approaches

### Approach 1: Coordinate Compression + Segment Tree
-   Map values to ranks.
-   Use a Segment Tree to store the minimum index for each value range.
-   Process Right-to-Left.
-   Complexity: `O(N log N)`.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `3 1 4 6 5`, `t=2`

1.  **Distinct**: `[1, 3, 4, 5, 6]`. Ranks: `1->0, 3->1, 4->2, 5->3, 6->4`.
2.  Process right to left:
    -   `i=4` (5): Target `5+2=7`. No element >= 7. Res `0`.
    -   `i=3` (6): Target `6+2=8`. No element >= 8. Res `0`.
    -   `i=2` (4): Target `4+2=6`. Element `6` at index 3. Res `3 - 2 = 1`.
    -   `i=1` (1): Target `1+2=3`. Element `3` at index 0, `4` at index 2. Nearest is index 2. Res `2 - 1 = 1`.
    -   `i=0` (3): Target `3+2=5`. Element `5` at index 4, `6` at index 3. Nearest is index 3. Res `3 - 0 = 3`.

**Output:** `3 1 1 0 0`

## Proof of Correctness

-   **Range Query**: By mapping values to ranks, we transform the condition `val >= target` into `rank >= target_rank`.
-   **Min Index**: The Segment Tree efficiently finds the minimum index in the suffix of ranks, which corresponds to the nearest future element satisfying the value condition.
-   **Right-to-Left**: Processing in reverse ensures that when we query for `p[i]`, the tree only contains indices `j > i`.

## Interview Extensions

1.  **Max Wait Time**: Find the maximum wait time instead of per-element.
2.  **Dynamic Updates**: What if prices change? (SegTree handles updates in `O(log N)`).

### Common Mistakes

-   **Coordinate Compression**: Forgetting to compress values when they can be up to `10^9`.
-   **SegTree Range**: Querying `[0, size-1]` instead of `[target_rank, size-1]`.
-   **Infinity**: Initializing min-tree with 0 instead of infinity.
