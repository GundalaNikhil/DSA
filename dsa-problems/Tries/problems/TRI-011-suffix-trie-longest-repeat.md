---
problem_id: TRI_SUFFIX_LONGEST_REPEAT__3945
display_id: TRI-011
slug: suffix-trie-longest-repeat
title: "Suffix Trie Longest Repeat"
difficulty: Medium
difficulty_score: 58
topics:
  - Trie
  - String
  - Suffix Structures
tags:
  - trie
  - suffix-trie
  - longest-repeat
  - string-algorithms
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-011: Suffix Trie Longest Repeat

## Problem Statement

Build a suffix trie (or use suffix array alternative) to find the length of the longest repeated substring in string `s`.

![Problem Illustration](../images/TRI-011/problem-illustration.png)

## Input Format

- Single line: string `s` (lowercase letters)

## Output Format

Return an integer representing the length of the longest repeated substring.

## Constraints

- `1 <= |s| <= 10^5`
- String contains only lowercase English letters

## Example

**Input:**

```
banana
```

**Output:**

```
3
```

**Explanation:**

"ana" appears twice (at positions 1-3 and 3-5), length = 3.

![Example Visualization](../images/TRI-011/example-1.png)

## Notes

- A repeated substring must appear at least twice
- Return 0 if no substring repeats
- Overlapping occurrences count (e.g., "ana" in "banana")

## Related Topics

Trie, Suffix Structures, String Algorithms

---

## Solution Template

### Java


### Python


### C++


### JavaScript

