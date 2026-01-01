---
problem_id: MTH_LARGEST_EIGENVALUE_POWER__2197
display_id: MTH-014
slug: largest-eigenvalue-power
title: "Largest Eigenvalue Power Method"
difficulty: Medium
difficulty_score: 58
topics:
  - MathAdvanced
  - Largest
tags:
  - math-advanced
  - eigenvalue
  - medium
premium: true
subscription_tier: basic
---

# MTH-014: Largest Eigenvalue Power Method

## 📋 Problem Summary

Find the **largest eigenvalue** (by absolute value) of a square matrix `A` using the **Power Iteration** method.
- Start with a random vector `v`.
- Repeatedly apply `v_new = A v_old`.
- Normalize `v` at each step to prevent overflow.
- The Rayleigh Quotient `fracv^T A vv^T v` converges to the largest eigenvalue `lambda_max`.

## 🌍 Real-World Scenario

**Scenario Title:** The Search Engine Ranker

Google's original **PageRank** algorithm is essentially finding the principal eigenvector of the web graph's transition matrix.
- The web is a graph where pages are nodes and links are edges.
- A "random surfer" moves from page to page.
- The probability distribution of the surfer's location after infinite steps is the **stationary distribution**.
- This stationary distribution is the eigenvector corresponding to the eigenvalue 1 (which is the largest for stochastic matrices).
- By computing this, search engines determine the "importance" of a webpage.

**Why This Problem Matters:**

- **Data Science:** Principal Component Analysis (PCA) finds directions of maximum variance (eigenvectors of covariance matrix).
- **Structural Engineering:** Resonance frequencies are eigenvalues of the stiffness matrix.
- **Quantum Mechanics:** Energy levels are eigenvalues of the Hamiltonian.

![Real-World Application](../images/MTH-014/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Convergence

Imagine a vector `v` as a mix of all eigenvectors `e_1, e_2, dots`.
`v = c_1 e_1 + c_2 e_2 + dots`
Applying `A`:
`Av = c_1 lambda_1 e_1 + c_2 lambda_2 e_2 + dots`
Applying `A^k`:
`A^k v = c_1 lambda_1^k e_1 + c_2 lambda_2^k e_2 + dots`

If `|lambda_1| > |lambda_2|`, then for large `k`, the term `lambda_1^k` dominates.
`A^k v ~= c_1 lambda_1^k e_1`.
The vector aligns with the direction of `e_1`.

```
       /
      /  e1 (Strong pull)
     /
    /
   v_0 -> v_1 -> v_2 -> ... -> v_inf (Aligned with e1)
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** Matrix `A`, max iterations, tolerance `epsilon`.
- **Output:** A single float.
- **Normalization:** Divide vector by its norm (Euclidean or Max-norm) at each step. Max-norm (`L_infinity`) is cheaper and sufficient.
- **Convergence Check:** If `|lambda_new - lambda_old| < epsilon`, stop.

### Core Concept: Rayleigh Quotient

Once `v` is close to the eigenvector `e`, `Av ~= lambda v`.
We can find `lambda` by projecting `Av` onto `v`:
`lambda ~= fracv * Avv * v`.
If `v` is normalized (`v * v = 1`), then `lambda ~= v * Av`.

## Naive Approach

### Intuition

Analytic solution (Characteristic Polynomial).

### Algorithm

Compute `det(A - lambda I)`, solve polynomial roots.
- **Impossible** for `N > 4` analytically (Abel-Ruffini).
- Numerical root finding is complex.

## Optimal Approach

### Key Insight

Power Iteration is simple, robust, and effective for the largest eigenvalue.

### Algorithm

1. Initialize `v` to a random vector (e.g., all 1s).
2. Loop `iter` from 1 to `maxIter`:
   - Compute `w = A v`.
   - Find `lambda = fracv * wv * v` (Rayleigh Quotient).
   - Normalize `w`: `v = w / |w|_infinity` (divide by element with max absolute value).
   - Check convergence: If `|lambda - lambda_old| < epsilon`, break.
   - Update `lambda_old = lambda`.
3. Return `lambda`.

### Time Complexity

- **O(k \cdot n^2)** where `k` is iterations.

### Space Complexity

- **O(n^2)** to store matrix.

![Algorithm Visualization](../images/MTH-014/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-014/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `A = [[2, 0], [0, 1]]`.
1. `v = [1, 1]`.
2. `w = A v = [2, 1]`.
3. `RQ = (1*2 + 1*1) / (1*1 + 1*1) = 3/2 = 1.5`.
4. `Norm w`: max is 2. `v = [1, 0.5]`.
5. `w = A v = [2, 0.5]`.
6. `RQ = (1*2 + 0.5*0.5) / (1*1 + 0.5*0.5) = 2.25 / 1.25 = 1.8`.
7. `Norm w`: max is 2. `v = [1, 0.25]`.
8. Converges to `v = [1, 0]`, `lambda = 2`.

![Example Visualization](../images/MTH-014/example-1.png)

## ✅ Proof of Correctness

### Invariant
The vector `v` aligns closer to the principal eigenvector with each iteration.
The Rayleigh Quotient provides an increasingly accurate estimate of the eigenvalue.

### Why the approach is correct
- Assuming a unique largest eigenvalue, the component of `v` in the direction of the principal eigenvector grows as `(lambda_1 / lambda_2)^k`.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Inverse Iteration.
  - *Hint:* Apply power method to `(A - mu I)^-1` to find eigenvalue closest to `mu`.
- **Extension 2:** Deflation.
  - *Hint:* Find largest, remove it, find next largest.
- **Extension 3:** QR Algorithm.
  - *Hint:* Finds all eigenvalues.

### Common Mistakes to Avoid

1. **Normalization**
   - ❌ Wrong: Forgetting to normalize leads to overflow/underflow.
   - ✅ Correct: Divide by norm at each step.

2. **Convergence**
   - ❌ Wrong: Assuming it always works.
   - ✅ Correct: Fails if `lambda_1 = -lambda_2` (oscillation).

## Related Concepts

- **PageRank:** A variant for stochastic matrices.
- **SVD:** Uses power method on `A^T A`.
