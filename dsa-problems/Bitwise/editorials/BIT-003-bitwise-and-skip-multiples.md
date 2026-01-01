---
problem_id: BIT_AND_SKIP_MULTIPLES__8403
display_id: BIT-003
slug: bitwise-and-skip-multiples
title: "Bitwise AND Skipping Multiples"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - AND
  - Number Theory
  - Mathematics
tags:
  - bitwise
  - and-operation
  - number-theory
  - medium
premium: true
subscription_tier: basic
---

# BIT-003: Bitwise AND Skipping Multiples

## 📋 Problem Summary

Compute the Bitwise AND of all integers in the range `[L, R]` that are **not** divisible by `m`. If no such numbers exist, return -1.

## 🌍 Real-World Scenario

**Scenario Title:** The Secure Channel Hopping

You are configuring a frequency hopping spread spectrum system.
- **Spectrum**: Channels are numbered `L` to `R`.
- **Interference**: Some channels are blocked by a strong 50Hz hum harmonic (multiples of `m`).
- **Configuration**: You need to set a "Master Mask" that defines the bits that are *always* 1 across all valid hops. This helps the receiver synchronize.
- **Goal**: Calculate the AND of all valid channel IDs to find the stable bits.

**Why This Problem Matters:**

- **Range Queries**: Efficiently aggregating properties over large intervals.
- **Sparse Data**: Dealing with data that has regular "holes".
- **Bitwise Logic**: Understanding how `AND` converges to the common prefix.

![Real-World Application](../images/BIT-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Skipping Pattern
```
L=10, R=15, m=3
Range: 10, 11, 12, 13, 14, 15
Skip multiples of 3: 12, 15.

Valid Numbers:
10: 1 0 1 0
11: 1 0 1 1
13: 1 1 0 1
14: 1 1 1 0

AND Calculation:
Col 3 (8s): 1, 1, 1, 1 -> 1
Col 2 (4s): 0, 0, 1, 1 -> 0
Col 1 (2s): 1, 1, 0, 1 -> 0
Col 0 (1s): 0, 1, 1, 0 -> 0

Result: 1 0 0 0 (8)
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **L, R**: 64-bit integers.
- **m**: Integer up to 1,000,000.
- **-1**: If `[L, R]` has no valid numbers (e.g. `L=3, R=3, m=3`), return -1.

Common interpretation mistake:

- ❌ Using `(L & R)` or standard range AND shortcut immediately.
- ✅ realizing that skipping numbers *might* keep some bits as 1 that would otherwise become 0 (e.g., if we skip all even numbers).

### Core Concept: Convergence of AND

The bitwise AND of a continuous range `[L, R]` is determined by the common high-order bits of `L` and `R`. The lower bits become 0 quickly because the range usually includes numbers with 0 and 1 at those positions.
Skipping multiples of `m` preserves this property unless `m` is related to bit positions (e.g., `m=2` removes all even numbers, forcing bit 0 to stay 1).

### Why Naive Approach is too slow

Looping `L` to `R` takes O(R-L). Since `R-L` can be `10^12`, this TLEs.
However, `m` is small. The pattern of multiples repeats every `m`. The bitwise AND converges very fast.

## Naive Approach (Linear Scan)

### Intuition

Loop through all valid numbers and AND them.

### Algorithm

1. `ans = -1` (All 1s).
2. `found = false`
3. loop `i` from `L` to `R`:
   - if `i % m != 0`:
     - `ans &= i`
     - `found = true`
4. Return `found ? ans : -1`

### Time Complexity

- **O(R - L)**. Good if range is small, unused if large.

### Space Complexity

- **O(1)**.

## Optimal Approach (Hybrid)

### Key Insight

1. **Small Range**: If `R - L` is small (e.g., `< 2*10^6`), use the naive scan. It's fast enough.
2. **Large Range**: If `R - L` is huge, the range contains many full cycles of `m`.
   - The result is simply the **Standard Range AND** of `[L, R]`, with one exception.
   - **Exception**: If `m=2`, we remove all even numbers. Valid numbers are all Odd. Bit 0 will be 1.
   - For all `m > 2`, we retain enough variation in parity and bit positions that the result matches the Standard Range AND (Common Prefix followed by 0s).

### Algorithm

1. **Constraint Check**: `limit = 5 * m` (or fixed `2*10^6`).
2. If `R - L <= limit`:
   - Run Naive Loop.
3. Else:
   - Calculate Standard Range AND:
     - Find MSB where `L` and `R` differ.
     - Mask out all bits below that MSB.
     - `RangeAND = L & Mask`.
   - If `m == 2`: `RangeAND |= 1`.
   - Return `RangeAND`.

Note: The threshold `limit` ensures we don't miss edge cases where specific bit patterns align with multiples. Since AND reduces bits, once the range is large, the "Standard AND" zeros dominate.

### Time Complexity

- **O(min(R-L, m))**. Worst case O(m).

### Space Complexity

- **O(1)**.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `L=10, R=15, m=3`.
Range Small (`5 <= 2e6`). Run Loop.
- 10: `1010` (Valid). Ans=1010.
- 11: `1011` (Valid). Ans = 1010 & 1011 = `1010`.
- 12: Skip.
- 13: `1101` (Valid). Ans = 1010 & 1101 = `1000`.
- 14: `1110` (Valid). Ans = 1000 & 1110 = `1000`.
- 15: Skip.
Result: 8. Matches Example.

**Large Case**: `L=16 (10000), R=31 (11111), m=2`.
Loop huge? No, here small.
Common Prefix of 16, 31: `10000` (16).
`m=2` -> Result `16 | 1 = 17`.
Is `17` correct?
Valid: 17, 19, 21, ..., 31.
All have bit 4 set (value 16) and bit 0 set (odd).
Lower bits (1, 2, 3) vary and will AND to 0.
Result: `10001` (17).

## ✅ Proof of Correctness

### Invariant

For range `[L, R]`, bits below the common prefix cycle through `0` and `1`. Deleting sparse numbers (multiples of `m > 2`) cannot prevent us from seeing at least one `0` in every bit position below the prefix, provided the range is large enough (`> m`).
Case `m=2` is the only dense deletion pattern that systematically removes `0`s from bit 0.

## 💡 Interview Extensions (High-Value Add-ons)

- **Range OR**: Logic is symmetric (find common prefix, rest 1s).
- **Count Set Bits**: Population count in usage.

## Common Mistakes to Avoid

1. **Off-by-one**:
   - ❌ `i < R` loop.
   - ✅ `i <= R`.
2. **Infinite Loop**:
   - ❌ `while (l != r)` with regular Ints could overflow if not careful (but right shift converges).

