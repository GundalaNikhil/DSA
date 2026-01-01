---
problem_id: HSH_POLYNOMIAL_HASH_PREFIXES__3824
display_id: HSH-001
slug: polynomial-hash-prefixes
title: "Polynomial Hash of Prefixes"
difficulty: Easy
difficulty_score: 25
topics:
  - Hashing
  - Rolling Hash
  - String Algorithms
tags:
  - hashing
  - rolling-hash
  - polynomial-hash
  - easy
premium: true
subscription_tier: basic
---

# HSH-001: Polynomial Hash of Prefixes

## 📋 Problem Summary

You are given a string `s` and two integers `B` (base) and `M` (modulus). Your task is to compute the polynomial rolling hash for every prefix of the string.
The hash of a prefix `s[0 dots i]` is defined recursively:

- `H_0 = s[0] +/-od M`
- `H_i = (H_i-1 x B + s[i]) +/-od M`

## 🌍 Real-World Scenario

**Scenario Title:** Digital Fingerprinting

Imagine you are building a system to detect plagiarism in documents. Comparing entire documents character by character is slow. Instead, you convert each document (or sentence) into a unique number called a "fingerprint" or "hash".

- If two documents have different fingerprints, they are definitely different.
- If they have the same fingerprint, they are likely the same.

In this problem, we are computing the fingerprint for every "beginning part" (prefix) of a document. This is the first step in more complex algorithms like Rabin-Karp, which can find a specific pattern inside a massive text by comparing these fingerprints efficiently.

![Real-World Application](../images/HSH-001/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Rolling Calculation

String: "abc", Base: 10, Mod: 1000 (for simplicity)
ASCII: 'a'=97, 'b'=98, 'c'=99

```text
Step 1: Prefix "a"
Hash = 97
Result: [97]

Step 2: Prefix "ab"
Previous Hash = 97
New Char = 'b' (98)
Hash = (97 * 10 + 98) % 1000
     = (970 + 98) % 1000
     = 1068 % 1000
     = 68
Result: [97, 68]

Step 3: Prefix "abc"
Previous Hash = 68
New Char = 'c' (99)
Hash = (68 * 10 + 99) % 1000
     = (680 + 99) % 1000
     = 779 % 1000
     = 779
Result: [97, 68, 779]
```

### Key Concept: Polynomial Rolling Hash

The formula `H_i = (H_i-1 x B + s[i]) +/-od M` essentially treats the string as a number in base `B`.
For string "abc":

- "a" `~= 97`
- "ab" `~= 97 x B + 98`
- "abc" `~= (97 x B + 98) x B + 99 = 97 x B^2 + 98 x B^1 + 99 x B^0`

This allows us to compute the hash of a new prefix in `O(1)` time using the previous result, rather than re-scanning the whole string.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s`, integers `B` and `M`.
- **Output:** Array of integers where the `i`-th element is the hash of `s[0 dots i]`.
- **Indexing:** 0-based.
- **Modulo:** All calculations must be modulo `M` to prevent overflow.

## Naive Approach

### Intuition

For each prefix `s[0 dots i]`, loop from `0` to `i` to compute the polynomial value.

### Algorithm

1. Loop `i` from 0 to `n-1`.
2. Inside, loop `j` from 0 to `i`.
3. Compute `sum s[j] x B^i-j +/-od M`.
4. Store result.

### Time Complexity

- **O(N^2)**: Sum of `1 + 2 + dots + N` operations. Too slow for `N=2 * 10^5`.

## Optimal Approach

### Key Insight

Use the recursive property:
`H_i = (H_i-1 x B + s[i]) +/-od M`
This is the definition of a **Rolling Hash**. We can compute the current hash using only the previous hash and the current character.

### Algorithm

1. Initialize `current_hash = 0`.
2. Create a result list.
3. Iterate through each character `c` in `s`:
   - `current_hash = (current_hash * B + ASCII(c)) % M`
   - Append `current_hash` to result.
4. Return result.

### Time Complexity

- **O(N)**: One pass through the string.

### Space Complexity

- **O(N)**: To store the output array.

![Algorithm Visualization](../images/HSH-001/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**

```
abc
911382323 1000000007
```

**Variables:**

- `s` = "abc"
- `B` = 911382323
- `M` = 1000000007

**Iteration 1 (char 'a', code 97):**

- `currentHash` = `(0 x B + 97) +/-od M = 97`
- Output: `[97]`

**Iteration 2 (char 'b', code 98):**

- `currentHash` = `(97 x 911382323 + 98) +/-od M`
- `97 x 911382323 = 88404085331`
- `88404085331 + 98 = 88404085429`
- `88404085429 +/-od1000000007 = 374134515`
- Output: `[97, 374134515]`

**Iteration 3 (char 'c', code 99):**

- `currentHash` = `(374134515 x 911382323 + 99) +/-od M`
- Product `~= 3.4 x 10^17` (Fits in 64-bit integer, requires BigInt in JS)
- Result modulo `M = 549818522`
- Output: `[97, 374134515, 549818522]`

## ✅ Proof of Correctness

### Invariant

At the end of iteration `i`, `currentHash` holds the polynomial hash of the prefix `s[0 dots i]`.
Base case (`i=0`): `H_0 = s[0] +/-od M`. Correct.
Inductive step: Assume `H_i-1` is correct.
`H_i = (H_i-1 x B + s[i]) +/-od M`.
This matches the definition of the polynomial rolling hash.

## 💡 Interview Extensions

- **Extension 1:** How to calculate the hash of any substring `s[i dots j]` in `O(1)`?
  - _Answer:_ `H(s[i dots j]) = (H_j - H_i-1 x B^j-i+1) +/-od M`. You need to precompute powers of `B`.
- **Extension 2:** What if collisions occur?
  - _Answer:_ Use double hashing (two different pairs of `B` and `M`).

### Common Mistakes to Avoid

1. **Integer Overflow**

   - ❌ Wrong: Using 32-bit `int` for intermediate calculations (`H x B`).
   - ✅ Correct: Use `long long` (C++), `long` (Java), or `BigInt` (JS).

2. **Negative Modulo**
   - ❌ Wrong: In subtraction (for substrings), result might be negative.
   - ✅ Correct: Add `M` before taking modulo: `(a - b + M) % M`. (Not needed for this specific prefix problem, but good to know).

## Related Concepts

- **Rabin-Karp Algorithm:** Uses this rolling hash for pattern matching.
- **Modular Arithmetic:** Essential for preventing overflow.
