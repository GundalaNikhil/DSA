---
problem_id: BIT_TWO_UNIQUE_TRIPLES__8402
display_id: BIT-002
slug: two-unique-with-triples-mask
title: "Two Unique With Triple Others Under Mask"
difficulty: Medium
difficulty_score: 45
topics:
  - Bitwise Operations
  - XOR
  - Array
  - Bit Counting
  - Mathematics
tags:
  - bitwise
  - xor
  - bit-manipulation
  - array
  - medium
premium: true
subscription_tier: basic
---

# BIT-002: Two Unique With Triple Others Under Mask

## 📋 Problem Summary

You have an array where two distinct numbers appear exactly once, and all other numbers appear exactly three times. You are given a mask `M` and guaranteed that the two unique numbers differ in at least one bit present in `M`. Find the two numbers.

## 🌍 Real-World Scenario

**Scenario Title:** The Radio Frequency Isolation

You are monitoring a frequency band where devices broadcast signals.

- **Protocol**: Most devices broadcast a standard "Keep-Alive" sequence exactly 3 times for redundancy (Triple Modular Redundancy).
- **Anomalies**: Two rogue devices broadcast only once.
- **Interference**: If you just listen to everything, signals overlap. Simple XORing doesn't work because triple signals don't cancel out cleanly (`A^A^A = A`).
- **Filter**: You know the rogue devices operate on different sub-channels. The mask `M` represents the channel bits. You can tune your filter to a specific channel bit to separate the rogues and identify them individually.

**Why This Problem Matters:**

- **Generalizing XOR**: Standard "Single Number" problems rely on 2-redundancy (cancellation). Dealing with 3-redundancy requires counting modulo 3.
- **Divide and Conquer**: Using a bitmask to split a hard problem into two easier sub-problems.
- **Digital Logic**: Fundamental to error correction codes.

