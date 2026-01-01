---
problem_id: MTH_CONVOLUTION_NTT__5931
display_id: MTH-002
slug: convolution-ntt
title: "Convolution Mod Prime Using NTT"
difficulty: Medium
difficulty_score: 58
topics:
  - MathAdvanced
  - NTT
  - Convolution
tags:
  - math-advanced
  - ntt
  - number-theoretic-transform
  - medium
premium: true
subscription_tier: basic
---

# MTH-002: Convolution Mod Prime Using NTT

## 📋 Problem Summary

You are given two sequences `A` and `B`. You need to compute their **convolution** `C` modulo `998244353`.
- `C[k] = sum_i=0^k A[i] x B[k-i]`
- This is equivalent to multiplying two polynomials `A(x)` and `B(x)` and returning the coefficients of the product.

## 🌍 Real-World Scenario

**Scenario Title:** The Image Blurring Filter

Imagine you are writing a photo editing app. You want to apply a "Gaussian Blur" to an image.
- The image is a 2D grid of pixels (intensities).
- The blur effect is defined by a "kernel" (a small matrix of weights).
- Applying the blur means replacing every pixel with a weighted average of its neighbors. This operation is exactly **convolution**.

While images are 2D, the concept is the same for 1D signals (like audio). If the kernel is large, direct convolution is slow (`O(N * K)`). By transforming the signal and kernel into the frequency domain (using FFT/NTT), multiplying them, and transforming back, we can apply massive filters instantly (`O(N log N)`).

**Why This Problem Matters:**

- **Computer Vision:** Convolutional Neural Networks (CNNs) are built on this operation.
- **Competitive Programming:** Many counting problems (e.g., "number of ways to form sum K") reduce to polynomial multiplication.
- **Cryptography:** Lattice-based cryptography (like Kyber/Dilithium) relies heavily on polynomial multiplication over finite fields.

