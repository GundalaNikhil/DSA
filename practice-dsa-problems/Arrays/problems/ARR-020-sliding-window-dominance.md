---
problem_id: ARR_SLIDING_WINDOW_DOMINANCE__7376
display_id: NTB-ARR-7376
slug: sliding-window-dominance
title: "Sliding Window Dominance"
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
  - searching
  - sliding-window-dominance
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Sliding Window Dominance

## Problem Statement

Given an array `a1..an` and a window size `W`, for each window of length `W` output the element that appears more than `W/2` times in that window. If no such element exists, output `-1` for that window.

## Input Format

- First line: integers `n` and `W`
- Second line: `n` integers `a1 a2 ... an`

## Output Format

- `n - W + 1` integers separated by spaces: the dominant element of each window, or `-1`

## Constraints

- `1 <= n <= 200000`
- `1 <= W <= n`
- `-10^9 <= a_i <= 10^9`

## Clarifying Notes

- There can be at most one dominant element in a window.
- Windows are evaluated from left to right.

## Example Input

```
5 3
1 2 2 2 3
```

## Example Output

```
2 2 2
```
