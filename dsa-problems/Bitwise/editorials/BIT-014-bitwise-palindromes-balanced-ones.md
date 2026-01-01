---
problem_id: BIT_PALINDROMES_BALANCED_ONES__8414
display_id: BIT-014
slug: bitwise-palindromes-balanced-ones
title: "Bitwise Palindromes With Balanced Ones"
difficulty: Medium
difficulty_score: 62
topics:
  - Bitwise Operations
  - Palindrome
  - Bit Counting
  - Number Theory
tags:
  - bitwise
  - palindrome
  - popcount
  - number-generation
  - medium
premium: true
subscription_tier: basic
---

# BIT-014: Bitwise Palindromes With Balanced Ones

## 📋 Problem Summary

Count the integers in the range `[L, R]` that satisfy two conditions:

1. Their binary representation is a palindrome (reads same forwards and backwards).
2. The total number of set bits (1s) is even.

## 🌍 Real-World Scenario

**Scenario Title:** The Symmetric Verification Code

You are designing a secure optical recognition system.

- **Markers**: The system uses binary markers printed on objects.
- **Robustness**: To ensure the marker is read correctly regardless of orientation (left-to-right or right-to-left), the codes must be **palindromes**.
- **Error Checking**: To detect single-bit flip errors (dirt/damage), the codes must have a fast parity check (Even Parity - even number of 1s).
- **Task**: You need to calculate how many valid codes exist within a specific numeric range `[L, R]` to see if the ID space is large enough.

**Why This Problem Matters:**

- **Constructive Counting**: Instead of iterating $10^{12}$ numbers, we construct valid numbers directly.
- **Symmetry Properties**: Leveraging palindrome structure to halve the search space.
- **Parity Constraints**: Combining structural constraints with arithmetic ones.

