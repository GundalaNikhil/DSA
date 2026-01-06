---
problem_id: ARR_FREQUENCY_DECAY_ARRAY__7031
display_id: NTB-ARR-7031
slug: frequency-decay-array
title: "Frequency Decay Array"
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
  - frequency-decay-array
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Frequency Decay Array

## Problem Statement

You are given an array of non-negative integers `a1..an`. Traverse the array from left to right. For each value `v`, let `k` be the number of times `v` has appeared so far (including the current position). The **decayed contribution** of this occurrence is:

```
contribution = floor(v * 90^(k-1) / 100^(k-1))
```

Let the transformed array be `b1..bn`, where `b_i` is the contribution of `a_i`. Find the maximum subarray sum of `b`.

## Input Format

- First line: integer `n`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- Single integer: maximum subarray sum of the transformed array

## Constraints

- `1 <= n <= 200000`
- `0 <= a_i <= 10^9`

## Clarifying Notes

- The decay is deterministic and applied globally as the array is scanned left to right.
- The maximum subarray must be non-empty.

## Example Input

```
4
10 10 10 1
```

## Example Output

```
28
```
