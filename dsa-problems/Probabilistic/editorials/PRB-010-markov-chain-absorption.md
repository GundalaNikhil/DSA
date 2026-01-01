---
problem_id: PRB_MARKOV_CHAIN_ABSORPTION__9031
display_id: PRB-010
slug: markov-chain-absorption
title: "Markov Chain Absorption"
difficulty: Medium
difficulty_score: 55
topics:
  - Probability
  - Markov Chains
  - Linear Algebra
tags:
  - probability
  - markov
  - absorption
  - medium
premium: true
subscription_tier: basic
---

# PRB-010: Markov Chain Absorption

## 📋 Problem Summary

Given a Markov Chain with n states, some of which are absorbing (once entered, cannot leave).
Starting from state s, calculate:

1. The expected number of steps until absorption.
2. The probability of being absorbed into each specific absorbing state.

| | |
|---|---|
| **Input** | Transition matrix P, start state s |
| **Output** | Expected steps, List of absorption probabilities |

## 🌍 Real-World Scenario

**Scenario Title:** The Customer Conversion Funnel

You are analyzing user behavior on an e-commerce site.

- States: "Homepage", "Product Page", "Cart", "Checkout", "Purchase" (Absorbing), "Exit" (Absorbing).
- Users move between states with certain probabilities (e.g., 30% from Cart to Checkout, 10% to Exit).
- You want to know:
  - **Expected Steps:** How many pages does a user visit before either buying or leaving? (Engagement metric).
  - **Absorption Probabilities:** What is the probability a user eventually buys vs. exits? (Conversion Rate).
- This helps in optimizing the UX flow to maximize purchases.

**Why This Problem Matters:**

- **Finance:** Credit rating migration (probability of default).
- **Genetics:** Wright-Fisher model for gene fixation.
- **Board Games:** Snakes and Ladders analysis.

