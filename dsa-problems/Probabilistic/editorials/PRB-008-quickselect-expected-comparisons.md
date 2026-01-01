---
problem_id: PRB_QUICKSELECT_EXPECTED_COMPARISONS__4028
display_id: PRB-008
slug: quickselect-expected-comparisons
title: "Randomized Quickselect Expected Comparisons"
difficulty: Medium
difficulty_score: 55
topics:
  - Probability
  - Divide and Conquer
  - Expected Value
tags:
  - probability
  - quickselect
  - expectation
  - medium
premium: true
subscription_tier: basic
---

# PRB-008: Randomized Quickselect Expected Comparisons

## 📋 Problem Summary

Calculate the expected number of comparisons performed by Randomized Quickselect to find the k-th smallest element in an array of size n.

| | |
|---|---|
| **Algorithm** | Pick random pivot, partition (cost n-1), recurse on the side containing k |
| **Input** | n, k |
| **Output** | Expected comparisons (float) |

## 🌍 Real-World Scenario

**Scenario Title:** The Median Salary Report

You are a data analyst for a large corporation with n employees.
- You need to find the median salary (or the 90th percentile) to generate a report.
- Sorting the entire database takes O(n \log n) time, which is slow for massive datasets.
- Instead, you use **Quickselect**, which finds the k-th element in O(n) expected time.
- However, the "expected" time depends on randomness. If you are unlucky, it could be O(n^2).
- You want to compute the theoretical expected cost (comparisons) to justify using this algorithm over sorting.

**Why This Problem Matters:**

- **Algorithm Analysis:** Understanding average-case complexity vs worst-case.
- **Database Optimization:** Selecting efficient query plans.
- **Order Statistics:** Finding medians, percentiles efficiently.

