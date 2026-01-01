---
problem_id: PRB_PERMUTATION_CYCLE_STRUCTURE__9150
display_id: PRB-016
slug: permutation-cycle-structure
title: "Random Permutation Cycle Structure"
difficulty: Medium
difficulty_score: 52
topics:
  - Probability
  - Combinatorics
  - Expectations
tags:
  - probability
  - permutations
  - expectation
  - medium
premium: true
subscription_tier: basic
---

# PRB-016: Random Permutation Cycle Structure

## 📋 Problem Summary

For a random permutation of n elements, we need to find:

1. The expected number of cycles of length exactly k.
2. The expected length of the longest cycle.

| | |
|---|---|
| **Input** | n, k |
| **Output** | Expected cycles of length k, Expected longest cycle |

## 🌍 Real-World Scenario

**Scenario Title:** Secret Santa Chaos

Imagine a Secret Santa gift exchange with n people.
- Everyone puts their name in a hat.
- Everyone draws a name.
- If you draw your own name, you put it back and redraw (usually). But let's assume a pure random draw where drawing yourself is allowed (forming a cycle of length 1).
- A "cycle" forms a closed loop of gift-giving: Alice gives to Bob, Bob gives to Charlie, Charlie gives to Alice.
- **Question 1:** How many pairs of people just swap gifts with each other (cycles of length 2)?
- **Question 2:** What is the expected size of the largest loop? If the largest loop is huge, it means most people are connected in one giant chain.

**Why This Problem Matters:**

- **Cryptography:** Cycle structure affects the security of certain permutation-based ciphers.
- **Genetics:** Chromosome breakage and rejoining models.
- **Sorting:** The number of cycles relates to the number of swaps needed to sort an array (`N - cycles`).

![Real-World Application](../images/PRB-016/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Permutation Cycles

Permutation: `[2, 3, 1, 5, 4]` (1-based index)

```
Index: 1  2  3  4  5
Value: 2  3  1  5  4

Cycles:
1 -> 2 -> 3 -> 1   (Length 3)
4 -> 5 -> 4        (Length 2)
```

In this example:
- Cycles of length 2: 1
- Longest cycle length: 3

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** n (total elements), k (target cycle length).
- **Output:** Two values.
  1. Expected count of cycles of length k.
  2. Expected length of the longest cycle.
- **Constants:** The problem gives the Golomb-Dickman constant `lambda ~= 0.624330` for the second part.
- **Constraint:** k \le n$.

## Naive Approach

### Intuition

Monte Carlo simulation. Generate thousands of random permutations, decompose them into cycles, and average the results.

### Algorithm

1. Loop M times:
   - Generate random permutation of size n.
   - `visited` array to track elements.
   - For `i` from 1 to `n`:
     - If not visited, trace cycle, count length.
   - Update stats.
2. Print averages.

### Time Complexity

- **O(M \cdot n)**.

### Space Complexity

- **O(n)**.

### Limitations

- Slow and approximate.

## Optimal Approach

### Key Insight 1: Expected Number of Cycles of Length k

Surprisingly, this is **independent of n** (as long as n \ge k$).
The expected number of cycles of length k is exactly `1/k`.

*Why?*
There are `binomnk` ways to choose k elements.
There are `(k-1)!` ways to form a cycle with them.
The probability that a specific set of k elements forms a cycle in a random permutation is `frac(k-1)! (n-k)!n!`.
Total Expected = `binomnk x (k-1)! x frac(n-k)!n! = fracn!k!(n-k)! frac(k-1)! (n-k)!n! = frac1k`.

### Key Insight 2: Expected Longest Cycle

This is a known result in combinatorics. The expected length of the longest cycle `L_n` is asymptotically:
.  E[L_n] \approx n \times \lambda . 
Where `lambda ~= 0.6243299885` is the Golomb-Dickman constant.

### Algorithm

1. Read `n, k`.
2. Result 1: `1.0 / k`.
3. Result 2: `n * 0.624330`.
4. Print results.

### Time Complexity

- **O(1)**.

### Space Complexity

- **O(1)**.

### Why This Is Optimal

Direct formula application.

![Algorithm Visualization](../images/PRB-016/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-016/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `n = 5, k = 2`

1. Expected cycles of length 2: `1/2 = 0.5`.
2. Expected longest cycle: `5 x 0.624330 = 3.121650`.
3. Output: `0.500000 3.121650`.

Matches example.

![Example Visualization](../images/PRB-016/example-1.png)

## ✅ Proof of Correctness

### Invariant
The expected number of cycles of length k is `1/k` for all `1 <= k <= n`.

### Why the approach is correct
Derived from linearity of expectation.
Let `X_S` be indicator that set S of size k forms a cycle.
`E[sum X_S] = sum E[X_S] = binomnk frac(k-1)! (n-k)!n! = frac1k`.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Expected total number of cycles?
  - *Hint:* Sum of `1/k` for k = 1`to n. This is the Harmonic Number`H_n \approx \ln n$.
- **Extension 2:** Probability that element 1 is in a cycle of length k?
  - *Hint:* Also `1/n`. Uniform distribution of cycle lengths containing a specific element.
- **Extension 3:** 100 Prisoners Problem.
  - *Hint:* Relates to the probability that the longest cycle is `> 50`.

### Common Mistakes to Avoid

1. **Dependency on N**
   - ❌ Wrong: Thinking expected cycles of length k is `n/k`.
   - ✅ Correct: It's just `1/k`.
2. **Integer Division**
   - ❌ Wrong: `1/k` in integer arithmetic.
   - ✅ Correct: `1.0/k`.

## Related Concepts

- **Stirling Numbers of the First Kind:** Count permutations with specific cycle counts.
- **Harmonic Series:** Sum of reciprocals.
- **Derangements:** Permutations with no fixed points (no cycles of length 1).
