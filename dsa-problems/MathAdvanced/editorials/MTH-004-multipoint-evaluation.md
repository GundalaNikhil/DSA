---
problem_id: MTH_MULTIPOINT_EVALUATION__8129
display_id: MTH-004
slug: multipoint-evaluation
title: "Multipoint Evaluation"
difficulty: Hard
difficulty_score: 75
topics:
  - MathAdvanced
  - Multipoint
tags:
  - math-advanced
  - polynomial-evaluation
  - hard
premium: true
subscription_tier: basic
---

# MTH-004: Multipoint Evaluation

## 📋 Problem Summary

You are given a polynomial `P(x)` of degree `d` and a set of `n` points `x_1, x_2, dots, x_n`. You need to compute `P(x_i)` for all `i`.
- Naive evaluation takes `O(n * d)`.
- The goal is to do this faster, specifically `O(n log^2 n)`.

## 🌍 Real-World Scenario

**Scenario Title:** The GPS Signal Decoder

In Global Positioning Systems (GPS), receivers need to decode signals from multiple satellites simultaneously. The signal processing often involves evaluating a high-degree polynomial (representing the signal's phase or frequency components) at many distinct points in time to synchronize clocks or determine position.
- If a receiver tracks 10 satellites and samples at 1000 points, naive evaluation is fine.
- But in high-frequency trading or radio astronomy, we might evaluate a degree-100,000 polynomial at 100,000 points.
- `10^10` operations is too slow. `10^5 log^2(10^5) ~= 2.5 x 10^7` operations is instant.

**Why This Problem Matters:**

- **Cryptography:** Shamir's Secret Sharing involves evaluating a polynomial to generate shares.
- **Coding Theory:** Reed-Solomon encoding is exactly multipoint evaluation.
- **Computational Geometry:** Evaluating curves at many intersection points.

![Real-World Application](../images/MTH-004/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Subproduct Tree

To evaluate `P(x)` at `x_0, x_1, x_2, x_3`, we use the property: `P(x_i) = P(x) +/-odx - x_i`.

We build a tree of polynomials:
```
Level 0:           (x-x0)(x-x1)(x-x2)(x-x3)
                  /                        \
Level 1:   (x-x0)(x-x1)                (x-x2)(x-x3)
          /            \              /            \
Level 2: x-x0          x-x1        x-x2          x-x3
```

**Algorithm Flow:**
1. **Build Tree (Bottom-Up):** Multiply polynomials to get the root.
2. **Evaluate (Top-Down):**
   - Start with `P(x)` at root.
   - Go Left: `P_left = P +/-odLeftChildPoly`.
   - Go Right: `P_right = P +/-odRightChildPoly`.
   - Base Case (Leaf): `P +/-odx-x_i` is a constant, which is `P(x_i)`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Modulus:** `10^9+7`. This is NOT NTT-friendly.
- **Strategy:** Since the problem is "Hard" and constraints are `10^5`, standard `O(N log^2 N)` usually assumes NTT. With `10^9+7`, we strictly need **3-modulus NTT + CRT** or **Split FFT**.
- **However:** For the sake of a clean editorial, we will describe the algorithm assuming an NTT-friendly modulus (like 998244353) or assuming the user implements the modular arithmetic abstraction. Given the constraints and typical competitive programming context, usually one uses a template that handles the modulo.
- **Note:** The problem specifically says "modulo `10^9+7`". This makes it significantly harder (requires MTT). We will provide the MTT implementation logic where possible or describe it.

### Core Concept: Polynomial Remainder Theorem

`P(a) = P(x) +/-odx-a`.
Generalizing: To evaluate at `x_0, dots, x_k`, we can first compute `R(x) = P(x) +/-od(x-x_0)dots(x-x_k)`.
Then `R(x_i) = P(x_i)`.
Since degree of `R` is much smaller than `P`, we save work.

## Naive Approach

### Intuition

Horner's Method for each point.

### Algorithm

For each `x_i`:
  `val = 0`
  For coeff in `P`:
    `val = val * x_i + coeff`

### Time Complexity

- **O(N \cdot D)**.

### Space Complexity

- **O(1)**.

## Optimal Approach

### Key Insight

Divide and Conquer using the Subproduct Tree.
1. **Build Tree:** Compute product of `(x-x_i)` for ranges.
2. **Down Pass:** Compute remainders.
   - `Val(node) = ParentVal +/-odTreePoly(node)`.
   - Root starts with `P(x)`.

### Algorithm

1. **Build Subproduct Tree:**
   - Leaves: `Poly_i = x - x_i`.
   - Internal: `Poly_node = Poly_left * Poly_right`.
2. **Solve Function (Top-Down):**
   - Input: Polynomial `F`, Node index `v`.
   - Base Case (Leaf): Return `F[0]` (constant term).
   - Recursive:
     - `F_left = F +/-odTree[2v]`.
     - `F_right = F +/-odTree[2v+1]`.
     - Recurse left and right.
3. **Polynomial Modulo:**
   - `A +/-od B = A - B * (A / B)`.
   - Requires Polynomial Division (Inverse).
   - `A/B` can be computed using Newton Inversion on the reversed polynomials.

### Time Complexity

- **O(N \log^2 N)**.

### Space Complexity

- **O(N \log N)** to store the tree.

![Algorithm Visualization](../images/MTH-004/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-004/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `P(x) = 1 + x^2` (Coeffs: `1, 0, 1`), Points: `0, 1, 2`.

1. **x = 0:**
   - `val = 0`
   - `i=2 (coeff 1): val = 0*0 + 1 = 1`
   - `i=1 (coeff 0): val = 1*0 + 0 = 0`
   - `i=0 (coeff 1): val = 0*0 + 1 = 1`
   - Result: 1.
2. **x = 1:**
   - `i=2: val = 1`
   - `i=1: val = 1*1 + 0 = 1`
   - `i=0: val = 1*1 + 1 = 2`
   - Result: 2.
3. **x = 2:**
   - `i=2: val = 1`
   - `i=1: val = 1*2 + 0 = 2`
   - `i=0: val = 2*2 + 1 = 5`
   - Result: 5.

![Example Visualization](../images/MTH-004/example-1.png)

## ✅ Proof of Correctness

### Invariant
Horner's method correctly computes `sum a_i x^i` by restructuring it as `(dots((a_d x + a_d-1)x + a_d-2)x + dots)x + a_0`.

### Why the approach is correct
- It performs the exact arithmetic operations defined by the polynomial.
- Modulo is applied at each step to prevent overflow.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Interpolation.
  - *Hint:* The reverse of evaluation. Given points and values, find coefficients.
- **Extension 2:** Chirp-Z Transform.
  - *Hint:* Evaluate at `g^0, g^1, dots, g^n-1`. Can be done in `O(N log N)` using convolution.
- **Extension 3:** Batch Modular Inverse.
  - *Hint:* Use multipoint evaluation to find product of all others.

### Common Mistakes to Avoid

1. **Coefficient Order**
   - ❌ Wrong: Assuming highest degree first.
   - ✅ Correct: Problem specifies lowest to highest (`a_0, a_1, dots`).

2. **Negative Modulo**
   - ❌ Wrong: `val % MOD` in languages like C++/Java can be negative.
   - ✅ Correct: `(val % MOD + MOD) % MOD`.

## Related Concepts

- **Horner's Method:** The standard way to evaluate polynomials.
- **Subproduct Tree:** Key structure for fast algebra.
