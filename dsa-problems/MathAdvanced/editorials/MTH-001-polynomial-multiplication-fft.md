---
problem_id: MTH_POLYNOMIAL_MULTIPLICATION_FFT__2847
display_id: MTH-001
slug: polynomial-multiplication-fft
title: "Polynomial Multiplication via FFT"
difficulty: Medium
difficulty_score: 55
topics:
  - MathAdvanced
  - FFT
  - Polynomial
tags:
  - math-advanced
  - fft
  - polynomial-multiplication
  - medium
premium: true
subscription_tier: basic
---

# MTH-001: Polynomial Multiplication via FFT

## 📋 Problem Summary

You are given two polynomials, `A(x)` and `B(x)`, represented by their coefficients. You need to compute their product `C(x) = A(x) x B(x)` and return the coefficients of `C(x)` modulo `1,000,000,007`.
- Input: Two arrays of coefficients.
- Output: One array of coefficients representing the product polynomial.

## 🌍 Real-World Scenario

**Scenario Title:** The Audio Equalizer

Imagine you are an audio engineer working on a music production software. You have a raw audio signal (represented as a sequence of samples over time) and you want to apply a specific filter (like a bass boost or reverb).
- In signal processing, the audio signal can be viewed as a polynomial `A(x)`.
- The filter's impulse response is another polynomial `B(x)`.
- Applying the filter to the audio is mathematically equivalent to the **convolution** of these two sequences, which is exactly what polynomial multiplication computes.

If the audio track is long (e.g., 3 minutes at 44.1kHz = 8 million samples), a naive multiplication would take trillions of operations (`O(N^2)`). Using Fast Fourier Transform (FFT), we can do this in seconds (`O(N log N)`), making real-time audio effects possible.

**Why This Problem Matters:**

- **Signal Processing:** Convolution is the core operation for filtering, blurring images, and reverb.
- **Big Integer Multiplication:** Multiplying two massive numbers (millions of digits) uses FFT-based polynomial multiplication.
- **Competitive Programming:** A fundamental building block for advanced combinatorial counting problems.

