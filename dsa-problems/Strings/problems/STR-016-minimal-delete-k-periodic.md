---
problem_id: STR_MINIMAL_DELETE_K_PERIODIC__1016
display_id: STR-016
slug: minimal-delete-k-periodic
title: "Minimal Delete to Make K-Periodic"
difficulty: Medium
difficulty_score: 39
topics:
  - String Manipulation
  - Greedy
  - Frequency Analysis
tags:
  - periodicity
  - deletion
  - position-class
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# STR-016: Minimal Delete to Make K-Periodic

## Problem Statement

Given a string `s` and an integer `k`, delete the minimum number of characters so that the resulting string is periodic with period exactly `k` (can be written as repetitions of a k-length block).

## Input Format

- First line: String `s` (1 ≤ |s| ≤ 10^5)
- Second line: Integer `k` (1 ≤ k ≤ |s|)

## Output Format

- A single integer representing minimum deletions

## Constraints

- `1 ≤ |s| ≤ 10^5`
- `1 ≤ k ≤ |s|`
- `s` contains only lowercase English letters

## Example 1

**Input:**

```
abac
2
```

**Output:**

```
1
```

**Explanation:**

- Position 0 (mod 2): 'a','a' → keep 'a'
- Position 1 (mod 2): 'b','c' → keep 'b' (or 'c')
- Delete 'c' → 1 deletion
- Pattern: "ab" repeated

## Example 2

**Input:**

```
aabbcc
3
```

**Output:**

```
3
```

**Explanation:**

- For each position mod 3, keep most frequent character
- Total deletions needed: 3

## Notes

- Group positions by i mod k
- Keep most frequent char at each position class
- O(n) greedy algorithm