![Real-World Application](../images/BIT-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Palindrome Construction

```
Length 5 (Odd):
Structure: [A B C B A]
Pairs: (A, A), (B, B). Middle: C.
Popcount = 2*weight(A) + 2*weight(B) + weight(C).
Since 2*k is always even, Popcount parity depends ONLY on C.
For Even Popcount -> Middle bit C must be 0.

Length 4 (Even):
Structure: [A B B A]
Pairs: (A, A), (B, B).
Popcount = 2*weight(A) + 2*weight(B).
Always Even!
Condition is automatically satisfied for all even-length palindromes.
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input**: Range `[L, R]`.
- **Leading Zeros**: Not allowed. This implies the Most Significant Bit (MSB) is 1. Consequently, the Least Significant Bit (LSB) must also be 1.
- **Constraints**: Up to $10^{12}$. $O(\sqrt{N})$ or $O(N)$ is too slow. $O(\log N)$ required.

Common interpretation mistake:

- ❌ Iterating from L to R.
- ✅ Counting valid numbers $\le X$ and computing `Solve(R) - Solve(L-1)`.

### Core Concept: Constructing Palindromes

A binary palindrome of length `k` is fully determined by its first $\lceil k/2 \rceil$ bits.
Let `H = ceil(k/2)`.
Value `V` is an integer of `H` bits (where MSB is 1).
We can "unfold" `V` to create the palindrome.

**Parity Check**:

1. **Even Length k**: Every bit in the first half is mirrored. Total 1s is even. **All** even-length palindromes are valid.
2. **Odd Length k**: The middle bit is unique. The rest are mirrored (contribute even 1s). For total 1s to be even, the **middle bit must be 0**. In the "first half" representation, this corresponds to the LSB of `V` being 0.

## Naive Approach (Iterate)

### Intuition

Check every number.

### Algorithm

1. Loop `i` from `L` to `R`.
2. Convert to binary string.
3. Check palindrome + count bits.

### Time Complexity

- **O(R - L)**. TLE for large ranges.

### Space Complexity

- **O(log R)**.

## Optimal Approach (digit DP / Construction)

### Key Insight

Calculate `count(N)`: number of valid integers in `[0, N]`.
Sum valid counts for all lengths `len < BitLen(N)`.
Then specifically count valid numbers of length `BitLen(N)` that are $\le N$.

### Algorithm for `count(N)`

1. If `N < 0` return 0. Base count = 1 (for 0).
2. Let `L` = bit length of `N`.
3. **Phase 1: Smaller Lengths**:
   - Loop `len` from 1 to `L-1`.
   - `half_len = (len + 1) / 2`.
   - Number of choices for "half":
     - Basic count is $2^{\text{half\_len} - 1}$ (MSB fixed to 1).
     - If `len` even: Use full count.
     - If `len` odd: Half must end in 0. So we fix MSB=1, LSB=0. Free bits: `half_len - 2`. Count $2^{\text{half\_len} - 2}$. (If `half_len < 2`, count is determined).
   - Add to total.
4. **Phase 2: Same Length**:
   - Construct the "target half" from the first `ceil(L/2)` bits of `N`. Let this be `limit_prefix`.
   - Iterate valid prefixes from `10...0` up to `limit_prefix`.
   - Note: We can calculate how many are strictly less than `limit_prefix` mathematically.
   - **Boundary Check**: For `limit_prefix` itself, construct the full palindrome. If `palindrome <= N`, count it.
   - Constraint Logic:
     - If `L` even: `limit_prefix` is valid. All values `< limit_prefix` valid.
     - If `L` odd: `limit_prefix` must have LSB 0. We count multiples of 2 in range `[LB, limit_prefix)`.

### Time Complexity

- **O(log N)** (proportional to number of bits).

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/BIT-014/algorithm-visualization.png)
![Algorithm Steps](../images/BIT-014/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `5, 12`. Range `[101₂, 1100₂]` = `[5, 12]` in decimal.

**Solve(12)** (Binary `1100`, length=4):

- **Len 1**: Number `1` (binary `1`). Popcount=1 (odd). Even popcount required → Invalid. Count: 0
- **Len 2**: Number `11` (binary `11` = 3). Popcount=2 (even). Valid palindrome. Count: 1

- **Len 3**: Checking `101` (5, even popcount) and `111` (7, odd popcount).

  - HalfLen=2. Min=`10₂`, Max=`11₂`
  - Range [2, 3) in decimal
  - Even count in range: 1 (value 2 → generates `101`)
  - Boundary value 3 (odd) → Invalid
  - Valid: `101` (5). Count: 1

- **Len 4**: N=`1100₂` (12). HalfLen=2. Min=`10₂`, Max=`11₂`
  - Prefix of N: `11₂`
  - Below prefix `11`: Value `10` → generates `1001₂` (9, even popcount). Valid.
  - Check boundary `11`: Palindrome `1111₂` (15). `15 > 12` → Not counted.
  - Valid from len 4: 9. Count: 1

**Total**: `0 + 1 + 1 + 1 = 3` valid numbers: **3, 5, 9**
**Solve(4)** (Binary 100).

- Len 1: 0.
- Len 2: 1 (3).
- Len 3: Limit 4 (100). Half `10`.
  - Prefix `10`. MaxHalf `10`.
  - Below `10`: Empty.
  - Check `10`: `101` (5). `5 > 4`.
  - Valid 0.
    Total `0 + 1 + 0 = 1`. (Number: 3).
    **Result**: `3 - 1 = 2`.
    Valid Numbers in `[5, 12]`: 5, 9. (3 is outside).
    Correct. Matches Example.

## ✅ Proof of Correctness

### Invariant

The construction correctly identifies the bijection between the first $\lceil L/2 \rceil$ bits and the full palindrome. The parity condition simplifies cleanly to "All even lengths valid" and "Odd lengths must have 0 middle". We effectively iterate the smaller search space of prefixes.

## 💡 Interview Extensions (High-Value Add-ons)

- **Divisibility**: Count palindromes divisible by K (much harder).
- **Base-K**: Generalize to base K palindromes.

## Common Mistakes to Avoid

1. **Length 1**:
   - ❌ `1` has odd bits.
   - ✅ My logic handles it (Odd len, must be even half -> bit 0 -> invalid for leading 1).
2. **0 Case**:
   - ❌ Skipping 0.
   - ✅ Handled explicitly.

## Related Concepts

- **Digit DP**: Thinking in terms of constructing prefixes.
- **Combinatorics**: Counting with symmetries.
