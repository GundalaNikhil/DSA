---
problem_id: TRI_REPLACE_RARE__4255
display_id: TRI-004
slug: replace-words-shortest-rare-prefix
title: "Replace Words with Shortest Rare Prefix"
difficulty: Medium
difficulty_score: 50
topics:
  - Trie
  - String
  - Greedy
  - Dictionary
tags:
  - trie
  - string
  - greedy
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Replace Words with Shortest Rare Prefix

## Problem Statement

Given a dictionary of root words with rarity scores and a sentence, replace each word in the sentence with the prefix from the dictionary that:

1. Is a prefix of the word
2. Has the smallest rarity score
3. If multiple prefixes have the same rarity, choose the shortest one
4. If no prefix exists, keep the original word

![Problem Illustration](../images/TRI-004/problem-illustration.png)

## Input Format

- First line: Integer `n` (1 ≤ n ≤ 10^5) - number of dictionary roots
- Next `n` lines: Each contains a string `root` and integer `rarity` separated by space
- Last line: String `sentence` containing words separated by spaces

## Output Format

Print the modified sentence with words replaced according to the rules.

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ word length ≤ 30
- 1 ≤ rarity ≤ 10^9
- 1 ≤ sentence length ≤ 10^5

## Examples

### Example 1

**Input:**

```
2
cat 1
car 2
the cattle carried
```

**Output:**

```
the cat car
```

**Explanation:**

- "the" has no prefix match → remains "the"
- "cattle" has prefix "cat" (rarity 1) → becomes "cat"
- "carried" has prefix "car" (rarity 2) → becomes "car"

![Example 1 Visualization](../images/TRI-004/example-1.png)

### Example 2

**Input:**

```
3
a 3
aa 2
aaa 1
aaaa
```

**Output:**

```
aaa
```

**Explanation:**

Word "aaaa" has three prefix matches:

- "a" (rarity 3)
- "aa" (rarity 2)
- "aaa" (rarity 1) ← lowest rarity, chosen

## Notes

- Lower rarity score means more specialized/important
- Tie-break by shortest length if rarity is equal
- Words are separated by single spaces
- All words and roots consist of lowercase English letters only

## Related Topics

Trie, String, Greedy, Dictionary Lookup

---

## Solution Template

### Java


### Python


### C++


### JavaScript

