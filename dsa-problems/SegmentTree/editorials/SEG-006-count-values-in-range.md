---
title: Count of Values in Range
slug: count-values-in-range
difficulty: Medium
difficulty_score: 51
tags:
- Segment Tree
- Fenwick Tree
- Range Counting
problem_id: SEG_COUNT_VALUES_IN_RANGE__1637
display_id: SEG-006
topics:
- Segment Tree
- BIT
- Range Queries
---
# Count of Values in Range - Editorial

## Problem Summary

You are given an array `a`. You need to support:
1.  **SET i x**: Update `a[i] = x`.
2.  **COUNT l r x y**: Count how many elements in `a[l..r]` satisfy `x <= a[i] <= y`.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x, y <= 10^9`
- Indices are 0-based
## Real-World Scenario

Imagine a **Product Inventory System**.
-   **Set**: Update the price of a specific product.
-   **Count**: A customer asks, "How many products in the 'Electronics' category (indices `l` to `r`) cost between `100 and`500?"

## Problem Exploration

### 1. 2D Range Counting
This problem can be mapped to counting points in a 2D plane.
-   Index `i` corresponds to X-coordinate.
-   Value `a[i]` corresponds to Y-coordinate.
-   **SET i x**: Remove point `(i, old_val)`, add point `(i, x)`.
-   **COUNT l r x y**: Count points in rectangle `[l, r] x [x, y]`.

### 2. Data Structures
-   **2D Segment Tree**: Supports dynamic updates and range sums. Space/Time `O(log^2 N)`.
-   **Fenwick Tree of Segment Trees**: Similar to 2D Segment Tree.
-   **Square Root Decomposition**: `O(sqrtN)` per update/query.
-   **Merge Sort Tree**: Supports query in `O(log^2 N)`, but updates are `O(N)` or `O(log^2 N)` if dynamic (using BSTs/Treaps inside nodes).

Given `N, Q <= 200,000`, `O(sqrtN)` might be too slow (`200000 x 450 ~= 9 x 10^7`, borderline). `O(log^2 N)` is preferred (`200000 x 324 ~= 6 x 10^7`).

### 3. Coordinate Compression
Values are up to `10^9`. We must coordinate compress them to range `[0, N+Q]`.

## Approaches

### Approach 1: Fenwick Tree of Dynamic Segment Trees (or BIT of BITs)
We can use a Fenwick Tree over the **indices** `0..N-1`.
Each node in the Fenwick Tree stores a data structure representing the **values** in that range.
Since we need to count values in range `[x, y]`, the inner structure should support `add(val, +1)` and `query(val)`.
A Fenwick Tree inside a Fenwick Tree works!
-   Outer BIT: Index `i`.
-   Inner BIT: Value `v`.
-   **Update**: `update(i, val, delta)`:
    -   For `i` in outer BIT: `inner_bit[i].add(val, delta)`.
-   **Query**: `query(i, val)`:
    -   For `i` in outer BIT: `sum += inner_bit[i].query(val)`.
    -   Result is `query(r, y) - query(l-1, y) - query(r, x-1) + query(l-1, x-1)`.

**Complexity**: `O(log N * log (max_val))`. With coordinate compression, `O(log^2 N)`.

### Approach 2: Square Root Decomposition
Divide into blocks. Maintain sorted values in each block.
-   **Update**: Remove old, insert new (maintain sorted). `O(sqrtN)`.
-   **Query**: Binary search in full blocks, brute force partials. `O(sqrtN log N)`.
This is easier to implement but slower. Given 2 seconds, it might pass.

Let's stick to the **BIT of BITs** (or BIT of Segment Trees) approach for optimal performance.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3 1`
`1 5 2`
`COUNT 0 2 2 5`

1.  **Initial**: `[1, 5, 2]`.
2.  **Query**: `l=0, r=2, x=2, y=5`.
    -   Check `a[0]=1`: `1 notin [2, 5]`.
    -   Check `a[1]=5`: `5 in [2, 5]`. Count = 1.
    -   Check `a[2]=2`: `2 in [2, 5]`. Count = 2.
3.  **Result**: 2.

## Proof of Correctness

-   **Square Root Decomposition**: Correctly splits range into full blocks and partial blocks.
-   **Full Blocks**: Sorted property allows binary search to count elements in range `[x, y]` in `O(log B)`.
-   **Partial Blocks**: Brute force check is correct.
-   **Updates**: Maintaining sorted order ensures future queries are correct.

## Interview Extensions

1.  **2D Range Sum?**
    -   This is effectively 2D range count. 2D Range Sum is similar but sums values instead of counting.
2.  **Range Updates?**
    -   If we had `ADD l r v`, we'd need lazy propagation on blocks. For sorted blocks, adding `v` shifts the range `[x, y]` to `[x-v, y-v]`.

### Common Mistakes

-   **Block Indices**: Careful with `startBlock` and `endBlock` logic.
-   **Binary Search**: Ensure `upperBound` and `lowerBound` are implemented correctly for the range `[x, y]`.
    -   Count is `upperBound(y) - lowerBound(x)`.
