---
problem_id: MTH_INVERSE_POLYNOMIAL__7264
display_id: MTH-003
slug: inverse-polynomial
title: "Inverse Polynomial Mod x^n"
difficulty: Hard
difficulty_score: 72
topics:
  - MathAdvanced
  - Polynomial
  - Newton Iteration
tags:
  - math-advanced
  - polynomial-inverse
  - newton-method
  - hard
premium: true
subscription_tier: basic
---

# MTH-003: Inverse Polynomial Mod x^n

## 📋 Problem Summary

Given a polynomial `P(x)`, find another polynomial `Q(x)` such that `P(x) * Q(x) equiv 1 +/-odx^n`.
- The coefficients are in a finite field modulo a prime `MOD`.
- `P[0]` is non-zero (guaranteeing an inverse exists).
- Output the first `n` coefficients of `Q(x)`.

## 🌍 Real-World Scenario

**Scenario Title:** The Corrupted Data Stream

In advanced communication systems (like satellite links), data is encoded as polynomials to survive noise. This is the basis of **Reed-Solomon Error Correction**.
- To decode a message, we often need to divide polynomials.
- In modular arithmetic, "division" by `P(x)` is actually "multiplication by the inverse of `P(x)`".
- Finding this inverse efficiently is crucial for decoding gigabytes of data in real-time.

Just like finding `1/7` in decimal gives an infinite series `0.142857...`, finding `1/P(x)` gives an infinite polynomial series. We only need the first `n` terms (modulo `x^n`) to reconstruct the message accurately.

**Why This Problem Matters:**

- **Cryptography:** Polynomial operations are central to post-quantum cryptography schemes (like NTRU).
- **Generating Functions:** In combinatorics, `1/P(x)` is the generating function for linear recurrences.
- **Computer Algebra Systems:** Tools like Mathematica use this for fast symbolic computation.

