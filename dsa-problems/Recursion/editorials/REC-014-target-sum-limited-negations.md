---
title: Target Sum With Limited Negations
slug: target-sum-limited-negations
difficulty: Medium
difficulty_score: 49
tags:
- Recursion
- Backtracking
- Target Sum
problem_id: REC_TARGET_SUM_LIMITED_NEGATIONS__8206
display_id: REC-014
topics:
- Recursion
- Backtracking
- DP
---
# Target Sum With Limited Negations - Editorial

## Problem Summary

You are given an array of integers `nums`. You need to assign a sign (`+` or `-`) to each integer such that the sum of the resulting values equals `target`. However, there is a constraint: you can use the `-` sign at most `K` times. Return the number of ways to achieve the target.


## Constraints

- `1 <= n <= 20`
- `0 <= K <= n`
- `|nums[i]| <= 20`
- `|target| <= 10^9`
## Real-World Scenario

Imagine **Budget Balancing**. You have a list of potential expenses and incomes. By default, everything is an income (+). You can choose to classify at most `K` items as expenses (-) to make your final balance exactly `target`.

## Problem Exploration

### 1. Relation to Subset Sum
Let `P` be the set of numbers assigned `+`, and `N` be the set of numbers assigned `-`.
Sum = `sum P - sum N = target`.
We also know `sum P + sum N = sum_all nums = S`.
Adding equations: `2 sum P = S + target`.
So `sum P = (S + target) / 2`.
This transforms the standard Target Sum problem into finding a subset `P` with a specific sum.
However, we have an additional constraint: `|N| <= K`.
This means we need to pick a subset `N` (the negated numbers) such that:
1.  Sum of `N` is `(S - target) / 2`.
2.  Size of `N` is `<= K`.

### 2. Recursive Structure
We can stick to the original formulation for backtracking:
`solve(index, current_sum, negations_count)`
-   **Base Case**:
    -   If `index == n`: Return 1 if `current_sum == target`, else 0.
-   **Transitions**:
    -   **Add (+)**: `solve(index + 1, current_sum + nums[index], negations_count)`
    -   **Subtract (-)**: Only if `negations_count < K`. `solve(index + 1, current_sum - nums[index], negations_count + 1)`

### 3. Constraints
-   `N <= 20`: `2^20 ~= 10^6`. This is small enough for pure recursion without memoization.
-   If `N` were larger (e.g., 100), we would need DP: `dp[index][current_sum][negations_count]`.

## Approaches

### Approach 1: Pure Backtracking
Since `N` is small, we explore the decision tree.
At each step, try adding `nums[i]` and subtracting `nums[i]` (if allowed).
Sum up the valid paths.

### Approach 2: Meet-in-the-middle (Optimization)
Split array into two halves. Generate all `(sum, negation_count)` pairs for both halves. Combine them. This reduces complexity to `O(2^N/2)`. Not needed for `N=20`.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
**Input:** `nums=[1, 2, 3]`, `K=1`, `target=2`

1.  `solve(0, 0, 0)`
    -   **+1**: `solve(1, 1, 0)`
        -   **+2**: `solve(2, 3, 0)`
            -   **+3**: `solve(3, 6, 0)` -> Sum 6 != 2. Return 0.
            -   **-3**: `solve(3, 0, 1)` -> Sum 0 != 2. Return 0.
        -   **-2**: `solve(2, -1, 1)`
            -   **+3**: `solve(3, 2, 1)` -> Sum 2 == 2. **Found**. path: `+1 -2 +3`.
            -   **-3**: (Negations 1 < 1 False). Skip.
    -   **-1**: `solve(1, -1, 1)`
        -   **+2**: `solve(2, 1, 1)`
            -   **+3**: `solve(3, 4, 1)` -> Sum 4 != 2. Return 0.

Total valid: 1.

The algorithm explores all valid assignments respecting the negation limit.

## Proof of Correctness

The algorithm explores all `2^N` sign combinations (pruned by K).
-   **Correctness**: It sums the terms and checks against `target`.
-   **Constraint**: It ensures `negations <= K`.

## Interview Extensions

1.  **Optimize for large N?**
    -   Use DP if sum range is small. `dp[i][current_sum][negations]`.
    -   Use Meet-in-the-middle if sum is large.

### Common Mistakes

-   **Base Case**: Returning 1 only if `sum == target`.
-   **Negation Count**: Only increment when using `-`.
