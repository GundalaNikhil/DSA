---
problem_id: MTH_LAGRANGE_INTERPOLATION_MOD__3542
display_id: MTH-005
slug: lagrange-interpolation-mod
title: "Lagrange Interpolation Mod Prime"
difficulty: Medium
difficulty_score: 60
topics:
  - MathAdvanced
  - Lagrange
tags:
  - math-advanced
  - lagrange-interpolation
  - medium
premium: true
subscription_tier: basic
---

# MTH-005: Lagrange Interpolation Mod Prime

## 📋 Problem Summary

Given `k` points `(x_i, y_i)` where all `x_i` are distinct, find the value of the unique polynomial `P(x)` of degree at most `k-1` evaluated at a query point `X`. All calculations are modulo a prime `MOD`.

## 🌍 Real-World Scenario

**Scenario Title:** The Secret Vault Key

A company wants to secure its master password using **Shamir's Secret Sharing**.
- The secret key `S` is the constant term `P(0)` of a random polynomial `P(x)`.
- The company distributes "shares" to 5 executives. Each share is a point `(x_i, P(x_i))`.
- To unlock the vault, any 3 executives must combine their shares.
- Combining shares means reconstructing the polynomial `P(x)` from the points and evaluating it at `X=0`.

This problem generalizes this: given any set of points, find the value at any other point `X`.

**Why This Problem Matters:**

- **Cryptography:** Secure multi-party computation and threshold schemes.
- **Data Recovery:** Reconstructing lost data packets (Reed-Solomon codes) is essentially interpolation.
- **Computer Graphics:** Curve fitting through control points.

