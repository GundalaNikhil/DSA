---
problem_id: REC_RECURSION_OVER_EVOLVING_GRAMMAR__9167
display_id: NTB-REC-9167
slug: recursion-over-evolving-grammar
title: "Recursion over Evolving Grammar"
difficulty: Medium
difficulty_score: 50
topics:
  - Recursion
tags:
  - algorithms
  - backtracking
  - coding-interviews
  - data-structures
  - recursion
  - recursion-over-evolving-grammar
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Recursion over Evolving Grammar

## Problem Statement

You are given a grammar with nonterminals `A..Z`. Each nonterminal has a list of production rules. The grammar evolves: every time a nonterminal `X` is expanded, it uses the next rule in its list (cyclically).

Starting from symbol `S`, expand until all symbols are terminals (lowercase letters). If the expansion length exceeds `Lmax`, stop and output `TOO_LONG`.

Output the final string.

## Input Format

- First line: character `S`
- Second line: integer `R` (number of nonterminals with rules)
- Next `R` blocks:
  - Line: character `X` and integer `k`
  - Next `k` lines: production strings for `X`
- Last line: integer `Lmax`

## Output Format

- The expanded string or `TOO_LONG`

## Constraints

- Total length of all productions <= 2000
- `1 <= Lmax <= 200000`

## Clarifying Notes

- Production strings contain only uppercase (nonterminals) and lowercase (terminals).
- Expansions are leftmost-first.

## Example Input

```
A
1
A 2
ab
A
10
```

## Example Output

```
abab
```
