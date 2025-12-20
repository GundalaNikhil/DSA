---
problem_id: STR_SMALLEST_MISSING_SUBSTRING__1003
display_id: STR-003
slug: smallest-missing-substring
title: "Smallest Missing Substring"
difficulty: Medium
difficulty_score: 40
topics:
  - String Manipulation
  - DFS
  - Hashing
tags:
  - substring-search
  - lexicographic
  - lazy-generation
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-003: Smallest Missing Substring

## Problem Statement

Given a string `s` consisting of lowercase English letters and an integer `k`, find the lexicographically smallest string of length `k` that is NOT a substring of `s`.

## Input Format

- First line: String `s` (1 ≤ |s| ≤ 2 × 10^5)
- Second line: Integer `k` (1 ≤ k ≤ 20)

## Output Format

- A single string of length `k` representing the lexicographically smallest string not present in `s`

## Constraints

- `1 ≤ |s| ≤ 2 × 10^5`
- `1 ≤ k ≤ 20`
- `s` contains only lowercase English letters

## Example 1

**Input:**

```
ababa
2
```

**Output:**

```
aa
```

**Explanation:**

- Substrings of length 2 in "ababa": "ab", "ba", "ab", "ba"
- Unique: {"ab", "ba"}
- Checking lexicographically: "aa" is not in set → answer

## Example 2

**Input:**

```
abc
3
```

**Output:**

```
aaa
```

**Explanation:**

- "abc" only has one substring of length 3: "abc"
- "aaa" is lexicographically first and not in "abc"

## Notes

- Use DFS with lazy generation to avoid creating all 26^k possibilities
- Build a set of existing k-length substrings for O(1) lookup
- Generate candidates in lexicographic order and stop at first missing
