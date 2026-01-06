---
problem_id: ARR_BOUNDED_VAR__0032
display_id: ARR-028
slug: subarrays-bounded-variance
title: "Subarrays with Bounded Variance"
difficulty: Hard
difficulty_score: 55
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - counting
  - data-structures
  - searching
  - sequence-stability
  - sliding-window-max-min
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-028: Subarrays with Bounded Variance

## 📋 Problem Summary

Given an array of $n$ integers and a threshold $K$, count all contiguous subarrays where the difference between the **maximum** element and the **minimum** element in that subarray is at most $K$.

Formally, count pairs $(i, j)$ such that:
$$\max(a_i, \dots, a_j) - \min(a_i, \dots, a_j) \le K$$

**Key Requirements:**

- Subarrays must be contiguous.
- Variance is defined simply as the range (Max - Min).
- $N=200,000$ requires an extremely efficient approach.

## 🌍 Real-World Scenarios

**Scenario 1: 🌡️ Industrial Process Stability**
In a chemical manufacturing plant, a reaction is "stable" if the temperature variance remains within $K$ degrees. Engineers need to identify all possible time intervals (subarrays of the sensor log) that maintained this stability to certify the batch of product.

**Scenario 2: 📉 Financial Risk Assessment (Volatile Assets)**
A trader looks at the price of a stock over $N$ days. They want to find all periods where the stock stayed relatively "flat"—meaning the difference between its highest and lowest price during that period was small. This helps identify periods of low volatility or consolidation.

**Scenario 3: 🧱 Quality Control in Manufacturing**
A laser sensor measures the thickness of a steel sheet at regular intervals. A segment of the sheet is "Grade A" if the difference between the thickest and thinnest points in that segment is $\le K$. Counting these segments helps assess overall production quality.

**Scenario 4: 🔊 Audio Signal Normalization**
An audio compressor analyzes segments of a waveform. If a segment has a peak-to-peak amplitude (max - min) within a certain range, it doesn't need gain adjustment. Engineers count these segments to optimize the processing algorithm.

**Scenario 5: 🏃 Fitness Tracking (Consistency)**
An athlete tracks their heart rate during a marathon. A "consistent effort" phase is defined as any continuous period where the heart rate didn't fluctuate by more than $K$ BPM. Analyzing these phases helps in training strategy optimization.

### Real-World Relevance

This problem addresses **Sequence Stability**. In nearly every field of data science, we need to find intervals where the range of data is bounded, as these represent periods of consistency or controlled behavior.

## 🚀 Detailed Explanation

### 1. The Monotonicity Property

The key to avoiding $O(N^2)$ is observing how the variance behaves:

- If we have a subarray $[L, R]$ and we **expand** it to $[L, R+1]$, the maximum can only increase or stay the same, and the minimum can only decrease or stay the same. Therefore, the variance $(\text{Max} - \text{Min})$ can **only increase**.
- Conversely, if we have a subarray $[L, R]$ and we **shrink** it to $[L+1, R]$, the variance can **only decrease**.

### 2. The Two-Pointers (Sliding Window) Strategy

For every possible right endpoint $R$ in the array:

