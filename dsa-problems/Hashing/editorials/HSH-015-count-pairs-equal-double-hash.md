---
problem_id: HSH_COUNT_PAIRS_EQUAL_DOUBLE_HASH__9418
display_id: HSH-015
slug: count-pairs-equal-double-hash
title: "Count Pairs with Equal Hash Mod Two Mods"
difficulty: Medium
difficulty_score: 50
topics:
  - Hashing
  - Combinatorics
  - String Algorithms
tags:
  - hashing
  - double-hash
  - pairs
  - medium
premium: true
subscription_tier: basic
---

# HSH-015: Count Pairs with Equal Hash Mod Two Mods

## 📋 Problem Summary

You are given a string `s` and a length `L`.
Find the number of pairs of indices `(i, j)` such that `i < j` and the substring starting at `i` with length `L` is "equal" to the substring starting at `j` with length `L`.
Equality is determined by checking if their **Double Hashes** match.

## 🌍 Real-World Scenario

**Scenario Title:** Duplicate Log Entry Detection

Imagine a system processing millions of log lines.
- You want to find how many times the exact same error message of length `L` appears.
- If a message appears `K` times, it contributes `K(K-1)/2` pairs of duplicates.
- Using double hashing ensures we don't accidentally group different messages together (collisions), providing accurate statistics.

![Real-World Application](../images/HSH-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Grouping by Hash

String: "banana", L=2
Substrings:
1. "ba" -> Hash Pair (H1_a, H2_a)
2. "an" -> Hash Pair (H1_b, H2_b)
3. "na" -> Hash Pair (H1_c, H2_c)
4. "an" -> Hash Pair (H1_b, H2_b)
5. "na" -> Hash Pair (H1_c, H2_c)

Groups:
- (H1_a, H2_a): Count 1 ("ba"). Pairs: 0.
- (H1_b, H2_b): Count 2 ("an"). Pairs: 1.
- (H1_c, H2_c): Count 2 ("na"). Pairs: 1.

Total Pairs: 2.

### Key Concept: Double Hashing

Single hashing with modulo `10^9+7` has a collision probability of `~= 1/10^9`.
With `N=10^5` substrings, we have `~= 10^10` pairs, so collisions are possible (Birthday Paradox).
**Double Hashing** uses two pairs of `(Base, Mod)`.
Collision probability drops to `~= 1/10^18`, making it virtually impossible to have a false positive.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** String `s`, integer `L`.
- **Output:** Long integer (count of pairs).
- **Constraints:** `N <= 10^5`.
- **Note:** The number of pairs can be up to `N(N-1)/2 ~= 5 * 10^9`, so use 64-bit integer (`long` in Java/C++) for the result.

## Naive Approach

### Intuition

Compare every pair of substrings.

### Time Complexity

- **O(N^2 * L)**: String comparison.
- **O(N^2)**: With hashing but checking all pairs. Too slow.

## Optimal Approach

### Key Insight

1. Compute rolling hashes for all substrings of length `L`.
2. Store counts of each hash pair in a Map.
   - Key: `(hash1, hash2)`
   - Value: `count`
3. If a hash pair appears `k` times, it contributes `k * (k - 1) / 2` pairs.
4. Sum up these contributions.

### Algorithm

1. Initialize `Map<Pair<Long, Long>, Integer> counts`.
2. Compute rolling hashes for `s` with two sets of parameters.
3. Iterate `i` from 0 to `N-L`:
   - Get `h1` and `h2` for `s[i..i+L-1]`.
   - Increment count in Map.
4. Iterate Map values: `ans += count * (count - 1) / 2`.
5. Return `ans`.

### Time Complexity

- **O(N)**: Single pass to compute hashes and populate map.

### Space Complexity

- **O(N)**: Map storage.

![Algorithm Visualization](../images/HSH-015/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `aaaa`, `L=2`.

**Iter 0 (i=0):**
- Substring "aa". Hash pair (X, Y).
- Map: `{(X,Y): 1}`.

**Iter 1 (i=1):**
- Substring "aa". Hash pair (X, Y).
- Map: `{(X,Y): 2}`.

**Iter 2 (i=2):**
- Substring "aa". Hash pair (X, Y).
- Map: `{(X,Y): 3}`.

**Calc:**
- Count = 3.
- Pairs = `3 x 2 / 2 = 3`.

## ✅ Proof of Correctness

### Invariant
We iterate through all possible substrings of length `L`.
Double hashing ensures unique identification of substring content.
Grouping counts allows combinatorial calculation of pairs.

## 💡 Interview Extensions

- **Extension 1:** Find the most frequent substring of length `L`.
  - *Answer:* Return max value in Map.
- **Extension 2:** Longest substring that appears at least K times.
  - *Answer:* Binary search on Length + Hashing.

### Common Mistakes to Avoid

1. **Integer Overflow**
   - ❌ Wrong: Using `int` for answer.
   - ✅ Correct: Use `long` (64-bit).
2. **Single Hash**
   - ❌ Wrong: Using one hash.
   - ✅ Correct: Double hash minimizes collision risk significantly.

## Related Concepts

- **Rabin-Karp:** The core hashing mechanism.
- **Suffix Automaton:** Can solve this without hashing in `O(N)`.
