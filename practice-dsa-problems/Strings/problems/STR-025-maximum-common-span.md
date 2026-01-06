---
problem_id: STR_MAXIMUM_COMMON_SPAN__8165
display_id: NTB-STR-8165
slug: maximum-common-span
title: "Maximum Common Span"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - maximum-common-span
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Maximum Common Span

## Problem Statement

Given two strings `s1` and `s2`, find the longest common contiguous substring. If multiple substrings tie for maximum length, choose the one with the smallest starting index in `s1`. If still tied, choose the one with the smallest starting index in `s2`.

## Input Format

- First line: string `s1`
- Second line: string `s2`

## Output Format

- The chosen substring (possibly empty)

## Constraints

- `1 <= |s1|, |s2| <= 200000`
- Strings contain only lowercase English letters

## Clarifying Notes

- If there is no common substring, output an empty line.

## Example Input

```
abcdef
xbcdy
```

## Example Output

```
bcd
```
