---
problem_id: QUE_CORRIDOR_WINDOW_SECOND_MINIMUM__2748
display_id: QUE-008
slug: corridor-window-second-minimum
title: "Corridor Window Second Minimum"
difficulty: Medium
difficulty_score: 48
topics:
  - Sliding Window
  - Ordered Map
  - Queue
tags:
  - sliding-window
  - multiset
  - queue
  - medium
premium: true
subscription_tier: basic
---

# QUE-008: Corridor Window Second Minimum

## 📋 Problem Summary

For every sliding window of size `K` in a sequence of `N` integers, find the **second smallest** value.
- If the smallest value appears multiple times, the second smallest is equal to the smallest.
- If `K=1`, the second smallest is the element itself (by problem definition).

## 🌍 Real-World Scenario

**Scenario Title:** Backup Server Load Monitoring

Imagine a cluster of `K` servers handling requests.
- You monitor their CPU loads.
- The **least loaded** server (minimum) is the primary target for new jobs.
- The **second least loaded** server is the designated **failover** backup.
- If the primary crashes, you instantly switch to the backup.
- You need to know the load of this backup server at all times as the window of active servers shifts.

**Why This Problem Matters:**

- **Redundancy Planning:** Identifying the next best resource.
- **Outlier Detection:** Sometimes the absolute minimum is an error (0), so the second minimum is the true low.

![Real-World Application](../images/QUE-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Sliding Window

Values: `[6, 2, 5, 1, 7]`, `K=3`.

1. **Window 1:** `[6, 2, 5]`
   - Sorted: `2, 5, 6`
   - Min: 2, Second Min: 5.

2. **Window 2:** `[2, 5, 1]`
   - Sorted: `1, 2, 5`
   - Min: 1, Second Min: 2.

3. **Window 3:** `[5, 1, 7]`
   - Sorted: `1, 5, 7`
   - Min: 1, Second Min: 5.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `N, K`, array of integers.
- **Output:** Array of second minimums.
- **Duplicates:** If window is `[2, 2, 5]`, sorted is `2, 2, 5`. Min is 2. Second min is 2.

## Naive Approach

### Intuition

Extract window, sort, pick second element.

### Algorithm

1. Loop `i` from 0 to `n-k`.
2. Copy window.
3. Sort.
4. If `K=1` return `window[0]`, else `window[1]`.

### Limitations

- **Time Complexity:** `O(N * K log K)`.
- Too slow for `N=200,000`.

## Optimal Approach

### Key Insight

We need a data structure that maintains sorted order (or at least the bottom 2 elements) and supports efficient insertion/deletion.
- **TreeMap / Multiset:** Supports `O(log K)` insert/delete/min.
- **Two Heaps:** Possible but complex with lazy deletion.
- **Monotonic Queue:** Good for min, but hard for *second* min.

**TreeMap/Multiset Approach:**
- Maintain a frequency map of elements in the current window.
- The keys are sorted.
- The first key is the minimum.
- If the count of the first key `> 1`, the second minimum is also the first key.
- Otherwise, the second minimum is the second key.

### Algorithm

1. Use a `TreeMap<Integer, Integer>` (Java) or `multiset` (C++).
2. Initialize with first `K` elements.
3. Loop `i` from 0 to `n-k`:
   - **Query:**
     - Get first key (`min`).
     - If count(`min`) > 1, answer is `min`.
     - Else, get `higherKey(min)`, answer is that.
   - **Slide:**
     - Remove `values[i]`. If count becomes 0, remove key.
     - Add `values[i+k]`.

### Time Complexity

- **O(N log K)**.

### Space Complexity

- **O(K)**.

![Algorithm Visualization](../images/QUE-008/algorithm-visualization.png)
![Algorithm Steps](../images/QUE-008/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `6 2 5 1 7`, `k=3`

1. `i=0` (6): Heap `[(6,0)]`.
2. `i=1` (2): Heap `[(2,1), (6,0)]`.
3. `i=2` (5): Heap `[(2,1), (6,0), (5,2)]`.
   - Clean: Top (2,1) valid.
   - Pop First: (2,1).
   - Clean: Top (5,2) valid.
   - Second: 5. Res: `[5]`.
   - Push First back.
4. `i=3` (1): Heap `[(1,3), (2,1), (5,2), (6,0)]`.
   - Clean: Top (1,3) valid.
   - Pop First: (1,3).
   - Clean: Top (2,1) valid (index 1 > 3-3=0).
   - Second: 2. Res: `[5, 2]`.
   - Push First back.
5. `i=4` (7): Heap `[(1,3), (2,1), (5,2), (6,0), (7,4)]`.
   - Clean: Top (1,3) valid.
   - Pop First: (1,3).
   - Clean: Top (2,1) invalid (index 1 <= 4-3=1). Pop.
   - Clean: Top (5,2) valid.
   - Second: 5. Res: `[5, 2, 5]`.
   - Push First back.

Result: `5 2 5`.

## ✅ Proof of Correctness

### Invariant
The heap contains all elements in the current window (plus some expired ones). By lazily removing expired elements from the top, we guarantee finding the valid minimums.

### Why the approach is correct
We need the 2nd smallest. By removing the smallest, finding the next smallest, and restoring the smallest, we correctly identify the target without permanently altering the structure.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** `M`-th smallest?
  - *Hint:* Two heaps (or Order Statistic Tree) are needed for general `M`. The "pop and push back" method scales poorly (`O(M log K)`).
- **Extension 2:** Stream of data?
  - *Hint:* Same logic applies, just infinite loop.

### Common Mistakes to Avoid

1. **Destructive Pop**
   - ❌ Wrong: Popping the minimum and forgetting to push it back.
   - ✅ Correct: Must restore the state for the next window overlap.
2. **Lazy Deletion**
   - ❌ Wrong: Assuming the second element in heap array `heap[1]` is the second smallest.
   - ✅ Correct: Heap array structure is not fully sorted. Must pop to find second.

## Related Concepts

- **Priority Queue:** Core data structure.
- **Lazy Deletion:** Technique to handle removals in heaps.
