---
title: Lab Sliding-Min Stack
slug: lab-sliding-min-stack
difficulty: Medium
difficulty_score: 52
tags:
- Stack
- Min Stack
- Range Queries
problem_id: STK_LAB_SLIDING_MIN_STACK__5027
display_id: STK-009
topics:
- Stack
- Range Minimum
- Data Structures
---
# Lab Sliding-Min Stack - Editorial

## Problem Summary

You need to implement a stack that supports `PUSH x`, `POP`, and a special query `MIN k`.
-   `MIN k`: Returns the minimum value among the top `k` elements of the stack.
-   Standard error handling for empty stack or insufficient elements.


## Constraints

- `1 <= m <= 100000`
- `-10^9 <= x <= 10^9`
- `1 <= k <= 100000`
## Real-World Scenario

Imagine you are a **Lab Technician** recording temperature readings in a logbook.
-   You write down readings one by one (Push).
-   Sometimes you realize a mistake and cross out the last entry (Pop).
-   Occasionally, your supervisor asks: "What was the lowest temperature recorded in the last 5 readings?" (Min k).
-   You need a way to answer this quickly without scanning through the last 5 pages every time.

## Problem Exploration

### 1. Standard Min-Stack
-   A standard Min-Stack stores pairs `(val, current_min)`.
-   `current_min` is the minimum of *all* elements currently in the stack.
-   This answers `MIN k` where `k == stack.size()`.
-   But we need `MIN k` for *any* `k`.

### 2. Naive Approach
-   For `MIN k`, iterate through the top `k` elements.
-   Complexity: `O(k)` per query. In worst case `O(N)`.
-   Total time `O(M * N)` is too slow for `M=100,000`.

### 3. Sliding Window Minimum?
-   The "top k" elements form a window.
-   As we push, the window slides/expands.
-   But `k` is not fixed. One query might be `MIN 2`, next `MIN 10`.
-   This suggests we need to query the minimum in the range `[size - k, size - 1]`.
-   This is a **Range Minimum Query (RMQ)** on a dynamic array.
-   We can use a Segment Tree or Fenwick Tree over the stack indices.
-   Complexity: `O(log N)` per operation.
-   Can we do `O(1)`?

### 4. Auxiliary Monotonic Stack?
-   What if we store "candidates" for minimums?
-   Consider stack: `[5, 1, 3, 2, 4]` (Top is right).
-   Top 1: `4`. Min 4.
-   Top 2: `2, 4`. Min 2.
-   Top 3: `3, 2, 4`. Min 2.
-   Top 4: `1, 3, 2, 4`. Min 1.
-   Top 5: `5, 1, 3, 2, 4`. Min 1.
-   Notice the minimums for `k=1..5` are `4, 2, 2, 1, 1`.
-   This sequence is non-increasing.
-   We need to find the minimum in a suffix of the stack.
-   We use a **Segment Tree** approach which provides efficient range minimum queries.
-   Operations:
    -   `PUSH`: Update position `size` with value. `size++`.
    -   `POP`: `size--`. (Value at old size is effectively removed).
    -   `MIN k`: Query range `[size - k, size - 1]`.
-   This is `O(log N)` per operation, which is efficient for the given constraints.

## Approaches

### Approach 1: Segment Tree on Stack Indices
-   Maintain a global array `arr` and a variable `size`.
-   Build a Segment Tree over `[0, MAX_M]`.
-   `PUSH x`: `update(size, x)`, `size++`.
-   `POP`: `size--`.
-   `MIN k`: `query(size - k, size - 1)`.
-   Complexity: `O(log M)` per op.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:**
```
PUSH 5
PUSH 1
PUSH 3
MIN 2
POP
MIN 2
```

1.  `PUSH 5`: Stack `[5]`. SegTree `[5, inf...]`. Size 1.
2.  `PUSH 1`: Stack `[5, 1]`. SegTree `[5, 1, inf...]`. Size 2.
3.  `PUSH 3`: Stack `[5, 1, 3]`. SegTree `[5, 1, 3, inf...]`. Size 3.
4.  `MIN 2`: Query `[3-2, 3-1] = [1, 2]`. Elements at indices 1 and 2 are `1` and `3`. Min is `1`. Output `1`.
5.  `POP`: Output `3`. Size 2. (SegTree effectively ignores index 2 now).
6.  `MIN 2`: Query `[2-2, 2-1] = [0, 1]`. Elements at indices 0 and 1 are `5` and `1`. Min is `1`. Output `1`.

**Output:** `1`, `3`, `1`. Matches example.

## Proof of Correctness

-   **Segment Tree**: Provides correct Range Minimum Query results for any valid range `[L, R]`.
-   **Dynamic Updates**: Pushing updates the tree at the new index. Popping just reduces the valid range size (future pushes overwrite).
-   **Complexity**: `O(log N)` per operation fits within limits.

## Interview Extensions

1.  **O(1) Approach**: Can you do this in `O(1)`?
    -   *Hint*: Since it's a stack, a "Min-Queue" structure using two stacks could work, but `k` is variable.
2.  **Max Query**: Support `MAX k` as well.
    -   *Hint*: Another Segment Tree or augment the existing one.

### Common Mistakes

-   **Index Bounds**: Querying `[size-k, size]` instead of `[size-k, size-1]`.
-   **Empty Checks**: Forgetting `NA` or `EMPTY`.
-   **Tree Size**: Making tree too small. `4 * MAX_OPS` is safe.
