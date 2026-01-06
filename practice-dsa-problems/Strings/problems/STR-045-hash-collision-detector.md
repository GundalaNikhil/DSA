---
problem_id: STR_HASH_COLLISION_DETECTOR__4214
display_id: NTB-STR-4214
slug: hash-collision-detector
title: "Hash Collision Detector"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - hash-collision-detector
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Hash Collision Detector

## Problem Statement

You are given a string `s` and `q` substring comparison queries. Use **double hashing** with the following fixed constants:

- `mod1 = 1000000007`
- `mod2 = 1000000009`
- `base = 911382323`

A query provides ranges `[l1, r1]` and `[l2, r2]`. If both hash values match but the substrings differ, count it as a hash collision.

Your task is to report the total number of collisions across all queries.

## Input Format

- First line: string `s`
- Second line: integer `q`
- Next `q` lines: integers `l1 r1 l2 r2`

## Output Format

- Single integer: total number of collisions

## Constraints

- `1 <= |s| <= 200000`
- `1 <= q <= 200000`
- `1 <= l1 <= r1 <= |s|`
- `1 <= l2 <= r2 <= |s|`
- `s` contains only lowercase English letters

## Clarifying Notes

- If the substrings are exactly equal, it is not a collision.
- All comparisons are case-sensitive.

## Example Input

```
ababab
3
1 3 2 4
1 2 3 4
1 4 3 6
```

## Example Output

```
0
```
