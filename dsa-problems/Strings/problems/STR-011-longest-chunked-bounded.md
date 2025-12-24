---
problem_id: STR_LONGEST_CHUNKED_BOUNDED__1011
display_id: STR-011
slug: longest-chunked-bounded
title: "Longest Chunked Decomposition (Bounded)"
difficulty: Medium
difficulty_score: 44
topics:
  - String Manipulation
  - Two Pointers
  - Greedy
tags:
  - palindrome-decomposition
  - chunk-matching
  - symmetric-structure
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-011: Longest Chunked Decomposition (Bounded)

## Problem Statement

Split a string `s` into the maximum number of chunks where the i-th chunk from the start equals the i-th chunk from the end. All chunks must have length ≤ `L`.

## Input Format

- First line: String `s` (1 ≤ |s| ≤ 10^5)
- Second line: Integer `L` (1 ≤ L ≤ |s|)

## Output Format

- A single integer representing the maximum number of chunks

## Constraints

- `1 ≤ |s| ≤ 10^5`
- `1 ≤ L ≤ |s|`
- `s` contains only lowercase English letters

## Example 1

**Input:**

```
abcabc
3
```

**Output:**

```
2
```

**Explanation:**

- Match "abc" from both ends → 2 chunks
- Middle is empty

## Example 2

**Input:**

```
abacaba
3
```

**Output:**

```
5
```

**Explanation:**

- Match "a" from both ends → 2 chunks
- Match "b" from both ends → 2 chunks
- Middle "aca" → 1 chunk
- Total: 5 chunks

## Notes

- Greedy two-pointer matching
- Match smallest valid chunks first
- O(n × L) time complexity
