---
problem_id: ARR_FIRST_STABLE__1122
display_id: ARR-002
slug: first-stable-increase
title: "First Stable Increase"
difficulty: Easy
difficulty_score: 10
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - comparison
  - data-structures
  - iteration
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-002: First Stable Increase

## 📋 Problem Summary

Find the first index $i$ (1-based) in an array such that there is a sequence of **three strict increases** starting at $i$. Formally, find the smallest $i$ such that:
$$a_i < a_{i+1} < a_{i+2} < a_{i+3}$$

**Key Requirements:**

- The sequence requires **four consecutive elements**.
- The increases must be **strict** (plateaus like $2, 2$ do not count).
- Return $-1$ if no such sequence exists.
- The output should be the **1-based index** of the start of this sequence.

**Example Walkthrough:**
Array: `[10, 12, 11, 14, 15, 17, 16]`

- $i=1: [10, 12, 11, 14]$ $\rightarrow$ $12 > 11$ (No)
- $i=2: [12, 11, 14, 15]$ $\rightarrow$ $12 > 11$ (No)
- $i=3: [11, 14, 15, 17]$ $\rightarrow$ $11 < 14 < 15 < 17$ (Yes!)
- Output: 3

## 🌍 Real-World Scenarios

**Scenario 1: 📈 Stock Market Trend Detection**
In high-frequency trading, a single price jump might be a fluke. Analysts often look for "stable trends" to filter out noise. A sequence of 3 consecutive increases across 4 data points might signal the start of a bullish recovery phase.

**Scenario 2: ⛰️ Geological Fault Analysis**
Sensors monitoring seismic activity record ground displacement. A "stable increase" in displacement over several consecutive measurements often precedes a minor tremor or tectonic shift. Detecting the earliest such occurrence helps in disaster early-warning systems.

**Scenario 3: 🤒 Medical Fever Monitoring**
A patient's temperature is logged hourly. If the temperature increases strictly for three consecutive hour-intervals (4 readings total), it might trigger an alert for a rapidly onset infection rather than normal metabolic fluctuations.

**Scenario 4: 🏃 Athletic Performance Gains**
An athlete tracks their pace daily. Finding the first time they improved their pace for three consecutive days identifies the precise moment their new training regimen started yielding measurable, consistent results.

**Scenario 5: 🌡️ Climate Anomaly Detection**
Meteorologists analyze daily high temperatures. A "stable increase" of three consecutive days during a transition season can mark the definitive start of a heatwave or a sudden seasonal shift.

### Real-World Relevance

Identifying the _starting point_ of a trend is a fundamental task in time-series analysis. Whether it's finance, healthcare, or engineering, the "First Stable Increase" logic allows systems to react early to emerging patterns while ignoring one-off spikes.

## 🚀 Detailed Explanation

### 1. The Sliding Window Principle

To find a pattern involving four consecutive elements, we use a "window" of size 4. We slide this window one element at a time across the array from left to right.

- **Window 1:** Indices $1, 2, 3, 4$
- **Window 2:** Indices $2, 3, 4, 5$
- **...**
- **Last Window:** Indices $n-3, n-2, n-1, n$

### 2. The Search Strategy

The goal is to find the **first** occurrence. A simple linear scan is the most efficient approach because as soon as we find a valid window, we can stop and return the result.

1. Start a loop from index $i = 0$ up to $n-4$ (using 0-based internal indexing).
2. For each $i$, check if $a[i] < a[i+1]$ and $a[i+1] < a[i+2]$ and $a[i+2] < a[i+3]$.
3. If the condition is met, return $i+1$ (the 1-based index).
4. If the loop finishes without finding anything, return $-1$.

### 3. Understanding "Strict" Increase

A common error is confusing "increasing" with "strictly increasing."

- **Increasing:** $1, 2, 2, 3$ (This has a plateau where $2=2$. This is **not** a stable increase in this problem.)
- **Strictly Increasing:** $1, 2, 3, 4$ (Every element is purely larger than the previous.)

### 4. Mathematical Complexity

This approach is highly efficient. We look at each element a constant number of times (at most 4 times, since each element can be part of up to 4 windows). This results in a linear time complexity, which is optimal for a search across an unsorted array.

### 🔄 Algorithm Flow Diagram

```mermaid
flowchart TD
    Start([Start]) --> CheckN{n < 4?}
    CheckN -- Yes --> ReturnNeg1([Return -1])
    CheckN -- No --> InitLoop[Initialize i = 0]
    InitLoop --> LoopHeader{i <= n - 4?}

    LoopHeader -- Yes --> CheckCond{a[i] < a[i+1] AND<br>a[i+1] < a[i+2] AND<br>a[i+2] < a[i+3]}
    CheckCond -- Yes --> Found[Return i + 1]
    CheckCond -- No --> Increment[i = i + 1]
    Increment --> LoopHeader

    LoopHeader -- No --> ReturnFinalNeg1([Return -1])
```