![Real-World Application](../images/PRB-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Customer Journey Visualization

Real-world example of the e-commerce funnel:

```
         0.3           0.5           0.7
Homepage ───→ Product ───→ Cart ───→ Checkout ───→ [Purchase] ✓
   │            │           │            │         (Absorbing)
   │ 0.7        │ 0.5       │ 0.3        │ 0.3
   └────────────┴───────────┴────────────┴────────→ [Exit] ✗
                                                   (Absorbing)

States:
• 0: Homepage  (Transient) ─┐
• 1: Product   (Transient)  ├─ Can move between these
• 2: Cart      (Transient)  │
• 3: Checkout  (Transient) ─┘
• 4: Purchase  (Absorbing) ─ Once here, stays forever
• 5: Exit      (Absorbing) ─ Once here, stays forever
```

### Matrix Canonical Form

States: 0 (Transient), 1 (Transient), 2 (Absorbing), 3 (Absorbing).
Rearrange matrix so transient states come first, then absorbing.

```
         Transient | Absorbing
              T1 T2 | A1 A2
            +-------+-------+
  Transient | Q     | R     |  ← Transient → Transient (Q)
         T1 |       |       |  ← Transient → Absorbing (R)
         T2 |       |       |
            +-------+-------+
  Absorbing | 0     | I     |  ← Always 0 (can't leave)
         A1 |       |       |  ← Identity (stay in place)
         A2 |       |       |
            +-------+-------+
```

**Key Submatrices:**

- **Q:** Transitions between transient states (size: t×t)
- **R:** Transitions from transient to absorbing (size: t×a)
- **0:** Zero matrix - absorbing states can't go to transient
- **I:** Identity matrix - absorbing states stay put

**Fundamental Matrix:** N = (I - Q)^{-1}$

- Element `N_ij` = Expected visits to state j starting from state i
- Each row sums to total expected steps before absorption

**Key Formulas:**

1. Expected steps vector: t = N \times \mathbf{1}$ (column of 1s)
2. Absorption probabilities: B = N \times R$

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Absorbing State:** A state i where P_ii = 1.
- **Constraints:** n \le 20$. Matrix inversion is O(n^3), perfectly fine.
- **Output Format:**
  - First line: Expected steps (scalar).
  - Second line: Probabilities for _all_ absorbing states, sorted by their original index.
  - If start state is absorbing, expected steps = 0, prob for itself = 1, others = 0.

### Core Concept: Fundamental Matrix

**What is the Fundamental Matrix N?**

For an absorbing Markov chain, the matrix N = (I - Q)^{-1}$ is called the **Fundamental Matrix**.

**Intuitive Meaning:**

- Element `N_ij` = "Starting from transient state i, how many times (on average) will I visit transient state j before getting absorbed?"
- The sum of row i in N = "Starting from state i, how many total steps until absorption?"

**Why It Works:**

Think of it as an infinite series:

- Visit state j directly: `Q_ij` (1 step)
- Visit via 2 steps: `(Q^2)_ij` (go through one intermediate)
- Visit via 3 steps: `(Q^3)_ij` (go through two intermediates)
- ...and so on

Total expected visits: N = I + Q + Q^2 + Q^3 + \dots$

This infinite geometric series sums to `(I - Q)^-1` (just like `1 + r + r^2 + dots = frac11-r`)

**Absorption Probabilities:**

Once we know N (expected visits to transient states), we multiply by R (probabilities of jumping to absorbing states from transient states) to get B = N \times R$, which gives the probability of ending in each absorbing state.

## Naive Approach

### Intuition

Simulate random walks until absorption.

### Algorithm

Monte Carlo simulation.

### Time Complexity

- **O(Trials \cdot Steps)**. Inaccurate and slow.

## Optimal Approach

### Key Insight

Use Gaussian Elimination to invert the matrix `(I - Q)` or solve the linear systems directly.
Since we only need the result for a specific start state s, we can solve the linear equations just for variable s (or all variables if we want full matrix).
Given n is small (20), full matrix operations are easiest.

### Algorithm Flowchart

```
                ┌─────────────────┐
                │  Input: P, s    │
                └────────┬─────────┘
                         ↓
            ┌────────────────────────┐
            │ Identify Absorbing     │
            │ (P[i][i] = 1.0)       │
            └────────┬────────────────┘
                     ↓
          ┌──────────────────────┐
          │ Is start state s     │────Yes──→ ┌────────────────┐
          │ absorbing?           │           │ Steps = 0      │
          └──────────┬───────────┘           │ Prob[s] = 1.0  │
                     │ No                    │ Others = 0.0   │
                     ↓                       └────────────────┘
         ┌────────────────────────┐
         │ Separate states into:  │
         │ • Transient list (T)   │
         │ • Absorbing list (A)   │
         └────────┬───────────────┘
                  ↓
      ┌───────────────────────────┐
      │ Build Q matrix (T × T)    │
      │ Build R matrix (T × A)    │
      └────────┬──────────────────┘
               ↓
      ┌───────────────────────────┐
      │ Compute I - Q             │
      └────────┬──────────────────┘
               ↓
      ┌───────────────────────────┐
      │ Invert: N = (I-Q)^(-1)    │
      │ (Gaussian Elimination)    │
      └────────┬──────────────────┘
               ↓
      ┌───────────────────────────┐
      │ Find s_idx in transient   │
      │ list                      │
      └────────┬──────────────────┘
               ↓
      ┌───────────────────────────┐
      │ Expected Steps:           │
      │ E = Σ N[s_idx][j]        │
      └────────┬──────────────────┘
               ↓
      ┌───────────────────────────┐
      │ Absorption Probs:         │
      │ B[j] = Σ N[s_idx][k]×R[k][j] │
      └────────┬──────────────────┘
               ↓
         ┌─────────────┐
         │   Output    │
         └─────────────┘
```

### Detailed Algorithm Steps

1. Identify absorbing states (P_ii == 1).
2. If start state s is absorbing:
   - Expected steps = 0.
   - Probs: 1.0 for s, 0.0 for others.
   - Return.
3. Separate states into Transient (T) and Absorbing (A).
4. Construct submatrices Q (TxT) and R (TxA).
5. Compute I - Q$.
6. Invert M = I - Q$ to get N.
7. Expected steps from s: Sum of row in N corresponding to s.
   - Note: s is an index in original matrix. Map it to index in T.
8. Absorption probs from s: Row in B = N \times R$ corresponding to s.
9. Print results.

### Time Complexity

- **O(n^3)** for inversion.

### Space Complexity

- **O(n^2)**.

![Algorithm Visualization](../images/PRB-010/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-010/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

### Example: Simple 3-State Chain

**Input:**

```
3 0
0.5 0.5 0
0 0.5 0.5
0 0 1
```

**Step-by-Step Visualization:**

```
State Diagram:
     0.5       0.5
  0 ────→ 1 ────→ [2]
  ↑       ↑       Absorbing
  │ 0.5   │ 0.5   (Stays forever)
  └───────┘
```

**Step 1: Identify States**

- Absorbing states: {2} (P[2][2] = 1.0)
- Transient states: {0, 1}
- Start state: s = 0 (transient)

**Step 2: Build Submatrices**

Original Matrix P:

```
     0    1    2
0 [0.5  0.5  0.0]
1 [0.0  0.5  0.5]
2 [0.0  0.0  1.0]
```

Extract Q (Transient → Transient):

```
Q =  0    1
  0[0.5  0.5]
  1[0.0  0.5]
```

Extract R (Transient → Absorbing):

```
R =  2
  0[0.0]
  1[0.5]
```

**Step 3: Compute I - Q**

```
I - Q =  0    1
      0[0.5 -0.5]
      1[0.0  0.5]
```

**Step 4: Invert to get N**

Using Gaussian elimination:

```
N = (I - Q)^(-1) =  0   1
                  0[2.0 2.0]
                  1[0.0 2.0]
```

**Interpretation of N:**

- N[0][0] = 2.0: Starting from state 0, visit state 0 an average of 2 times
- N[0][1] = 2.0: Starting from state 0, visit state 1 an average of 2 times
- N[1][1] = 2.0: Starting from state 1, visit state 1 an average of 2 times

**Step 5: Calculate Expected Steps**

For s = 0:

```
E[0] = Σ N[0][j] = N[0][0] + N[0][1]
     = 2.0 + 2.0
     = 4.0 steps
```

**Step 6: Calculate Absorption Probabilities**

B = N × R:

```
B[0][2] = N[0][0] × R[0][0] + N[0][1] × R[1][0]
        = 2.0 × 0.0 + 2.0 × 0.5
        = 0.0 + 1.0
        = 1.0
```

**Output:**

```
4.000000      (Expected steps)
1.000000      (Probability of absorbing into state 2)
```

**Verification:**

- Makes sense! From state 0, you can only reach state 2 eventually
- On average, you bounce between states 0 and 1 about 4 times before reaching 2
- Probability of ending in state 2 is 100% (only absorbing state reachable)

## ✅ Proof of Correctness

### Invariant

The Fundamental Matrix N correctly sums the geometric series of visits to transient states.

### Why the approach is correct

Standard linear algebra solution for Absorbing Markov Chains.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** PageRank.
  - _Hint:_ Eigenvector of transition matrix (for ergodic chains).
- **Extension 2:** Sparse Matrices.
  - _Hint:_ Use iterative methods (Power Iteration) if n is large.
- **Extension 3:** Infinite State Space.
  - _Hint:_ Random Walk on 1D line (Gambler's Ruin).

### Common Mistakes to Avoid

1. **Singular Matrix**
   - ❌ Wrong: Assuming `I-Q` is always invertible.
   - ✅ Correct: It is invertible if every transient state can eventually reach an absorbing state.
2. **Row Sums**
   - ❌ Wrong: Rows not summing to 1.
   - ✅ Correct: Verify input validity.

## Related Concepts

- **Eigenvalues:** 1 is always an eigenvalue of stochastic matrices.
- **Dynamic Programming:** Special case when graph is a DAG.
