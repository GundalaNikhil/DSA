---
problem_id: ARR_LONGEST_NONDECREASING_ONE_DROP__9964
display_id: NTB-ARR-9964
slug: longest-nondecreasing-one-drop
title: "Longest Non-Decreasing with One Drop"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - longest-nondecreasing-one-drop
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Longest Non-Decreasing with One Drop

## Problem Statement

Given an array `a1..an`, find the length of the longest contiguous subarray where the sequence is non-decreasing **except** that you may allow at most one drop. A drop is an index `i` such that `a_i > a_{i+1}`.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum length of a valid subarray

## Constraints

- `1 <= n <= 200000`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- A valid subarray may contain zero or one drop.
- Equal consecutive values do not count as drops.

## Example Input

```
6
1 2 5 3 4 6
```

## Example Output

```
6
```
