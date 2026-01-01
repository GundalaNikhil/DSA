---
problem_id: NUM_COUNT_STRINGS_EXACT_VOWELS__6419
display_id: NUM-013
slug: count-strings-exact-vowels
title: "Count Strings With Exact Vowels"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Combinatorics
  - Modular Arithmetic
tags:
  - number-theory
  - combinatorics
  - modular
  - medium
premium: true
subscription_tier: basic
---

# NUM-013: Count Strings With Exact Vowels

## 📋 Problem Summary

Count the number of strings of length `n` that contain exactly `k` vowels.
- Alphabet: 26 lowercase English letters.
- Vowels: `a, e, i, o, u` (5).
- Consonants: 21.
- Output: Count modulo `10^9+7`.

## 🌍 Real-World Scenario

**Scenario Title:** The Password Validator

You are designing a password policy for a secure system. The policy requires passwords to be exactly `n` characters long and contain exactly `k` special characters (in this analogy, vowels).
- To estimate the strength of this policy against brute-force attacks, you need to calculate the total size of the valid password space.
- A larger space implies higher security (entropy).
- Since the numbers are massive, you compute them modulo a large prime for verification purposes.

**Why This Problem Matters:**

- **Combinatorics:** Fundamental counting principles (multiplication rule, combinations).
- **Probability:** Calculating the probability of specific events in a sequence (Bernoulli trials).
- **Coding Theory:** Error correcting codes often involve counting strings with specific weights.

![Real-World Application](../images/NUM-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: String Construction

`n=3, k=1`.
We need strings like `VCC`, `CVC`, `CCV` (V=Vowel, C=Consonant).

```
Structure 1: V C C
Choices:     5 * 21 * 21 = 2205

Structure 2: C V C
Choices:     21 * 5 * 21 = 2205

Structure 3: C C V
Choices:     21 * 21 * 5 = 2205

Total = 3 * 2205 = 6615.
Formula: C(3, 1) * 5^1 * 21^2 = 3 * 5 * 441 = 6615.
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** `n <= 10^6`. We need `O(n)` or `O(1)` if precomputed.
- **Modulo:** `10^9+7`.
- **Formula:** `binomnk x 5^k x 21^n-k`.

### Core Concept: Binomial Coefficients

We choose `k` positions for the vowels out of `n` available positions: `binomnk`.
For each of the `k` vowel positions, we have 5 choices. Total `5^k`.
For each of the `n-k` consonant positions, we have 21 choices. Total `21^n-k`.
Result: `binomnk * 5^k * 21^n-k`.

## Naive Approach

### Intuition

Generate all strings (recursion) and count.

### Algorithm

Recursive backtracking.

### Time Complexity

- **O(26^n)**. Impossible for `n > 10`.

## Optimal Approach

### Key Insight

Use the closed-form formula.
Precompute factorials to compute `binomnk` in `O(1)` or `O(log MOD)` time.
Use modular exponentiation for powers.

### Algorithm

1. Precompute factorials up to `n`.
2. Compute `binomnk = fracn!k!(n-k)! +/-od M`.
3. Compute `P_1 = 5^k +/-od M`.
4. Compute `P_2 = 21^n-k +/-od M`.
5. Result = `(binomnk * P_1 * P_2) +/-od M`.

### Time Complexity

- **O(n)** for precomputation (or `O(1)` if just one query and we compute factorials on fly, but usually `O(n)` is standard).
- **O(\log M)** for modular inverse and exponentiation.

### Space Complexity

- **O(n)** for factorials.

![Algorithm Visualization](../images/NUM-013/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-013/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `2 1`.
1. `nCr(2, 1) = 2`.
2. `5^1 = 5`.
3. `21^1 = 21`.
4. `2 * 5 * 21 = 10 * 21 = 210`.
Matches example.

## ✅ Proof of Correctness

### Invariant
The formula counts disjoint sets of strings based on vowel positions.
Since we sum over all possible positions (`binomnk`), we cover all cases exactly once.

### Why the approach is correct
Standard combinatorics.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** At least `k` vowels.
  - *Hint:* Sum the results for `i = k dots n`.
- **Extension 2:** No two vowels adjacent.
  - *Hint:* Stars and Bars or DP.
- **Extension 3:** Palindromes with `k` vowels.
  - *Hint:* Construct half the string.

### Common Mistakes to Avoid

1. **Integer Overflow**
   - ❌ Wrong: `fact[i] * i` without modulo.
   - ✅ Correct: Always modulo.
2. **Inverse Calculation**
   - ❌ Wrong: Division `a / b % MOD`.
   - ✅ Correct: `a * modInverse(b) % MOD`.

## Related Concepts

- **Binomial Distribution:** Probability version of this problem.
- **Fermat's Little Theorem:** Used for modular inverse.
