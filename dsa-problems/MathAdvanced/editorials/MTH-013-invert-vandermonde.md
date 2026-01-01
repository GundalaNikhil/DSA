---
problem_id: MTH_INVERT_VANDERMONDE__8453
display_id: MTH-013
slug: invert-vandermonde
title: "Fast Inversion of Vandermonde Matrix"
difficulty: Hard
difficulty_score: 76
topics:
  - MathAdvanced
  - Fast
tags:
  - math-advanced
  - vandermonde-matrix
  - hard
premium: true
subscription_tier: basic
---

# MTH-013: Fast Inversion of Vandermonde Matrix

## 📋 Problem Summary

Given `n` distinct points `x_0, dots, x_n-1`, compute the inverse of the Vandermonde matrix `V` where `V_ij = x_i^j`.
- Standard matrix inversion is `O(n^3)`.
- We need a faster approach, ideally `O(n^2)`.

## 🌍 Real-World Scenario

**Scenario Title:** The Polynomial Interpolator

In scientific computing, we often need to fit a polynomial to a set of data points.
- Given points `(x_i, y_i)`, we want to find coefficients `c_j` such that `sum c_j x_i^j = y_i`.
- This is the linear system `V c = y`.
- Solving this requires `V^-1`.
- If we need to interpolate many different sets of `y` values for the *same* `x` locations (e.g., sensors at fixed locations reading different data over time), precomputing `V^-1` allows us to solve for coefficients in `O(n^2)` instead of re-solving the system every time.

**Why This Problem Matters:**

- **Coding Theory:** Reed-Solomon decoding involves solving systems with Vandermonde matrices.
- **Signal Processing:** Reconstruction of signals from non-uniform samples.
- **Numerical Analysis:** Stable methods for interpolation.

![Real-World Application](../images/MTH-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Matrix Structure


`V = \beginbmatrix
1 & x_0 & x_0^2 & \dots \\
1 & x_1 & x_1^2 & \dots \\
\vdots & \vdots & \vdots & \ddots
\endbmatrix`


The inverse `U = V^-1` has entries `U_ji` related to the coefficients of the Lagrange basis polynomials.
Specifically, the `i`-th column of `U` contains the coefficients of the polynomial `L_i(x)` such that `L_i(x_k) = delta_ik`.


`L_i(x) = \prod_j !=q i \fracx - x_jx_i - x_j`


### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `n` distinct values `x_i`.
- **Output:** The `n x n` inverse matrix.
- **Modulo:** `10^9+7`.
- **Constraints:** `n <= 2000`. `O(n^2)` is required.

### Core Concept: Lagrange Basis Coefficients

The polynomial `L_i(x)` can be written as:

`L_i(x) = \frac1\prod_j !=q i (x_i - x_j) \prod_j !=q i (x - x_j)`

Let `w_i = frac1prod_j !=q i (x_i - x_j)`.
Let `P(x) = prod_k=0^n-1 (x - x_k)`.
Then `prod_j !=q i (x - x_j) = fracP(x)x - x_i`.

So the `i`-th column of `V^-1` contains the coefficients of `w_i fracP(x)x - x_i`.

## Naive Approach

### Intuition

Gaussian Elimination.

### Algorithm

Standard row reduction.

### Time Complexity

- **O(n^3)**. Too slow for `n=2000` (`8 x 10^9` ops).

### Space Complexity

- **O(n^2)**.

## Optimal Approach

### Key Insight

Use the explicit formula for Lagrange coefficients.
1. Compute the master polynomial `P(x) = prod (x - x_k)`.
2. For each `i`, compute `P_i(x) = P(x) / (x - x_i)`. This division is simple synthetic division.
3. Scale coefficients by `w_i`.

### Algorithm

1. **Compute Coefficients of P(x):**
   - Start with `poly = [1]`.
   - For each `x_k`, multiply `poly` by `(x - x_k)`.
   - This takes `O(n^2)`.
2. **Compute Weights `w_i`:**
   - For each `i`, `w_i = prod_j !=q i (x_i - x_j)^-1`.
   - This takes `O(n^2)`.
3. **Compute Columns of Inverse:**
   - For each `i`:
     - Compute `Q(x) = P(x) / (x - x_i)`.
     - Since we know `P(x)`, we can do this division in `O(n)`.
     - Multiply each coeff of `Q(x)` by `w_i`.
     - Store in column `i`.

### Time Complexity

- **O(n^2)**.

### Space Complexity

- **O(n^2)** for the output matrix.

![Algorithm Visualization](../images/MTH-013/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-013/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `x = [1, 2]`.
1. **Compute P(x):**
   - Init `P = [1, 0, 0]`.
   - `k=0, x[0]=1`: `P = [-1, 1, 0]`. (`(x-1) = -1 + x`)
   - `k=1, x[1]=2`: `P = [2, -3, 1]`. (`(x-1)(x-2) = x^2 - 3x + 2`)
2. **Column 0 (`x_0=1`):**
   - `w_0 = (1-2)^-1 = -1`.
   - `Q(x) = (x^2 - 3x + 2) / (x-1) = x - 2`.
   - Coeffs: `-2, 1`.
   - Scaled by `w_0`: `2, -1`.
   - Col 0: `[2, -1]^T`.
3. **Column 1 (`x_1=2`):**
   - `w_1 = (2-1)^-1 = 1`.
   - `Q(x) = (x^2 - 3x + 2) / (x-2) = x - 1`.
   - Coeffs: `-1, 1`.
   - Scaled by `w_1`: `-1, 1`.
   - Col 1: `[-1, 1]^T`.
4. **Result Matrix:**
   - Row 0: `[2, -1]`
   - Row 1: `[-1, 1]`
   - Matches example.

![Example Visualization](../images/MTH-013/example-1.png)

## ✅ Proof of Correctness

### Invariant
The columns of `V^-1` are the coefficients of the Lagrange basis polynomials.
The synthetic division correctly computes `P(x)/(x-x_i)`.

### Why the approach is correct
- By definition, `V x V^-1 = I`.
- The dot product of row `i` of `V` (powers of `x_i`) and column `j` of `V^-1` (coeffs of `L_j`) is `L_j(x_i)`, which is `delta_ij`.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Solve `V c = y` without explicit inverse.
  - *Hint:* This is just polynomial interpolation. `O(n^2)`.
- **Extension 2:** Transpose Inverse `V^-T y`.
  - *Hint:* Related to multipoint evaluation.
- **Extension 3:** Dynamic updates (add point).
  - *Hint:* Update Lagrange weights in `O(n)`.

### Common Mistakes to Avoid

1. **Polynomial Indexing**
   - ❌ Wrong: `P[i]` is coeff of `x^n-i`.
   - ✅ Correct: `P[i]` is coeff of `x^i`. Be consistent.

2. **Synthetic Division Loop**
   - ❌ Wrong: Iterate 0 to n.
   - ✅ Correct: Iterate n down to 1. `q_k-1` depends on `q_k`.

## Related Concepts

- **Lagrange Interpolation:** The theoretical basis.
- **Synthetic Division:** For polynomial division.
