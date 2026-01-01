---
problem_id: HEP_RUNNING_MEDIAN_DELETE_THRESHOLD__4217
display_id: HEP-001
slug: running-median-with-delete-threshold
title: "Running Median with Delete and Threshold"
difficulty: Medium
difficulty_score: 55
topics:
  - Heaps
  - Median
  - Data Streams
tags:
  - heaps
  - median
  - lazy-deletion
  - medium
premium: true
subscription_tier: basic
---

# HEP-001: Running Median with Delete and Threshold

## 📋 Problem Summary

You need to maintain a multiset of integers supporting `ADD`, `DEL`, and `MEDIAN` operations.
- `ADD x`: Insert `x`.
- `DEL x`: Remove one instance of `x`.
- `MEDIAN`: Return the median if the size is at least `T`. If empty, return `EMPTY`. If size < `T`, return `NA`.

## 🌍 Real-World Scenario

**Scenario Title:** Real-Time Sensor Data Filtering

Imagine a monitoring system for a nuclear reactor.
- Sensors stream temperature readings continuously (`ADD`).
- Occasionally, a sensor reading is flagged as erroneous and retracted (`DEL`).
- To monitor the "typical" temperature, you need the **Median**.
- However, calculating the median is only statistically significant if you have enough data points (Threshold `T`). If you have too few readings, reporting a median is misleading (`NA`).

![Real-World Application](../images/HEP-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Two Heaps Approach

We use two heaps:
1. **Max-Heap (Left):** Stores the smaller half of numbers.
2. **Min-Heap (Right):** Stores the larger half of numbers.

Invariant:
- `size(Left) == size(Right)` OR `size(Left) == size(Right) + 1`.
- All elements in `Left` <= All elements in `Right`.

```text
       Left (Max-Heap)       Right (Min-Heap)
           [5]                    [8]
          /   \                  /   \
        [3]   [2]              [10]  [12]

Median = Top of Left (5)
```

**Lazy Deletion:**
Since standard heaps don't support efficient arbitrary deletion, we use **Lazy Deletion**.
- When `DEL x` comes, we don't search and remove `x` immediately (`O(N)`).
- Instead, we record that `x` is "to be deleted" in a frequency map (`debt`).
- We only physically remove `x` from the top of the heap when it surfaces during `top()` or `pop()` operations.
- We maintain `valid_size` variables for each heap to track the count of non-deleted elements.

### Key Concept: Balancing Heaps with Lazy Deletion

1. **Add:** Push to appropriate heap. Rebalance.
2. **Delete:** Increment debt count. Update valid sizes. **Do not rebalance yet.** Rebalancing happens only if the valid size difference violates the invariant.
3. **Median:**
   - Clean the tops of both heaps (remove "dead" elements).
   - Ensure balance (move elements if needed).
   - Return `Left.top()`.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Operations list.
- **Output:** Strings for `MEDIAN` queries.
- **Constraints:** `Q <= 10^5`, Values up to `10^9`.
- **Median Definition:** Lower middle. If sorted array is `[1, 2, 3, 4]`, median is `2`.

## Naive Approach

### Intuition

Maintain a sorted list.
- `ADD`: Insert in sorted order (`O(N)`).
- `DEL`: Remove (`O(N)`).
- `MEDIAN`: Access middle (`O(1)`).

### Time Complexity

- **O(Q * N)**: Too slow for `10^5` operations.

## Optimal Approach

### Key Insight

Use **Two Heaps** with **Lazy Deletion**.
- `ADD`: `O(log N)`.
- `DEL`: `O(log N)` (amortized).
- `MEDIAN`: `O(1)` (after cleaning).

### Algorithm

1. `maxHeap` (Left), `minHeap` (Right).
2. `debt` map: stores counts of deleted numbers.
3. `balance` variable: `valid_left - valid_right`.
4. **ADD(x):**
   - If `x <= maxHeap.top()`, push to Left. Else Right.
   - Update `balance`.
   - Rebalance if `balance` is not 0 or 1.
5. **DEL(x):**
   - Increment `debt[x]`.
   - Determine which heap `x` "belongs" to (conceptually) to update `balance`.
     - *Tricky part:* We don't know if the specific instance of `x` we are deleting is in Left or Right if `x` can be in both.
     - *Better Strategy:* Just track global valid count. For balancing, we rely on the `size()` of heaps including dead elements, but clean tops frequently.
     - *Refined Strategy:*
       - Push `x` to `debt`.
       - If `x <= current_median`, decrement `valid_left`. Else `valid_right`.
       - Rebalance based on `valid_left` and `valid_right`.
6. **Rebalance:**
   - While `valid_left > valid_right + 1`: Move from Left to Right.
   - While `valid_right > valid_left`: Move from Right to Left.
   - *Crucial:* Before moving an element from top of heap, **clean** the heap (pop deleted elements).

### Time Complexity

- **O(Q log N)**.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/HEP-001/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4 2
ADD 1
ADD 5
DEL 1
MEDIAN
```

1. `ADD 1`:
   - Left: `{1}`, Right: `{}`. Valid: 1, 0.
2. `ADD 5`:
   - 5 > 1. Push Right.
   - Left: `{1}`, Right: `{5}`. Valid: 1, 1. Balanced.
3. `DEL 1`:
   - `1` is in Left. `validLeft` becomes 0.
   - Debt: `{1: 1}`.
   - Rebalance: `validRight` (1) > `validLeft` (0).
   - Move from Right to Left.
   - Right pop `5`. Left push `5`.
   - Left: `{1, 5}` (1 is dead). Right: `{}`.
   - Valid: 1, 0.
4. `MEDIAN`:
   - Clean Left. Top is `5` (1 is dead, popped).
   - Total valid size: 1.
   - T=2.
   - Output: `NA`.

## ✅ Proof of Correctness

### Invariant
- `validLeft` and `validRight` accurately track the count of non-deleted elements.
- `Left` contains `validLeft` smallest elements. `Right` contains `validRight` largest.
- `validLeft` is always equal to `validRight` or `validRight + 1`.
- Lazy deletion ensures we don't scan heaps, keeping operations logarithmic.

## 💡 Interview Extensions

- **Extension 1:** Sliding Window Median?
  - *Answer:* Same logic, `ADD` new element, `DEL` old element leaving window.
- **Extension 2:** Percentile instead of Median?
  - *Answer:* Adjust the ratio of `validLeft` vs `validRight` (e.g., 90% vs 10%).

### Common Mistakes to Avoid

1. **Incorrect Valid Counts**
   - ❌ Wrong: Decrementing valid count only when physically removing from heap.
   - ✅ Correct: Decrement immediately upon `DEL` request to keep balance logic correct.
2. **Infinite Loops**
   - ❌ Wrong: Not cleaning heaps before `peek` or `pop` during rebalance.
   - ✅ Correct: Always pop dead elements first.

## Related Concepts

- **Lazy Propagation:** Similar concept in Segment Trees.
- **Balanced BST:** Can also solve this (Order Statistic Tree).
