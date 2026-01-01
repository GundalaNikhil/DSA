---
problem_id: STC_LONGEST_REPEATED_SUBSTRING_SA__2764
display_id: STC-007
slug: longest-repeated-substring-sa
title: "Longest Repeated Substring via SA/LCP"
difficulty: Medium
difficulty_score: 50
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

# STC-007: Longest Repeated Substring via SA/LCP

## 📋 Problem Summary

Given a string `s`, find the longest substring that appears at least twice in `s`. If there are multiple substrings with the same maximum length, return the one that is lexicographically smallest. If no repeated substring exists, output `NONE`.

## 🌍 Real-World Scenario

**Scenario Title:** Data Deduplication

In storage systems, "deduplication" is a technique to eliminate duplicate copies of repeating data. By identifying large chunks of data that appear multiple times (repeated substrings), the system can store just one copy and replace others with references. This significantly saves storage space. Finding the longest repeated substring is a simplified version of identifying the most redundant parts of a file.

**Why This Problem Matters:**

- **Compression:** Core concept in dictionary-based compression algorithms (like LZ77).
- **Music Analysis:** Identifying recurring themes or motifs in a musical score (represented as a string of notes).
- **Plagiarism:** Detecting copied sections within a single large document.

![Real-World Application](../images/STC-007/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Concept Visualization

Let `s = "banana"`.
Suffixes sorted (SA):
0. `a` (5)
1. `ana` (3)
2. `anana` (1)
3. `banana` (0)
4. `na` (4)
5. `nana` (2)

LCP Array (adjacent common prefixes):
- `a` vs `ana`: "a" (len 1)
- `ana` vs `anana`: "ana" (len 3)
- `anana` vs `banana`: "" (len 0)
- `banana` vs `na`: "" (len 0)
- `na` vs `nana`: "na" (len 2)

LCP Values: `[1, 3, 0, 0, 2]`
Max LCP is 3.
Corresponding substring: "ana".

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Overlapping:** Repeated substrings can overlap. In "aaaa", "aaa" appears twice (indices 0 and 1).
- **Lexicographically Smallest:** If "abc" and "xyz" both appear twice and are the longest, return "abc".
- **NONE:** If max LCP is 0, output `NONE`.

## Naive Approach

### Intuition

Generate all substrings, count their occurrences using a hash map, and track the max length.

### Algorithm

1. Iterate length `L` from `N-1` down to 1.
2. For each `L`, extract all substrings of length `L`.
3. Use a HashSet to check for duplicates.
4. If a duplicate is found, return it (since we started from max length).

### Time Complexity

- **O(N^2)**: With hashing.
- **O(N^3)**: Without hashing.
- Too slow for N=100,000.

## Optimal Approach (SA + LCP)

### Key Insight

Any repeated substring must be a prefix of two different suffixes.
If we sort all suffixes (Suffix Array), suffixes starting with the same prefix will be adjacent.
The longest common prefix between any two suffixes `i` and `j` is the minimum LCP value in the interval between their ranks in the Suffix Array.
Therefore, the longest common prefix between *any* pair of suffixes is the maximum value in the LCP array (which stores LCP of adjacent sorted suffixes).

### Algorithm

1. Construct the **Suffix Array (SA)** for `s`.
2. Construct the **LCP Array** using Kasai's algorithm.
3. Iterate through the LCP array to find the maximum value `max_len`.
4. Since we want the lexicographically smallest result among ties, and the SA is already sorted lexicographically, we should pick the *first* occurrence of `max_len` in the LCP array.
   - `lcp[i]` is the common prefix of `sa[i]` and `sa[i+1]`.
   - Since `sa[i]` comes before `sa[i+1]`, they both start with the same prefix.
   - We can extract the substring from `s` starting at `sa[i]` with length `max_len`.
5. If `max_len == 0`, return `NONE`.

### Time Complexity

- **O(N log N)**: Dominated by Suffix Array construction. LCP construction is O(N).

### Space Complexity

- **O(N)**: To store SA and LCP arrays.

![Algorithm Visualization](../images/STC-007/algorithm-visualization.png)
![Algorithm Steps](../images/STC-007/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

`s = "cababa"`
SA: `[5, 3, 1, 4, 2, 0]` ("a", "aba", "ababa", "ba", "baba", "cababa")
LCP: `[1, 3, 0, 2, 0]`

Scan LCP:
- `i=0`: `lcp[0]=1`. `maxLen=1`, `startIdx=sa[0]=5` ("a").
- `i=1`: `lcp[1]=3`. `maxLen=3`, `startIdx=sa[1]=3` ("aba").
- `i=2`: `lcp[2]=0`.
- `i=3`: `lcp[3]=2`. `2 < 3`, no update.
- `i=4`: `lcp[4]=0`.

Result: `s.substring(3, 3+3)` = "aba".

![Example Visualization](../images/STC-007/example-1.png)

## ✅ Proof of Correctness

### Invariant

The longest common prefix of any set of suffixes is the minimum LCP value in the range covering those suffixes in the Suffix Array.
The longest repeated substring corresponds to the longest common prefix of *some* pair of suffixes.
The LCP of any pair `(i, j)` is `min(lcp[rank[i]...rank[j]-1])`.
This minimum is maximized when `rank[i]` and `rank[j]` are adjacent (i.e., `rank[j] = rank[i] + 1`).
Thus, the maximum value in the adjacent LCP array is the length of the longest repeated substring.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1: Longest Substring Repeated K Times**
  - Use a sliding window of size `K-1` over the LCP array. Find `max(min(window))`.

- **Extension 2: Longest Common Substring of Two Strings**
  - Concatenate `s1 + '#' + s2`. Build SA/LCP. Find max LCP where one suffix is from `s1` and other from `s2`.

### Common Mistakes to Avoid

1. **Not handling ties correctly**
   - ❌ Updating `maxLen` even if `lcp[i] == maxLen`.
   - ✅ Only update if `lcp[i] > maxLen`. Since we scan left-to-right (lexicographically increasing), the first one we see is the smallest.

2. **Edge case: No repetition**
   - ❌ Returning empty string or crashing.
   - ✅ Check `maxLen == 0` and return "NONE".

## Related Concepts

- **Suffix Tree**: Can solve this in linear time (O(N)).
- **Rabin-Karp + Binary Search**: O(N log N) alternative.
