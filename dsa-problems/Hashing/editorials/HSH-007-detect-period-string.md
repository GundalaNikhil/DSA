---
problem_id: HSH_DETECT_PERIOD_STRING__6183
display_id: HSH-007
slug: detect-period-string
title: "Detect Period of String"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - String Algorithms
  - Periodicity
tags:
  - hashing
  - period
  - pattern
  - medium
premium: true
subscription_tier: basic
---

# HSH-007: Detect Period of String

## 📋 Problem Summary

You are given a string `s`. You need to find the smallest length `p` such that `s` is composed of the prefix `s[0..p-1]` repeated multiple times. If no such `p` exists (other than the string itself), return the length of `s`.

## 🌍 Real-World Scenario

**Scenario Title:** Signal Compression

Imagine you are analyzing a digital signal or a heartbeat pattern.
- The signal might look like `101101101...`.
- If you can detect that it's just `101` repeating, you can compress the data significantly by storing only the pattern `101` and the repetition count.
- Finding the smallest period is essential for efficient data storage and pattern recognition.

![Real-World Application](../images/HSH-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Checking Periodicity

String: "ababab" (Length 6)
Divisors of 6: 1, 2, 3, 6.

```text
Check p=1 ("a"):
Expected: "aaaaaa"
Actual:   "ababab" -> Fail.

Check p=2 ("ab"):
Expected: "ababab"
Actual:   "ababab" -> Match!
Smallest Period = 2.
```

### Key Concept: Hashing for Periodicity

A string `S` has period `P` if `S[0 dots N-P-1] == S[P dots N-1]`.
Alternatively, using hashing:
If period is `P`, then the prefix of length `N-P` must equal the suffix of length `N-P`.
Why?
`S = T + T + dots + T` (where `T` is length `P`).
Prefix `N-P`: `T + T + dots` (one less `T`).
Suffix `N-P`: `T + T + dots` (shifted by one `T`).
They must be identical.
So, we can check if `hash(0, n-p-1) == hash(p, n-1)`.
This check is `O(1)`!

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s`.
- **Output:** Smallest period length.
- **Constraints:** `|s| <= 2 * 10^5`.
- **Divisors:** We only need to check `P` that are divisors of `N`.

## Naive Approach

### Intuition

For every divisor `P` of `N`:
Construct the string by repeating `s[0..P-1]`. Compare with `s`.

### Algorithm

1. Find all divisors of `N`.
2. Sort divisors.
3. For each `P`:
   - Construct candidate string.
   - If candidate == s, return `P`.

### Time Complexity

- **O(N * Divisors(N))**: Constructing string takes `O(N)`. Number of divisors is small, but can be up to 128 for `N=10^5`. Total roughly `O(N)`. This is actually acceptable!
- However, constructing strings repeatedly is memory heavy. Hashing avoids construction.

## Optimal Approach (Hashing)

### Key Insight

Use the property: `S` has period `P` `iff` `S[0 dots N-P-1] == S[P dots N-1]`.
This check takes `O(1)` with rolling hash.
We iterate through all divisors of `N`. The first one that satisfies the condition is the answer.

### Algorithm

1. Compute prefix hashes of `s`.
2. Find all divisors of `n`.
3. Sort divisors in ascending order.
4. For each divisor `p`:
   - Check if `hash(0, n-p-1) == hash(p, n-1)`.
   - If true, return `p`.
5. Return `n` (guaranteed to match itself).

### Time Complexity

- **O(N + Divisors(N))**: Preprocessing `O(N)`. Checking divisors is fast.

### Space Complexity

- **O(N)**: Hash arrays.

![Algorithm Visualization](../images/HSH-007/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
ababab
```
`N=6`. Divisors: 1, 2, 3, 6.

**Check 1:**
- `S[0..4]` ("ababa") vs `S[1..5]` ("babab").
- Mismatch.

**Check 2:**
- `S[0..3]` ("abab") vs `S[2..5]` ("abab").
- Match!
- Return 2.

## ✅ Proof of Correctness

### Invariant
If `S[0 dots N-P-1] == S[P dots N-1]`, then `S[i] == S[i+P]` for all valid `i`.
This implies periodicity `P`.
Since we check divisors in increasing order, we find the smallest period.

## 💡 Interview Extensions

- **Extension 1:** Find period using KMP.
  - *Answer:* Period `P = N - pi[N-1]` if `N % P == 0`. (`pi` is the failure function). `O(N)`.
- **Extension 2:** What if the string is not perfectly periodic but has a "period" that cuts off?
  - *Answer:* The hashing check `S[0 dots N-P-1] == S[P dots N-1]` still works for finding the "border" length, which implies the period.

### Common Mistakes to Avoid

1. **Checking Non-Divisors**
   - ❌ Wrong: Checking all `1 dots N`.
   - ✅ Correct: Only divisors can form a perfect period (where `N` is a multiple of `P`).
2. **Hash Collision**
   - ❌ Wrong: Single hash might fail.
   - ✅ Correct: Double hash or verify characters if collision suspected (though usually not needed for simple problems).

## Related Concepts

- **KMP Algorithm:** Failure function `pi` array directly gives the longest proper prefix which is also a suffix.
- **Z-Algorithm:** Z-array values can also determine periodicity.
