---
problem_id: NUM_DISTINCT_PRIME_FACTORS_PREFIX__5173
display_id: NUM-006
slug: distinct-prime-factors-prefix
title: "Distinct Prime Factors Count Prefix"
difficulty: Medium
difficulty_score: 50
topics:
  - Number Theory
  - Sieve
  - Prefix Sums
tags:
  - number-theory
  - sieve
  - prefix
  - medium
premium: true
subscription_tier: basic
---

# NUM-006: Distinct Prime Factors Count Prefix

## 📋 Problem Summary

Let `f(x)` be the number of distinct prime factors of `x`.
- Precompute `f(x)` for all `x` up to `N`.
- Answer queries for the sum of `f(x)` in range `[l, r]`.
- Input: `N`, `Q`, and queries.
- Output: Range sums.

## 🌍 Real-World Scenario

**Scenario Title:** The Chemical Compound Screener

Imagine you are screening a database of chemical compounds, where each compound is identified by an integer ID.
- The "complexity" of a compound is determined by the number of distinct basic elements (primes) that make up its structure (prime factorization).
- For example, a compound with ID 12 (`2^2 * 3`) has 2 distinct elements (2 and 3). A compound with ID 30 (`2 * 3 * 5`) has 3.
- You want to analyze the total complexity of all compounds in a specific range of IDs to estimate the processing power required for a batch simulation.
- Since you have millions of compounds and thousands of batch queries, you need an efficient way to sum these complexity scores.

**Why This Problem Matters:**

- **Number Theory:** Understanding the distribution of `omega(n)` (number of distinct prime factors).
- **Performance:** Combining sieving with prefix sums is a standard technique for range query problems.
- **Data Analysis:** Aggregating properties over ranges.

![Real-World Application](../images/NUM-006/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Sieve Process

Let `N=10`. We want to compute `f(x)`.
Initialize `count` array to 0.

```
i=2 (prime): Add 1 to multiples 2, 4, 6, 8, 10.
i=3 (prime): Add 1 to multiples 3, 6, 9.
i=4 (not prime): Skip.
i=5 (prime): Add 1 to multiples 5, 10.
...

Result f(x):
x: 1 2 3 4 5 6 7 8 9 10
f: 0 1 1 1 1 2 1 1 1 2

Prefix Sum P(x):
x: 0 1 2 3 4 5 6 7 8 9 10
P: 0 0 1 2 3 4 6 7 8 9 11
```

Query `[2, 5]`: `P[5] - P[1] = 4 - 0 = 4`.
(`f(2)+f(3)+f(4)+f(5) = 1+1+1+1 = 4`).

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Constraints:** `N <= 10^6`, `Q <= 10^5`.
- **Function:** `f(x)` counts **distinct** primes. `f(12) = f(2^2 * 3) = 2`.
- **Prefix Sum:** Use 1-based indexing for convenience. `P[i] = P[i-1] + f(i)`.

### Core Concept: Modified Sieve

Instead of marking numbers as composite, we iterate through primes and increment a counter for every multiple.
This is similar to the Sieve of Eratosthenes but additive.
The complexity is `sum_p <= N fracNp ~= N ln ln N`.

## Naive Approach

### Intuition

For each query, iterate `l` to `r`, factorize each number, and sum up.

### Algorithm

Factorization takes `O(sqrtx)`.
Total time: `O(Q * (r-l) * sqrtN)`.
With `N=10^6`, this is way too slow.

### Time Complexity

- **O(Q \cdot N \cdot \sqrt{N})** worst case.

### Space Complexity

- **O(1)**.

## Optimal Approach

### Key Insight

1. **Precompute `f(x)`:** Use a sieve. Iterate `i` from 2 to `N`. If `f(i) == 0`, it's prime. Iterate multiples `j = i, 2i, dots` and increment `f(j)`.
2. **Prefix Sums:** Build `P[i] = P[i-1] + f(i)`.
3. **Query:** Answer in `O(1)`.

### Algorithm

1. Init `f` array of size `N+1` with 0.
2. For `i` from 2 to `N`:
   - If `f[i] == 0`: (i is prime)
     - For `j` from `i` to `N` step `i`:
       - `f[j]++`
3. Init `pref` array.
4. `pref[0] = 0`.
5. For `i` from 1 to `N`: `pref[i] = pref[i-1] + f[i]`.
6. Answer queries: `pref[r] - pref[l-1]`.

### Time Complexity

- **Precomputation:** `O(N log log N)`.
- **Query:** `O(1)`.
- **Total:** `O(N log log N + Q)`.

### Space Complexity

- **O(N)**.

![Algorithm Visualization](../images/NUM-006/algorithm-visualization.png)
![Algorithm Steps](../images/NUM-006/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `N=6, Query=[2, 5]`.
1. `f` init 0.
2. `i=2`: `f[2]++, f[4]++, f[6]++`. `f=[0,0,1,0,1,0,1]`.
3. `i=3`: `f[3]++, f[6]++`. `f=[0,0,1,1,1,0,2]`.
4. `i=4`: Skip.
5. `i=5`: `f[5]++`. `f=[0,0,1,1,1,1,2]`.
6. `i=6`: Skip.
7. `pref`:
   - `P[0]=0`
   - `P[1]=0`
   - `P[2]=1`
   - `P[3]=2`
   - `P[4]=3`
   - `P[5]=4`
   - `P[6]=6`
8. Query `[2, 5]`: `P[5] - P[1] = 4 - 0 = 4`.
   - Correct.

## ✅ Proof of Correctness

### Invariant
The sieve iterates every prime `p` and adds 1 to all its multiples.
Thus, `f[x]` counts exactly how many distinct primes divide `x`.

### Why the approach is correct
Standard application of additive sieve and prefix sums.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Sum of total prime factors (with multiplicity).
  - *Hint:* Instead of `f[j]++`, do `temp = j; while(temp%i==0) { count++; temp/=i; }`. Or better: `f[j] = f[j/p] + 1` where `p` is smallest prime factor.
- **Extension 2:** Count numbers with exactly `k` prime factors.
  - *Hint:* Use the same sieve, then build prefix sums for each `k` (or just store counts).
- **Extension 3:** Square-free numbers.
  - *Hint:* Check if any prime factor has exponent > 1.

### Common Mistakes to Avoid

1. **Memory Limit**
   - ❌ Wrong: Using `long` array for `f` if `int` suffices (saves memory).
   - ✅ Correct: `f[x]` is small (`<= 8` for `N=10^6`), so `int` or even `byte` is fine. `pref` needs `long` for very large `N`, but here `int` fits.
2. **Loop Bounds**
   - ❌ Wrong: `j` starts at `i*i`.
   - ✅ Correct: `j` starts at `i` because we count the prime itself too.

## Related Concepts

- **Omega Function `omega(n)`:** Number of distinct prime factors.
- **Big Omega Function `Omega(n)`:** Total number of prime factors.
- **Harmonic Series:** Complexity analysis.