![Real-World Application](../images/MTH-003/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Newton Iteration

We want to solve `F(Q) = frac1Q - P = 0`.
Newton's Method finds roots by iterating: `x_new = x_old - fracf(x_old)f'(x_old)`.

For polynomials:
1. **Base Case:** `n=1`. `Q(x) equiv P[0]^-1 +/-od x`.
2. **Step:** If we know `Q_k(x)` such that `P * Q_k equiv 1 +/-odx^lceil n/2 rceil`, we can find `Q_2k(x)` modulo `x^n`.
3. **Formula:** `Q_new(x) = Q_old(x) * (2 - P(x) * Q_old(x)) +/-odx^n`.

```
Iteration 0: [1]          (Mod x^1)
      |
      v Double Precision
Iteration 1: [1, -1]      (Mod x^2)
      |
      v Double Precision
Iteration 2: [1, -1, 1, 0] (Mod x^4)
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Modulus:** The problem typically uses `998244353`, which supports NTT.
- **Degree:** If input `P` has degree `K`, and we need inverse mod `x^N`, we only care about the first `N` terms of `P`.
- **Output:** Exactly `N` coefficients.

### Core Concept: Newton-Raphson for Polynomials

The standard Newton iteration for finding root of `f(x)=0` is `x_i+1 = x_i - fracf(x_i)f'(x_i)`.
We want to find `Q` such that `Q = 1/P`, or `1/Q - P = 0`.
Let `f(Q) = Q^-1 - P`.
Then `f'(Q) = -Q^-2`.
`Q_new = Q - fracQ^-1 - P-Q^-2 = Q + Q^2(Q^-1 - P) = Q + Q - P Q^2 = 2Q - P Q^2 = Q(2 - PQ)`.

## Naive Approach

### Intuition

Polynomial long division. Compute `1 / P(x)` term by term.

### Algorithm

1. `Q[0] = P[0]^-1`.
2. For `i` from 1 to `n-1`:
   - Compute coefficient of `x^i` in `P * Q`.
   - Adjust `Q[i]` to make the term zero.

### Time Complexity

- **O(N^2)**.

### Space Complexity

- **O(N)**.

## Optimal Approach

### Key Insight

Use **Divide and Conquer** with **NTT**.
To compute inverse mod `x^n`, first compute inverse mod `x^lceil n/2 rceil`, then use the Newton formula to double the precision.

### Algorithm

1. **Base Case:** If `n=1`, return `[power(P[0], MOD-2)]`.
2. **Recursive Step:**
   - Recursively compute `Q_half = Inverse(P, lceil n/2 rceil)`.
   - We want `Q_full = Q_half (2 - P * Q_half) +/-odx^n`.
   - Use NTT for multiplication:
     - Pad `Q_half` and `P` (first `n` terms) to suitable power of 2.
     - `NTT(Q_half)`, `NTT(P)`.
     - Pointwise: `Res[i] = Q_half[i] * (2 - P[i] * Q_half[i])`.
     - Inverse NTT.
   - Truncate to `n` terms.

### Time Complexity

- `T(n) = T(n/2) + O(n log n)`.
- By Master Theorem, **O(n \log n)**.

### Space Complexity

- **O(n)**.

![Algorithm Visualization](../images/MTH-003/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-003/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `P = [1, 1]`, `n = 3`, `MOD = 998244353`
`P(x) = 1 + x`.

1. **Base Case:** `n=1`. `Q_0 = [1^-1] = [1]`.
2. **Iteration 1:** Target `n=2`.
   - `Q_old = [1]`.
   - `P` (mod `x^2`) = `[1, 1]`.
   - `Q_new = Q(2 - PQ) +/-odx^2`.
   - `PQ = 1+x`.
   - `2 - PQ = 1-x`.
   - `Q(2-PQ) = 1(1-x) = 1-x`.
   - `Q_1 = [1, -1] equiv [1, 998244352]`.
3. **Iteration 2:** Target `n=4` (covers 3).
   - `Q_old = [1, -1]`.
   - `P = [1, 1]`.
   - `PQ = (1+x)(1-x) = 1-x^2`.
   - `2 - PQ = 1+x^2`.
   - `Q(2-PQ) = (1-x)(1+x^2) = 1-x+x^2-x^3`.
   - `Q_2 = [1, -1, 1, -1]`.
4. **Truncate:** First 3 terms: `[1, -1, 1]`.
   - Modulo: `[1, 998244352, 1]`.

![Example Visualization](../images/MTH-003/example-1.png)

## ✅ Proof of Correctness

### Invariant
If `P * Q_k equiv 1 +/-odx^2^k`, then `Q_k+1 = Q_k(2 - P Q_k)` satisfies `P * Q_k+1 equiv 1 +/-odx^2^k+1`.

### Why the approach is correct
- Let `A = P^-1`. Then `A - Q_k equiv 0 +/-odx^2^k`.
- Squaring both sides: `(A - Q_k)^2 equiv 0 +/-odx^2^k+1`.
- `A^2 - 2AQ_k + Q_k^2 equiv 0`.
- Multiply by `P` (where `PA=1`): `A - 2Q_k + P Q_k^2 equiv 0`.
- `A equiv 2Q_k - P Q_k^2 = Q_k(2 - P Q_k)`.
- This confirms the quadratic convergence of Newton iteration.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Polynomial Division.
  - *Hint:* `A(x) / B(x)` can be computed by reversing coefficients and multiplying by `Inverse(B_rev)`.
- **Extension 2:** Polynomial Logarithm.
  - *Hint:* `ln P(x) = int fracP'(x)P(x) dx`. Requires inverse.
- **Extension 3:** Polynomial Exponentiation.
  - *Hint:* `P(x)^k = exp(k ln P(x))`.

### Common Mistakes to Avoid

1. **Array Sizing**
   - ❌ Wrong: Using size `n` for NTT.
   - ✅ Correct: Must use `2n` (next power of 2) because intermediate product `P * Q` has degree `2n-2`.

2. **Modular Arithmetic**
   - ❌ Wrong: Negative results in subtraction.
   - ✅ Correct: Add MOD before modulo.

## Related Concepts

- **Newton's Method:** General root finding.
- **Formal Power Series:** The theoretical framework.
- **NTT:** The engine for fast multiplication.
