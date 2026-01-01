---
problem_id: QUE_LAB_WINDOW_INSTABILITY__3951
display_id: QUE-007
slug: lab-window-instability
title: "Lab Window Instability"
difficulty: Medium
difficulty_score: 50
topics:
  - Sliding Window
  - Queue
  - Heaps
tags:
  - sliding-window
  - deque
  - median
  - medium
premium: true
subscription_tier: basic
---

# QUE-007: Lab Window Instability

## 📋 Problem Summary

We are given a series of sensor readings. For every sliding window of size `K`, we need to calculate the "instability" metric:

`instability = \lfloor \frac\max - \minmedian \rfloor`

- If median is 0, output 0.
- Median is the lower median if `K` is even.

## 🌍 Real-World Scenario

**Scenario Title:** Stock Market Volatility Analysis

Traders analyze stock prices over time windows (e.g., 1-hour moving window).
- **Max - Min:** Represents the range or spread of the price.
- **Median:** Represents the "typical" price, filtering out brief spikes.
- **(Max - Min) / Median:** This is a normalized volatility measure.
- A high value means the stock is swinging wildly relative to its price.
- A low value means it's stable.
- Computing this efficiently for millions of ticks is crucial for high-frequency trading algorithms.

**Why This Problem Matters:**

- **Signal Processing:** Normalizing noise amplitude by signal strength.
- **Quality Control:** Detecting unstable manufacturing processes.

![Real-World Application](../images/QUE-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Sliding Window

Values: `[5, 1, 4, 6, 2]`, `K=3`.

1. **Window 1:** `[5, 1, 4]`
   - Sorted: `1, 4, 5`
   - Min: 1, Max: 5, Median: 4
   - Instability: `(5-1)/4 = 1`.

2. **Window 2:** `[1, 4, 6]`
   - Sorted: `1, 4, 6`
   - Min: 1, Max: 6, Median: 4
   - Instability: `(6-1)/4 = 1.25 -> 1`.

3. **Window 3:** `[4, 6, 2]`
   - Sorted: `2, 4, 6`
   - Min: 2, Max: 6, Median: 4
   - Instability: `(6-2)/4 = 1`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `N, K`, array of integers.
- **Output:** Array of instability values.
- **Median Definition:** If sorted window is `w_0, dots, w_k-1`, median is `w_lfloor (k-1)/2 rfloor`.
- **Division by Zero:** Handle median = 0 case.

## Naive Approach

### Intuition

For each window, extract elements, sort them to find min/max/median.

### Algorithm

1. Loop `i` from 0 to `n-k`.
2. Extract subarray `window = values[i : i+k]`.
3. Sort `window`.
4. `min = window[0]`, `max = window[k-1]`, `med = window[(k-1)/2]`.
5. Compute and print.

### Limitations

- **Time Complexity:** `O(N * K log K)`. With `N=200,000`, this is too slow.

## Optimal Approach

### Key Insight

We need three statistics efficiently:
1. **Min/Max:** Use **Monotonic Deques** (Sliding Window Minimum/Maximum). `O(N)` total.
2. **Median:** Use **Two Heaps** (Min-Heap for upper half, Max-Heap for lower half) with **Lazy Deletion**. `O(N log K)`.

### Algorithm

1. **Min/Max:** Maintain two deques.
   - `minDeque`: Stores indices of increasing values. Front is min.
   - `maxDeque`: Stores indices of decreasing values. Front is max.
2. **Median:** Maintain two heaps (`small` max-heap, `large` min-heap) and a `balance`.
   - Use a Hash Map `delayed` to track elements that left the window but are still in heaps.
   - **Add new element:** Push to `small`, then move top of `small` to `large`. Balance sizes so `small` has `lceil K/2 rceil` elements.
   - **Remove old element:** Mark in `delayed`. Rebalance heaps if necessary. Prune tops of heaps if they are in `delayed`.
3. **Compute:** For each window, get min/max from deques, median from `small.top()`.

### Time Complexity

- **O(N log K)** due to heap operations.

### Space Complexity

- **O(N)** for heaps and delayed map (worst case lazy deletion).

![Algorithm Visualization](../images/QUE-007/algorithm-visualization.png)
![Algorithm Steps](../images/QUE-007/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `5 1 4 6 2`, `k=3`

1. `i=0` (5): MinD`[0]`, MaxD`[0]`, Med`{5}`.
2. `i=1` (1): MinD`[1]`, MaxD`[0,1]`, Med`{1,5}`.
3. `i=2` (4): MinD`[1,2]`, MaxD`[2]`, Med`{1,4,5}`.
   - Window `[5, 1, 4]`. Min=1, Max=5, Med=4. Res=1.
4. `i=3` (6): Remove 5. Add 6.
   - MinD`[1,2,3]`, MaxD`[3]`. Med`{1,4,6}`.
   - Window `[1, 4, 6]`. Min=1, Max=6, Med=4. Res=1.
5. `i=4` (2): Remove 1. Add 2.
   - MinD`[4]`, MaxD`[3,4]`. Med`{2,4,6}`.
   - Window `[4, 6, 2]`. Min=2, Max=6, Med=4. Res=1.

Result: `1 1 1`.

## ✅ Proof of Correctness

### Invariant
Deques correctly maintain min/max candidates in `O(1)`. Dual heaps correctly maintain the median property with `O(log K)` updates.

### Why the approach is correct
Combining these standard sliding window techniques allows computing the complex metric efficiently.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** What if `K` varies?
  - *Hint:* Standard sliding window techniques don't apply directly. Segment Trees or Treaps might be needed.
- **Extension 2:** Percentile instead of Median?
  - *Hint:* Dual heaps can be generalized to two heaps of size `P x K` and `(1-P) x K`.

### Common Mistakes to Avoid

1. **Lazy Deletion Balance**
   - ❌ Wrong: Only checking `delayed` count without adjusting `smallSize`/`largeSize`.
   - ✅ Correct: Must logically track which heap the removed element belonged to.
2. **Deque Indices**
   - ❌ Wrong: Storing values in Deque.
   - ✅ Correct: Store indices to check expiry `i - k`.

## Related Concepts

- **Sliding Window Median:** The core subproblem here.
- **Monotonic Queue:** Used for Min/Max.
