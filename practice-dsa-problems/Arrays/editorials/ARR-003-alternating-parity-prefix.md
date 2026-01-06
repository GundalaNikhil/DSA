---
problem_id: ARR_ALT_PARITY__3920
display_id: ARR-003
slug: alternating-parity-prefix
title: "Alternating Parity Prefix"
difficulty: Easy
difficulty_score: 18
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - bitwise-logic
  - coding-interviews
  - data-structures
  - parity
  - prefix
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-003: Alternating Parity Prefix

## 📋 Problem Summary

Given an array of $n$ integers, identify the length of the longest **prefix** (starting from the first element) where the parity of adjacent elements strictly alternates (Even, then Odd, then Even... or vice-versa).

**Key Rules:**

- A prefix of length 1 is always valid.
- The alternation must start from the very first element.
- Parity is defined by whether a number is divisible by 2.
- Stop counting as soon as two adjacent elements share the same parity.

**Example:**
Input: `[4, 7, 2, 8, 9]`

- 4 (Even)
- 7 (Odd) - Alternates!
- 2 (Even) - Alternates!
- 8 (Even) - **Same as 2!** Stop here.
  Result: 3

## 🌍 Real-World Scenarios

**Scenario 1: 🔗 The Magnetic Link Chain**
Imagine you have a bucket of magnets. Some have the North pole (Even) facing out, others have the South pole (Odd). Magnets will only stick together if you alternate poles: `N-S-N-S`. If you try to join two Norths or two Souths, they repel. The "Alternating Parity Prefix" is the length of the longest chain you can build starting from your first magnet before a repulsion occurs.

**Scenario 2: 🧶 Textile Weaving (Over-Under Pattern)**
In mechanical weaving, a thread must go **Over** (Even) and **Under** (Odd) the cross-threads. If the machine makes a mistake and tries to go "Over-Over," the structural integrity of the fabric is compromised at that point. We want to find how much of the fabric was woven correctly from the start.

**Scenario 3: 🚦 Traffic Light Validation**
A city's traffic logs record state changes. A valid sequence from the start of the day must strictly alternate between `GO` (Odd) and `STOP` (Even) signals. An "Alternating Parity Prefix" check detects the first point of failure in the signaling logic.

**Scenario 4: 🔌 Alternating Current (AC) Phase Detection**
Electrical sensors record pulses. In some phases, pulses must strictly alternate between positive-offset (Odd) and negative-offset (Even) parity bytes. A system monitor finds the longest valid data stream starting from the synchronization pulse.

**Scenario 5: 🎤 Rhythm Game Scoring (Perfect Streaks)**
In a rhythm game, a player must alternate between "Left" (Even) and "Right" (Odd) buttons. Their "Early Accuracy Streak" is the number of notes they correctly alternated from the beginning of the song.

### Real-World Relevance

Alternation is proof of **Systematic Variation**. Many natural and mechanical processes rely on binary states flipping at every step. Detecting the first break in this pattern is a fundamental diagnostic tool.

## 🚀 Detailed Explanation

### 1. Parity: The Modulo vs. Bitwise Approach

To check if a number is even or odd, we have two main mathematical tools:

- **Modulo Operator (`%`):** `x % 2` returns 0 for even, and 1 or -1 for odd.
- **Bitwise AND (`&`):** `x & 1` returns 0 for even and 1 for odd.

**Why Bitwise is Often Better:**
In many programming languages, `-5 % 2` results in `-1`, which can complicate your `if` statements. However, bitwise operators look at the binary digits. For any integer (positive or negative), the last bit is `0` if it's even and `1` if it's odd.

- `...010` (2) $\rightarrow$ `& 1` is `0`
- `...011` (3) $\rightarrow$ `& 1` is `1`
- `...111` (-1) $\rightarrow$ `& 1` is `1`

### 2. The Linear Scan Strategy

Since the condition must hold strictly from the start, we don't need complex data structures. We just walk through the array.

1. Set `currentLength = 1`.
2. Look at the second element and compare its parity with the first.
3. If they are different, increase the length and move to the third.
4. If they are the same, **immediately stop**. Once a prefix is broken, it can never be extended further.

### 3. Mathematical Intuition

This is a "Short-Circuit" algorithm. We are looking for the **first failure**.
Mathematically, we are finding the smallest index $i$ where $P(a_i) = P(a_{i+1})$, where $P$ is the parity function. The answer is then $(i+1)$.

### 🔄 Algorithm Flow Diagram