![Real-World Application](../images/BIT-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Bit Counting Partition

```
Example Array: [5, 5, 5, 9, 9, 9, 3, 6]
Unique numbers: 3 (011₂) and 6 (110₂)
Repeating numbers: 5 (101₂) appears 3x, 9 (1001₂) appears 3x

Counting Bits Modulo 3:

Bit 0 (rightmost):
  Count: 5(1)×3 + 9(1)×3 + 3(1) + 6(0) = 3 + 3 + 1 + 0 = 7
  7 % 3 = 1 → Distinguishing bit (unique numbers differ here)

Bit 1:
  Count: 5(0)×3 + 9(0)×3 + 3(1) + 6(1) = 0 + 0 + 1 + 1 = 2
  2 % 3 = 2 → Both unique numbers have this bit set

Bit 2:
  Count: 5(1)×3 + 9(0)×3 + 3(0) + 6(1) = 3 + 0 + 0 + 1 = 4
  4 % 3 = 1 → Distinguishing bit (unique numbers differ here)

Strategy:
1. Find a distinguishing bit (count % 3 == 1)
2. Split array into two groups based on that bit
3. Each group has ONE unique number and triples
4. Apply "Single Number II" to each group
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: Array `a`, Mask `M`.
- **Ordering**: Return `[min, max]`.
- **Constraint**: `M` is valid (separating bit exists).

Common interpretation mistake:

- ❌ Trying to use `XOR` sum of array. `A^A^A = A`. XOR sum becomes `U1 ^ U2 ^ (X1^X2^...)`. The repeats don't vanish.
- ✅ We must use bit counting modulo 3.

### Core Concept: Modulo 3 Counting

For any bit position `i`:
Total count of set bits `C_i`.
Since repeating numbers contribute `3` or `0` to the count:
`C_i % 3 = (u1_i + u2_i) % 3`.

Possible outcomes for `rem = C_i % 3`:

- `rem == 0`: `u1` and `u2` both 0.
- `rem == 2`: `u1` and `u2` both 1.
- `rem == 1`: One is 0, One is 1. (They differ!).

So, if `(C_i % 3) == 1`, bit `i` is a **distinguishing bit**. u1 and u2 have different values here.

### Why M is given

Strictly speaking, we could find a distinguishing bit just by checking all 32 bits. The problem gives `M` to guarantee/simplify the choice or simulate a "filter" constraint. We just need to pick `bit = M & DiffMask`.

## Naive Approach (HashMap)

### Intuition

Count all frequencies. Return keys with count 1.

### Algorithm

1. `counts = {}`.
2. Iterate `a`, update `counts`.
3. Filter `counts` for value 1.
4. Sort and return.

### Time Complexity

- **O(N)**.

### Space Complexity

- **O(N)**.

## Optimal Approach (Partition + Bitwise Mod 3)

### Key Insight

1. Determine a distinguishing bit `k`. We iterate 0..31, sum bits mod 3. If result is 1, and `(1<<i) & M` is true, choose `k = i`.
2. Partition array into `Group0` (k-th bit 0) and `Group1` (k-th bit 1).
3. In `Group0`, `u1` is the only unique. `u2` went to Group1. All repeats went together to one group or the other (since repeats are identical).
4. Solve "Find single unique where others appear 3 times" for both groups.
   - For a group: Answer bit `j` = `(Sum of j-th bits in group) % 3`.

### Algorithm

1. **Find Split Bit**:
   - `splitBit = -1`.
   - Loop `i` from 0 to 30:
     - `cnt = 0`.
     - For `x` in `a`: `if (x >> i) & 1: cnt++`.
     - If `cnt % 3 == 1` AND `(M >> i) & 1`:
       - `splitBit = i`. Break.
2. **Solve Subproblems**:
   - `ans1 = 0`, `ans2 = 0`.
   - For each bit position `b` from 0 to 30:
     - `c1 = 0, c2 = 0` (counters for each group).
     - For each `x` in array:
       - `bitVal = (x >> b) & 1` (check if bit b is set).
       - `group = (x >> splitBit) & 1` (determine which group x belongs to).
       - If `group == 0`: `c1 += bitVal`.
       - Else: `c2 += bitVal`.
     - If `c1 % 3 == 1`: Set bit `b` in `ans1` → `ans1 |= (1 << b)`.
     - If `c2 % 3 == 1`: Set bit `b` in `ans2` → `ans2 |= (1 << b)`.
3. Return sorted `[ans1, ans2]`.

### Time Complexity

- **O(32 \* N)** which is **O(N)**. We iterate bits (outer) and array (inner) or vice versa.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/BIT-002/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-002/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `[5, 5, 5, 9, 9, 9, 3, 6]`, `M=1`

**Binary representations**:

- `3 = 0011`
- `5 = 0101`
- `6 = 0110`
- `9 = 1001`

**Unique numbers**: `3` and `6`

### Step 1: Find Distinguishing Bit

For **Bit 0** (value 1):

- Count set bits: `3(1) + 6(0) + 5×3(1,1,1) + 9×3(1,1,1)` → Total = `1 + 0 + 3 + 3 = 7`
- `7 % 3 = 1` ✓ (Distinguishing bit found!)
- `M & 1 = 1` ✓ (Bit is in mask)
- **Split bit = 0**

**Analysis**: Bit 0 separates our unique numbers:

- `3` has bit 0 set (odd)
- `6` has bit 0 unset (even)

### Step 2: Partition and Reconstruct

**Group 0** (bit 0 = 0): `[6, ...trailing 9s and 5s with bit 0 = 0]`
**Group 1** (bit 0 = 1): `[3, 5, 5, 5, 9, 9, 9]`

For each bit position, count occurrences in each group:

**Reconstructing Group 0's unique**:

- Bit 1: Count = 1 (from 6), `1 % 3 = 1` → Set
- Bit 2: Count = 1 (from 6), `1 % 3 = 1` → Set
- Result: `0110₂ = 6` ✓

**Reconstructing Group 1's unique**:

- Bit 0: Count = 7 (all odds), `7 % 3 = 1` → Set
- Bit 1: Count = 1 (from 3), `1 % 3 = 1` → Set
- Bit 2: Count = 0, `0 % 3 = 0` → Unset
- Result: `0011₂ = 3` ✓

**Output**: `[3, 6]`

## ✅ Proof of Correctness

### Invariant

With `count % 3`, repeating elements contribute 0 to the remainder. The remainder is purely `(u1_bit + u2_bit) % 3`.

- `1` implies `1+0` (Diff).
- `2` implies `1+1` (Same).
- `0` implies `0+0` (Same).
  Thus we correctly identify separating bits. Partitioning ensures we separate `u1` and `u2`, reducing to the solved problem of "1 unique in triples".

## 💡 Interview Extensions (High-Value Add-ons)

- **General K**: What if elements appear K times? (Use count % K).
- **No Mask**: If Mask not given, just use `count % 3 == 1` to find ANY diff bit.

## Common Mistakes to Avoid

1. **Incorrect Modulo**:
   - ❌ `count % 2`.
   - ✅ `count % 3` is required for triples.
2. **Mask Validation**:
   - ❌ Assuming `M` is always perfect.
   - ✅ Algorithm robustness depends on finding _one_ valid bit.
