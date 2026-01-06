---
problem_id: ARR_ARRAY_COMPRESSION_ERROR_TOLERANCE__4723
display_id: NTB-ARR-4723
slug: array-compression-error-tolerance
title: "Array Compression with Error Tolerance"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-compression-error-tolerance
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

# Array Compression with Error Tolerance

## Problem Statement

You are given an array `a1..an` and an integer tolerance `E`. You may partition the array into contiguous segments. Each segment is replaced by a single value equal to the **floor of its average**.

A segment `[l..r]` is valid if for every `i` in `[l..r]`:

```
|a_i - floor(avg(l..r))| <= E
```

Your task is to minimize the number of segments. Output the minimum number of segments and one valid segmentation by segment lengths.

## Input Format

- First line: integers `n` and `E`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- First line: integer `s`, the minimum number of segments
- Second line: `s` integers: the lengths of each segment in order

## Constraints

- `1 <= n <= 200000`
- `0 <= E <= 10^9`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- A segment of length 1 is always valid.
- If multiple optimal segmentations exist, output any one.

## Example Input

```
5 1
2 3 4 10 11
```

## Example Output

```
2
3 2
```
