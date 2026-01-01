---
problem_id: TRI_WILDCARD_SEARCH__5672
display_id: TRI-009
slug: wildcard-search
title: "Wildcard Search"
difficulty: Medium
difficulty_score: 52
topics:
  - Trie
  - String
  - Recursion
  - Backtracking
tags:
  - trie
  - pattern-matching
  - wildcards
  - dfs
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-009: Wildcard Search

## Problem Statement

Implement search on a trie with wildcard pattern matching. The pattern may contain:

- `?` matches any single character
- `*` matches any sequence of characters (including empty)

Return `true` if any word in the trie matches the pattern.

![Problem Illustration](../images/TRI-009/problem-illustration.png)

## Input Format

- First line: integer `n` (number of words)
- Next `n` lines: lowercase words to insert into trie
- Last line: pattern string (may contain lowercase letters, `?`, and `*`)

## Output Format

Return `true` if any word matches the pattern, `false` otherwise.

## Constraints

- `1 <= n <= 10^5` (total words)
- `1 <= |word| <= 30` (word length)
- `1 <= |pattern| <= 30` (pattern length)
- Words contain only lowercase English letters
- Pattern contains lowercase letters, `?`, and `*`

## Example 1

**Input:**

```
3
code
coder
codec
co*e
```

**Output:**

```
true
```

**Explanation:**

Pattern `co*e`:

- `*` can match "d" → `code` matches ✓
- `*` can match "dec" → `codec` matches ✓

![Example Visualization](../images/TRI-009/example-1.png)

## Example 2

**Input:**

```
4
hello
help
helper
helpful
hel?
```

**Output:**

```
true
```

**Explanation:**

Pattern `hel?`:

- `?` matches 'l' → `hell` (not in trie) ✗
- `?` matches 'p' → `help` matches ✓

## Notes

- `?` matches exactly one character
- `*` matches zero or more characters
- Use DFS/backtracking to explore all possibilities
- Early termination when match is found

## Related Topics

Trie, String, Recursion, Backtracking, Pattern Matching

---

## Solution Template

### Java


### Python


### C++


### JavaScript