![Real-World Application](../images/MTH-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: NTT Process

```
Input A: [1, 2]   Input B: [3, 4]
      |                |
      v NTT            v NTT
A_eval: [3, -1]   B_eval: [7, -1]  (Evaluated at roots of unity)
      |                |
      +-------+--------+
              | Pointwise Multiply
              v
      C_eval: [21, 1]
              |
              v Inverse NTT
Output C: [11, 10] (Coefficients: 11 + 10x)
```
*Note: This is a simplified view. Real NTT uses bit-reversal permutation and butterfly operations.*

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Modulus:** `998244353` is a special prime. It equals `119 x 2^23 + 1`. This means `P-1` is divisible by a large power of 2 (`2^23`), allowing us to use NTT for arrays up to size `2^23 ~= 8 x 10^6`.
- **Primitive Root:** For this prime, `g=3` is a primitive root. This plays the role of the complex root of unity in standard FFT.
- **Padding:** The result length is `N+M-1`. You must pad inputs to the next power of 2 that is `>= N+M-1`.

### Core Concept: Roots of Unity in Finite Fields

In standard FFT, we use `omega_n = e^2pi i / n`.
In NTT, we use `g^(P-1)/n +/-od P`.
- This integer has the property that `omega^n equiv 1 +/-od P` and `omega^n/2 equiv -1 +/-od P`, exactly mimicking the behavior of complex roots of unity.
- This allows us to use the exact same Divide & Conquer algorithm as FFT, but with integer modular arithmetic.

## Naive Approach

### Intuition

Directly compute the sum for each index `k`.

### Algorithm

1. Initialize `C` of size `N+M-1`.
2. Nested loops: `for i in 0..N-1`, `for j in 0..M-1`.
3. `C[i+j] = (C[i+j] + A[i] * B[j]) % MOD`.

### Time Complexity

- **O(N * M)**. Too slow for `N, M = 100,000`.

### Space Complexity

- **O(N + M)**.

## Optimal Approach

### Key Insight

Use **Number Theoretic Transform (NTT)** with the prime `998244353` and primitive root `3`.

### Algorithm

1. **Setup:**
   - Find smallest power of 2, `limit`, such that `limit >= n + m - 1`.
   - Precompute "bit-reversal" permutation indices for iterative FFT (optional but faster).
2. **NTT Function:**
   - Input: Array `a`, boolean `invert`.
   - Reorder `a` using bit-reversal.
   - Iterate `len` from 2 to `limit`:
     - Calculate `wlen = g^((P-1)/len)`. If `invert`, use modular inverse.
     - For each block of size `len`:
       - `w = 1`.
       - For each pair `(u, v)` in the butterfly:
         - `u = a[i+j]`, `v = a[i+j+len/2] * w`.
         - `a[i+j] = u + v`.
         - `a[i+j+len/2] = u - v`.
         - `w = w * wlen`.
   - If `invert`, multiply all elements by `inv(limit)`.
3. **Convolution:**
   - Pad `A` and `B` with zeros to size `limit`.
   - `NTT(A, false)`.
   - `NTT(B, false)`.
   - Pointwise multiply: `A[i] = A[i] * B[i]`.
   - `NTT(A, true)` (Inverse).
   - Output first `n + m - 1` elements.

### Time Complexity

- **O((N+M) \log (N+M))**.

### Space Complexity

- **O(N + M)**.

![Algorithm Visualization](../images/MTH-002/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-002/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `A = [1, 1, 1]`, `B = [1, 2]`
Target Modulo: 998244353.

1. **Padding:** Target size `3+2-1=4`. Next power of 2 is 4.
   - `A = [1, 1, 1, 0]`
   - `B = [1, 2, 0, 0]`
2. **NTT (Forward):**
   - `A_eval = [3, dots]` (Values in frequency domain)
   - `B_eval = [3, dots]`
3. **Pointwise Multiply:**
   - `C_eval[i] = A_eval[i] x B_eval[i] +/-od P`
4. **NTT (Inverse):**
   - Transform back.
   - Result: `[1, 3, 3, 2]`
   - Check:
     - `x^0: 1 * 1 = 1`
     - `x^1: 1 * 2 + 1 * 1 = 3`
     - `x^2: 1 * 0 + 1 * 2 + 1 * 1 = 3`
     - `x^3: 1 * 0 + 1 * 0 + 1 * 2 = 2`

![Example Visualization](../images/MTH-002/example-1.png)

## ✅ Proof of Correctness

### Invariant
The NTT transforms a polynomial `A(x)` into a vector of values `(A(g^0), A(g^1), dots, A(g^n-1))`.
Pointwise multiplication in this domain corresponds to polynomial multiplication in the coefficient domain because `C(x_i) = A(x_i)B(x_i)` holds for any `x_i`.

### Why the approach is correct
- `998244353` is a prime of form `c * 2^k + 1`, ensuring existence of `2^k`-th roots of unity.
- The algorithm is isomorphic to FFT but operates in the finite field `mathbbZ_P`, avoiding all precision issues.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Polynomial Inverse.
  - *Hint:* Use Newton's Method with NTT. `B_k = B_k-1(2 - A B_k-1) +/-od x^2^k`.
- **Extension 2:** Multipoint Evaluation.
  - *Hint:* Build a subproduct tree and use polynomial division.
- **Extension 3:** Circular Convolution.
  - *Hint:* Just standard NTT/FFT without padding to `N+M-1` (pad to `N` if `N=M`).

### Common Mistakes to Avoid

1. **Modulo Arithmetic**
   - ❌ Wrong: Forgetting `+ MOD` when subtracting: `(u - v) % MOD` can be negative.
   - ✅ Correct: `(u - v + MOD) % MOD`.

2. **Primitive Root**
   - ❌ Wrong: Using `G=3` for any prime.
   - ✅ Correct: `G=3` is specific to `998244353`. For `10^9+7`, no such simple `2^k`-th root exists easily.

## Related Concepts

- **FFT:** The continuous version.
- **Generating Functions:** Used for combinatorial counting.
- **Divide and Conquer:** The underlying algorithmic paradigm.
