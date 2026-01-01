---
problem_id: MTH_MATRIX_EXP_LINEAR_RECURRENCE__6283
display_id: MTH-007
slug: matrix-exp-linear-recurrence
title: "Matrix Exponentiation for Linear Recurrence"
difficulty: Medium
difficulty_score: 58
topics:
  - MathAdvanced
  - Matrix
tags:
  - math-advanced
  - matrix-exponentiation
  - medium
premium: true
subscription_tier: basic
---

# MTH-007: Matrix Exponentiation for Linear Recurrence

## 📋 Problem Summary

Given a linear recurrence relation `a_n = c_0 a_n-1 + c_1 a_n-2 + dots + c_k-1 a_n-k` and initial terms `a_0, dots, a_k-1`, find the `n`-th term modulo `MOD`.
- `n` can be up to `10^18`.
- `k` is small (`<= 50`).

## 🌍 Real-World Scenario

**Scenario Title:** The Rabbit Population Explosion

Fibonacci's original problem was about rabbits: pairs breed, and after a month, the offspring also breed.
- `F_n = F_n-1 + F_n-2`.
- In ecology, population models often depend on the previous few years (e.g., salmon returning to spawn after 4 years).
- If we want to predict the population 1 billion years from now (or steps in a simulation), iterating one by one is too slow (`10^9` steps).
- Matrix Exponentiation allows us to "jump" through time, calculating the state at `t=10^18` in logarithmic time.

**Why This Problem Matters:**

- **Computer Graphics:** Transformations (rotation, scaling) are matrix multiplications. Repeated application is exponentiation.
- **Dynamic Programming:** Many DP problems on graphs or sequences with small states can be optimized from `O(N)` to `O(log N)` using matrices.
- **Cryptography:** Some stream ciphers use linear feedback shift registers (LFSRs), which are linear recurrences.

![Real-World Application](../images/MTH-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: State Transition

We represent the "state" at step `i` as a vector:

`V_i = [a_i, a_i-1, \dots, a_i-k+1]^T`


We want a matrix `T` such that `V_i+1 = T x V_i`.

For Fibonacci (`a_n = a_n-1 + a_n-2`):

`\beginbmatrix a_i+1 \\ a_i \endbmatrix = 
\beginbmatrix 1 & 1 \\ 1 & 0 \endbmatrix 
\beginbmatrix a_i \\ a_i-1 \endbmatrix`


To get to step `n`, we compute `V_n = T^n-k+1 x V_k-1`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Coefficients:** The problem gives `c_0, dots, c_k-1` corresponding to `a_n-1, dots, a_n-k`.
- **Base Cases:** If `n < k`, just return `a_n` directly.
- **Matrix Size:** `k x k`.
- **Complexity:** Matrix multiplication is `O(k^3)`. Exponentiation is `O(log n)`. Total `O(k^3 log n)`. With `k=50`, `k^3 = 125,000`, `log n ~= 60`. Total ops `~= 7.5 x 10^6`, well within time limit.

### Core Concept: Transition Matrix Construction

The first row of `T` represents the recurrence equation:
`a_n = c_0 a_n-1 + c_1 a_n-2 + dots + c_k-1 a_n-k`.
Row 0: `[c_0, c_1, dots, c_k-1]`.

The subsequent rows simply shift the values:
`a_n-1 = 1 * a_n-1`.
Row 1: `[1, 0, dots, 0]`.
Row 2: `[0, 1, dots, 0]`.
...
Row `k-1`: `[0, 0, dots, 1, 0]`.

## Naive Approach

### Intuition

Iterate from `k` to `n`.

### Algorithm

Loop `i` from `k` to `n`, computing `a[i]` using the formula.

### Time Complexity

- **O(n \cdot k)**. For `n=10^18`, this will take forever.

### Space Complexity

- **O(k)** (if we only store last k terms).

## Optimal Approach

### Key Insight

Use **Binary Exponentiation** (Square and Multiply) on the transition matrix.

### Algorithm

1. **Handle Base Case:** If `n < k`, return `a_n`.
2. **Construct Matrix T:**
   - Top row: coefficients `c_0, dots, c_k-1`.
   - Sub-diagonal: `1`s at `T[i][i-1]` for `i > 0`.
3. **Construct Initial Vector V:**
   - `[a_k-1, a_k-2, dots, a_0]^T`.
   - Note the order! `a_k-1` is at the top because it's the "most recent" term needed to compute `a_k`.
4. **Compute Power:** `M = T^n - (k-1)`.
5. **Multiply:** `ResultVector = M x V`.
6. **Result:** The first element of `ResultVector` is `a_n`.

### Time Complexity

- **O(k^3 \log n)**.

### Space Complexity

- **O(k^2)**.

![Algorithm Visualization](../images/MTH-007/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-007/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `k=2, n=5, MOD=10^9+7`.
Coeffs: `[1, 1]` (`a_n = a_n-1 + a_n-2`).
Initial: `[0, 1]` (`a_0=0, a_1=1`).

1. **Matrix T:**
   - Row 0: `[1, 1]`
   - Row 1: `[1, 0]`
2. **Initial Vector V:**
   - `[a_1, a_0]^T = [1, 0]^T`.
3. **Exponent:**
   - `n - k + 1 = 5 - 2 + 1 = 4`.
   - Compute `T^4`.
   - `T^1 = [[1, 1], [1, 0]]`
   - `T^2 = [[2, 1], [1, 1]]`
   - `T^4 = [[5, 3], [3, 2]]`
4. **Result Vector:**
   - `T^4 x V = [[5, 3], [3, 2]] x [1, 0]^T = [5 * 1 + 3 * 0, 3 * 1 + 2 * 0]^T = [5, 3]^T`.
5. **Ans:**
   - First element is 5. Correct (`F_5 = 5`).

![Example Visualization](../images/MTH-007/example-1.png)

## ✅ Proof of Correctness

### Invariant
The matrix multiplication `T x V_i` correctly produces `V_i+1`.
- Top row: `c_0 a_i + c_1 a_i-1 + dots = a_i+1`.
- Other rows: `1 * a_i-j = a_i-j`.
By induction, `T^p x V_i = V_i+p`.

### Why the approach is correct
- Matrix multiplication is associative, allowing binary exponentiation.
- Modular arithmetic applies at each step.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Sum of terms `S_n = sum_i=0^n a_i`.
  - *Hint:* Augment the matrix to size `(k+1) x (k+1)` to track the sum.
- **Extension 2:** Non-homogeneous recurrence (`a_n = dots + C`).
  - *Hint:* Add a constant 1 to the state vector and matrix.
- **Extension 3:** Find `k` given sequence (Berlekamp-Massey).
  - *Hint:* Inverse problem.

### Common Mistakes to Avoid

1. **Vector Order**
   - ❌ Wrong: `[a_0, a_1, ...]`.
   - ✅ Correct: `[a_{k-1}, a_{k-2}, ..., a_0]`. The transition matrix expects the most recent terms first.

2. **Exponent Calculation**
   - ❌ Wrong: `T^n`.
   - ✅ Correct: `T^n-k+1` because we start from state `k-1`.

## Related Concepts

- **Cayley-Hamilton Theorem:** Characteristic polynomial of the matrix.
- **Berlekamp-Massey:** Finding the recurrence relation.
