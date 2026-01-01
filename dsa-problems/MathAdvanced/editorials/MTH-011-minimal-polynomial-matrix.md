---
problem_id: MTH_MINIMAL_POLYNOMIAL_MATRIX__3891
display_id: MTH-011
slug: minimal-polynomial-matrix
title: "Minimal Polynomial of Matrix (Krylov)"
difficulty: Hard
difficulty_score: 82
topics:
  - MathAdvanced
  - Minimal
tags:
  - math-advanced
  - minimal-polynomial
  - hard
premium: true
subscription_tier: basic
---

# MTH-011: Minimal Polynomial of Matrix (Krylov)

## 📋 Problem Summary

Given an `n x n` matrix `A`, find its **minimal polynomial** `mu_A(x)`.
- `mu_A(x)` is the monic polynomial of lowest degree such that `mu_A(A) = 0` (the zero matrix).
- It divides the characteristic polynomial `chi_A(x) = det(xI - A)`.

## 🌍 Real-World Scenario

**Scenario Title:** The Control System Stabilizer

In control theory, a dynamic system is often modeled by a state-space equation `dotx = Ax + Bu`.
- The stability and controllability of the system depend on the eigenvalues of `A`.
- The **minimal polynomial** tells us the size of the largest Jordan block for each eigenvalue.
- If the minimal polynomial has distinct roots, the matrix is diagonalizable, meaning the system can be decoupled into independent modes.
- Calculating this efficiently allows engineers to design controllers for complex systems (like stabilizing a fighter jet).

**Why This Problem Matters:**

- **Linear Algebra:** Fundamental property of a matrix.
- **Krylov Subspace Methods:** Used in solving massive sparse linear systems (GMRES, Conjugate Gradient).
- **Coding Theory:** Finding the error locator polynomial.

![Real-World Application](../images/MTH-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Krylov Sequence

We pick a random vector `v` and compute the sequence:
`v, Av, A^2v, A^3v, dots`

Since the space is `n`-dimensional, these vectors must eventually become linearly dependent.
The relation `sum c_i A^i v = 0` gives us a polynomial `P(x) = sum c_i x^i` such that `P(A)v = 0`.
With high probability (if `v` is random), this `P(x)` is the minimal polynomial.

```
v  = [1, 0]
Av = [1, 1] * [1, 0] = [1, 0]
A^2v = [1, 0]
...
Here v is an eigenvector. Minimal poly for v is x-1.
But true minimal poly for A is (x-1)^2.
We might need multiple random vectors or a better v.
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Random Vector:** A single random vector usually works if the field is large enough.
- **Output:** Coefficients of the polynomial.
- **Degree:** Can be up to `n`.
- **Constraint:** `n <= 200`. `O(n^3)` is acceptable (`8 x 10^6`).

### Core Concept: Wiedemann's Algorithm (Simplified)

1. Pick random vector `u` and `v`.
2. Compute scalar sequence `S_k = u^T A^k v`.
3. Use **Berlekamp-Massey** on `S_k` to find the minimal recurrence.
4. The characteristic polynomial of this recurrence is likely the minimal polynomial of `A`.

## Naive Approach

### Intuition

Compute characteristic polynomial using interpolation or Faddeev-LeVerrier. Then check factors.

### Algorithm

Hard to implement and slow.

## Optimal Approach

### Key Insight

Combine **Krylov Sequence** generation with **Berlekamp-Massey**.

### Algorithm

1. **Generate Sequence:**
   - Pick random vector `v` (or random `u, v`).
   - Compute `S_k = u^T (A^k v)` for `k=0 dots 2n`.
   - Efficient computation:
     - `v_0 = v`.
     - `v_k+1 = A v_k`. (Matrix-Vector multiplication: `O(n^2)`).
     - Total for `2n` terms: `O(n^3)`.
     - Then `S_k = u * v_k` (`O(n)`).
2. **Find Recurrence:**
   - Run Berlekamp-Massey on `S_0, dots, S_2n-1`.
   - This gives a polynomial `P(x)`.
3. **Verification (Optional):**
   - Ideally, verify `P(A) = 0`. If not, repeat with different random vectors and take LCM of polynomials.
   - For competitive programming with random constraints, one pass is usually sufficient.

### Time Complexity

- **O(n^3)**.

### Space Complexity

- **O(n^2)**.

![Algorithm Visualization](../images/MTH-011/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-011/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `2x2` Jordan Block `[[1, 1], [0, 1]]`.
1. **Krylov Sequence:**
   - `v = [1, 0]^T`.
   - `Av = [1, 0]^T`.
   - `A^2v = [1, 0]^T`.
   - Sequence is constant. BM gives `x-1`.
   - This is minimal poly for `v`, but not for `A`.
   - `v = [0, 1]^T`.
   - `Av = [1, 1]^T`.
   - `A^2v = [2, 1]^T`.
   - `A^3v = [3, 1]^T`.
   - Sequence: `0, 1, 2, 3 dots`
   - BM finds recurrence `S_n = 2S_n-1 - S_n-2`.
   - Char poly: `x^2 - 2x + 1 = (x-1)^2`.
2. **Random Vectors:**
   - With random `u, v`, we likely capture the largest block structure.
   - Result: `x^2 - 2x + 1`.
   - Coeffs: `1, -2, 1` (from constant to `x^2`).
   - Output: `1 1000000005 1`.

![Example Visualization](../images/MTH-011/example-1.png)

## ✅ Proof of Correctness

### Invariant
The sequence `u^T A^k v` is linearly recurrent with characteristic polynomial equal to the minimal polynomial of `A` (with high probability).

### Why the approach is correct
- The minimal polynomial of the sequence divides the minimal polynomial of `A`.
- For random `u, v`, the probability that they fall into a proper subspace is low (inverse of field size).

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Characteristic Polynomial.
  - *Hint:* Same degree as `n`. Minimal poly divides it.
- **Extension 2:** Eigenvalues.
  - *Hint:* Roots of minimal polynomial.
- **Extension 3:** Sparse Matrix.
  - *Hint:* This algorithm works in `O(E * n)` for sparse matrices!

### Common Mistakes to Avoid

1. **Sequence Length**
   - ❌ Wrong: `n` terms.
   - ✅ Correct: `2n` terms are needed to recover degree `n` polynomial.

2. **Coefficient Order**
   - ❌ Wrong: Highest degree first.
   - ✅ Correct: Problem asks for constant to highest (or check example carefully). Example: `1 -2 1` for `x^2-2x+1`. `1` is constant term? No, example says `1 1000000005 1`. `1` is `x^2`, `-2` is `x`, `1` is constant.
   - `x^2 - 2x + 1`.
   - If order is constant to highest: `1, -2, 1`.
   - If order is highest to constant: `1, -2, 1`. Symmetric.
   - **Example Check:** `x-2`. Coeffs: `-2, 1` (const, high).
   - So for `x^2 - 2x + 1`, it is `1, -2, 1`.
   - My code reverses C (which is `1, -c1, -c2`) to get `1, -c1, -c2`.
   - `C` corresponds to `1 - c_1 x - c_2 x^2`.
   - Minimal poly is `x^d - c_1 x^d-1 - c_2 x^d-2`.
   - So coeffs are `C[d], C[d-1], dots, C[0]`.
   - My code does `res[i] = C.get(d-i)`.
   - `res[0] = C[d]`. `res[d] = C[0] = 1`.
   - This matches "constant to highest".

## Related Concepts

- **Wiedemann Algorithm:** The sparse version.
- **Block Wiedemann:** Parallel version.
