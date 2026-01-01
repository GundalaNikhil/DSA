---
problem_id: NUM_CRT_EXISTENCE_VALUE__5186
display_id: NUM-015
slug: crt-existence-value
title: "CRT Existence and Value"
difficulty: Medium
difficulty_score: 58
topics:
  - Number Theory
  - Chinese Remainder Theorem
  - GCD
tags:
  - number-theory
  - crt
  - gcd
  - medium
premium: true
subscription_tier: basic
---

# NUM-015: CRT Existence and Value

## 📋 Problem Summary

Solve a system of `k` linear congruences:
`x equiv a_1 +/-odm_1`
`x equiv a_2 +/-odm_2`
`dots`
`x equiv a_k +/-odm_k`
- Moduli `m_i` are **not necessarily coprime**.
- Determine if a solution exists. If yes, find the smallest non-negative `x`.

## 🌍 Real-World Scenario

**Scenario Title:** The Planetary Alignment

You are an astronomer tracking `k` different planets orbiting a star.
- Planet `i` completes an orbit every `m_i` days.
- Currently, Planet `i` is at position `a_i` (measured in days since passing a reference point).
- You want to know when all planets will simultaneously be at their respective reference points (or a specific alignment configuration).
- This requires finding a time `x` that satisfies the orbital periodicity constraints for all planets simultaneously.
- Since orbital periods might share common factors (resonances), a perfect alignment might never happen. You need to verify existence first.

**Why This Problem Matters:**

- **Cryptography:** Secret sharing schemes (Shamir's Secret Sharing uses polynomial interpolation, but CRT is used in others like Mignotte's).
- **Scheduling:** Synchronizing periodic tasks with offsets.
- **Parallel Computing:** Reconstructing large integers from modular residues.

![Real-World Application](../images/NUM-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Merging Congruences

Eq 1: `x equiv 2 +/-od 6 implies x in 2, 8, 14, 20, dots`
Eq 2: `x equiv 5 +/-od 9 implies x in 5, 14, 23, 32, dots`

Intersection:
- 14 is in both.
- Next is `14 + lcm(6, 9) = 14 + 18 = 32`.
- Solution: `x equiv 14 +/-od18`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Coprimality:** Standard CRT requires `gcd(m_i, m_j) = 1`. Here, we must handle `gcd > 1`.
- **Condition:** `x equiv a_1 +/-odm_1` and `x equiv a_2 +/-odm_2` has a solution iff `a_1 equiv a_2 +/-odgcd(m_1, m_2)`.
- **Overflow:** Intermediate moduli can grow up to `lcm(m_1 dots m_k)`. With `m_i <= 10^9` and `k=10`, this can exceed 64-bit integers. However, usually test cases for "Medium" keep the LCM within `long long` range, or we need `__int128` (C++) / `BigInt` (Java/JS/Python). Given constraints `m_i <= 10^9`, LCM can be huge. But typical CP problems with this constraint imply the answer fits in 64-bit or we use BigInt. Python/Java/JS handle this. C++ needs `__int128`.

### Core Concept: Generalized CRT

Iteratively merge two congruences:
1. `x = k_1 m_1 + a_1`
2. `k_1 m_1 + a_1 equiv a_2 +/-odm_2`
3. `k_1 m_1 equiv a_2 - a_1 +/-odm_2`
   - Let `g = gcd(m_1, m_2)`.
   - If `(a_2 - a_1) % g !=q 0`, no solution.
   - Divide by `g`: `k_1 fracm_1g equiv fraca_2 - a_1g +/-odfracm_2g`.
   - Solve for `k_1` using Modular Inverse.
   - Substitute `k_1` back to find `x`.
   - New modulus is `lcm(m_1, m_2)`.

## Naive Approach

### Intuition

Check numbers `0, 1, 2, dots` until one satisfies all.

### Algorithm

Loop `x` from 0 to `lcm(m_i)`.

### Time Complexity

- **O(LCM)**. Exponential.

## Optimal Approach

### Key Insight

Use the iterative merging strategy described above.
Use Extended Euclidean Algorithm for modular inverse.
Handle potential overflows with `__int128` in C++.

### Algorithm

1. Start with `current_a = 0`, `current_m = 1`.
2. For each `(a_i, m_i)`:
   - Solve system:
     - `X equiv current_a +/-odcurrent_m`
     - `X equiv a_i +/-odm_i`
   - Let `g = gcd(current_m, m_i)`.
   - Check if `(a_i - current_a) % g == 0`. If not, return NO.
   - Solve `p * current_m equiv (a_i - current_a) +/-odm_i` for `p`.
     - This reduces to `p * fraccurrent_mg equiv fraca_i - current_ag +/-odfracm_ig`.
     - Let `inv = modInverse(fraccurrent_mg, fracm_ig)`.
     - `p = (inv * fraca_i - current_ag) % fracm_ig`.
   - New `X = current_a + p * current_m`.
   - New modulus `M = lcm(current_m, m_i)`.
   - Update `current_a = X`, `current_m = M`.
   - Ensure `current_a` is normalized to `[0, M-1]`.
3. Return `current_a`.

### Time Complexity

- **O(k \log(\text{max\_m}))**.

### Space Complexity

- **O(1)**.

![Algorithm Visualization](../images/NUM-015/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-015/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `2 6`, `5 9`.
1. `curA=0, curM=1`.
2. Eq 1: `2 6`.
   - `rhs = 2`. `g=1`. `inv=1`. `k=2`.
   - `curA = 0 + 2*1 = 2`. `curM = 6`.
3. Eq 2: `5 9`.
   - `curA=2, curM=6`.
   - `rhs = (5-2)%9 = 3`.
   - `gcd(6, 9) = 3`.
   - `3 % 3 == 0`. Valid.
   - `mod = 9/3 = 3`.
   - `inv`: `6x + 9y = 3`. `2x + 3y = 1`. `x=-1` (or 2 mod 3).
   - `k = (3/3) * 2 % 3 = 2`.
   - `newM = 6 * (9/3) = 18`.
   - `curA = 2 + 2*6 = 14`.
   - `curA = 14 % 18 = 14`.
4. Result 14.

## ✅ Proof of Correctness

### Invariant
`curA` is the unique solution modulo `curM` for the first `i` equations.
We inductively extend this to `i+1`.

### Why the approach is correct
Generalized CRT logic handles non-coprime moduli by checking consistency with GCD.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Output all solutions in range `[0, N]`.
  - *Hint:* Solutions are `x, x+M, x+2M dots`. Just iterate.
- **Extension 2:** Moduli are large primes.
  - *Hint:* Standard CRT with precomputed inverses.
- **Extension 3:** Parallel CRT.
  - *Hint:* Divide and conquer merging.

### Common Mistakes to Avoid

1. **Overflow**
   - ❌ Wrong: `curA + k * curM` overflows `long long`.
   - ✅ Correct: Use `__int128` or `BigInt`.
2. **Negative Modulo**
   - ❌ Wrong: `(a - b) % m` can be negative in C++/Java.
   - ✅ Correct: `((a - b) % m + m) % m`.

## Related Concepts

- **Extended Euclidean Algorithm:** The core engine here.
- **Modular Inverse:** Special case of linear congruence.
