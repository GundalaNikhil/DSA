---
problem_id: STC_LCS_TWO_STRINGS_SA__4927
display_id: STC-011
slug: lcs-two-strings-sa
title: "Longest Common Substring of Two Strings (SA)"
difficulty: Medium
difficulty_score: 56
topics:
  - Strings
  - Suffix Array
  - LCP
tags:
  - strings
  - suffix-array
  - lcp
  - medium
premium: true
subscription_tier: basic
---

# STC-011: Longest Common Substring of Two Strings (SA)

## 📋 Problem Summary

Given two strings `a` and `b`, find the length of the **Longest Common Substring**. This is the longest string that appears as a contiguous sequence of characters in both `a` and `b`.

## 🌍 Real-World Scenario

**Scenario Title:** Code Plagiarism Detection

Imagine you are a professor checking student assignments for plagiarism. Students might copy code but rename variables or reorder functions. However, significant chunks of logic often remain identical. By finding the longest common substring between two code submissions (after some normalization), you can detect if one student copied from another. If the longest common substring is unusually long, it's a strong indicator of copying.

**Why This Problem Matters:**

- **Bioinformatics:** Finding homologous regions in DNA or protein sequences.
- **Data Deduplication:** Identifying shared data chunks between files to save storage.
- **Spam Detection:** Finding common phrases in spam emails.

![Real-World Application](../images/STC-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let `a = "abcd"`, `b = "bc"`.
Concatenate with sentinel: `S = "abcd#bc"`.

Suffixes of S (sorted):
1. `abcd#bc` (starts in `a`)
2. `bc` (starts in `b`)
3. `bcd#bc` (starts in `a`)
4. `c` (starts in `b`)
5. `cd#bc` (starts in `a`)
6. `d#bc` (starts in `a`)
... (and others starting with #)

Notice `bc` (from `b`) and `bcd#bc` (from `a`) are close in sorted order.
LCP("bc", "bcd#bc") = "bc" (length 2).
This is the longest common substring.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Contiguous:** Must be a substring, not a subsequence. "ace" is a subsequence of "abcde", but "abc" is a substring.
- **Sentinel:** Use a character like `#` or `$` that doesn't appear in `a` or `b`.
- **Constraints:** Total length up to 200,000. O(N^2) DP solution is too slow.

## Naive Approach

### Intuition

Check every substring of `a` to see if it exists in `b`.

### Algorithm

1. Iterate length `len` from `|a|` down to 1.
2. For each substring of `a` with length `len`:
3. Check if it is a substring of `b` (using `b.contains()` or similar).
4. If found, return `len`.

### Time Complexity

- **O(|a| * |b| * min(|a|, |b|))** or **O(|a|^2)** depending on implementation.
- Too slow.

### Space Complexity

- **O(1)**.

## Optimal Approach (SA + LCP)

### Key Insight

If a string `w` is a substring of both `a` and `b`, then `w` is a prefix of some suffix of `a` AND a prefix of some suffix of `b`.
If we construct the Suffix Array for `S = a + '#' + b`, all suffixes are sorted lexicographically.
Suffixes starting with the same prefix `w` will be grouped together.
The longest common substring will correspond to the maximum LCP between a suffix starting in `a` and a suffix starting in `b`.
Since the SA is sorted, we only need to check **adjacent** suffixes in the Suffix Array. If `sa[i]` and `sa[i+1]` belong to different original strings, their LCP is a candidate for the answer.

### Algorithm

1. Construct `S = a + '#' + b`.
2. Build Suffix Array (`sa`) and LCP Array (`lcp`) for `S`.
3. Iterate `i` from `0` to `|S| - 2`.
4. Check if `sa[i]` and `sa[i+1]` belong to different strings:
   - One index is `< |a|`.
   - The other index is `> |a|` (i.e., inside `b`).
5. If they are from different strings, update `max_len = max(max_len, lcp[i])`.
6. Return `max_len`.

### Time Complexity

- **O(N log N)**: Where `N = |a| + |b|`. Dominated by SA construction.

### Space Complexity

- **O(N)**: To store SA and LCP.

![Algorithm Visualization](../images/STC-011/algorithm-visualization.png)
![Algorithm Steps](../images/STC-011/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

`a = "abcd"`, `b = "bc"`
`S = "abcd#bc"`
SA:
0. `#bc` (4)
1. `abcd#bc` (0)
2. `bc` (5) - from B
3. `bcd#bc` (1) - from A
4. `c` (6) - from B
5. `cd#bc` (2) - from A
6. `d#bc` (3) - from A

LCP:
- `#` vs `abcd`: 0
- `abcd` vs `bc`: 0
- `bc` vs `bcd`: 2 ("bc") -> `sa[2]=5` (B), `sa[3]=1` (A). Diff strings. `maxLen = 2`.
- `bcd` vs `c`: 0
- `c` vs `cd`: 1 ("c") -> `sa[4]=6` (B), `sa[5]=2` (A). Diff strings. `maxLen` stays 2 (1 < 2).
- `cd` vs `d`: 0

Result: 2.

![Example Visualization](../images/STC-011/example-1.png)

## ✅ Proof of Correctness

### Invariant

The longest common substring corresponds to the maximum LCP between a suffix of `a` and a suffix of `b`.
In the sorted Suffix Array, suffixes starting with the same prefix are grouped together.
The "best" match for any suffix `u` is either its immediate predecessor or immediate successor in the SA.
Thus, we only need to check adjacent pairs `(sa[i], sa[i+1])` in the SA. If they belong to different strings, their LCP is a candidate.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: K Strings**

- **Extension 2: Generalized Suffix Tree**
  - Build a suffix tree for multiple strings. Find the deepest node marked with all string IDs.

### Common Mistakes to Avoid

1. **Sentinel Character**
   - ❌ `a + b`. If `a="ab"`, `b="ba"`, `S="abba"`. Suffix "abba" (from a) and "ba" (from b) might mix.
   - ✅ `a + '#' + b`.

2. **Checking Origin**
   - ❌ `max(lcp)`.
   - ✅ `max(lcp)` only if `sa[i]` and `sa[i+1]` are from different strings. Otherwise, we might find a repeated substring inside `a` itself.

## Related Concepts

- **Suffix Automaton**: Can solve this by building automaton for `a` and streaming `b` through it.
- **DP**: O(|a|*|b|) solution using `dp[i][j]`.
