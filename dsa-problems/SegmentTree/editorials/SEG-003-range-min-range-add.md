---
title: Range Minimum with Range Add
slug: range-min-range-add
difficulty: Medium
difficulty_score: 48
tags:
- Segment Tree
- Range Minimum Query
- Lazy Propagation
problem_id: SEG_RANGE_MIN_RANGE_ADD__3915
display_id: SEG-003
topics:
- Segment Tree
- Lazy Propagation
- Range Updates
---
# Range Minimum with Range Add - Editorial

## Problem Summary

You are given an array and need to support two operations:
1.  **ADD l r x**: Add value `x` to all elements in the range `[l, r]`.
2.  **MIN l r**: Find the minimum value in the range `[l, r]`.


## Constraints

- `1 <= n, q <= 200000`
- `-10^9 <= a[i], x <= 10^9`
- Indices are 0-based
## Real-World Scenario

Imagine a **Temperature Monitoring System**.
-   **Range Add**: A heatwave increases the temperature of all sensors in a specific region (indices `l` to `r`) by `x` degrees.
-   **Range Min**: You want to find the coolest spot in a region to direct emergency cooling resources.

## Problem Exploration

### 1. Segment Tree with Lazy Propagation
Similar to the "Range Add, Range Sum" problem, we need a Segment Tree with Lazy Propagation.
The key difference is the aggregation function: instead of maintaining the `sum`, we maintain the `min`.

### 2. Node Structure
-   `min_val`: The minimum value in the node's range.
-   `lazy`: The pending addition value to be propagated to children.

### 3. Update Logic
When adding `x` to a range:
-   Update `min_val`: `min_val += x`. (Adding `x` to every element increases the minimum by exactly `x`).
-   Update `lazy`: `lazy += x`.

### 4. Push Logic
When pushing `lazy` to children:
-   Left child: `min_val += lazy`, `lazy += lazy`.
-   Right child: `min_val += lazy`, `lazy += lazy`.
-   Reset current `lazy` to 0.

## Approaches

### Approach 1: Segment Tree with Lazy Propagation
-   **Build**: `O(N)`. Compute min of children.
-   **Update**: `O(log N)`. Add to min and lazy.
-   **Query**: `O(log N)`. Return min of relevant segments.
-   **Space**: `O(4N)`.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
`3 2`
`3 1 4`
1.  `ADD 0 2 2`:
    -   Add 2 to `[0, 2]`.
    -   Root `[0, 2]` covers fully. `min` becomes `min(3,1,4)+2 = 1+2 = 3`. `lazy` += 2.
    -   Array effectively `[5, 3, 6]`.
2.  `MIN 1 2`:
    -   Query `[1, 2]`.
    -   Push root lazy (2) to children.
        -   Left `[0, 1]`: `min` was `min(3,1)=1`. Becomes `1+2=3`. `lazy`=2.
        -   Right `[2, 2]`: `min` was 4. Becomes `4+2=6`. `lazy`=2.
    -   Query `[1, 2]` splits:
        -   Left child `[0, 1]` intersects `[1, 1]`. Recurse.
            -   Push lazy (2) to `[0, 0]` and `[1, 1]`.
            -   `[1, 1]` min becomes `1+2=3`.
            -   Return 3.
        -   Right child `[2, 2]` intersects `[2, 2]`.
            -   Return 6.
    -   Result `min(3, 6) = 3`.

**Output:**
3

## Proof of Correctness

-   **Lazy Propagation**: Ensures updates are efficient (`O(log N)`).
-   **Min Property**: `min(A + x) = min(A) + x`. This property allows us to update the node's `min_val` directly by adding `x` without needing to know the distribution of values in the subtree. This is crucial. If the operation were `Set` or `Multiply` (with negative numbers), it would be more complex.

## Interview Extensions

1.  **Range Set to Value?**
    -   `min_val = x`. `lazy_set = x`. Need to handle precedence if mixing Add and Set.
2.  **Range Max?**
    -   Symmetric to Range Min.
3.  **Range Add, Range Min Count?**
    -   Store `{min_val, count}` in each node. When combining, if left.min < right.min, take left; if equal, sum counts.

### Common Mistakes

-   **Initial Query Value**: Use `INFINITY` (or `LLONG_MAX`) for out-of-bounds queries, not 0.
-   **Push Order**: Always push before recursing to children.
