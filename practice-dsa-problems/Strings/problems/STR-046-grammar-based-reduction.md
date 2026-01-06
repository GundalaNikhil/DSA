---
problem_id: STR_GRAMMAR_BASED_REDUCTION__5482
display_id: NTB-STR-5482
slug: grammar-based-reduction
title: "Grammar-Based Reduction"
difficulty: Medium
difficulty_score: 50
topics:
  - Strings
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - grammar-based-reduction
  - pattern-matching
  - string-manipulation
  - strings
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Grammar-Based Reduction

## Problem Statement

You are given a string `s` of uppercase letters and a set of reduction rules. Each rule replaces an adjacent pair of symbols with a single symbol:

```
XY -> Z
```

Each replacement counts as one operation and reduces the string length by 1. Given a target symbol `T`, find the minimum number of operations required to reduce the string to exactly `T`. If it is impossible, output `-1`.

## Input Format

- First line: string `s`
- Second line: integer `m` (number of rules)
- Next `m` lines: rules in the form `XY Z`
- Last line: target symbol `T`

## Output Format

- Single integer: minimum operations, or `-1`

## Constraints

- `1 <= |s| <= 200`
- `1 <= m <= 2000`
- `s`, `X`, `Y`, `Z`, and `T` are uppercase English letters

## Clarifying Notes

- Rules can be reused multiple times.
- Use 64-bit integers for safety.

## Example Input

```
ABCD
3
AB X
XC Y
YD Z
Z
```

## Example Output

```
3
```
