---
problem_id: HSH_SUBARRAY_HASH_EQUALITY__6271
display_id: HSH-012
slug: subarray-hash-equality
title: "Subarray Hash Equality (Integers)"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Arrays
  - Rolling Hash
tags:
  - hashing
  - array
  - subarray
  - medium
premium: true
subscription_tier: basic
---

# HSH-012: Subarray Hash Equality (Integers)

## 📋 Problem Summary

You are given an array of integers `arr` and multiple queries. Each query consists of two ranges `[l1, r1]` and `[l2, r2]`. You need to determine if the subarray `arr[l1..r1]` is identical to `arr[l2..r2]`.
This is essentially "Substring Equality" but for arrays of numbers instead of characters.

## 🌍 Real-World Scenario

**Scenario Title:** Audio Snippet Matching

Digital audio is often represented as an array of integer samples (amplitudes).
- You have a long recording (the array).
- You want to check if a sound effect at timestamp A is the same as the one at timestamp B.
- Comparing sample-by-sample is slow (`O(N)`).
- Hashing allows `O(1)` comparison after preprocessing.

![Real-World Application](../images/HSH-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Integer Rolling Hash

Array: `[10, 20, 30, 40]`
Base: `B=100` (Must be larger than max element, or map elements to smaller range)

Prefix Hashes:
- `H[0] = 10`
- `H[1] = 10 * 100 + 20 = 1020`
- `H[2] = 1020 * 100 + 30 = 102030`

Query `[1..2]` (Values 20, 30):
- Formula: `H[2] - H[0] * B^2`
- `102030 - 10 * 10000 = 102030 - 100000 = 2030`.
- Expected Hash for `[20, 30]`: `20 * 100 + 30 = 2030`. Matches!

### Key Concept: Handling Large/Negative Integers

Standard rolling hash works on characters (0-255). Here, integers can be large (`10^9`) or negative.
- **Large Values:** The Base `B` doesn't strictly need to be larger than the max element if we rely on modulo arithmetic, but collisions are more likely if `B` is small. A random large prime `B > N` is usually good.
- **Negative Values:** Add a large offset (e.g., `10^9 + 7`) to make them positive before hashing. Or just use raw values in modulo arithmetic (handling negative results correctly).

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Array of size `N`, `Q` queries.
- **Output:** Boolean for each query.
- **Constraints:** `N, Q <= 2 * 10^5`.
- **Values:** `-10^9 dots 10^9`.
- **Strategy:** Use double hashing to avoid collisions.

## Naive Approach

### Intuition

Compare subarrays element by element.

### Time Complexity

- **O(Q * N)**: Too slow.

## Optimal Approach

### Key Insight

Treat the integer array exactly like a string.
- Map each integer `x` to a positive value if necessary (though modulo handles negatives fine if we do `(x % M + M) % M`).
- Compute prefix hashes.
- Answer queries in `O(1)`.

### Algorithm

1. Choose Base `B` and Modulus `M`.
2. Precompute `powers[]`.
3. Precompute `hashes[]`: `H[i] = (H[i-1] * B + arr[i]) +/-od M`.
4. For query `(l1, r1, l2, r2)`:
   - Check lengths: if `r1-l1 != r2-l2`, return false.
   - Compute hash of first subarray.
   - Compute hash of second subarray.
   - Compare.

### Time Complexity

- **O(N + Q)**.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/HSH-012/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
4
1 2 1 2
1
0 1 2 3
```
Array: `[1, 2, 1, 2]`
Query: `[0, 1]` vs `[2, 3]`.

**Hashes:**
- `H[0]=0`.
- `H[1]=1`.
- `H[2]=1 * B + 2`.
- `H[3]=(1 * B + 2) * B + 1 = B^2 + 2B + 1`.
- `H[4]=(B^2 + 2B + 1) * B + 2 = B^3 + 2B^2 + B + 2`.

**Subarray 1 (0..1):**
- `H[2] - H[0] * B^2 = (B+2) - 0 = B+2`.

**Subarray 2 (2..3):**
- `H[4] - H[2] * B^2`.
- `(B^3 + 2B^2 + B + 2) - (B+2) * B^2`.
- `B^3 + 2B^2 + B + 2 - (B^3 + 2B^2) = B + 2`.

**Result:**
- `B+2 == B+2`. True.

## ✅ Proof of Correctness

### Invariant
Polynomial hash works for any sequence of numbers, not just characters.
`Hash([x_1, x_2]) = x_1 * B + x_2`.
As long as `x_i` are treated consistently, equality holds.

## 💡 Interview Extensions

- **Extension 1:** Longest Common Subarray between two arrays.
  - *Answer:* Binary search on length + Hashing.
- **Extension 2:** Find if array is a palindrome.
  - *Answer:* Check if `Hash(Forward) == Hash(Reverse)`.

### Common Mistakes to Avoid

1. **Negative Numbers**
   - ❌ Wrong: `val % MOD` can be negative in Java/C++.
   - ✅ Correct: `(val % MOD + MOD) % MOD`.
2. **Base Size**
   - ❌ Wrong: Base smaller than max element value (e.g., Base 10 for array `[12, 5]`).
   - ✅ Correct: Base should ideally be larger than max element to avoid simple collisions like `[1, 2]` vs `[12]`, though modulo helps. Random large prime is best.

## Related Concepts

- **Suffix Array:** Can handle this for general comparisons.
- **KMP:** For pattern matching in arrays.
