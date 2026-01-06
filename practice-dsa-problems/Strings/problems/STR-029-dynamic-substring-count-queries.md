---
problem_id: STR_DYNAMIC_SUBSTRING_COUNT_QUERIES__4248
display_id: NTB-STR-4248
slug: dynamic-substring-count-queries
title: "Dynamic Substring Count Queries"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dynamic-substring-count-queries
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Dynamic Substring Count Queries

## Problem Statement

You are given a string `s` and must process `q` operations:

- `UPDATE i c`: set `s[i] = c`
- `QUERY l r`: output the number of distinct substrings of `s[l..r]`

Indices are 1-based.

## Input Format

- First line: string `s`
- Second line: integer `q`
- Next `q` lines: operations as described

## Output Format

- For each `QUERY`, output the number of distinct substrings

## Constraints

- `1 <= |s| <= 200000`
- `1 <= q <= 200000`
- `s` contains only lowercase English letters

## Clarifying Notes

- Substrings are contiguous and non-empty.
- Use 64-bit integers for counts.

## Example Input

```
aba
3
QUERY 1 3
UPDATE 2 c
QUERY 1 3
```

## Example Output

```
5
6
```
