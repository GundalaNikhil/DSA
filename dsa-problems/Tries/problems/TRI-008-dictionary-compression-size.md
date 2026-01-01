---
problem_id: TRI_DICTIONARY_COMPRESSION__2931
display_id: TRI-008
slug: dictionary-compression-size
title: "Dictionary Compression Size"
difficulty: Medium
difficulty_score: 45
topics:
  - Trie
  - String
  - Data Structures
tags:
  - trie
  - compression
  - memory-optimization
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-008: Dictionary Compression Size

## Problem Statement

Given `n` lowercase words, compute the total number of nodes in the trie needed to store them, including the root node.

![Problem Illustration](../images/TRI-008/problem-illustration.png)

## Input Format

- First line: integer `n` (number of words)
- Next `n` lines: each contains a single lowercase word

## Output Format

Return a single integer representing the total number of trie nodes (including root).

## Constraints

- `1 <= n <= 10^5` (number of words)
- Total character length across all words <= `2 × 10^5`
- All words consist of lowercase English letters (a-z)
- Words may have duplicates

## Example 1

**Input:**

```
3
a
ab
abc
```

**Output:**

```
4
```

**Explanation:**

Trie structure:

```
  root (node 1)
    |
    a (node 2, word end)
    |
    b (node 3, word end)
    |
    c (node 4, word end)
```

Total nodes: 4 (root + a + b + c)

![Example Visualization](../images/TRI-008/example-1.png)

## Example 2

**Input:**

```
4
cat
car
card
dog
```

**Output:**

```
7
```

**Explanation:**

Trie structure:

```
      root (node 1)
      /    \
    c(2)   d(6)
    |       |
    a(3)    o(7)
   / \      |
  t(4) r(5) g
       |
     d
```

Total nodes: 7

## Notes

- The root node always counts as 1
- Duplicate words don't create additional nodes
- Shared prefixes result in node reuse

## Related Topics

Trie, String, Data Structures, Memory Optimization

---

## Solution Template

### Java


### Python


### C++


### JavaScript

