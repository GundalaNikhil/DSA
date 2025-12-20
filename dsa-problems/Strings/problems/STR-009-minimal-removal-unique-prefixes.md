---
problem_id: STR_MINIMAL_REMOVAL_UNIQUE_PREFIXES__1009
display_id: STR-009
slug: minimal-removal-unique-prefixes
title: "Minimal Removal for Unique Prefixes"
difficulty: Medium
difficulty_score: 45
topics:
  - String Manipulation
  - Trie
  - Greedy
tags:
  - prefix-conflict
  - deletion
  - trie-structure
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-009: Minimal Removal for Unique Prefixes

## Problem Statement

Given an integer `L` and `n` strings, delete the minimum total number of characters (only from the ends of strings) so that all resulting strings have distinct prefixes of length `L`.

## Input Format

- First line: Integer `L` (1 ≤ L ≤ 20)
- Second line: Integer `n` (1 ≤ n ≤ 2 × 10^5)
- Next n lines: One string per line (total length ≤ 2 × 10^5)

## Output Format

- A single integer representing minimum deletions

## Constraints

- `1 ≤ n ≤ 2 × 10^5`
- `1 ≤ L ≤ 20`
- Total string length ≤ `2 × 10^5`

## Example 1

**Input:**

```
2
3
ab
ac
ad
```

**Output:**

```
0
```

**Explanation:**

- All prefixes already distinct: "ab", "ac", "ad"

## Example 2

**Input:**

```
2
3
abc
abd
acc
```

**Output:**

```
2
```

**Explanation:**

- Prefixes: "ab", "ab", "ac" → conflict on first two
- Delete 2 chars from "abd" → "a" (prefix length < L)
- Result prefixes: "ab", "a", "ac" (all distinct)

## Notes

- Use trie to identify prefix conflicts
- Greedy: keep longest string in each conflict group
- Deletion formula: len(s) - (L-1) for conflicts
