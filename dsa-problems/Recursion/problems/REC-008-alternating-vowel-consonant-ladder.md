---
problem_id: REC_ALTERNATING_VOWEL_CONSONANT_LADDER__6073
display_id: REC-008
slug: alternating-vowel-consonant-ladder
title: "Alternating Vowel-Consonant Ladder"
difficulty: Medium
difficulty_score: 54
topics:
  - Recursion
  - Backtracking
  - Graphs
tags:
  - recursion
  - word-ladder
  - bfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-008: Alternating Vowel-Consonant Ladder

## Problem Statement

Given a start word, an end word, and a dictionary, find all shortest transformation sequences where each step changes exactly one letter and remains in the dictionary.

Additionally, the first letter of successive words must alternate between vowel-start and consonant-start. Return all shortest valid ladders.

![Problem Illustration](../images/REC-008/problem-illustration.png)

## Input Format

- First line: start word
- Second line: end word
- Third line: integer `m` (dictionary size)
- Next `m` lines: dictionary words

## Output Format

- Each shortest ladder on its own line (words space-separated)
- Output `NONE` if no ladder exists

## Constraints

- `1 <= |word| <= 6`
- `1 <= m <= 3000`
- All words are lowercase and of equal length

## Example

**Input:**

```
eat
cot
4
eat
cat
cot
eot
```

**Output:**

```
eat cat cot
eat eot cot
```

**Explanation:**

Both sequences have length 3 and alternate vowel-start/consonant-start at each step.

![Example Visualization](../images/REC-008/example-1.png)

## Notes

- Use BFS to find the shortest distance levels
- Use backtracking to enumerate all shortest paths
- The start and end words may appear in the dictionary
- Treat vowels as `a, e, i, o, u`

## Related Topics

BFS, Backtracking, Word Ladder

---

## Solution Template
### Java


### Python


### C++


### JavaScript