- There exists exactly one "leftmost" valid index $L_{min}$ such that the subarray $[L_{min}, R]$ satisfies the variance condition.
- Because of monotonicity, every subarray $[L, R]$ where $L_{min} < L \le R$ will **also** satisfy the condition $(\text{since it's a smaller window})$.
- The number of valid subarrays ending at $R$ is therefore $R - L_{min} + 1$.

### 3. The Challenge: Efficient Range Min/Max

As we move $R$ to the right and potentially move $L$ to the right to maintain the condition, we need to know the **current minimum and maximum** of the window in $O(1)$ time. A Segment Tree would take $O(\log N)$, but we can do even better.

### 4. The Monotonic Deque Solution

We maintain two deques (double-ended queues):

1. **Max-Deque:** Stores indices of elements in the current window in **decreasing** order of their values. The front is always the index of the maximum.
2. **Min-Deque:** Stores indices of elements in the current window in **increasing** order of their values. The front is always the index of the minimum.

**Algorithm Logic:**

- **When $R$ moves right:** Add $a[R]$ to both deques, maintaining the monotonic property by popping elements from the back that are "worse" than $a[R]$ (smaller for Max-Deque, larger for Min-Deque).
- **While $(\text{front of Max} - \text{front of Min} > K)$:** The window is too volatile. Increment $L$. If the index at the front of either deque is now outside the window (i.e., less than $L$), pop it.
- **Count:** Add $R - L + 1$ to your total.

### 🔄 Algorithm Flow Diagram

```mermaid
flowchart TD
    Start([Start]) --> Init[L = 0, totalCount = 0<br>MaxDQ = [], MinDQ = []]
    Init --> LoopR{R from 0 to n-1}

    LoopR -- Yes --> AddR[Update MaxDQ/MinDQ with index R<br>maintaining monotonic order]
    AddR --> Check{a[MaxDQ.front] - a[MinDQ.front] > K?}

    Check -- Yes (Invalid) --> ShiftL[L = L + 1<br>Remove front indices if < L]
    ShiftL --> Check

    Check -- No (Valid) --> Result[totalCount += R - L + 1]
    Result --> IncrementR[R = R + 1]
    IncrementR --> LoopR

    LoopR -- No --> End([Return totalCount])
```

## 🔍 Complexity Analysis

### Time Complexity: $O(N)$

- Every element enters each deque exactly once and leaves each deque at most once.
- The $R$ pointer moves from $0$ to $n-1$.
- Despite the "while" loop for $L$, $L$ also only moves from $0$ to $n-1$ once throughout the entire algorithm.
- Total complexity is **Amortized $O(N)$**. For $N=200,000$, this is incredibly efficient ($\sim 0.02$ seconds).

### Space Complexity: $O(N)$

- We store the $Max$ and $Min$ deques, each of which can hold up to $N$ indices in the worst case.
- No other significant memory is used besides the input array.

## 🧪 Edge Cases & Testing

### 1. $K = 0$ (Search for Constant Segments)

- **Input:** `[1, 1, 1, 2, 2]` with $K=0$.
- **Subarrays:** `[1], [1], [1], [1,1], [1,1], [1,1,1], [2], [2], [2,2]`.
- **Logic:** Only subarrays with all identical elements are counted.

### 2. Large $K$

- **Input:** `[1, 10, 100]` with $K=1000$.
- **Expectation:** All possible subarrays satisfy the condition. Total count = $n(n+1)/2 = 6$.

### 3. All Elements Identical

- **Input:** `[5, 5, 5, 5]`
- **Expectation:** Returns $10$ (every subarray is valid).

### 4. Strictly Increasing/Decreasing

- **Input:** `[1, 2, 3, 4, 5]` with $K=1$.
- **Valid:** Length 1 and Length 2 subarrays (e.g., `[1,2]`, `[2,3]`).
- **Logic:** The sliding window will naturally keep $L$ very close to $R$.

### 5. Large Negative Values

- **Input:** `[-10^9, 10^9]` with $K=10^5$.
- **Expectation:** Only single-element subarrays will be valid.

### 6. Single Element Array

- **Input:** `[42]`
- **Expectation:** returns $1$ (variance is $0 \le K$).

## ⚠️ Common Pitfalls & Debugging

**1. Deque Storing Values vs Indices**

- **Pitfall:** Storing the actual numbers in the deque.
- **Consequence:** When you increment $L$, you don't know if the maximum at the front of the deque was the element at $L-1$ or somewhere else.
- **Fix:** **Always store indices** in the deque. You can access the value using `a[deque.front()]`.

**2. Off-by-One in Count**

- **Pitfall:** Using `R - L` instead of `R - L + 1`.
- **Fix:** If $L=5$ and $R=5$, there is $5-5+1 = 1$ valid subarray.

**3. Maintaining Monotonicity Incorrectly**

- **Pitfall:** Forgetting to pop from the **back** of the deque.
- **Correct Logic for Max-Deque:** When adding $a[R]$, while $a[\text{back}] \le a[R]$, pop back. Then push $R$. This ensures the front is always the biggest.

**4. Integer Overflow**

- **Pitfall:** Using `int` for the total count.
- **Consequence:** For $N=200,000$, the count could be up to $2 \times 10^{10}$, which overflows a 32-bit integer.
- **Fix:** Use a **64-bit integer** (long/long long) for the result.

## 🎯 Variations & Extensions

### Variation 1: Longest Subarray with Bounded Variance

Instead of counting, find the length of the longest subarray.
_Solution: `maxLength = max(maxLength, R - L + 1)`._

### Variation 2: Subarrays with Variance > K

Count the number of subarrays where the range exceeds $K$.
_Solution: $\text{Total Subarrays} - \text{Subarrays with Variance} \le K$._

### Variation 3: At Most M Distinct Integers

A similar sliding window problem where the constraint is on the number of unique elements.

### Variation 4: Multiple Windows

Find all intervals where $K_1 \le (\text{Max} - \text{Min}) \le K_2$.
_Solution: Solve for $\le K_2$ and subtract the result for $\le (K_1 - 1)$._

### Variation 5: Higher Dimensions

In a 2D matrix, count subrectangles where $(\text{Max} - \text{Min}) \le K$.
_Note: Much more difficult ($O(N^3)$ or $O(N^2 \log N)$)._

## 🎓 Key Takeaways

1. **Monotonicity + Sliding Window:** The perfect combination for range-based constraints.
2. **Monotonic Deque:** The "magic" data structure that provides $O(1)$ range queries in a moving window.
3. **Index Tracking:** Storing indices in data structures is usually more robust than storing values.
4. **Counting Strategy:** For sliding window problems, the total count is often the sum of valid window lengths.

## 📚 Related Problems

- **Sliding Window Maximum:** The standalone deque challenge.
- **Longest Subarray with Absolute Diff $\le$ Limit:** (LeetCode 1438) Identical logic.
- **Shortest Subarray with Sum at least K:** Uses deques with prefix sums.
- **Count Subarrays with Sum in Range:** Combine sliding window with prefix sums.
- **ARR-014:** Subarray Score (Monotonic Stack vs Deque).
