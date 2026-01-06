---
problem_id: STR_WEIGHTED_CHARACTER_MAPPING__1527
display_id: NTB-STR-1527
slug: weighted-character-mapping
title: "Weighted Character Mapping"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
  - weighted-character-mapping
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Weighted Character Mapping

## Problem Statement

Given two strings `s` and `t` of equal length and a weight for each lowercase letter, determine if there exists a one-to-one mapping `f` from characters in `s` to characters in `t` such that:

- For all positions `i`, `f(s_i) = t_i`.
- If `f(c) = d`, then `weight[c] = weight[d]`.

Output `true` if such a mapping exists, otherwise `false`.

## Input Format

- First line: string `s`
- Second line: string `t`
- Third line: 26 integers: weights for `a` to `z`

## Output Format

- `true` or `false`

## Constraints

- `1 <= |s| == |t| <= 200000`
- `0 <= weight[c] <= 10^9`
- Strings contain only lowercase English letters

## Clarifying Notes

- The mapping must be injective (no two characters in `s` map to the same character in `t`).

## Example Input

```
egg
add
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
```

## Example Output

```
true
```
