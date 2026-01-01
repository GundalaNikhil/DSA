---
problem_id: TRI_LONGEST_WORD_K_PREFIXES__8329
display_id: TRI-014
slug: longest-word-by-k-prefixes
title: "Longest Word Buildable by At Least K Prefixes"
difficulty: Medium
difficulty_score: 55
topics:
  - Trie
  - String
  - DFS
tags:
  - trie
  - prefix-matching
  - word-building
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-014: Longest Word Buildable by At Least K Prefixes

## Problem Statement

Given a dictionary of lowercase words and an integer `k`, find the longest word that has at least `k` of its prefixes present in the dictionary. If multiple words have the same maximum length, return the lexicographically smallest one. If no word meets the requirement, return an empty string.

A prefix of a word `w` is any substring `w[0...i]` where `0 <= i < len(w)-1` (excluding the word itself).

![Problem Illustration](../images/TRI-014/problem-illustration.png)

## Input Format

- First line: two integers `n` (number of words) and `k` (minimum prefix count)
- Next `n` lines: each contains a single lowercase word

## Output Format

Return the longest word with at least `k` prefixes in the dictionary, or an empty string if none exists.

## Constraints

- `1 <= n <= 10^5` (number of words)
- `1 <= k <= 30`
- `1 <= word length <= 30`
- All words consist of lowercase English letters (a-z)
- No duplicate words in dictionary

## Example

**Input:**

```
5 3
a
ap
app
apple
apex
```

**Output:**

```
apple
```

**Explanation:**

Analyzing each word:

- "a": No prefixes → 0 < k=3 ✗
- "ap": Prefix "a" exists → 1 < k=3 ✗
- "app": Prefixes "a", "ap" exist → 2 < k=3 ✗
- "apple": Prefixes "a", "ap", "app", "appl"
  - "a" exists ✓
  - "ap" exists ✓
  - "app" exists ✓
  - "appl" doesn't exist ✗
  - Total: 3 >= k=3 ✓ (length 5)
- "apex": Prefixes "a", "ap", "ape"
  - "a" exists ✓
  - "ap" exists ✓
  - "ape" doesn't exist ✗
  - Total: 2 < k=3 ✗

Result: "apple" (longest with >= 3 prefixes)

![Example Visualization](../images/TRI-014/example-1.png)

## Notes

- A word's prefix does NOT include the word itself or the empty string
- For tie-breaking, use lexicographic order (dictionary order)
- Use a trie to efficiently check prefix existence

## Related Topics

Trie, String, Prefix Matching, Lexicographic Order

---

## Solution Template

### Java


### Python


### C++


### JavaScript

