---
problem_id: STR_MAXIMUM_UNIQUE_PARTITIONING__4090
display_id: NTB-STR-4090
slug: maximum-unique-partitioning
title: "Maximum Unique Partitioning"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - maximum-unique-partitioning
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Maximum Unique Partitioning

## Problem Statement

Given a string `s`, split it into the maximum number of contiguous substrings such that all substrings are distinct. You must output one optimal partition.

## Input Format

- Single line: string `s`

## Output Format

- First line: integer `k`, the maximum number of substrings
- Second line: the `k` substrings separated by spaces

## Constraints

- `1 <= |s| <= 30`
- `s` contains only lowercase English letters

## Clarifying Notes

- If multiple optimal partitions exist, output any one.

## Example Input

```
ababccc
```

## Example Output

```
5
a b ab c cc
```
