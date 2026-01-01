---
problem_id: TRI_KTH_MISSING__4257
display_id: TRI-006
slug: kth-string-not-present
title: "Lexicographic k-th String Not Present"
difficulty: Medium
difficulty_score: 50
topics:
  - Trie
  - String
  - Combinatorics
  - DFS
tags:
  - trie
  - string
  - combinatorics
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Lexicographic k-th String Not Present

## Problem Statement

Given a trie of inserted lowercase strings, find the k-th lexicographically smallest string of length up to `L` that is NOT present in the trie.

![Problem Illustration](../images/TRI-006/problem-illustration.png)

## Input Format

- First line: Three integers `n`, `L`, `k` (number of strings, max length, kth position)
- Next `n` lines: Each contains a lowercase string already inserted in the trie

## Output Format

Print the k-th missing string of length ≤ L in lexicographic order, or an empty string if k exceeds the total missing count.

## Constraints

- 0 ≤ n ≤ 10^5
- 1 ≤ L ≤ 6
- 1 ≤ k ≤ 10^9
- All strings consist of lowercase English letters (a-z)

## Examples

### Example 1

**Input:**

```
2 2 1
a
b
```

**Output:**

```
aa
```

**Explanation:**

Inserted: "a", "b"
Missing strings of length ≤ 2 in order:

1. "aa" ← answer
2. "ab"
3. "ac"
   ...

![Example 1 Visualization](../images/TRI-006/example-1.png)

## Notes

- Strings can end at any depth from 1 to L
- Empty string not counted
- Lexicographic order: a < aa < ab < ... < z < za < ...
- Use DFS to count missing strings efficiently

## Related Topics

Trie, String, Combinatorics, DFS, Missing Elements

---

## Solution Template

### Java


### Python


### C++


### JavaScript

