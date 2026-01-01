---
problem_id: TRI_MINIMUM_UNIQUE_PREFIX__1847
display_id: TRI-007
slug: minimum-unique-prefix-lengths
title: "Minimum Unique Prefix Lengths"
difficulty: Medium
difficulty_score: 50
topics:
  - Trie
  - String
  - Hash Table
tags:
  - trie
  - prefix
  - string-matching
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-007: Minimum Unique Prefix Lengths

## Problem Statement

Given an array of lowercase words, for each word, find the minimum prefix length that makes it unique among all words in the array.

![Problem Illustration](../images/TRI-007/problem-illustration.png)

## Input Format

- First line: integer `n` (number of words)
- Next `n` lines: each contains a single lowercase word

## Output Format

Return an array of integers where the i-th integer represents the minimum prefix length for the i-th word.

Format: `[length1,length2,...]`

## Constraints

- `1 <= n <= 10^5` (number of words)
- Total character length across all words <= `2 × 10^5`
- All words consist of lowercase English letters (a-z)
- No two words are identical

## Example 1

**Input:**

```
4
zebra
dog
duck
dove
```

**Output:**

```
[1,2,2,2]
```

**Explanation:**

- "zebra": First character 'z' is unique among all first characters → prefix length = 1
- "dog": Shares 'd' with duck/dove, shares "do" with dove → at position 2, differs from "duck" → prefix length = 2
- "duck": Shares 'd' with dog/dove, but "du" is unique → prefix length = 2
- "dove": Shares 'd' with dog/duck, shares "do" with dog, but at position 2 has 'v' vs 'g'/'u' → prefix length = 2

Note: The minimum prefix is the earliest position where the count of words sharing that prefix becomes 1 for this word's path.

![Example Visualization](../images/TRI-007/example-1.png)

## Example 2

**Input:**

```
3
apple
application
app
```

**Output:**

```
[5,5,3]
```

**Explanation:**

- "apple": Shares "app" with others, shares "appl" with "application" → needs "apple" (5 chars)
- "application": Shares "app" with others, shares "appl" with "apple" → needs "appli" (5 chars)
- "app": Shortest word, but shares with others → needs full length (3 chars)

![Example Visualization](../images/TRI-007/example-2.png)

## Notes

- The minimum prefix length is determined by the trie structure
- If a word is a prefix of another word, it needs its full length
- Use a trie with node counts to efficiently compute minimum prefixes

## Related Topics

Trie, String, Prefix Matching, Hash Table

---

## Solution Template

### Java


### Python


### C++


### JavaScript

