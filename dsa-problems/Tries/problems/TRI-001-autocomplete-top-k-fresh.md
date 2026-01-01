---
problem_id: TRI_AUTOCOMPLETE_DECAY__7294
display_id: TRI-001
slug: autocomplete-top-k-fresh
title: "Autocomplete Top-K with Freshness Decay"
difficulty: Medium
difficulty_score: 55
topics:
  - Trie
  - Priority Queue
  - Hash Table
  - Sorting
tags:
  - trie
  - heap
  - autocomplete
  - ranking
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# TRI-001: Autocomplete Top-K with Freshness Decay

## Problem Statement

Build a trie of lowercase words, each with a base frequency and last-used timestamp. Given the current time and a prefix, return the top `k` words ranked by a freshness decay score calculated as:

**score = frequency × exp(-(currentTime - lastUsed) / D)**

where `D` is a decay constant. If scores are equal, rank lexicographically.

![Problem Illustration](../images/TRI-001/problem-illustration.png)

## Input Format

- First line: integer `n` (number of words)
- Next `n` lines: each contains `word frequency timestamp`
  - `word`: lowercase string
  - `frequency`: integer representing base popularity
  - `timestamp`: integer representing last access time
- Next line: `prefix currentTime D k`
  - `prefix`: query prefix (lowercase)
  - `currentTime`: current timestamp
  - `D`: decay constant
  - `k`: number of results to return

## Output Format

Return a list of the top `k` words matching the prefix, sorted by:

1. Decayed score (descending)
2. Lexicographic order (ascending) for ties

Format: `["word1", "word2", ...]`

## Constraints

- `1 <= n <= 10^5` (total words)
- `1 <= |word| <= 30` (word length)
- `1 <= frequency <= 10^6`
- `0 <= timestamp, currentTime <= 10^9`
- `1 <= D <= 10^9` (decay constant)
- `1 <= k <= 10`
- All words are lowercase English letters

## Example

**Input:**

```
3
hello 5 0
helium 3 5
he 4 9
he 10 10 2
```

**Output:**

```
["he", "hello"]
```

**Explanation:**

Words with prefix "he": hello, helium, he

Calculate decayed scores at currentTime=10 with D=10:

- "hello": 5 × exp(-(10-0)/10) = 5 × exp(-1) ≈ 5 × 0.368 = 1.84
- "helium": 3 × exp(-(10-5)/10) = 3 × exp(-0.5) ≈ 3 × 0.606 = 1.82
- "he": 4 × exp(-(10-9)/10) = 4 × exp(-0.1) ≈ 4 × 0.905 = 3.62

Sorted by score (descending): "he" (3.62), "hello" (1.84), "helium" (1.82)

Top k=2 results: ["he", "hello"]

![Example Visualization](../images/TRI-001/example-1.png)

## Notes

- The exponential decay formula ensures recently used words rank higher
- Smaller `D` values create stronger recency bias
- If no words match the prefix, return an empty list
- Exact floating-point precision is not required; standard library `exp()` is sufficient

## Related Topics

Trie, Priority Queue, Hash Table, Sorting, Autocomplete Systems

---

## Solution Template

### Java


### Python


### C++


### JavaScript

