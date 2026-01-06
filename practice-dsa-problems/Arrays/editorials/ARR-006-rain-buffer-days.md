---
problem_id: ARR_RAIN_BUFFER__1106
display_id: ARR-006
slug: rain-buffer-days
title: "Rain Buffer Days"
difficulty: Easy
difficulty_score: 15
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - counting
  - data-structures
  - iteration
  - pattern-recognition
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-006: Rain Buffer Days

## 📋 Problem Summary

Given an array of $n$ integers representing sequential data (e.g., daily rainfall/sunlight), you need to identify and count specific "Three-Day Patterns" called **Rain Buffer Days**.

A day $i$ is a Rain Buffer Day if:

1. It is a **Rainfall Day**: $a_i < 0$.
2. It is followed by **Two Recovery Days**: $a_{i+1} > 0$ AND $a_{i+2} > 0$.

Essentially, we are counting occurrences of the pattern: **(Negative, Positive, Positive)**.

**Key Constraints:**

- $1 \le n \le 200,000$.
- The pattern requires three indices ($i, i+1, i+2$), so indices too close to the end of the array ($n-1, n-2$) cannot be Rain Buffer Days.
- Strict inequalities ($< 0$ and $> 0$) mean that a value of $0$ is neither negative nor positive.

## 🌍 Real-World Scenarios

**Scenario 1: 🌱 The Fragile Seedling Growth (Hydration + Recovery)**
In ecology, certain seedlings require a burst of moisture to germinate but will rot if the soil remains soggy. A "Successful Germination" occurs only when a rainy day ($a_i < 0$) is followed by two consecutive clear, sunny days ($a_{i+1}, a_{i+2} > 0$) to dry the topsoil and stimulate root growth. Scientists use this calculation to estimate the yield of a specific planting season.

**Scenario 2: 📉 Stock Market "Dead Cat Bounce" vs. Recovery**
Traders look for patterns where a "Red Day" (negative return) is followed by two "Green Days" (positive returns). This 3-day sequence is often used as a simple indicator of a trend reversal or a "Stabilized Recovery," suggesting that the initial dip was just a "Rain Buffer" rather than the start of a deep crash.

**Scenario 3: 💊 Patient Recovery Monitoring (Fever/Normal)**
A hospital monitors a patient's temperature relative to the baseline. A "Fever Break" is recorded if a day of high fever (negative deviation from healthy state) is followed by two days of normal, healthy temperature (positive stability). Counting these events helps doctors assess how well a treatment plan is working over months of data.

**Scenario 4: 🧪 Chemical Saturation Cycles**
In a chemical reactor, an "Acidity Spike" ($< 0$) needs to be buffered by two cycles of base-neutralization ($> 0$, $> 0$) to reset the system. If the third day isn't positive, the system enters an "Acid Loop." Finding the number of successfully buffered spikes is crucial for reactor maintenance.

**Scenario 5: 🔋 Battery Voltage Stabilization**
When a high-power device is unplugged, the voltage might dip ($< 0$). The system is "Stable" if the dip is followed by two consecutive intervals of rising or stable positive voltage ($> 0$). An engineer counts these "successful buffers" to measure the quality of the voltage regulator.

### Real-World Relevance

The Rain Buffer Day is a primitive form of **Sequential State Verification**. In many systems, a "negative" event is only safe or useful if it is followed by a "positive" recovery period. Detecting these sequences helps in risk assessment and trend analysis.

## 🚀 Detailed Explanation

### 1. The Sliding Window Perspective

Instead of looking at individual numbers, we look at a **window of three elements** starting at index $i$:
$$[a_i, a_{i+1}, a_{i+2}]$$

We slide this window across the array, one index at a time.

- At $i=0$, we look at $(a_0, a_1, a_2)$.
- At $i=1$, we look at $(a_1, a_2, a_3)$.
- At $i=n-3$, we look at $(a_{n-3}, a_{n-2}, a_{n-1})$.

Any window starting _after_ $n-3$ is too small to contain the required three elements.

### 2. The Logic Filter

For each window, we apply three strict filters:

1. `filter1`: is the first element negative?
2. `filter2`: is the second element positive?
3. `filter3`: is the third element positive?

If `filter1 AND filter2 AND filter3` is true, the counter increases.

### 3. Handling Zeroes

A common mistake in logic problems is treating $a_i \le 0$ as "not positive." In this specific problem:

- $a_i = 0$ is **NOT** a rain day ($0 < 0$ is False).
- $a_i = 0$ is **NOT** a recovery day ($0 > 0$ is False).
  Zeros effectively act as "Neutral Days" that always break the required pattern.

### 🔄 Algorithm Flow Diagram

```mermaid
flowchart TD
    Start([Start]) --> Init[count = 0]
    Init --> Loop{i from 0 to n-3}

    Loop -- Next --> RainCheck{a[i] < 0?}
    RainCheck -- Yes --> Recovery1{a[i+1] > 0?}
    Recovery1 -- Yes --> Recovery2{a[i+2] > 0?}

    Recovery2 -- Yes --> Match[Increment count]
    Match --> Loop

    RainCheck -- No --> Loop
    Recovery1 -- No --> Loop
    Recovery2 -- No --> Loop

    Loop -- Done --> End([Return count])
```