## 🔍 Complexity Analysis

### Time Complexity: $O(N)$

- We iterate through the array once, from index $0$ to $n-4$.
- At each step, we perform exactly 3 comparisons.
- In the worst case (no valid sequence exists), we perform $3 \times (n-3)$ comparisons.
- This simplifies to $O(N)$.

### Space Complexity: $O(1)$

- We only use a single loop counter $i$.
- We do not store any additional data structures or copies of the array.
- The amount of memory used does not grow with the input size.

## 🧪 Edge Cases & Testing

### 1. Minimal Size ($n < 4$)

- **Input:** `n=3, [1, 5, 10]`
- **Expectation:** Return `-1`. There aren't enough elements to form a 4-element sequence.

### 2. Sequence at the Very Start

- **Input:** `[1, 2, 3, 4, 0, 0, 0]`
- **Expectation:** Return `1`. The algorithm should return the _earliest_ index.

### 3. Sequence at the Very End

- **Input:** `[10, 10, 10, 1, 2, 3, 4]`
- **Expectation:** Return `4`. The algorithm must scan until the very last possible window.

### 4. Non-Strict Increases (Plateaus)

- **Input:** `[1, 2, 2, 3, 4, 5]`
- **Expectation:** Return `3`. Even though `1, 2, 2, 3` starts at index 1, it's not strictly increasing. The first valid sequence is `2, 3, 4, 5` starting at index 3.

### 5. All Equal Elements

- **Input:** `[7, 7, 7, 7, 7]`
- **Expectation:** Return `-1`. No increases occur.

### 6. Strictly Decreasing Array

- **Input:** `[10, 9, 8, 7, 6]`
- **Expectation:** Return `-1`.

### 7. Large Values (Overflow check)

- **Input:** `[-10^9, 0, 10^9, 10^9 + 1]`
- **Expectation:** Return `1`. Ensure comparisons handle large integers correctly (though standard 64-bit integers found in most languages handle this).

## ⚠️ Common Pitfalls & Debugging

**1. 0-based vs 1-based Indexing**

- **Pitfall:** Returning the index from your code loop (usually 0, 1, 2...) directly.
- **Fix:** Always add 1 to your internal index before returning to match the problem's 1-based output requirement.

**2. Loop Boundary Conditions**

- **Pitfall:** `i < n` or `i < n-1`.
- **Fix:** Accessing `a[i+3]` when `i = n-1` will cause an "Index Out of Bounds" error. Ensure the loop stops at `i <= n-4`.

**3. Strict Inequality Error**

- **Pitfall:** Using `<=` instead of `<`.
- **Fix:** If the problem asks for "increases," it usually means strict ($a < b$). If it meant "non-decreasing," it would use $a \le b$. Double-check the wording.

**4. Short-Circuiting Evaluations**

- In languages like C++, Java, or Python, using `if (a < b && b < c && c < d)` is efficient because if $a < b$ is false, the computer won't even waste time checking $b < c$.

## 🎯 Variations & Extensions

### Variation 1: First Stable Decrease

Instead of increases, find the first sequence where $a_i > a_{i+1} > a_{i+2} > a_{i+3}$.
_Application: Identifying the start of a market crash._

### Variation 2: Stable Increase of Length $K$

Instead of a fixed length 3 (4 elements total), find the first sequence of $K-1$ increases starting at $i$. This requires a nested loop or a counter-based approach.

### Variation 3: Counting All Stable Increases

Find the total _number_ of windows that satisfy the stable increase condition.
_Application: Measuring how many distinct "growth phases" an economy had._

### Variation 4: Longest Stable Increase

Instead of the first occurrence, find the _longest_ continuous sequence of strict increases.
_Solution: Requires tracking a current "streak" counter._

### Variation 5: Almost-Stable Increase

Find a sequence where $a_i < a_{i+1} < a_{i+2} < a_{i+3}$, but allow at most **one** plateau or decrease.

## 🎓 Key Takeaways

1. **Linear Scan:** The simplest tool is often the most effective for O(N) search problems.
2. **Window Management:** When a pattern involves $K$ elements, your search space is limited to $N - (K-1)$ starting points.
3. **Stop Fast:** For "First Occurrence" problems, return immediately upon success to save time.
4. **Boundary Verification:** Always test the extreme start and extreme end of your input.

## 📚 Related Problems

- **ARR-018:** Circular Peak Detection (Pattern detection in circular arrays)
- **ARR-023:** Longest Zigzag Subarray (Alternating pattern patterns)
- **Subarray Sum Equals K:** Window-based sum patterns
- **Longest Increasing Subsequence (LIS):** A more complex, non-contiguous version of this problem.
