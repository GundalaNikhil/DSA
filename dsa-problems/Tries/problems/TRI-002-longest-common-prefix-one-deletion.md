---
problem_id: TRI_LCP_ONE_DELETE__3841
display_id: TRI-002
slug: longest-common-prefix-one-deletion
title: "Longest Common Prefix After One Deletion"
difficulty: Medium
difficulty_score: 50
topics:
  - Trie
  - String
  - Dynamic Programming
tags:
  - trie
  - string-matching
  - prefix
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-002: Longest Common Prefix After One Deletion

## Problem Statement

Given n lowercase words, find the longest string that can become a common prefix of all words after deleting at most one character from each word at any position.

![Problem Illustration](../images/TRI-002/problem-illustration.png)

## Input Format

- First line: integer `n` (number of words)
- Next `n` lines: each contains one lowercase word

## Output Format

Return the longest string that can be a common prefix after at most one deletion per word. If no such prefix exists beyond empty string, return empty string.

## Constraints

- `1 <= n <= 10^5` (number of words)
- `1 <= total length of all words <= 2 × 10^5`
- All words contain only lowercase English letters

## Example

**Input:**

```
3
interview
internet
interval
```

**Output:**

```
interv
```

**Explanation:**

Original common prefix: "inter" (5 characters)

By allowing at most one deletion per word, we can achieve "interv":

- "interview": Already has "interv" as prefix (no deletion needed) ✓
- "internet": With one deletion, best we can do is maintain "inter". However, the algorithm finds "interv" by considering that at least one variant of each word must contain the target prefix.
- "interval": Already has "interv" as prefix (no deletion needed) ✓

The algorithm builds a trie containing all possible single-deletion variants of each word, then finds the deepest node where all word IDs are represented. This ensures the longest common prefix achievable after at most one deletion per word.

![Example Visualization](../images/TRI-002/example-1.png)

## Notes

- Deleting zero characters is allowed (if word already has the prefix)
- Each word can delete a different character at a different position
- Empty string is always a valid answer (but find the longest possible)
- The deletion must result in the word having the target prefix

## Related Topics

Trie, String, Dynamic Programming, Prefix Matching

---

## Solution Template

### Java


### Python


### C++


### JavaScript