![Real-World Application](../images/MTH-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: FFT Butterfly

The core of FFT is the "butterfly" operation, which combines results from smaller sub-problems.

```
      u --------+--------> u + v * w
                 \     /
                  \   /
                   \ /
                    X
                   / \
                  /   \
                 /     \
      v --------+--------> u - v * w
```
- `u` and `v` are values from the previous stage.
- `w` is a "root of unity" (a complex number that rotates the value).
- This structure allows us to reuse calculations, reducing complexity from `N^2` to `N log N`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Coefficients:** Input is given from lowest degree (`x^0`) to highest (`x^n-1`).
- **Modulo:** The problem asks for the result modulo `10^9 + 7`. Since standard FFT uses complex numbers which have precision issues, we typically use **Number Theoretic Transform (NTT)** for modular arithmetic.
- **Degree:** If `A` has degree `n-1` and `B` has degree `m-1`, the product has degree `n+m-2`. The output array size will be `n+m-1`.

### Core Concept: Point-Value Representation

1. **Coefficient Form:** `A(x) = a_0 + a_1x + dots` (Hard to multiply: `O(N^2)`).
2. **Point-Value Form:** `A(x)` evaluated at `N` distinct points: `(x_0, y_0), (x_1, y_1), dots`.
3. **Multiplication:** In point-value form, `C(x_i) = A(x_i) x B(x_i)`. This is just `O(N)` scalar multiplications!

**The Strategy:**
1. **Evaluation (FFT):** Convert `A` and `B` from coefficient form to point-value form.
2. **Pointwise Multiply:** Compute `C(x_i) = A(x_i) * B(x_i)`.
3. **Interpolation (Inverse FFT):** Convert `C` back to coefficient form.

## Naive Approach

### Intuition

Multiply every term in `A` by every term in `B` and sum up the coefficients for each power of `x`.

### Algorithm

1. Initialize `result` array of size `n+m-1` with zeros.
2. Loop `i` from 0 to `n-1`.
3. Loop `j` from 0 to `m-1`.
4. `result[i+j] += A[i] * B[j]`.
5. Take modulo at each step.

### Time Complexity

- **O(N * M)**. Too slow for `N, M = 100,000`.

### Space Complexity

- **O(N + M)**.

## Optimal Approach

### Key Insight

Use **Number Theoretic Transform (NTT)**. It's exactly like FFT but works in a finite field (integers modulo `P`) instead of complex numbers. This avoids floating-point errors and naturally handles the modulo requirement.

**Prerequisites for NTT:**
- Modulus `P` must be a prime of the form `c * 2^k + 1`.
- `10^9 + 7` is not an NTT-friendly prime.
- Standard approaches for arbitrary modulo (like `10^9+7`):
  1. Perform NTT with 3 different NTT-friendly primes (e.g., 998244353) and use Chinese Remainder Theorem (CRT) to combine results.
  2. Use the "Split FFT" method:
     - Split each coefficient `x` into `x = x_1 * M + x_0` where `M ≈ sqrt(P)`.
     - Then `A(x) = A_1(x)M + A_0(x)`.
     - Compute: `A * B = (A_1 M + A_0)(B_1 M + B_0) = A_1 B_1 M^2 + (A_1 B_0 + A_0 B_1) M + A_0 B_0`.
     - Use standard Complex FFT as the split values fit in `double` precision without error.

### Algorithm (Split FFT / Arbitrary Modulo FFT)

1. Choose `S = sqrtMOD ~= 31622`.
2. Split `A(x) -> A_1(x) * S + A_0(x)` where coefficients of `A_0, A_1 < S`.
3. Split `B(x) -> B_1(x) * S + B_0(x)`.
4. We need to compute `P_1 = A_1 B_1`, `P_2 = A_1 B_0`, `P_3 = A_0 B_1`, `P_4 = A_0 B_0`.
6. Use Complex FFT. Since inputs are small (`~= 3 * 10^4`), max output is `~= 10^5 * (3 * 10^4)^2 ~= 10^14`, which fits in `double`'s mantissa (53 bits `~= 9 * 10^15`).
7. Perform FFTs, multiply pointwise, Inverse FFT.
8. Reconstruct result: `Result = P_1 S^2 + (P_2 + P_3) S + P_4 +/-odMOD`.

### Time Complexity

- **O(N \log N)**.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/MTH-001/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-001/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `A = [1, 2]`, `B = [3, 4]`
- `A(x) = 1 + 2x`
- `B(x) = 3 + 4x`

1. **Pad to power of 2:** `N=4`.
   - `A = [1, 2, 0, 0]`
   - `B = [3, 4, 0, 0]`
2. **FFT (Evaluation):**
   - Evaluate at roots of unity `omega^0, omega^1, omega^2, omega^3`.
   - `A_eval = [3, 1+2i, -1, 1-2i]`
   - `B_eval = [7, 3+4i, -1, 3-4i]`
3. **Pointwise Multiply:**
   - `C_eval[0] = 3 x 7 = 21`
   - `C_eval[1] = (1+2i)(3+4i) = 3 + 4i + 6i - 8 = -5 + 10i`
   - `C_eval[2] = (-1)(-1) = 1`
   - `C_eval[3] = (1-2i)(3-4i) = -5 - 10i`
4. **Inverse FFT (Interpolation):**
   - Transform back to coefficients: `[3, 10, 8, 0]`.
5. **Result:** `3 10 8`.

![Example Visualization](../images/MTH-001/example-1.png)

## ✅ Proof of Correctness

### Invariant
The convolution theorem states that `mathcalF(A * B) = mathcalF(A) x mathcalF(B)`, where `mathcalF` is the Fourier Transform and `x` is pointwise multiplication.

### Why the approach is correct
- **Evaluation:** FFT correctly evaluates the polynomial at `N` points in `O(N log N)`.
- **Uniqueness:** A polynomial of degree `N-1` is uniquely determined by `N` points.
- **Interpolation:** Inverse FFT correctly reconstructs the coefficients from the point values.
- **Splitting:** The "Split FFT" technique avoids floating point precision errors for large coefficients by breaking them into smaller chunks that fit within `double` precision.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Multiply polynomials with arbitrary modulo (e.g., `10^9+9`).
  - *Hint:* Use the splitting method (MTT) shown above or 3-modulus NTT + CRT.
- **Extension 2:** Multiply large integers.
  - *Hint:* Treat integers as polynomials where `x=10`. Handle carries after multiplication.
- **Extension 3:** Count subsets with sum `K`.
  - *Hint:* Generating functions. If item `v` exists, term is `x^v`. Square the polynomial.

### Common Mistakes to Avoid

1. **Precision Errors**
   - ❌ Wrong: Using standard `complex<double>` FFT directly on coefficients `> 10^4` without splitting.
   - ✅ Correct: Use Split FFT (MTT) or NTT if the modulus allows.

2. **Array Sizing**
   - ❌ Wrong: Using size `N+M`.
   - ✅ Correct: Must be a **power of 2** greater than `N+M-2`.

## Related Concepts

- **NTT:** FFT for modular arithmetic.
- **Karatsuba Algorithm:** `O(N^1.58)` multiplication (simpler but slower than FFT for very large `N`).
- **Generating Functions:** Combinatorial counting using polynomials.
