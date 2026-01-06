---
problem_id: ARR_ALTERNATING_PARITY_PREFIX__5892
display_id: NTB-ARR-5892
slug: alternating-parity-prefix
title: "Alternating Parity Prefix"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - alternating-parity-prefix
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Alternating Parity Prefix

## Problem Statement

Given an array `a1..an`, find the length of the longest prefix starting at index 1 such that the parity strictly alternates between even and odd.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: length of the longest alternating-parity prefix

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- Parity is determined by `a_i % 2`.
- A prefix of length 1 always qualifies.

## Example Input

```
5
4 7 2 9 12
```

## Example Output

```
5
```