![Real-World Application](../images/PRB-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Quickselect Partition

n = 5, k=3$. Array `[A, B, C, D, E]`.
Pivot chosen randomly.
Partition cost: 5-1 = 4 comparisons.

Cases for Pivot Rank i:
1. i = 1(Pivot is min). Recurse on right (size 4) for k-1=2$.
2. i = 2. Recurse on right (size 3) for k-2=1.
3. i = 3$. Found! Cost 0 more.
4. i = 4. Recurse on left (size 3) for k = 3$.
5. i = 5. Recurse on left (size 4) for k = 3$.

`E(5, 3) = 4 + frac15 [ E(4, 2) + E(3, 1) + 0 + E(3, 3) + E(4, 3) ]`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Recurrence:**
  `E(n, k) = (n-1) + frac1n sum_i=1^n cost_subproblem(i)`.
  - If i = = k$: Done. Cost 0.
  - If i > k: Recurse Left. Size i-1, target k. Cost E(i-1, k)$.
  - If i < k: Recurse Right. Size n-i, target k-i`. Cost E(n-i, k-i)`.
- **Base Case:** `E(1, 1) = 0` (0 comparisons to find 1st in size 1). Or `E(0, dots) = 0`.
- **Constraints:** n \le 2000$. O(n^2) DP is required.

### Core Concept: Linearity of Expectation

The total expected comparisons is the sum of the probability that any pair `(x, y)` is compared.
However, using the recursive definition is more direct for specific n, k.
The recurrence relation builds the solution bottom-up.

## Naive Approach

### Intuition

Recursive function without memoization.

### Algorithm

Direct recursion.

### Time Complexity

- **Exponential**. Many overlapping subproblems.

## Optimal Approach

### Key Insight

Dynamic Programming (Memoization).
State is `(n, k)`.
Table size `2000 x 2000`.
Fill table or use memoized recursion.

### Algorithm

1. Initialize `memo[n+1][n+1]` with -1.
2. Define `solve(n, k)`:
   - If n \le 1$, return 0.
   - If `memo[n][k]` exists, return it.
   - `sum = 0`.
   - Loop `i` from 1 to `n`:
     - If `i > k`: `sum += solve(i-1, k)`.
     - If `i < k`: `sum += solve(n-i, k-i)`.
     - If `i == k`: `sum += 0`.
   - `res = (n-1) + sum / n`.
   - Store and return `res`.

### Time Complexity

- **O(n^2)**. Each state takes O(n) to compute? No.
- - 2000³ = 8 \cdot 10^9$. Too slow.
- **Optimization:**
  - Notice `sum` involves ranges of `solve`.
  - `sum_i=k+1^n E(i-1, k)` is a prefix sum of column k.
  - `sum_i=1^k-1 E(n-i, k-i)` is a diagonal sum.
  - We can optimize to O(n^2) by maintaining prefix sums or computing the sum incrementally.
  -   -   - We need O(N^2).
  - Let's optimize the transition.
  - `E(n, k) = (n-1) + frac1n [ sum_j=k^n-1 E(j, k) + sum_j=1^k-1 E(n-1-j+1, k-j) ]`.
  -   - Left side (pivot i > k): Subproblems are `(k, k), (k+1, k), dots, (n-1, k)`.
  - Right side (pivot i < k): Subproblems are `(n-1, k-1), (n-2, k-2), dots, (n-k+1, 1)`.
  - We can precompute prefix sums for columns to handle the Left side in O(1).
  - The Right side is a sum along a diagonal `E(size, target)` where `size - target = n - k`.
  - We can precompute diagonal prefix sums too.

### Optimized Algorithm

1. `dp[n][k]` stores `E(n, k)`.
2. `colSum[n][k]` stores `sum_j=1^n dp[j][k]`.
3. `diagSum[n][k]` stores `sum_j=0^n dp[j][k-n+j]`? No, simpler indexing.
   - Let `diff = n - k`. We want sum of `E(s, t)` where `s-t = diff`.
   - Store `diagSum[diff][k]`?
   -    - For a fixed n, we compute all k.
   - The sum for Left part is `sum_j=k^n-1 E(j, k)`. This is `colSum[n-1][k] - colSum[k-1][k]`.
   - The sum for Right part is `sum_j=n-k+1^n-1 E(j, j-(n-k))`.
     - Let d = n-k. Terms are `E(d+1, 1), E(d+2, 2), dots, E(n-1, k-1)`.
     - This is a sum along the diagonal `s-t = d`.
     - We can maintain `diagSum[d]` which accumulates `E(s, t)` as s increases.
4. Complexity O(N^2).

### Time Complexity

- **O(n^2)**.

### Space Complexity

- **O(n^2)**.

![Algorithm Visualization](../images/PRB-008/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-008/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `5 3`.
1. `dp[1][1] = 0`. `colSum[1][1]=0`, `diagSum[0][1]=0`.
2. `dp[2][1]`: `1 + (0)/2 = 1`.
3. `dp[2][2]`: `1 + (0)/2 = 1`.
4. ...
5. `dp[5][3]`:
   - Cost 4.
   - Left Sum: `E(4,3) + E(3,3)`.
   - Right Sum: `E(4,2) + E(3,1)`.
   - Average and add.
   - Result ≈ 6.733333$.

## ✅ Proof of Correctness

### Invariant
`dp[i][j]` correctly computes the recurrence relation using prefix sums for O(1) transitions.

### Why the approach is correct
Dynamic Programming with optimization reduces O(N^3) to O(N^2), fitting the constraints.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Worst case?
  - *Hint:* O(n^2) if pivot is always min/max.
- **Extension 2:** Median of Medians pivot.
  - *Hint:* Deterministic O(n) worst case, but higher constant factor.
- **Extension 3:** Variance of comparisons.
  - *Hint:* Requires computing `E[X^2]`.

### Common Mistakes to Avoid

1. **Complexity**
   - ❌ Wrong: Naive recursion or O(N^3) DP.
   - ✅ Correct: Use prefix sums for O(N^2).
2. **Indices**
   - ❌ Wrong: Off-by-one in diagonal or column sums.
   - ✅ Correct: Carefully map `size` and `rank` to array indices.

## Related Concepts

- **Quicksort:** Similar analysis (2n ln n).
- **Harmonic Numbers:** Appear in the closed form solution.
