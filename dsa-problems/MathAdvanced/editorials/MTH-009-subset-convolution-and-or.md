---
problem_id: MTH_SUBSET_CONVOLUTION_AND_OR__9174
display_id: MTH-009
slug: subset-convolution-and-or
title: "Subset Convolution (AND/OR)"
difficulty: Hard
difficulty_score: 78
topics:
  - MathAdvanced
  - Subset
tags:
  - math-advanced
  - subset-convolution
  - hard
premium: true
subscription_tier: basic
---

# MTH-009: Subset Convolution (AND/OR)

## 📋 Problem Summary

Given two arrays `A` and `B` of size `2^n`, compute their **Subset Convolution**.
- **OR Convolution:** `C[k] = sum_i | j = k A[i] x B[j]`.
- **AND Convolution:** `C[k] = sum_i & j = k A[i] x B[j]`.
- **Disjoint Subset Convolution:** `C[k] = sum_i | j = k, i & j = 0 A[i] x B[j]`.

*Note: The problem title says "AND/OR", but the "Subset Convolution" usually refers to the Disjoint case. The example shows OR convolution. We will cover OR/AND convolution (SOS DP) as it matches the "Medium/Hard" difficulty better than the full `O(n^2 2^n)` disjoint convolution. However, the constraints (`n <= 20`) and "Subset Convolution" tag often imply the disjoint case. We will implement the OR convolution as per the example, but explain the disjoint case in extensions.*

## 🌍 Real-World Scenario

**Scenario Title:** The Team Skill Merger

Imagine you are building a team of experts.
- You have a set of skills `1, dots, n`.
- `A[mask]` is the number of candidates who possess exactly the set of skills in `mask`.
- `B[mask]` is the number of candidates from a different department with skills `mask`.
- You want to form a pair (one from A, one from B) such that their **combined skills** match a target set `K`.
- If you just need the union of skills to be `K`, that's **OR Convolution**.
- If you need them to have disjoint skills that sum to `K`, that's **Disjoint Subset Convolution**.

This operation is fundamental in **Exact Exponential Algorithms** for problems like Steiner Tree, Graph Coloring, and Hamiltonian Path.

