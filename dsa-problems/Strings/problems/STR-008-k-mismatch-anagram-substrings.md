---
problem_id: STR_K_MISMATCH_ANAGRAM_SUBSTRINGS__1008
display_id: STR-008
slug: k-mismatch-anagram-substrings
title: "K-Mismatch Anagram Substrings"
difficulty: Medium
difficulty_score: 43
topics:
  - String Manipulation
  - Sliding Window
  - Frequency Analysis
tags:
  - anagram
  - fuzzy-matching
  - window-algorithm
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-008: K-Mismatch Anagram Substrings

## Problem Statement

Given a string `s`, a pattern `p`, and integers `m` (substring length) and `k` (allowed mismatches), count how many substrings of length `m` in `s` become anagrams of `p` after at most `k` character substitutions.

Note: `m = |p|`

## Input Format

- First line: String `s` (1 ≤ |s| ≤ 10^5)
- Second line: String `p` (1 ≤ |p| ≤ 10^5)
- Third line: Integer `k` (0 ≤ k ≤ m)

## Output Format

- A single integer representing the count of valid substrings

## Constraints

- `1 ≤ |s| ≤ 10^5`
- `1 ≤ m ≤ |s|`
- `m = |p|`
- `0 ≤ k ≤ m`

## Example 1

**Input:**

```
abxcab
aabc
1
```

**Output:**

```
3
```

**Explanation:**

- Substring "abxc": need 1 substitution (x→a) → valid
- Substring "bxca": need 1 substitution (x→a) → valid
- Substring "xcab": need 1 substitution (x→a) → valid

## Notes

- Use sliding window with incremental frequency updates
- Mismatch cost = Σ max(0, freq_p[c] - freq_window[c])
- O(n) time with O(1) space (fixed 26 chars)
