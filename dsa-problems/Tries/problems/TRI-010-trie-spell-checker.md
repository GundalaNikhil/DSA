---
problem_id: TRI_SPELL_CHECKER__8124
display_id: TRI-010
slug: trie-spell-checker
title: "Trie-Based Spell Checker"
difficulty: Medium
difficulty_score: 56
topics:
  - Trie
  - String
  - Edit Distance
  - Dynamic Programming
tags:
  - trie
  - spell-check
  - edit-distance
  - string-matching
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-010: Trie-Based Spell Checker

## Problem Statement

Given a dictionary of words in a trie, for each query word, return `true` if there exists a dictionary word at edit distance exactly 1 from the query. Edit distance 1 means one character insertion, deletion, or substitution.

![Problem Illustration](../images/TRI-010/problem-illustration.png)

## Input Format

- First line: integer `n` (number of dictionary words)
- Next `n` lines: lowercase dictionary words
- Last line: query word (lowercase)

## Output Format

Return `true` if any dictionary word is at edit distance 1 from query, `false` otherwise.

## Constraints

- `1 <= n <= 10^5` (dictionary size)
- `1 <= queries <= 10^5`
- `1 <= |word| <= 25` (word length)
- All words are lowercase English letters

## Example 1

**Input:**

```
2
cat
bat
cats
```

**Output:**

```
true
```

**Explanation:**

Query "cats" is edit distance 1 from "cat" (insert 's').

## Example 2

**Input:**

```
3
hello
world
help
hero
```

**Output:**

```
true
```

**Explanation:**

Query "car" is not in the dictionary {"cat", "bat"}. Check edit distance 1:

**Input:**

```
2
cat
bat
car
```

**Output:**

```
true
```

**Explanation:**

Query "car" is edit distance 1 from "cat" (substitute 't' with 'r').

## Notes

- Edit operations: insert one char, delete one char, or replace one char
- Must be exactly edit distance 1 (not 0, not 2+)
- Use trie structure to efficiently explore edit possibilities

## Related Topics

Trie, String, Edit Distance, Dynamic Programming, Spell Checking

---

## Solution Template

### Java


### Python


### C++


### JavaScript