```mermaid
flowchart TD
    Start([Start]) --> CheckN{n == 0?}
    CheckN -- Yes --> Return0([Return 0])
    CheckN -- No --> Init[length = 1]

    Init --> Loop{i from 1 to n-1}
    Loop -- Next --> ParityCheck{a[i] & 1 != a[i-1] & 1?}

    ParityCheck -- Yes --> Inc[length = length + 1]
    Inc --> Loop

    ParityCheck -- No --> Break[Break Loop]
    Loop -- Done --> End([Return length])
    Break --> End
```

## 🔍 Complexity Analysis

### Time Complexity: $O(N)$

- In the worst case (the entire array alternates), we visit every element once.
- In the best case (the first two elements have the same parity), we only check two elements.
- Average/Worst case: $O(N)$. For $N=200,000$, this is nearly instantaneous.

### Space Complexity: $O(1)$

- We only need one counter variable (`length` or `i`).
- We do not create any new arrays or use recursive calls.

## 🧪 Edge Cases & Testing

### 1. Single Element Array

- **Input:** `[42]`
- **Expectation:** Return `1`. A single element always "alternates" with a non-existent predecessor.

### 2. Immediate Failure

- **Input:** `[2, 4, 6, 8]`
- **Expectation:** Return `1`. The second element `4` has the same parity as `2`.

### 3. All Odd or All Even

- **Input:** `[1, 3, 5]` or `[2, 4, 6]`
- **Expectation:** Return `1`.

### 4. Negative Values

- **Input:** `[-2, 3, -4, 5]`
- **Expectation:** Return `4`. The alternation property should hold regardless of signs.
- **Note:** Ensure your code handles `-4 % 2` vs `3 % 2` correctly if using modulo.

### 5. Large Array with Alternation until End

- **Input:** `[1, 2, 1, 2, ..., 1, 2]` ($200,000$ elements).
- **Expectation:** Return $200,000$.

### 6. Zero as an Element

- **Input:** `[0, 1, 0, 1]`
- **Expectation:** Return `4`. Zero is mathematically Even.

## ⚠️ Common Pitfalls & Debugging

**1. Modulo with Negative Numbers**

- **Pitfall:** `if (a[i] % 2 == 1 && a[i-1] % 2 == 0)`.
- **Reason:** If `a[i] = -3`, then `-3 % 2` might be `-1`. Your check for `== 1` will fail.
- **Fix:** Use `(a[i] % 2 != a[i-1] % 2)` or bitwise `((a[i] & 1) != (a[i-1] & 1))`.

**2. Loop Overflow**

- **Pitfall:** Starting from `i = 0` and checking `a[i]` against `a[i+1]`.
- **Reason:** When `i = n-1`, `a[i+1]` will access memory out of bounds.
- **Fix:** Start from `i = 1` and check against `a[i-1]`.

**3. Initializing Length to 0**

- **Pitfall:** `length = 0`.
- **Fix:** Since a non-empty array always has a valid prefix of at least length 1, starting at 1 is more logical.

**4. Miscounting "Indices" vs "Length"**

- **Pitfall:** If the failure is at 0-based index `5`, the length of the valid part is `5`. (indices $0, 1, 2, 3, 4$).

## 🎯 Variations & Extensions

### Variation 1: Longest Alternating Subarray

Find the longest alternating segment **anywhere** in the array, not just at the start.
_Solution: Requires a sliding window or a "streak" counter ($O(N)$)._

### Variation 2: Longest Alternating Subsequence

Find the longest sequence of elements (not necessarily contiguous) that alternate parity.
_Solution: Greedy approach ($O(N)$) or DP._

### Variation 3: Alternating Parity with $K$ "Lives"

Find the longest prefix that alternates, but allow up to $K$ mistakes.

### Variation 4: Multi-Base Alternation

Instead of Even/Odd, check if numbers alternate between `mod 3 == 0`, `mod 3 == 1`, and `mod 3 == 2`.

### Variation 5: Almost-Alternating Prefix

The sequence alternates parity, but allow up to one pair of same-parity elements if they are both zero.

## 🎓 Key Takeaways

1. **Linear Prefix Search:** Problems asking for "Longest Prefix" are often $O(N)$ and allow early exit.
2. **Parity Implementation:** Bitwise `& 1` is more robust for negative numbers than `% 2`.
3. **Short-Circuiting:** Efficiency comes from stopping the moment a rule is violated.
4. **Boundary Checks:** Always ensure your iteration stays within $0$ and $n-1$.

## 📚 Related Problems

- **ARR-002:** First Stable Increase (Checking for a window of patterns).
- **ZigZag Subsequence:** A more complex pattern based on relative values ($> < > <$).
- **Valid Mountain Array:** Checking for a single rise and single fall.
- **Check if Array is Monotonic:** Simple sequential relationship check.
