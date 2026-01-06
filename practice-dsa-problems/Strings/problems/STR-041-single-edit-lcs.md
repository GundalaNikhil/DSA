---
problem_id: STR_SINGLE_EDIT_LCS__7729
display_id: NTB-STR-7729
slug: single-edit-lcs
title: "Single-Edit Longest Common Subsequence"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - pattern-matching
  - single-edit-lcs
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Single-Edit Longest Common Subsequence

## Problem Statement

Given two strings `A` and `B`, you may change **at most one** character in `A` to any other character for free. After this optional edit, compute the length of the longest common subsequence of `A` and `B`.

Output the maximum possible LCS length.

## Input Format

- First line: string `A`
- Second line: string `B`

## Output Format

- Single integer: maximum LCS length

## Constraints

- `1 <= |A|, |B| <= 2000`
- Strings contain only lowercase English letters

## Clarifying Notes

- The free edit can be skipped.

## Example Input

```
abcdef
azcdef
```

## Example Output

```
6
```
