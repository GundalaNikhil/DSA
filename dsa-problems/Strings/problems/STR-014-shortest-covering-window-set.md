---
problem_id: STR_SHORTEST_COVERING_WINDOW_SET__1014
display_id: STR-014
slug: shortest-covering-window-set
title: "Shortest Covering Window for Set"
difficulty: Medium
difficulty_score: 41
topics:
  - String Array
  - Sliding Window
  - Hashing
tags:
  - substring-search
  - coverage
  - two-pointers
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-014: Shortest Covering Window for Set

## Problem Statement

Given an array of strings `arr` and a set of required strings `T`, find the shortest contiguous subarray whose elements cover all strings in `T`. Return the length and one such window.

## Input Format

- First line: Integer `n` (size of arr)
- Next n lines: One string per line (elements of arr)
- Next line: Integer `m` (size of set T)
- Next m lines: One string per line (elements of T)

## Output Format

- First line: Integer representing window length
- Following lines: Strings in the shortest window

## Constraints

- `1 ≤ |arr| ≤ 10^5`
- `|T| ≤ 10^3`

## Example 1

**Input:**

```
6
db
aa
cc
db
aa
cc
2
aa
cc
```

**Output:**

```
2
aa
cc
```

**Explanation:**

- Window [1:3] = ["aa","cc"] covers all required strings
- Length 2 is minimal

## Notes

- Sliding window with frequency tracking
- Expand until all covered, then contract
- O(n) time complexity