![Real-World Application](../images/MTH-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Lagrange Basis

The formula constructs the polynomial as a weighted sum of "basis polynomials" `L_i(x)`.
`L_i(x)` has the property that `L_i(x_i) = 1` and `L_i(x_j) = 0` for `j !=q i`.

```
Points: (x0, y0), (x1, y1), (x2, y2)

P(x) = y0 * L0(x) + y1 * L1(x) + y2 * L2(x)

Where L0(x) = (x-x1)(x-x2) / (x0-x1)(x0-x2)
      L1(x) = (x-x0)(x-x2) / (x1-x0)(x1-x2)
      L2(x) = (x-x0)(x-x1) / (x2-x0)(x2-x1)
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Distinct x:** The denominator in Lagrange formula is never zero.
- **Modulus:** All operations (add, sub, mul, div) are modulo `MOD`. Division means multiplying by modular inverse.
- **Constraints:** `k <= 200,000`. An `O(k^2)` solution will TLE. We need `O(k)` or `O(k log k)`.
- **Special Case:** If `x_i` are consecutive (e.g., `0, 1, dots, k-1`), we can solve in `O(k)` using precomputed factorials. If `x_i` are arbitrary, we need `O(k^2)` generally, or `O(k log^2 k)` with multipoint evaluation techniques.
- **Implementation Note:** The standard Lagrange formula is `O(k^2)`. For "Medium" difficulty with `k <= 200,000`, the problem typically uses consecutive points (`x_i = i`), or the test cases have smaller `k` values in practice. Advanced FFT-based multipoint evaluation can achieve `O(k log^2 k)` but requires "Hard" difficulty.
- **Optimization:** The numerator for term `i` is `prod_j !=q i (X - x_j)`. Computing `TotalProd = prod (X - x_j)` allows calculating each numerator as `TotalProd * (X - x_i)^-1` in `O(1)`. However, the denominator `prod_j !=q i (x_i - x_j)` still requires `O(k)` per term, yielding total `O(k^2)` complexity for arbitrary points.

### Core Concept: Lagrange Formula


`P(X) = sum_i=0^k-1 y_i <=ft( \prod_j !=q i \fracX - x_jx_i - x_j \right) +/-odMOD`


## Naive Approach

### Intuition

Implement the formula directly with nested loops.

### Algorithm

1. Initialize `ans = 0`.
2. Loop `i` from 0 to `k-1`:
   - `term = y[i]`.
   - Loop `j` from 0 to `k-1`:
     - If `i == j` continue.
     - `term = term * (X - x[j]) * modInverse(x[i] - x[j])`.
   - `ans = (ans + term) % MOD`.

### Time Complexity

- **O(k^2)**.

### Space Complexity

- **O(k)**.

## Optimal Approach (for arbitrary points without FFT)

### Key Insight

We can precompute the numerator product prefix and suffix arrays to avoid recomputing `prod (X - x_j)` every time, but the denominator `prod (x_i - x_j)` still depends on `x_i`.
So for arbitrary points, `O(k^2)` is the standard "simple" solution.
However, if we compute the denominator using a similar prefix/suffix trick? No, because the base `x_i` changes.

**Optimization:**
Compute `Num = prod_j (X - x_j)`.
Then the numerator part for `i` is `Num * (X - x_i)^-1`.
This reduces the numerator work to `O(1)`.
The denominator is still the bottleneck.

### Algorithm

1. Calculate `TotalProduct = product(X - x[j])` for all `j`.
2. For each `i`:
   - `Numerator = TotalProduct * modInverse(X - x[i])`.
   - `Denominator = product(x[i] - x[j])` for all `j != i`. (This loop makes it `O(k^2)`).
   - `Term = y[i] * Numerator * modInverse(Denominator)`.
   - Add to `ans`.

### Time Complexity

- **O(k^2)**.

### Space Complexity

- **O(k)**.

![Algorithm Visualization](../images/MTH-005/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-005/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `(0, 1), (1, 3)`, Query `X=2`, `MOD=10^9+7`.

1. **i = 0 (Point 0, 1):**
   - `x_0=0, y_0=1`.
   - `j=1 (x_1=1)`:
     - `Num = (2 - 1) = 1`.
     - `Den = (0 - 1) = -1 equiv MOD-1`.
   - `Term = 1 * 1 * (-1)^-1 = -1`.
2. **i = 1 (Point 1, 3):**
   - `x_1=1, y_1=3`.
   - `j=0 (x_0=0)`:
     - `Num = (2 - 0) = 2`.
     - `Den = (1 - 0) = 1`.
   - `Term = 3 * 2 * 1^-1 = 6`.
3. **Sum:**
   - `Ans = -1 + 6 = 5`.

Result: 5.

![Example Visualization](../images/MTH-005/example-1.png)

## ✅ Proof of Correctness

### Invariant
The Lagrange basis polynomial `L_i(x)` is constructed such that it is 1 at `x_i` and 0 at all other `x_j`. The linear combination `sum y_i L_i(x)` therefore passes through all points.

### Why the approach is correct
- Since degree is at most `k-1`, and it matches `k` points, by the Uniqueness Theorem of interpolating polynomials, this IS the polynomial.
- Modular arithmetic preserves these algebraic properties.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Consecutive Points (`x_i = i`).
  - *Hint:* Denominator becomes factorials: `i! * (-1)^k-1-i (k-1-i)!`. Can solve in `O(k)`.
- **Extension 2:** Evaluate at all `0 dots N`.
  - *Hint:* Convolution.
- **Extension 3:** Secret Sharing.
  - *Hint:* Generate random coefficients, evaluate at `N` points.

### Common Mistakes to Avoid

1. **Division by Zero**
   - ❌ Wrong: If `X` matches one of the `x_i`, the term `(X-x_i)` in numerator is 0.

2. **Negative Modulo**
   - ❌ Wrong: `(a - b) % MOD`.
   - ✅ Correct: `(a - b + MOD) % MOD`.

## Related Concepts

- **Chinese Remainder Theorem:** Similar concept of reconstruction.
- **Vandermonde Matrix:** The matrix form of interpolation.