## 🔍 Complexity Analysis

### Time Complexity: $O(N)$

- We perform a single linear scan from $0$ to $n-3$.
- In each step, we perform at most 3 numerical comparisons.
- Total complexity: $O(N)$. For $N=200,000$, this takes roughly $0.01$ seconds.

### Space Complexity: $O(1)$

- We only store a few primitive variables (the counter and the loop index).
- No extra arrays or data structures are needed beyond the input storage.

## 🧪 Edge Cases & Testing

### 1. Array Length too Short

- **Input:** `[-1, 5]`, $n=2$
- **Logic:** The loop condition $i \le n-3$ (which is $0 \le -1$) is never met.
- **Expectation:** Return `0`.

### 2. Back-to-Back Patterns (Overlapping)

- **Input:** `[-1, 5, 2, 4, 1]`
- **Logic:** Window at 0: `(-1, 5, 2)` $\rightarrow$ **MATCH**. Next window is `(5, 2, 4)` $\rightarrow$ No.
- **Note:** Patterns can overlap in indices, but the Rain Buffer Day is specifically about the _start_ index $i$. An index $i+1$ can be part of the buffer for $i$ and also potentially a rain day itself?
- **Let's check:** `[-1, 5, -2, 4, 3]`.
  - Window 0: `(-1, 5, -2)` $\rightarrow$ **FAIL** (last element is negative).
  - Window 2: `(-2, 4, 3)` $\rightarrow$ **MATCH**.
  - Result: 1.

### 3. All Rainfall or All Recovery

- **Input:** `[-1, -2, -3]` or `[1, 2, 3]`
- **Expectation:** Return `0`.

### 4. Zero Interruption

- **Input:** `[-1, 0, 5]`
- **Expectation:** Return `0`. The zero prevents the first recovery day from being strictly positive.

### 5. Pattern at the Very End

- **Input:** `[1, 1, -1, 2, 3]` (size 5).
- **Match:** $i=2$ (`-1, 2, 3`). Since $2 \le 5-3$, this is the last valid starting index.
- **Expectation:** Return `1`.

## ⚠️ Common Pitfalls & Debugging

**1. Out-of-Bounds Access**

- **Pitfall:** `for (int i=0; i < n; i++)` and checking `a[i+1]`.
- **Consequence:** When $i=n-1$, $a[i+1]$ is out of bounds. The code will crash or return garbage values.
- **Fix:** Always limit your loop to $n-3$.

**2. Non-Strict Inequalities**

- **Pitfall:** Using `a[i] <= 0` or `a[i] >= 0`.
- **Reason:** $0$ is neither negative nor positive. If you include it, you'll miscount "Neutral" days as valid rain or recovery days.

**3. Resetting the Loop on Match**

- **Pitfall:** Skipping indices after a match (e.g., `i = i + 3`).
- **Reason:** The problem asks to check every day $i$. Even if day 1 is a buffer, day 2 should still be checked as a potential start of another buffer (unlikely for this specific pattern but a bad habit for others).

**4. Integer Range**

- **Pitfall:** Comparing $a_i$ assuming it's small.
- **Warning:** $a_i$ can be $10^9$. Standard 32-bit integers are fine for comparison, and the result (count) can be up to $200,000$, which also fits in 32-bit.

## 🎯 Variations & Extensions

### Variation 1: $K$-Day Buffer

A day $i$ is a buffer if it's rainy and followed by **$K$** consecutive sunny days.
_Note: This makes the logic more dynamic ($O(NK)$ or $O(N)$ with a sliding count)._

### Variation 2: Weighted Recovery

The sum of the two recovery days must be greater than the magnitude of the rain day.
_Condition: $a_{i+1} + a_{i+2} > |a_i|$._

### Variation 3: At Most $M$ Failures

Allow up to $M$ days of rain in the buffer period as long as the total remains positive.

### Variation 4: Rolling Window Threshold

A buffer isn't two days, but rather a 7-day window where the _average_ temperature is positive.

### Variation 5: Multi-State Patterns

Count patterns of (Rain, Sunny, Cloudy, Sunny).

## 🎓 Key Takeaways

1. **Window Boundaries:** The most common bug in array pattern problems is checking indices that don't exist.
2. **Logic Completeness:** Multi-condition filters are best handled as a sequence of early-exit "if" statements or a single clean boolean expression.
3. **Strictness:** Pay attention to "Greater than" vs "Greater than or equal to," especially regarding the number zero.
4. **Linearity:** Pattern matching in arrays is almost always $O(N)$.

## 📚 Related Problems

- **ARR-003:** Alternating Parity (2-element sequential pattern).
- **ARR-002:** First Stable Increase (4-element sequential pattern).
- **Three-Sum Problem:** Non-sequential pattern matching.
- **Valid Mountain Array:** Sequential trend recognition.
- **Sliding Window Maximum:** More complex window analytics.