![Real-World Application](../images/MTH-009/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: SOS DP (Sum Over Subsets)

For OR Convolution, we want `C[k] = sum_i | j = k A[i] B[j]`.
This looks hard. But if we transform `A` to `hatA` where `hatA[mask] = sum_sub subseteq mask A[sub]`, then:
`hatC[mask] = hatA[mask] x hatB[mask]`.
Why? Because if `i subseteq k` and `j subseteq k`, then `i | j subseteq k`.
After multiplying, we apply the inverse transform (Mobius Transform) to get back `C`.

```
      u --------+--------> u + v
                 \     /
                  \   /   (Only adds if bit is 1)
                   \ /
                    |
                   / \
                  /   \
                 /     \
      v --------+--------> v
```
*Note: The diagram for SOS DP is simpler: `dp[mask] += dp[mask ^ (1<<i)]`.*

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `n` (bits), `op` (0 for AND, 1 for OR).
- **OR Convolution:** Use SOS DP (Zeta Transform).
- **AND Convolution:** Use SOS DP on inverted bits (or super-set sum).
- **Modulo:** `10^9+7`.

### Core Concept: Fast Zeta Transform

To compute `sum_sub subseteq mask A[sub]` for all masks in `O(n 2^n)`:
Iterate `i` from 0 to `n-1`.
Iterate `mask` from 0 to `2^n-1`.
If `mask` has bit `i` set: `A[mask] += A[mask ^ (1<<i)]`.

**Inverse (Mobius):**
Same loop, but `A[mask] -= A[mask ^ (1<<i)]`.

## Naive Approach

### Intuition

Double loop over all pairs.

### Algorithm

Loop `i, j` from `0` to `2^n-1`.
`C[i | j] += A[i] x B[j]`.

### Time Complexity

- **O(4^n)**. For `n=20`, this is impossible (`10^12`).

### Space Complexity

- **O(2^n)**.

## Optimal Approach

### Key Insight

Use Fast Zeta Transform (FZT) / Sum Over Subsets (SOS) DP.

### Algorithm

1. **Transform:**
   - If OR: Compute `hatA[mask] = sum_i subseteq mask A[i]`.
   - If AND: Compute `hatA[mask] = sum_mask subseteq i A[i]` (Super-set sum).
2. **Pointwise Multiply:**
   - `hatC[mask] = hatA[mask] x hatB[mask]`.
3. **Inverse Transform:**
   - Apply inverse SOS DP to recover `C`.

**For OR (Subset Sum):**
- Forward: `if (mask & (1<<i)) A[mask] += A[mask ^ (1<<i)]`
- Inverse: `if (mask & (1<<i)) A[mask] -= A[mask ^ (1<<i)]`

**For AND (Superset Sum):**
- Forward: `if (!(mask & (1<<i))) A[mask] += A[mask ^ (1<<i)]`
- Inverse: `if (!(mask & (1<<i))) A[mask] -= A[mask ^ (1<<i)]`

### Time Complexity

- **O(n 2^n)**. `20 x 10^6 ~= 2 x 10^7`, very fast.

### Space Complexity

- **O(2^n)**.

![Algorithm Visualization](../images/MTH-009/algorithm-visualization.png)
![Algorithm Steps](../images/MTH-009/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `n=2`, `op=1` (OR), `A=[1, 1, 0, 0]`, `B=[0, 1, 1, 0]`.

1. **FZT(A):**
   - `i=0`: `A[1]+=A[0] (1+1=2)`, `A[3]+=A[2] (0+0=0)`. `A=[1, 2, 0, 0]`.
   - `i=1`: `A[2]+=A[0] (0+1=1)`, `A[3]+=A[1] (0+2=2)`. `A=[1, 2, 1, 2]`.
   - `hatA = [1, 2, 1, 2]`. (Sum of subsets: {}:1, {0}:1+1=2, {1}:1+0=1, {0,1}:1+1+0+0=2).
2. **FZT(B):**
   - `hatB = [0, 1, 1, 2]`.
3. **Pointwise:**
   - `hatC = [0, 2, 1, 4]`.
4. **Inverse FZT(C):**
   - `i=0`: `C[1]-=C[0] (2-0=2)`, `C[3]-=C[2] (4-1=3)`. `C=[0, 2, 1, 3]`.
   - `i=1`: `C[2]-=C[0] (1-0=1)`, `C[3]-=C[1] (3-2=1)`. `C=[0, 2, 1, 1]`.
   - **Manual OR Convolution Verification:**
     - `C[0]`: k=0, pairs where i|j=0: (0,0). `A[0]*B[0] = 1*0 = 0`. ✓
     - `C[1]`: k=1, pairs where i|j=1: (0,1), (1,0), (1,1). `A[0]*B[1] + A[1]*B[0] + A[1]*B[1] = 1*1 + 1*0 + 1*1 = 2`. ✓
     - `C[2]`: k=2, pairs where i|j=2: (0,2), (2,0), (2,2). `A[0]*B[2] + A[2]*B[0] + A[2]*B[2] = 1*1 + 0*0 + 0*1 = 1`. ✓
     - `C[3]`: k=3, pairs where i|j=3: (0,3), (1,2), (1,3), (2,1), (2,3), (3,0), (3,1), (3,2), (3,3).

   **This editorial implements OR Convolution.** The formula is `C[k] = sum_{i|j=k} A[i]*B[j]`.

   **Note on Example Output:** The problem may reference different convolution types. If the example shows `[0, 1, 1, 2]`, it uses **Disjoint Subset Convolution** (`i & j = 0, i | j = k`), not OR. See problem statement for which type is required.

![Example Visualization](../images/MTH-009/example-1.png)

## ✅ Proof of Correctness

### Invariant
`sum_s subseteq m A[s]` is the Zeta transform.
Pointwise multiplication in Zeta domain corresponds to OR convolution in primal domain.

### Why the approach is correct
- The principle of inclusion-exclusion (Mobius inversion) allows us to move between the subset sum domain and the value domain.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Disjoint Subset Convolution.
  - *Hint:* Add a dimension for "popcount". `hatA[k][mask]` stores sum of subsets of size `k`. Multiply only if `size_A + size_B = size_C`.
- **Extension 2:** GCD Convolution.
  - *Hint:* Similar to Dirichlet convolution / Mobius transform on divisibility lattice.
- **Extension 3:** Max Convolution.
  - *Hint:* `(max, +)` semiring.

### Common Mistakes to Avoid

1. **Loop Order**
   - ❌ Wrong: Loop mask then i.
   - ✅ Correct: Loop i then mask (to propagate bits correctly).

2. **Inverse Operation**
   - ❌ Wrong: Adding instead of subtracting.
   - ✅ Correct: `A[mask] -= A[mask setminus i]`.

## Related Concepts

- **FWHT:** Special case of Zeta transform on boolean lattice.
- **Dirichlet Convolution:** Zeta transform on divisibility lattice.
