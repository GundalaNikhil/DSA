---
problem_id: BIT_SWAP_ADJACENT_2BIT_BLOCKS__8415
display_id: BIT-015
slug: swap-adjacent-2bit-blocks
title: "Swap Adjacent 2-Bit Blocks"
difficulty: Easy-Medium
difficulty_score: 35
topics:
  - Bitwise Operations
  - Bit Manipulation
  - Masking
tags:
  - bitwise
  - bit-swapping
  - masking
  - easy
premium: true
subscription_tier: basic
---

# BIT-015: Swap Adjacent 2-Bit Blocks

## 📋 Problem Summary

Given a 32-bit integer `x`, swap every adjacent pair of 2-bit blocks. Specifically, swap bits `[0, 1]` with `[2, 3]`, bits `[4, 5]` with `[6, 7]`, and so on.

## 🌍 Real-World Scenario

**Scenario Title:** The Byte-Order Correction (Endianness Variant)

You are processing a raw data stream from a legacy hardware device.
- **Protocol**: The device transmits data in "nibble-swapped" chunks, but with a twist: it swaps 2-bit sub-nibbles instead of full 4-bit nibbles.
- **Goal**: You need to efficiently normalize the data stream by restoring the correct 2-bit block ordering.
- **Constraints**: This operation runs on a high-throughput router, so you cannot iterate bits. You need a constant-time bitwise solution (O(1)).

**Why This Problem Matters:**

- **Parallel Bit Ops**: Demonstrates how to operate on multiple data chunks simultaneously (SIMD-like logic using standard registers).
- **Masking**: Fundamental skill for isolating specific bit patterns (`0x33333333`).
- **Binary Arithmetic**: Understanding how shifting affects positions.

![Real-World Application](../images/BIT-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Swapping Logic
```
Value: 6 (00 00 ... 01 10)
Block Indices: ... 1  0
Bits:          ... 32 10

Block 0 (Bits 0-1): 10 (2)
Block 1 (Bits 2-3): 01 (1)

Swap:
Block 0 moves to Block 1 position.
Block 1 moves to Block 0 position.

Result:
New Block 0: 01 (1)
New Block 1: 10 (2)
Value: ... 10 01 = 9.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: Integer `x` (32-bit).
- **Behavior**: Swap `Block[2k]` with `Block[2k+1]`.
- **Masks**: Use hex constants for clarity. `3` is `0011`. `C` is `1100`.

Common interpretation mistake:

- ❌ Swapping bit `i` with `i+1`. (That is swapping adjacent bits, `0x5555...`).
- ✅ Swapping blocks of size 2. Mask is `0011 0011...` (`0x3333...`).

### Core Concept: Parallel Swapping

Instead of iterating, we process all "even blocks" and "odd blocks" in parallel.
1. **Isolate Even Blocks**: `x & 00110011...` (Blocks 0, 2, 4...)
2. **Isolate Odd Blocks**: `x & 11001100...` (Blocks 1, 3, 5...)
3. **Shift**: Move Even blocks LEFT by 2 positions. Move Odd blocks RIGHT by 2 positions.
4. **Combine**: OR the results.

### Why Naive Approach is too slow

Looping through 8 pairs of blocks is O(1) effectively (constant 8 loops), but bitwise parallelization is much faster and cleaner (no branching).

## Naive Approach (Iterate Blocks)

### Intuition

Extract bits manually, reconstruct.

### Algorithm

1. `res = 0`.
2. Loop `i` from 0 to 7:
   - Extract block `2i` and `2i+1`.
   - Place them in swapped positions in `res`.

### Time Complexity

- **O(1)** (8 iterations).

### Space Complexity

- **O(1)**.

## Optimal Approach (Mask & Shift)

### Key Insight

Use magic masks `0x33333333` and `0xCCCCCCCC`.

### Algorithm

1. `even_mask = 0x33333333`
2. `odd_mask = 0xCCCCCCCC`
3. `even_parts = (x & even_mask)`
4. `odd_parts = (x & odd_mask)`
5. `return (even_parts << 2) | (odd_parts >>> 2)`

### Time Complexity

- **O(1)**. Few instructions.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/BIT-015/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-015/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `6` (`...00 01 10`).
Even Mask (`...00 11 00`): Keeps `00`. `0`?
No, `0x33` is `00110011`.
Positions: 76 54 32 10
Even: Keeps 10 (Bits 0-1) and 54 (Bits 4-5).
Odd: Keeps 32 (Bits 2-3) and 76 (Bits 6-7).
So `6` (`00 01 10`):
Bits 0-1 (`10`): Kept in Even. (`000010`).
Bits 2-3 (`01`): Kept in Odd. (`000100`).
Even << 2: `00001000` (8).
Odd >> 2: `00000001` (1).
Result: 9.

## ✅ Proof of Correctness

### Invariant

The operation is a bijection on the 32-bit space. By masking and shifting, we move bits exactly 2 positions (block size) in opposite directions, effectively swapping the blocks without collision (since we mask disjoint sets).

## 💡 Interview Extensions (High-Value Add-ons)

- **Generalize**: Swap blocks of size 4 (`0x0F0F0F0F`), size 1 (`0x55555555`), size 8 (`0x00FF00FF`).
- **Reverse Bits**: Combining swap 1, 2, 4, 8, 16 reverses all bits in O(log bits).

## Common Mistakes to Avoid

1. **Mask Values**:
   - ❌ `0x55555555` is for 1-bit swap.
   - ✅ `0x33333333` is for 2-bit swap.
2. **Shift Direction**:
   - ❌ Shifting Even (Low) Right falls off edge.
   - ✅ Even (Low) needs to go High (Left). Odd (High) needs to go Low (Right).

## Related Concepts

- **SWAR**: SIMD Within A Register.
- **Bit Reversal**: Divide and conquer approach.
