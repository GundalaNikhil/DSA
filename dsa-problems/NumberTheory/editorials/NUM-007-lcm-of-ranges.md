---
problem_id: NUM_LCM_OF_RANGES__8402
display_id: NUM-007
slug: lcm-of-ranges
title: "LCM of Ranges"
difficulty: Medium
difficulty_score: 52
topics:
  - Number Theory
  - LCM
  - Prime Factorization
tags:
  - number-theory
  - lcm
  - queries
  - medium
premium: true
subscription_tier: basic
---

# NUM-007: LCM of Ranges

## 📋 Problem Summary

Given an array `A`, answer queries for the Least Common Multiple (LCM) of the subarray `A[l dots r]` modulo `M`.
- Constraint: The range length `r - l + 1` is small (`<= 21`).
- Input: Array `A`, queries `(l, r)`, modulus `M`.
- Output: `lcm(A[l], dots, A[r]) +/-od M`.

## 🌍 Real-World Scenario

**Scenario Title:** The Event Synchronizer

You are managing a factory with multiple machines. Each machine `i` has a cycle time `A[i]` seconds.
- You want to synchronize a specific group of machines (from index `l` to `r`) so that they all start a new cycle simultaneously.
- The time until they all align again is the Least Common Multiple (LCM) of their cycle times.
- Since the LCM can be huge (exceeding standard integer limits), you only need the value modulo a large number `M` for scheduling purposes (e.g., checking if alignment happens within a specific time window).

**Why This Problem Matters:**

- **Scheduling:** Finding common periods for tasks.
- **Cryptography:** Order of elements in groups.
- **Arithmetic:** Handling large numbers via modular arithmetic.

![Real-World Application](../images/NUM-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: LCM Calculation

Range: `[2, 6, 3]`

```
2 = 2^1
6 = 2^1 * 3^1
3 = 3^1

Max exponents:
Prime 2: max(1, 1, 0) = 1 -> 2^1
Prime 3: max(0, 1, 1) = 1 -> 3^1

LCM = 2^1 * 3^1 = 6
```

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Range Length:** Small (`<= 21`). This is the key constraint. We don't need a Segment Tree.
- **Modulo:** The result must be modulo `M`.
- **LCM Definition:** `lcm(a, b) = (a * b) / gcd(a, b)`. For multiple numbers, `lcm(S) = prod p_i^max(e_i)`.
- **Caution:** We cannot simply do `(a * b / gcd(a, b)) % M` because division modulo `M` requires modular inverse, which might not exist if `gcd(a, b)` is not coprime to `M`. Instead, we must use prime factorization.

### Core Concept: Prime Factorization

Since the range is small, we can collect all numbers in the range, find their prime factorizations, and for each prime `p`, find the maximum exponent `e` that appears in the range.
The answer is `prod p^max(e) +/-od M`.

## Naive Approach

### Intuition

Iteratively compute LCM: `res = lcm(res, A[i])`.

### Algorithm


### Issues

- Intermediate `res` can grow very large (hundreds of digits), causing overflow before modulo.
- Python handles large integers automatically, but C++/Java do not.
- Even in Python, operations on huge numbers are slow.

## Optimal Approach

### Key Insight

Use the property: `lcm(S) = prod_p p^max_x in S v_p(x)`.
Since range is small and numbers are up to `10^9`, we can just use a map to store max exponents.

### Algorithm

1. For each query `(l, r)`:
   - Create a map `max_exponents`.
   - For each number `x` in `A[l dots r]`:
     - Factorize `x`: `x = p_1^e_1 p_2^e_2 dots`
     - For each factor `p^e`, update `max_exponents[p] = max(max_exponents[p], e)`.
   - Compute result: `ans = 1`.
   - For each `p, e` in `max_exponents`:
     - `ans = (ans * power(p, e, M)) % M`.
   - Return `ans`.

### Time Complexity

- **Factorization:** `O(sqrtA[i])`.
- **Total per query:** `O(len * sqrtA[i])`.
- With len `<= 21` and `A[i] <= 10^9`, this is roughly `20 x 31622 ~= 6 * 10^5` ops per query.
- For `Q=10^5`, this is too slow (`6 * 10^10`).
- **Optimization:** Since the range length is small (`<= 21`), trial division up to `sqrtx` is efficient enough. Average case is very fast when we stop early once `x=1`.

### Space Complexity

- **O(1)** auxiliary (map size is small).

![Algorithm Visualization](../images/NUM-007/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-007/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `A = [2, 6, 3]`, Query `[0, 1]`.
1. `l=0, r=1`. Range `[2, 6]`.
2. `num=2`: `2^1`. Map: `{2: 1}`.
3. `num=6`: `2^1 * 3^1`. Map: `{2: 1, 3: 1}`.
4. Result: `2^1 x 3^1 = 6`.
5. `6 +/-od10^9+7 = 6`.

## ✅ Proof of Correctness

### Invariant
`lcm(S) = prod p^max(e_p)`.
We iterate all numbers, factorize them, and maintain the max exponent for each prime.

### Why the approach is correct
Fundamental theorem of arithmetic.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Large Ranges.
  - *Hint:* Use Segment Tree where each node stores LCM. Requires merging LCMs (expensive). Or Mo's Algorithm.
- **Extension 2:** GCD of range.
  - *Hint:* Sparse Table / Segment Tree.
- **Extension 3:** LCM of all pairs.
  - *Hint:* `lcm(a, b) = ab/gcd(a, b)`. Summing this is harder.

### Common Mistakes to Avoid

1. **Overflow**
   - ❌ Wrong: `res = res * x` without modulo.
   - ✅ Correct: Use modular arithmetic, but be careful with division (GCD). Map approach avoids division.
2. **Modulo Division**
   - ❌ Wrong: `(a / b) % M`.
   - ✅ Correct: `(a * modInverse(b)) % M`. Only works if `gcd(b, M) = 1`.

## Related Concepts

- **Prime Factorization:** Trial division.
- **Modular Arithmetic:** Power function.
