---
problem_id: MTH_PRIME_PRODUCTION_THRESHOLD__2307
display_id: NTB-MTH-2307
slug: prime-production-threshold
title: "Prime Production Threshold"
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
  - mathadvanced
  - prime-production-threshold
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Prime Production Threshold

## Problem Statement

Find the smallest `t >= 1` such that `N` divides `t!`.

If `t` exceeds `10^7`, output `-1`.

## Input Format

- First line: integer `q`.
- Next `q` lines: integer `N`.

## Output Format

- Smallest `t` or `-1` for each query.

## Constraints

- `1 <= q <= 2 * 10^5`.
- `1 <= N <= 10^{12}`.
- Search bound: `t <= 10^7`.

## Example Input

```
3
12
64
99991
```

## Example Output

```
4
8
99991
```
