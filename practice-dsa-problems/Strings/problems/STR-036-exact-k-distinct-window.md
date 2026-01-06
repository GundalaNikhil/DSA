---
problem_id: STR_EXACT_K_DISTINCT_WINDOW__2213
display_id: NTB-STR-2213
slug: exact-k-distinct-window
title: "Exact K-Distinct Window"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - exact-k-distinct-window
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Exact K-Distinct Window

## Problem Statement

Given a string `s` and an integer `K`, count the number of substrings that contain exactly `K` distinct characters.

## Input Format

- First line: string `s`
- Second line: integer `K`

## Output Format

- Single integer: number of substrings

## Constraints

- `1 <= |s| <= 200000`
- `1 <= K <= 26`
- `s` contains only lowercase English letters

## Clarifying Notes

- Substrings are contiguous and non-empty.
- Use 64-bit integers for counts.

## Example Input

```
abcabc
2
```

## Example Output

```
8
```
