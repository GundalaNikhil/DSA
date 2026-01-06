---
problem_id: STR_UNIFORM_STRING_BUILDER__2349
display_id: NTB-STR-2349
slug: uniform-string-builder
title: "Uniform String Builder"
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
  - uniform-string-builder
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Uniform String Builder

## Problem Statement

Given a string `s` and an integer `K`, find the length of the longest substring that can be converted into a string of identical characters by replacing at most `K` characters.

## Input Format

- First line: string `s`
- Second line: integer `K`

## Output Format

- Single integer: the maximum achievable length

## Constraints

- `1 <= |s| <= 200000`
- `0 <= K <= |s|`
- `s` contains only uppercase English letters

## Clarifying Notes

- Replacements can change a character into any other uppercase letter.

## Example Input

```
AABABBA
1
```

## Example Output

```
4
```
