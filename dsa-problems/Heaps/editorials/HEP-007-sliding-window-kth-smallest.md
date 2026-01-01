---
problem_id: HEP_SLIDING_WINDOW_KTH_SMALLEST__2665
display_id: HEP-007
slug: sliding-window-kth-smallest
title: "Sliding Window Kth Smallest"
difficulty: Medium
difficulty_score: 58
topics:
  - Heaps
  - Sliding Window
  - Order Statistics
tags:
  - heaps
  - sliding-window
  - order-statistics
  - medium
premium: true
subscription_tier: basic
---

# HEP-007: Sliding Window Kth Smallest

## 📋 Problem Summary

You have an array `arr` of size `n`.
Consider a sliding window of size `w`.
For each window position, find the `k`-th smallest element.
Return the list of `k`-th smallest elements.

## 🌍 Real-World Scenario

**Scenario Title:** Stock Market Volatility Analysis

Traders often look at the "median" or "25th percentile" price of a stock over the last `w` minutes to gauge trends without being affected by outliers.
- If `k = w/2`, you are finding the **Running Median**.
- If `k = 1`, you are finding the **Running Minimum**.
- If `k = w`, you are finding the **Running Maximum**.
This problem generalizes all these to the "Running K-th Percentile".

![Real-World Application](../images/HEP-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Two-Heap Strategy

Window: `[1, 5, 2, 8, 3]`, `k=3` (Median).
Sorted: `[1, 2, 3, 5, 8]`. 3rd smallest is 3.

We maintain two heaps (or balanced BSTs):
1. **Left Heap (Max-Heap):** Stores the smallest `k` elements.
2. **Right Heap (Min-Heap):** Stores the remaining `w-k` elements.

Invariant:
- Size of Left Heap = `k`.
- Size of Right Heap = `w-k`.
- `max(Left) <= min(Right)`.

The answer is always `Left.top()`.

**Sliding:**
- **Add** new element `x`.
- **Remove** old element `y`.

Steps:
1. Remove `y`:
   - If `y` was in Left, remove it. Left size decreases.
   - If `y` was in Right, remove it. Right size decreases.
2. Add `x`:
   - Insert into appropriate heap to maintain order.
3. Rebalance:
   - Ensure Left has exactly `k` elements.
   - Move elements between heaps if sizes are off.

### Key Concept: Lazy Deletion

Standard heaps don't support efficient removal of arbitrary elements (`O(N)`).
We use **Lazy Deletion**:
- Keep a `deleted` map (or hash table) of counts of elements to be removed.
- When `top()` of a heap is in `deleted`, pop it and decrement count.
- We also need to track the *logical* size of heaps, not just physical size.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `n`, `w`, `k`, array `arr`.
- **Output:** Array of size `n-w+1`.
- **Constraints:** `N <= 2 x 10^5`. `W <= N`.
- **Values:** Integers, can be negative.

## Naive Approach

### Intuition

For each window, copy elements, sort them, pick index `k-1`.

### Time Complexity

- **O(N * W log W)**: Too slow if `W` is large.

## Optimal Approach

### Key Insight

Use **Two Heaps with Lazy Deletion**.
- **Max-Heap `L`**: Stores smallest `k` elements.
- **Min-Heap `R`**: Stores largest `w-k` elements.
- **Balance**: `L.size == k`.
- **Lazy Removal**: Use a hash map `to_remove` to mark elements that left the window but are still in heaps. Clean up tops lazily.

### Algorithm

1. Initialize `L` (Max-Heap), `R` (Min-Heap), `to_remove` map.
2. `balance` function:
   - While `L.size > k`: Move top of `L` to `R`.
   - While `L.size < k`: Move top of `R` to `L`.
   - While `L.top` > `R.top`: Swap tops (if heaps not empty).
   - We must track `L_valid_size` and `R_valid_size` explicitly.
3. **Add(val)**:
   - If `L` empty or `val < L.top`: push to `L`, `L_valid++`.
   - Else: push to `R`, `R_valid++`.
   - Rebalance.
4. **Remove(val)**:
   - Increment `to_remove[val]`.
   - If `val` can be in `L` (i.e., `val <= L.top`): `L_valid--`.
   - Else: `R_valid--`.
   - Clean tops: `while L.top in to_remove: pop L`. Same for `R`.
   - Rebalance.
5. **Rebalance Logic**:
   - While `L_valid > k`:
     - Move `L.top` to `R`. (Pop L, Push R).
     - `L_valid--`, `R_valid++`.
     - Clean `L`.
   - While `L_valid < k`:
     - Move `R.top` to `L`.
     - `L_valid++`, `R_valid--`.
     - Clean `R`.
   - Note: We rely on `L.top` being the k-th smallest.

### Time Complexity

- **O(N log W)**.

### Space Complexity

- **O(N)** (due to lazy deletion, heap can grow up to N).

![Algorithm Visualization](../images/HEP-007/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `arr=[1, 3, 2, 6, 4]`, `w=3`, `k=2`.

1. `i=0, val=1`: L=[1], R=[]. Sizes: 1, 0. (Need k=2).
2. `i=1, val=3`: L=[1], R=[3]. Rebalance: Move 3 to L? No, L.max < R.min.
   - L=[3, 1], R=[]. Sizes: 2, 0.
3. `i=2, val=2`: L=[3, 1]. `2 < 3`. Insert to L. L=[3, 2, 1]. Sizes: 3, 0.
   - `leftSize > k` (3 > 2). Move L top (3) to R.
   - L=[2, 1], R=[3]. Sizes: 2, 1.
   - Output: L.peek() = 2.
4. `i=3, val=6`: Remove `arr[0]=1`.
   - `1 <= 2`. Decrement `leftSize` -> 1. Mark 1 deleted.
   - Add 6. `6 > 2`. Insert R. R=[3, 6]. Sizes: 1, 2.
   - Rebalance: `leftSize < k` (1 < 2). Move R top (3) to L.
   - L=[3, 2, (1 del)], R=[6]. Sizes: 2, 1.
   - Output: L.peek() = 3.
5. `i=4, val=4`: Remove `arr[1]=3`.
   - `3 <= 3`. Decrement `leftSize` -> 1. Mark 3 deleted.
   - Add 4. `4 > 3` (old peek). Insert R. R=[6, 4]. Sizes: 1, 2.
   - Rebalance: `leftSize < k`. Move R top (4) to L.
   - L=[4, 2, (1 del), (3 del)], R=[6]. Sizes: 2, 1.
   - Output: L.peek() = 4.

Result: `2, 3, 4`. Correct.

## ✅ Proof of Correctness

### Invariant
- `L` contains `k` valid elements. `R` contains `w-k` valid elements.
- `max(L) <= min(R)`.
- `L.peek()` is the k-th smallest element.
- Lazy deletion ensures amortized efficiency.

## 💡 Interview Extensions

- **Extension 1:** Stream of numbers?
  - *Answer:* Same logic, just no removal (or infinite window).
- **Extension 2:** Fractional K (e.g., median)?
  - *Answer:* Same logic, set `k = w/2`.

### Common Mistakes to Avoid

1. **Size Tracking**
   - ❌ Wrong: Using `heap.size()` which includes deleted elements.
   - ✅ Correct: Maintain explicit `validSize` counters.
2. **Lazy Deletion**
   - ❌ Wrong: Forgetting to clean heaps before peeking/popping.
   - ✅ Correct: Always `clean()` before accessing top.

## Related Concepts

- **Median of Medians:** Selection algorithm.
- **Two Heaps Pattern:** Standard for median maintenance.
