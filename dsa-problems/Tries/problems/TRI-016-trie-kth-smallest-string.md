---
problem_id: TRI_KTH_SMALLEST_STRING__5628
display_id: TRI-016
slug: trie-kth-smallest-string
title: "Trie-Based Kth Smallest String"
difficulty: Medium
difficulty_score: 51
topics:
  - Trie
  - String
  - Lexicographic Order
tags:
  - trie
  - kth-element
  - lexicographic
  - inorder-traversal
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-016: Trie-Based Kth Smallest String

## Problem Statement

Given a collection of `n` distinct lowercase strings and an integer `k`, return the k-th string in lexicographic order (1-indexed). If `k` exceeds the total number of strings, return an empty string.

![Problem Illustration](../images/TRI-016/problem-illustration.png)

## Input Format

- First line: two integers `n` (number of strings) and `k` (position)
- Next `n` lines: each contains a single lowercase string

## Output Format

Return the k-th smallest string in lexicographic order, or an empty string if k > n.

## Constraints

- `1 <= n <= 10^5` (number of strings)
- `1 <= k <= 10^9` (may exceed n)
- Total character length across all strings <= `2 × 10^5`
- All strings consist of lowercase English letters (a-z)
- No duplicate strings in input

## Example

**Input:**

```
3 2
b
a
aa
```

**Output:**

```
aa
```

**Explanation:**

Sorting strings lexicographically: `["a", "aa", "b"]`

Position 1: "a"
Position 2: "aa" ← answer
Position 3: "b"

The 2nd string is "aa".

![Example Visualization](../images/TRI-016/example-1.png)

## Notes

- k is 1-indexed (first string is at position 1)
- Lexicographic order: "a" < "aa" < "ab" < "b"
- Use trie with DFS traversal in alphabetical order
- Maintain subtree counts for efficient skip-counting

## Related Topics

Trie, String, Lexicographic Order, Kth Element, DFS

---

## Solution Template

### Java


### Python


### C++


### JavaScript

