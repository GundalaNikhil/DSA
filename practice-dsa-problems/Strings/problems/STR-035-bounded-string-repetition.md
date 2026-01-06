---
problem_id: STR_BOUNDED_STRING_REPETITION__9233
display_id: NTB-STR-9233
slug: bounded-string-repetition
title: "Bounded String Repetition"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - bounded-string-repetition
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

# Bounded String Repetition

## Problem Statement

Given strings `A` and `B` and an integer `R`, find the minimum number of repetitions of `A` such that `B` becomes a substring of the repeated string. If the minimum number exceeds `R`, output `-1`.

## Input Format

- First line: string `A`
- Second line: string `B`
- Third line: integer `R`

## Output Format

- Single integer: minimum repetitions, or `-1`

## Constraints

- `1 <= |A|, |B| <= 200000`
- `1 <= R <= 10^6`
- Strings contain only lowercase English letters

## Clarifying Notes

- Repetitions are exact concatenations of `A`.

## Example Input

```
abc
cabcabca
4
```

## Example Output

```
3
```
