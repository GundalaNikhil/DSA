---
problem_id: MTH_EFFICIENT_COMBINATION_CALCULATOR__3897
display_id: NTB-MTH-3897
slug: efficient-combination-calculator
title: "Efficient Combination Calculator"
difficulty: Medium
difficulty_score: 50
topics:
  - Math Advanced
tags:
  - advanced-math
  - algorithms
  - coding-interviews
  - cryptography
  - data-structures
  - efficient-combination-calculator
  - mathadvanced
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Efficient Combination Calculator

## Problem Statement

Researchers query how many ways to select `k` genes from a group of `n` genes, where the results need to fit within their database's modular arithmetic system (modulo a prime `P`).

Calculate: `n! / k! (mod P)` for each query.

## Input Format

- First line: `P` (prime modulus) and `q` (number of queries).
- Next `q` lines: `n` and `k`.

## Output Format

- One integer per query (the result mod P).

## Constraints

- `P` is prime, `2 <= P <= 2 * 10^9`.
- `1 <= q <= 2 * 10^5`.
- `0 <= k <= n <= 10^7`.

## Clarifying Notes

- If `k = 0`, the result is `n!`.
- If `k = n`, the result is `1`.
- `0! = 1`.

## Example Input

```
1000000007 3
5 3
10 0
6 6
```

## Example Output

```
20
3628800
1
```
