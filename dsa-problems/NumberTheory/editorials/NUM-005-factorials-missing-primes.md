---
problem_id: NUM_FACTORIALS_MISSING_PRIMES__2941
display_id: NUM-005
slug: factorials-missing-primes
title: "Factorials With Missing Primes"
difficulty: Medium
difficulty_score: 55
topics:
  - Number Theory
  - Modular Arithmetic
  - Factorials
tags:
  - number-theory
  - factorial
  - modular
  - medium
premium: true
subscription_tier: basic
---

# NUM-005: Factorials With Missing Primes

## 📋 Problem Summary

Compute the product of all integers in `[1, n]` that are **not divisible** by a given prime `p`, modulo `p`.
- Input: Large integer `n`, small prime `p`.
- Output: The product modulo `p`.

## 🌍 Real-World Scenario

**Scenario Title:** The Stable Compound Analyzer

In computational chemistry, you are analyzing the stability of a large polymer chain. The number of possible configurations is given by a factorial `n!`. However, due to a specific chemical constraint related to the prime number `p`, configurations that are multiples of `p` are unstable and immediately decay.
- To determine the number of stable configurations modulo `p` (for hash checking), you need to compute the product of all integers up to `n`, skipping multiples of `p`.
- Since `n` can be huge (`10^12`), you cannot iterate. You must use number theory properties.

**Why This Problem Matters:**

- **Lucas Theorem:** This is a key step in computing binomial coefficients `binomnk +/-od p` for large `n`.
- **Group Theory:** Related to the structure of the multiplicative group modulo `p`.
- **Combinatorics:** Counting problems with exclusion criteria.

![Real-World Application](../images/NUM-005/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Periodicity

Let `n=13, p=5`. We want product of `1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13`.

```
Block 1 (1-5):  1 * 2 * 3 * 4 * (skip 5)
                = 1 * 2 * 3 * 4 = 24 = 4 mod 5

Block 2 (6-10): 6 * 7 * 8 * 9 * (skip 10)
                = 1 * 2 * 3 * 4 mod 5 = 4 mod 5

Remainder (11-13): 11 * 12 * 13
                   = 1 * 2 * 3 = 6 = 1 mod 5
```

Notice the pattern: The product of terms in any full block of length `p` (excluding the multiple of `p`) is constant modulo `p`.
By Wilson's Theorem, `(p-1)! equiv -1 +/-od p`.
So each full block contributes `-1 +/-od p`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** `n <= 10^12`, `p <= 10^6`.
- **Problem Interpretation:** The problem asks for the product of integers in `[1, n]` that are **not divisible by p**.
  - This means we skip multiples of `p`: ignore `p, 2p, 3p, dots`.
  - We do NOT divide these multiples by `p` and include quotients (as in full factorial computation).
  - Example: `n=6, p=5`. Numbers: `1, 2, 3, 4, 6`. Product: `144 equiv 4 (mod 5)`.
  - This is simpler than computing `n! mod p` with all factors of `p` removed (which requires recursion).
  - The solution uses periodicity without recursion: a single-pass calculation.

### Core Concept: Wilson's Theorem & Periodicity

The sequence of residues modulo `p` repeats every `p`.
The product of terms `1, 2, dots, p-1` is `(p-1)! equiv -1 +/-od p`.
Number of full blocks of size `p` is `lfloor n/p rfloor`.
The contribution of full blocks is `(-1)^lfloor n/p rfloor`.
The remaining terms are `1, 2, dots, n +/-od p`.

## Naive Approach

### Intuition

Iterate `i` from 1 to `n`. If `i % p != 0`, multiply.

### Algorithm


### Time Complexity

- **O(n)**. With `n=10^12`, this is TLE.

### Space Complexity

- **O(1)**.

## Optimal Approach

### Key Insight

Use the periodicity.
1. Calculate full blocks count: `cnt = n // p`.
2. Calculate remainder: `rem = n % p`.
3. The product of a full block `1 dots (p-1)` modulo `p` is `-1` (Wilson's Theorem).
4. Total contribution from blocks is `(-1)^cnt +/-od p`.
5. Multiply by the factorial of the remainder: `rem! % p`.

### Algorithm

1. `res = power(p - 1, n // p, p)` (which is `(-1)^n//p`).
2. `rem = n % p`.
3. Compute `rem!` modulo `p` by iterating 1 to `rem`.
4. `res = (res * rem_fact) % p`.

### Time Complexity

- **O(p)** to compute factorial of remainder (worst case).
- Since `p <= 10^6`, this is fast.
- Total: `O(p)`.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/NUM-005/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-005/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `n=6, p=5`.
1. `numBlocks = 6 // 5 = 1`.
2. `remainder = 6 % 5 = 1`.
3. `res = (-1)^1 = -1 \equiv 4 \pmod 5`.
4. `remFact = 1! = 1`.
5. `Total = 4 * 1 = 4`.
Matches example.

Input: `n=13, p=5`.
1. `numBlocks = 2`.
2. `remainder = 3`.
3. `res = (-1)^2 = 1`.
4. `remFact = 1*2*3 = 6 \equiv 1 \pmod 5`.
5. `Total = 1 * 1 = 1`.
Check:
Block 1: 1,2,3,4 -> 24 -> 4.
Block 2: 6,7,8,9 -> 4.
Rem: 11,12,13 -> 1,2,3 -> 6 -> 1.
Total: `4 x 4 x 1 = 16 equiv 1`. Correct.

## ✅ Proof of Correctness

### Invariant
The product of terms in any range `[kp+1, kp+p-1]` is congruent to `(p-1)! +/-od p`.
Wilson's Theorem states `(p-1)! equiv -1 +/-od p`.

### Why the approach is correct
We decompose the range `[1, n]` into `lfloor n/p rfloor` full blocks and a remainder.
We skip multiples of `p` as requested.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Compute `n! +/-od p` excluding all factors of `p`.
  - *Hint:* This requires recursion. `F(n) = (missing_prime(n, p)) * F(lfloor n/p rfloor)`.
- **Extension 2:** Compute `binomnk +/-od p`.
  - *Hint:* Use Lucas Theorem for small `p`, or the recursive factorial method for large `p` (if `p` is not small enough for Lucas table but small enough for `O(p)`).
- **Extension 3:** Count trailing zeros in base `p`.
  - *Hint:* Legendre's Formula `sum lfloor n/p^k rfloor`.

### Common Mistakes to Avoid

1. **Including Multiples of p**
   - ❌ Wrong: Calculating standard factorial.
   - ✅ Correct: The problem explicitly says "NOT divisible by p".
2. **Wilson's Theorem Sign**
   - ❌ Wrong: Assuming product is 1.
   - ✅ Correct: Product is -1 (or `p-1`).
3. **Large N**
   - ❌ Wrong: Iterating up to `N`.
   - ✅ Correct: Use `O(p)` approach.

## Related Concepts

- **Wilson's Theorem:** `(p-1)! equiv -1 +/-od p`.
- **Legendre's Formula:** Exponent of prime in factorial.
- **Lucas Theorem:** Binomial coefficients mod p.
