---
problem_id: LNK_LECTURE_NOTES_SUBTRACT_FORWARD_FREQ__9284
display_id: LNK-016
slug: lecture-notes-subtract-forward-freq
title: "Lecture Notes Subtract Two Numbers with Digit Frequency Analysis"
difficulty: Medium
difficulty_score: 60
topics:
  - Linked List
  - Arithmetic
  - Stacks
tags:
  - linked-list
  - subtraction
  - digits
  - medium
premium: true
subscription_tier: basic
---

# LNK-016: Lecture Notes Subtract Two Numbers with Digit Frequency Analysis

## 📋 Problem Summary

You are given two non-negative integers represented as linked lists in **forward order** (most significant digit first). You need to:
1. Subtract the smaller number from the larger number.
2. Determine the sign of the result (1 if positive, 0 if zero).
3. Return the result as a linked list (forward order).
4. Count the frequency of each digit (0-9) in the result.

## 🌍 Real-World Scenario

**Scenario Title:** The Bank Ledger Audit

A bank needs to reconcile two massive ledgers. Each ledger contains a total balance that is too large to fit in a standard 64-bit integer (e.g., a country's national debt in cents). The balances are stored as linked lists of digits.
- Ledger A: `7 -> 1 -> 6` (716)
- Ledger B: `2 -> 9 -> 5` (295)

The auditor needs to find the exact difference (`421`), determine if it's a surplus or deficit, and analyze the distribution of digits in the difference for fraud detection (Benford's Law analysis).

**Why This Problem Matters:**

- **Big Integer Arithmetic:** Implementing core math operations for cryptography libraries (RSA keys are huge integers).
- **Arbitrary Precision:** Scientific computing where standard types lose precision.
- **Data Analysis:** Frequency analysis is a common first step in statistical modeling.

![Real-World Application](../images/LNK-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Subtraction with Borrow

`716 - 295`

1. **Align & Compare:** 716 > 295. Result is positive.
2. **Reverse/Stack:** Process from right to left.
   - `6 - 5 = 1`. No borrow. Result digit: 1.
   - `1 - 9`: Need borrow. `11 - 9 = 2`. Borrow = 1. Result digit: 2.
   - `7 - 2 - 1 (borrow) = 4`. Result digit: 4.
3. **Result:** `4 -> 2 -> 1`.
4. **Frequencies:** {1:1, 2:1, 4:1, others:0}.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Forward Order:** You cannot subtract easily from head to tail. You need to process from tail to head.
- **Comparison:** You must first determine which number is larger to ensure `Larger - Smaller`.
- **Leading Zeros:** If the result is `007`, return `7`. If result is `0`, return `0` (list with one node `0`).

Common interpretation mistake:

- ❌ **Wrong:** Converting to `BigInteger` or `string`.
- ✅ **Correct:** Manipulating the linked list structure (or using stacks/recursion) is the goal.

### Core Concept: Stacks for Reversal

Since the list is singly linked and forward, we can push all nodes onto stacks. Popping from the stack gives us the digits in reverse order (LSD first), allowing easy subtraction with borrow.

## Naive Approach

### Intuition

Reverse both lists. Subtract. Reverse result.

### Algorithm

1. `revA = reverse(A)`, `revB = reverse(B)`.
2. Compare `revA` and `revB` to find larger.
3. Iterate, subtracting `valA - valB - borrow`.
4. Store result in new list.
5. Reverse result list.
6. Count frequencies.

### Time Complexity

- **O(N + M)**.

### Space Complexity

- **O(N + M)** to store the reversed/result lists.

## Optimal Approach

### Key Insight

Use Stacks to avoid modifying the input lists (non-destructive).

### Algorithm

1. **Compare:**
   - If `len(A) != len(B)`, longer is larger.
   - If lengths equal, compare node by node. First non-equal determines larger.
   - If identical, return `sign=0, head=0, freq={1 at 0}`.
2. **Push to Stacks:** Push digits of Larger to `s1`, Smaller to `s2`.
3. **Subtract:**
   - While stacks not empty:
     - `val1 = s1.pop()`, `val2 = s2.pop()` (or 0 if empty).
     - `diff = val1 - val2 - borrow`.
     - If `diff < 0`: `diff += 10`, `borrow = 1`. Else `borrow = 0`.
     - Prepend `diff` to result list (build forward).
     - Update frequency map.
4. **Clean up:** Remove leading zeros.
5. Return result.

### Time Complexity

- **O(N + M)**.

### Space Complexity

- **O(N + M)** for stacks and result.

![Algorithm Visualization](../images/LNK-016/algorithm-visualization.png)
![Algorithm Steps](../images/LNK-016/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `7 1 6` - `2 9 5`

1. **Compare:** 716 > 295. Large=`716`, Small=`295`.
2. **Stacks:** `s1=[7,1,6]`, `s2=[2,9,5]`.
3. **Pop 1:** `6 - 5 - 0 = 1`. Head=`1`.
4. **Pop 2:** `1 - 9 - 0 = -8`. Borrow=1. Diff=`2`. Head=`2->1`.
5. **Pop 3:** `7 - 2 - 1 = 4`. Head=`4->2->1`.
6. **Clean:** No leading zeros.
7. **Freq:** {1:1, 2:1, 4:1}.

Result: `1`, `4 2 1`, `0 1 1 0 1 0 0 0 0 0`.

![Example Visualization](../images/LNK-016/example-1.png)

## ✅ Proof of Correctness

### Invariant
The stacks allow processing digits from least significant to most significant, correctly propagating the borrow bit.

### Why the approach is correct
- **Comparison:** Ensures we always subtract smaller from larger, avoiding negative intermediate results (except borrow).
- **Borrow Logic:** Standard elementary subtraction algorithm.
- **Leading Zeros:** Handled as a post-processing step.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Add two numbers.
  - *Hint:* Simpler, carry instead of borrow.
- **Extension 2:** Multiply two numbers.
  - *Hint:* O(N*M), much harder.
- **Extension 3:** Negative numbers support.
  - *Hint:* Check signs first. `(-A) - B = -(A+B)`.

### Common Mistakes to Avoid

1. **Comparison Logic**
   - ❌ Wrong: Comparing only lengths.
   - ✅ Correct: If lengths equal, must compare MSB to LSB.

2. **Borrow Propagation**
   - ❌ Wrong: Forgetting to subtract borrow in the next step.
   - ✅ Correct: `v1 - v2 - borrow`.

## Related Concepts

- **BigInt Arithmetic:** How Python handles large integers internally.
- **Stacks:** Reversing order of processing.
