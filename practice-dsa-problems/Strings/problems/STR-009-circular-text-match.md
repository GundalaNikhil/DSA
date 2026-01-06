---
problem_id: STR_CIRCULAR_TEXT_MATCH__7892
display_id: NTB-STR-7892
slug: circular-text-match
title: "Circular Text Match"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - circular-text-match
  - coding-interviews
  - data-structures
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Circular Text Match

## Problem Statement

Given two strings `s1` and `s2`, determine if `s2` can be obtained by rotating `s1` left by some number of positions (possibly zero). Output `true` if yes, otherwise `false`.

## Input Format

- First line: string `s1`
- Second line: string `s2`

## Output Format

- `true` or `false`

## Constraints

- `1 <= |s1|, |s2| <= 200000`
- Strings contain printable ASCII characters

## Clarifying Notes

- If lengths differ, the answer is `false`.

## Example Input

```
abcde
cdeab
```

## Example Output

```
true
```
