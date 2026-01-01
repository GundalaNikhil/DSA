---
problem_id: MTH_FWHT_XOR_CONVOLUTION__7451
display_id: MTH-008
slug: fwht-xor-convolution
title: "Fast Walsh-Hadamard Transform (XOR Convolution)"
difficulty: Medium
difficulty_score: 62
topics:
  - MathAdvanced
  - Fast
tags:
  - math-advanced
  - fwht
  - medium
premium: true
subscription_tier: basic
---

# MTH-008: Fast Walsh-Hadamard Transform (XOR Convolution)

## 📋 Problem Summary

Given two arrays `A` and `B` of size `2^k`, compute their **XOR convolution** `C`.
- `C[k] = sum_i oplus j = k A[i] x B[j]`.
- Output the result modulo `10^9+7`.

## 🌍 Real-World Scenario

**Scenario Title:** The Quantum Logic Gate Simulation

In quantum computing, the **Hadamard Gate** is a fundamental operation that creates superposition.
- A quantum state of `k` qubits is a vector of size `2^k`.
- Applying Hadamard gates to all qubits corresponds to performing a Walsh-Hadamard Transform on the state vector.
- XOR convolution appears when analyzing the interference patterns of quantum states or in coding theory (Walsh codes used in CDMA cellular networks).

Just like FFT speeds up standard multiplication, FWHT speeds up "XOR multiplication" from `O(N^2)` to `O(N log N)`.

**Why This Problem Matters:**

- **Signal Processing:** Analyzing boolean functions (spectral analysis).
- **Coding Theory:** Reed-Muller codes.
- **Competitive Programming:** Problems involving "number of pairs with XOR sum K".

![Real-World Application](../images/MTH-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: FWHT Butterfly

The structure is very similar to FFT, but the "twiddle factors" are just `+1` and `-1`.

For a block of size `2L`:
- Let `u` be an element from the first half (indices having bit 0).
- Let `v` be the corresponding element from the second half (indices having bit 1).
- **Forward Transform:**
  - `u_new = u + v`
  - `v_new = u - v`
- **Inverse Transform:**
  - Same operations, but divide by 2 at the end.

```
      u --------+--------> u + v
                 \     /
                  \   /
                   \ /
                    X
                   / \
                  /   \
                 /     \
      v --------+--------> u - v
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input Size:** `N = 2^k`.
- **Modulo:** `10^9+7`. Note that in the inverse transform, we divide by `N`. Division means multiplication by modular inverse.
- **Negative Numbers:** `u-v` can be negative. Always add `MOD` before taking modulo.

### Core Concept: The Transform Property

Just like `mathcalF(A * B) = mathcalF(A) * mathcalF(B)` for FFT:
`FWHT(A oplus B) = FWHT(A) * FWHT(B)` (pointwise multiplication).

**Algorithm:**
1. Transform `A -> hatA`.
2. Transform `B -> hatB`.
3. `hatC[i] = hatA[i] x hatB[i]`.
4. Inverse Transform `hatC -> C`.

## Naive Approach

### Intuition

Double loop over all pairs.

### Algorithm

1. Initialize `C` with zeros.
2. Loop `i` from `0` to `N-1`.
3. Loop `j` from `0` to `N-1`.
4. `C[i oplus j] += A[i] x B[j]`.

### Time Complexity

- **O(N^2)**. With `k=17`, `N ~= 1.3 x 10^5`, `N^2 ~= 1.7 x 10^10`. Too slow.

### Space Complexity

- **O(N)**.

## Optimal Approach

### Key Insight

Use Fast Walsh-Hadamard Transform (FWHT).

### Algorithm

1. **FWHT Function:**
   - Iterate length `len` from 1 to `N/2` (doubling each time).
   - Iterate `i` from 0 to `N-1` with step `2*len`.
   - Iterate `j` from 0 to `len-1`.
     - `u = A[i+j]`, `v = A[i+j+len]`.
     - `A[i+j] = u + v`.
     - `A[i+j+len] = u - v`.
2. **Convolution:**
   - `FWHT(A, false)`.
   - `FWHT(B, false)`.
   - `For i in 0..N-1: A[i] = A[i] * B[i]`.
   - `FWHT(A, true)` (Inverse).
     - Inverse is same as forward, but divide each element by `N` at the end.

### Time Complexity

- **O(N \log N)**. `17 x 2^17 ~= 2.2 x 10^6` operations.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/MTH-008/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-008/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `k=1`, `A=[1, 2]`, `B=[3, 4]`.
`N=2`.

1. **FWHT(A):**
   - `u=1, v=2`.
   - `A[0] = 1+2 = 3`.
   - `A[1] = 1-2 = -1 equiv MOD-1`.
   - `hatA = [3, -1]`.
2. **FWHT(B):**
   - `u=3, v=4`.
   - `B[0] = 3+4 = 7`.
   - `B[1] = 3-4 = -1`.
   - `hatB = [7, -1]`.
3. **Pointwise Multiply:**
   - `hatC[0] = 3 x 7 = 21`.
   - `hatC[1] = (-1) x (-1) = 1`.
   - `hatC = [21, 1]`.
4. **Inverse FWHT(C):**
   - `u=21, v=1`.
   - `C'[0] = 21+1 = 22`.
   - `C'[1] = 21-1 = 20`.
   - Divide by `N=2`:
     - `C[0] = 11`.
     - `C[1] = 10`.
5. **Result:** `[11, 10]`.

![Example Visualization](../images/MTH-008/example-1.png)

## ✅ Proof of Correctness

### Invariant
The Walsh-Hadamard Transform diagonalizes the XOR convolution operation.
`H_k = beginpmatrix 1 & 1  1 & -1 endpmatrix^otimes k`.

### Why the approach is correct
- The transform maps the convolution in the time domain to pointwise multiplication in the frequency (Walsh) domain.
- The inverse transform recovers the coefficients.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** AND/OR Convolution.
  - *Hint:* Use SOS DP (Sum Over Subsets) or Mobius Transform.
- **Extension 2:** K-dimensional FFT.
  - *Hint:* FWHT is essentially a K-dimensional FFT where each dimension has size 2.
- **Extension 3:** Subset Sum.
  - *Hint:* Use FWHT to count ways to get XOR sum `S`.

### Common Mistakes to Avoid

1. **Modulo Arithmetic**
   - ❌ Wrong: `(u - v) % MOD`.
   - ✅ Correct: `(u - v + MOD) % MOD`.

2. **Inverse Scaling**
   - ❌ Wrong: Forgetting to divide by `N` in inverse.
   - ✅ Correct: Multiply by `modInverse(N)`.

## Related Concepts

- **FFT:** For sum convolution (`i+j`).
- **SOS DP:** For subset convolution (`i & j`, `i | j`).
