---
problem_id: BIT_COUNT_SETBITS_INDEXED_XOR__8407
display_id: BIT-007
slug: count-set-bits-indexed-xor
title: "Count Set Bits Of Indexed XOR"
difficulty: Medium
difficulty_score: 50
topics:
  - Bitwise Operations
  - XOR
  - Bit Counting
  - Mathematics
tags:
  - bitwise
  - xor
  - popcount
  - mathematics
  - medium
premium: true
subscription_tier: basic
---

# BIT-007: Count Set Bits Of Indexed XOR

## 📋 Problem Summary

Given an array `a` of size `n`, compute the total number of set bits (1s) in the values `b[i] = i ^ a[i]` for all `0 <= i < n`.

## 🌍 Real-World Scenario

**Scenario Title:** The Hamming Distance Checksum

You are verifying data integrity across a communication bus.
- **Reference**: The bus slot index `i` (0, 1, 2...) represents the expected control signal pattern.
- **Received**: The actual signal received at slot `i` is `a[i]`.
- **metric**: You need to calculate the total "bit flips" (Hamming distance) between the expected indices and the received values across the entire transmission.
- **Goal**: Compute this total error count efficiently to trigger a re-transmission if it exceeds a threshold.

**Why This Problem Matters:**

- **Hamming Distance**: `Popcount(x ^ y)` is the definition of Hamming distance.
- **Efficiency**: Using hardware-accelerated instructions (like `__builtin_popcount`) vs manual loops.
- **Aggregation**: Summing properties over an array.

![Real-World Application](../images/BIT-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: XOR and Popcount
```
Index i:  0 (00)   1 (01)
Value a:  0 (00)   2 (10)

XOR sums:
i=0: 00 ^ 00 = 00. Bits = 0.
i=1: 01 ^ 10 = 11. Bits = 2.

Total = 0 + 2 = 2.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Index**: 0-based index `i`.
- **Values**: `a[i]` up to `10^9`.
- **Constraint**: `n` up to `200,000`.

Common interpretation mistake:

- ❌ Forgetting to XOR with the index `i`.
- ✅ The value to inspect is `i ^ a[i]`.

### Core Concept: Popcount

The "population count" or "Hamming weight" is the number of 1s in the binary representation.
Most modern languages and CPUs provide built-in functions to compute this in O(1) or close to it.

### Why Naive Approach is too slow

Manual bit extraction (`while n > 0: n &= n-1`) is reasonably fast (O(number of set bits)). Since integers are 32-bit, this is effectively O(1). Thus, even the "Naive" manual approach is optimal in time complexity O(N), but built-ins are faster in practice.

## Naive Approach (Manual Bit Counting)

### Intuition

For each element, manually count bits by shifting or clearing LSB.

### Algorithm

1. `total = 0`.
2. Loop `i` from 0 to `n-1`:
   - `val = i ^ a[i]`.
   - `cnt = 0`.
   - While `val > 0`:
     - `val &= (val - 1)` (Kernighan's Algorithm)
     - `cnt++`.
   - `total += cnt`.
3. Return `total`.

### Time Complexity

- **O(N * 30)**.

### Space Complexity

- **O(1)**.

## Optimal Approach (Built-in Popcount)

### Key Insight

Use language intrinsics which often map to the `POPCNT` CPU instruction.

### Algorithm

1. `total = 0`.
2. Loop `i` from 0 to `n-1`:
   - `total += popcount(i ^ a[i])`.
3. Return `total`.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/BIT-007/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-007/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `a = [0, 2]`.
Index 0: `0 XOR 0 = 0`. Bits: 0.
Index 1: `1 XOR 2 = 3` (11). Bits: 2.
Total = 2.

## ✅ Proof of Correctness

### Invariant

The problem definition is a straightforward summation of a deterministic function `f(i, a[i])`. Correctness relies solely on the correctness of the XOR and Popcount implementations.

## 💡 Interview Extensions (High-Value Add-ons)

- **Sum over Range**: Calculate `Sum of Popcount(i)` for `i` in `[0, N]`. (O(log N) digit DP).
- **Pairwise Hamming**: Sum Hamming distances for all pairs (check contribution of each bit position).

## Common Mistakes to Avoid

1. **JS Bitwise handling**:
   - ❌ JS treats numbers as 32-bit signed in bitwise ops. If `a[i]` uses bit 31, it becomes negative.
   - ✅ Unsigned right shift `>>>` usually fixes, but inputs are positive ints <= 10^9 (fits in 30 bits). Safe.

## Related Concepts

- **Hamming Distance**: Fundamental metric.
- **Brian Kernighan's Algorithm**: `n &= (n-1)` to count set bits.
