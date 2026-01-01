---
problem_id: STC_DISTINCT_SUBSTRINGS_SA__9517
display_id: STC-008
slug: distinct-substrings-sa
title: "Distinct Substrings Count via SA/LCP"
difficulty: Medium
difficulty_score: 46
topics:
  - Strings
  - Suffix Array
  - Counting
tags:
  - strings
  - suffix-array
  - counting
  - medium
premium: true
subscription_tier: basic
---

# STC-008: Distinct Substrings Count via SA/LCP

## 📋 Problem Summary

Given a string `s`, you need to calculate the total number of **distinct** (unique) substrings it contains. You are expected to use the Suffix Array and LCP Array to solve this efficiently.

## 🌍 Real-World Scenario

**Scenario Title:** Search Engine Index Size Estimation

When building an index for a large corpus of text (like the web), we need to estimate the size of the dictionary (the set of unique terms or phrases). If we treat the entire corpus as a single long string, the number of distinct substrings gives us an upper bound on the number of unique n-grams we might need to index. This helps in capacity planning and optimizing storage structures.

**Why This Problem Matters:**

- **Complexity Analysis:** It demonstrates how Suffix Arrays can solve counting problems that are otherwise difficult.
- **Data Compression:** The number of distinct substrings relates to the entropy and compressibility of the string.
- **Bioinformatics:** Counting unique k-mers in DNA sequences.

![Real-World Application](../images/STC-008/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let `s = "ababa"`. `n = 5`.
Total substrings (including duplicates) = `5 + 4 + 3 + 2 + 1 = 15`.

Suffixes (Sorted):
1. `a` (len 1)
2. `aba` (len 3)
3. `ababa` (len 5)
4. `ba` (len 2)
5. `baba` (len 4)

LCP Array:
- `a` vs `aba`: "a" (1)
- `aba` vs `ababa`: "aba" (3)
- `ababa` vs `ba`: "" (0)
- `ba` vs `baba`: "ba" (2)

LCP Sum = `1 + 3 + 0 + 2 = 6`.

Distinct Substrings = Total - Duplicates
= `15 - 6 = 9`.

Let's list them: `a`, `ab`, `aba`, `abab`, `ababa`, `b`, `ba`, `bab`, `baba`. (Count is indeed 9).

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Total Substrings:** The number of substrings of a string of length `n` is `n * (n + 1) / 2`.
- **Overflow:** The result can exceed `2^31 - 1`. Use 64-bit integers (`long` in Java/C++, `BigInt` or standard `Number` in JS/Python).
- **Empty String:** If `n=0`, result is 0.

## Naive Approach

### Intuition

Generate every substring and store them in a Set to count unique ones.

### Algorithm

1. Initialize an empty Set.
2. Iterate `i` from `0` to `n-1`.
3. Iterate `j` from `i` to `n-1`.
4. Add `s[i...j]` to the Set.
5. Return Set size.

### Time Complexity

- **O(N^2)**: String hashing/insertion takes time proportional to length. Total length processed is O(N^3) or O(N^2) with optimized hashing.
- Too slow for `N=100,000`.

### Space Complexity

- **O(N^2)**: To store all substrings.

## Optimal Approach (SA + LCP)

### Key Insight

Every substring is a prefix of some suffix.
The total number of prefixes of all suffixes is simply the sum of lengths of all suffixes: `n * (n + 1) / 2`.
However, we overcount because different suffixes can share the same prefix.
The Suffix Array sorts suffixes lexicographically. This means suffixes sharing a common prefix will be adjacent in the sorted list.
The `lcp[i]` value tells us exactly how many prefixes the suffix `sa[i+1]` shares with the suffix `sa[i]`. These shared prefixes have already been counted by `sa[i]` (or previous suffixes).
Therefore, `lcp[i]` is exactly the number of duplicate substrings contributed by `sa[i+1]` relative to `sa[i]`.

**Formula:**
`Distinct Count = (Sum of lengths of all suffixes) - (Sum of LCP values)`
`Distinct Count = n*(n+1)/2 - sum(lcp)`

### Algorithm

1. Construct Suffix Array (SA).
2. Construct LCP Array.
3. Calculate `total = n * (n + 1) / 2`.
4. Calculate `duplicates = sum(lcp)`.
5. Return `total - duplicates`.

### Time Complexity

- **O(N log N)**: Dominated by SA construction.

### Space Complexity

- **O(N)**: For SA and LCP arrays.

![Algorithm Visualization](../images/STC-008/algorithm-visualization.png)
![Algorithm Steps](../images/STC-008/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

`s = "aaa"`
`n = 3`
Total substrings = `3 * 4 / 2 = 6` ("a", "a", "a", "aa", "aa", "aaa")

SA: `[2, 1, 0]` ("a", "aa", "aaa")
LCP:
- "a" vs "aa": 1
- "aa" vs "aaa": 2
Sum LCP = `1 + 2 = 3`.

Distinct = `6 - 3 = 3`.
Correct ("a", "aa", "aaa").

![Example Visualization](../images/STC-008/example-1.png)

## ✅ Proof of Correctness

### Invariant

The number of distinct substrings is the number of nodes in the Suffix Tree (excluding root) or Suffix Automaton.
Using SA+LCP:
Each suffix `sa[i]` contributes `n - sa[i]` prefixes (substrings).
`lcp[i-1]` of these prefixes are shared with `sa[i-1]`.
Since `sa` is sorted, `sa[i]` shares the *most* prefixes with `sa[i-1]` compared to any other `sa[j]` where `j < i`.
Thus, the *new* distinct substrings contributed by `sa[i]` is `(n - sa[i]) - lcp[i-1]`.
Summing this over all `i` gives `Total Lengths - Sum LCP`.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: K-th Lexicographical Substring**
  - We know suffix `i` contributes `len - lcp` new substrings. We can find which suffix contains the K-th substring and extract it.

- **Extension 2: Suffix Automaton**
  - Solve the same problem in O(N) time and space using Suffix Automaton (sum of `len(u) - len(link(u))`).

### Common Mistakes to Avoid

1. **Integer Overflow**
   - ❌ Using `int` for the total count. `N=10^5` -> `N^2/2 = 5*10^9` > `2*10^9`.
   - ✅ Use `long long` (C++) or `long` (Java).

2. **Incorrect LCP Sum**
   - ❌ Summing `lcp[i]` where `lcp[i]` is undefined or garbage.
   - ✅ LCP array has size `N-1`.

## Related Concepts

- **Suffix Automaton**: `sum(len[u] - len[link[u]])` gives distinct substrings.
- **Trie**: Insert all suffixes into a Trie and count nodes (O(N^2)).
