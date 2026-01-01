---
problem_id: MTH_CONVOLUTION_MULTI_MOD_CRT__4736
display_id: MTH-012
slug: convolution-multi-mod-crt
title: "Convolution Under Multiple Mods with CRT"
difficulty: Medium
difficulty_score: 65
topics:
  - MathAdvanced
  - Convolution
tags:
  - math-advanced
  - crt
  - medium
premium: true
subscription_tier: basic
---

# MTH-012: Convolution Under Multiple Mods with CRT

## 📋 Problem Summary

Compute the convolution of two large arrays `A` and `B` modulo an arbitrary integer `M` (which may not be prime or NTT-friendly).
- Standard NTT only works for specific primes like `998244353`.
- FFT uses floating point numbers, which can lose precision for large results.
- The solution is to compute the convolution modulo several NTT-friendly primes and combine them using the **Chinese Remainder Theorem (CRT)**.

## 🌍 Real-World Scenario

**Scenario Title:** The Big Integer Multiplier

Imagine you are building a cryptographic library that needs to multiply two massive numbers (e.g., 1 million digits each).
- Multiplication is essentially convolution of digit arrays (followed by carry handling).
- Naive multiplication is `O(N^2)`.
- FFT-based multiplication is `O(N log N)`.
- However, the intermediate values in convolution can exceed `10^18` (e.g., sum of `10^5` products of digits up to 9). Standard 64-bit integers overflow.
- To handle this without slow arbitrary-precision arithmetic libraries, we compute the result modulo several large primes (e.g., three `10^9` primes give a range of `10^27`) and reconstruct the exact value.

**Why This Problem Matters:**

- **High-Performance Computing:** Multiplying polynomials with large coefficients.
- **Cryptography:** RSA key generation involves massive integer arithmetic.
- **Competitive Programming:** Solving "count ways" problems with arbitrary modulo.

![Real-World Application](../images/MTH-012/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: CRT Reconstruction

We have a value `X`. We don't know `X`, but we know:
- `X equiv a_1 +/-odp_1`
- `X equiv a_2 +/-odp_2`
- `X equiv a_3 +/-odp_3`

We want to find `X +/-od M`.
Since `p_1 p_2 p_3 > max possible value of convolution`, the CRT solution is the exact value of the convolution. Then we just take modulo `M`.

```
      [ NTT mod p1 ] ---> [ a1 ]
     /
A, B -- [ NTT mod p2 ] ---> [ a2 ]  ---> [ CRT ] ---> X ---> X % M
     \
      [ NTT mod p3 ] ---> [ a3 ]
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Primes:** Use `P_1 = 998244353`, `P_2 = 1004535809`, `P_3 = 469762049`. All are of form `c * 2^k + 1` with `2^20 | (P-1)`, supporting NTT size up to `10^6`.
- **Max Value:** If `N=10^5` and values are `10^9`, max convolution value is `10^5 x 10^9 x 10^9 = 10^23`.
- **Product of Primes:** `P_1 P_2 P_3 ~= 4 x 10^26 > 10^23`. So 3 primes are sufficient.
- **Garner's Algorithm:** A standard way to implement CRT for large numbers.

### Core Concept: Garner's Algorithm

To find `X` such that `X equiv a_i +/-odp_i`:
1. `X = x_1 + x_2 p_1 + x_3 p_1 p_2`.
2. `X equiv x_1 equiv a_1 +/-odp_1 implies x_1 = a_1`.
3. `X equiv x_1 + x_2 p_1 equiv a_2 +/-odp_2 implies x_2 = (a_2 - x_1) p_1^-1 +/-odp_2`.
4. `X equiv x_1 + x_2 p_1 + x_3 p_1 p_2 equiv a_3 +/-odp_3 implies x_3 = ((a_3 - x_1 - x_2 p_1) p_1^-1 p_2^-1) +/-odp_3`.

## Naive Approach

### Intuition

Standard `O(N^2)` convolution.

### Algorithm

Nested loops.

### Time Complexity

- **O(N^2)**. Too slow for `N=10^5`.

### Space Complexity

- **O(N)**.

## Optimal Approach

### Key Insight

Run NTT for 3 primes, then CRT.

### Algorithm

1. **NTT Implementation:** Write a generic NTT function that takes a modulus and a primitive root.
   - `P_1=998244353, g=3`.
   - `P_2=1004535809, g=3`.
   - `P_3=469762049, g=3`.
2. **Compute Convolutions:**
   - `C_1 = Conv(A, B) +/-odP_1`.
   - `C_2 = Conv(A, B) +/-odP_2`.
   - `C_3 = Conv(A, B) +/-odP_3`.
3. **Reconstruct:**
   - For each index `i`, use Garner's algorithm on `(C_1[i], C_2[i], C_3[i])` to find the true value `Val`.
   - Output `Val +/-od M`.

### Time Complexity

- **O(N \log N)**. 3 passes of NTT.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/MTH-012/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-012/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `A=[1, 2]`, `B=[3, 4]`, `MOD=10^9+7`.
1. **NTT Mod P1:**
   - `C_1 = [3, 10, 8]`.
2. **NTT Mod P2:**
   - `C_2 = [3, 10, 8]`.
3. **NTT Mod P3:**
   - `C_3 = [3, 10, 8]`.
4. **CRT:**
   - Since all `C_i` are equal and small, the reconstructed value is exactly `[3, 10, 8]`.
   - Modulo `10^9+7`, result is `3 10 8`.

![Example Visualization](../images/MTH-012/example-1.png)

## ✅ Proof of Correctness

### Invariant
The CRT guarantees a unique solution modulo `P_1 P_2 P_3`.
Since the true convolution value is less than `P_1 P_2 P_3`, the CRT solution is the exact integer value.

### Why the approach is correct
- We perform exact arithmetic in the ring `mathbbZ_P_1 P_2 P_3`.
- The final modulo `M` is applied to the exact integer.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Arbitrary Modulo NTT (Schonhage-Strassen).
  - *Hint:* Split coefficients into smaller chunks to avoid CRT.
- **Extension 2:** Polynomial Inverse.
  - *Hint:* Newton's method.
- **Extension 3:** BigInt Multiplication.
  - *Hint:* This IS BigInt multiplication (base `10^9`).

### Common Mistakes to Avoid

1. **Negative Modulo**
   - ❌ Wrong: `(a - b) % mod`.
   - ✅ Correct: `(a - b + mod) % mod`.

2. **Overflow in CRT**
   - ❌ Wrong: `x1 + x2 * P1` without modulo `M`.
   - *Correction:* In the code, we do `(x1 + x2 * P1) % targetMod`. This is safe if `targetMod` fits in long. But `x2 * P1` can be `10^18`. `x3 * P1 * P2` is definitely `> 2^63`.
   - We must be careful. `P1 * P2` is `10^18`. `x3` is `10^9`. Product is `10^27`.
   - In Java/C++, we need `__int128` or careful modular arithmetic.
   - However, we only need the result modulo `targetMod`.
   - So `(x3 * ((P1 * P2) % targetMod)) % targetMod` is safe!
   - `P1 * P2` might overflow `long` before modulo. `10^18` fits in `long` (max `9 x 10^18`).
   - `P_1 ~= 10^9, P_2 ~= 10^9 implies P_1 P_2 ~= 10^18`. Safe.

## Related Concepts

- **NTT:** Number Theoretic Transform.
- **Garner's Algorithm:** Efficient CRT.
