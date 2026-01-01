---
problem_id: HSH_SUBSTRING_EQUALITY_QUERIES__5917
display_id: HSH-002
slug: substring-equality-queries
title: "Substring Equality Queries"
difficulty: Medium
difficulty_score: 45
topics:
  - Hashing
  - Rolling Hash
  - String Matching
tags:
  - hashing
  - rolling-hash
  - substring
  - queries
  - medium
premium: true
subscription_tier: basic
---

# HSH-002: Substring Equality Queries

## 📋 Problem Summary

You are given a string `s` and multiple queries. Each query provides two pairs of indices `(l1, r1)` and `(l2, r2)`, representing two substrings `s[l1..r1]` and `s[l2..r2]`. Your task is to determine if these two substrings are identical for each query.

## 🌍 Real-World Scenario

**Scenario Title:** DNA Sequence Matching

Imagine you are a geneticist analyzing a massive DNA sequence (millions of base pairs). You want to check if a specific gene segment found at position X is identical to another segment at position Y.
- Comparing them character by character for every query is too slow if the segments are long and queries are frequent.
- Instead, you can "fingerprint" the entire DNA sequence once. Then, checking if two segments match becomes a simple comparison of their fingerprints.

![Real-World Application](../images/HSH-002/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Substring Hashing

String: "banana"
Query: `s[1..3]` ("ana") vs `s[3..5]` ("ana")

```text
Indices: 0 1 2 3 4 5
String:  b a n a n a

Prefix Hashes (Base 10, Mod 1000 for simplicity):
H[0] = 'b'(98)
H[1] = 98*10 + 97 = 1077 -> 77
H[2] = 77*10 + 110('n') = 880
H[3] = 880*10 + 97 = 8897 -> 897
H[4] = 897*10 + 110 = 9080 -> 80
H[5] = 80*10 + 97 = 897

Hash("ana" at 1..3):
Formula: (H[3] - H[0] * B^3) % M
H[3] = 897
H[0] = 98
Let's use larger mod to avoid 0. Say Mod large.

Hash(1..3) = H[3] - H[0] * B^3
Hash(3..5) = H[5] - H[2] * B^3

If Hash(1..3) == Hash(3..5), substrings are likely equal.
```

### Key Concept: O(1) Substring Hash

Using the prefix hash array `H` where `H[i]` is the hash of `s[0 dots i]`, we can calculate the hash of any substring `s[l dots r]` in `O(1)` time:


`Hash(s[l \dots r]) = (H[r] - H[l-1] x B^r-l+1) +/-od M`


(If `l=0`, the term `H[l-1]` is 0).
This works because `H[r]` contains the polynomial for `s[0 dots r]`, and `H[l-1] x B^len` represents the prefix `s[0 dots l-1]` shifted to align with the start of the substring, effectively subtracting it out.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Double Hashing:** Use two sets of (Base, Mod) to minimize collisions. A collision happens when two different strings have the same hash. With two hashes, the probability is negligible (`~= 10^-18`).
- **Indices:** 0-based inclusive.
- **Constraints:** `N, Q <= 2 * 10^5`. An `O(N * Q)` solution will TLE. We need `O(N + Q)`.

## Naive Approach

### Intuition

For each query, compare the substrings character by character.

### Algorithm

1. For each query `(l1, r1, l2, r2)`:
   - Check if lengths differ (`r1-l1 !=q r2-l2`). If so, return false.
   - Loop `k` from 0 to length-1.
   - If `s[l1+k] != s[l2+k]`, return false.
   - Return true.

### Time Complexity

- **O(Q * N)**: Worst case (e.g., all queries are for the whole string). Too slow.

## Optimal Approach

### Key Insight

Use **Polynomial Rolling Hash** with **Double Hashing**.
1. Precompute prefix hashes for the entire string.
2. Precompute powers of the base `B`.
3. Answer each query in `O(1)` by computing the substring hash using the formula.

### Algorithm

1. Choose two pairs of constants: `(B_1, M_1)` and `(B_2, M_2)`.
   - e.g., `B_1=31, M_1=10^9+7` and `B_2=37, M_2=10^9+9`.
2. Precompute `powers` arrays for `B_1` and `B_2`.
3. Precompute `prefix_hashes` arrays for both pairs.
4. For each query:
   - Calculate Hash1 for both substrings.
   - Calculate Hash2 for both substrings.
   - If (Hash1_sub1 == Hash1_sub2) AND (Hash2_sub1 == Hash2_sub2), return true.
   - Else return false.

### Time Complexity

- **O(N + Q)**: `O(N)` preprocessing, `O(1)` per query.

### Space Complexity

- **O(N)**: To store hashes and powers.

![Algorithm Visualization](../images/HSH-002/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:**
```
ababa
1
0 2 2 4
```
Query: `s[0..2]` ("aba") vs `s[2..4]` ("aba").

**Preprocessing:**
- Calculate prefixes for "ababa".
- `H[3]` (hash of "aba") will be computed.
- `H[5]` (hash of "ababa") will be computed.

**Query Processing:**
- Substring 1 (0..2): `H[3] - H[0] x B^3`. Since `H[0]=0`, this is just `H[3]`.
- Substring 2 (2..4): `H[5] - H[2] x B^3`.
- If we do the math (assuming no collisions), these values will be identical because the underlying strings "aba" are identical.
- Result: `true`.

## ✅ Proof of Correctness

### Invariant
The function `getHash(l, r)` correctly returns the polynomial hash of `s[l dots r]`.
Proof:
`H[r+1] = s[0]B^r + s[1]B^r-1 + dots + s[r]B^0`.
`H[l] = s[0]B^l-1 + dots + s[l-1]B^0`.
`H[l] x B^r-l+1 = s[0]B^r + dots + s[l-1]B^r-l+1`.
Subtracting gives: `s[l]B^r-l + dots + s[r]B^0`, which is exactly the hash of `s[l dots r]`.

## 💡 Interview Extensions

- **Extension 1:** Find the longest common substring between two strings.
  - *Answer:* Binary search on length + Hashing. `O(N log N)`.
- **Extension 2:** Check if a string is a palindrome using hashing.
  - *Answer:* Compute forward hash and reverse hash. Check if Hash(Forward) == Hash(Reverse).

### Common Mistakes to Avoid

1. **Single Hash Collision**
   - ❌ Wrong: Using only one modulus (e.g., `10^9+7`).
   - ✅ Correct: Use double hashing to make probability of failure negligible.

2. **Negative Modulo Result**
   - ❌ Wrong: `(a - b) % M` in languages like C++/Java can be negative.
   - ✅ Correct: `(a - b + M) % M`.

3. **1-based vs 0-based Indexing**
   - ❌ Wrong: Mixing up prefix array indices. `H[i]` usually stores hash of length `i` (indices `0 dots i-1`).
   - ✅ Correct: Be consistent. `H[i+1]` for prefix ending at `i`.

## Related Concepts

- **Rabin-Karp:** Uses this technique for pattern matching.
- **Suffix Structures:** Suffix Array/Tree can also solve this but are harder to implement.
