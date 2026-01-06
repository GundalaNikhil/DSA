---
problem_id: MTH_WAREHOUSE_PACKAGE_DISTRIBUTION__2534
display_id: NTB-MTH-2534
slug: warehouse-package-distribution
title: "Warehouse Package Distribution"
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
  - technical-interview-prep
  - warehouse-package-distribution
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Warehouse Package Distribution

## Problem Statement

A warehouse processes packages at positions `0` to `n-1`. The processing cost for a package at position `i` is `floor((a * i + b) / m)` dollars.

Calculate the total processing cost for all `n` packages:

```
S = Σ (i=0 to n-1) floor((a * i + b) / m)
```

## Input Format

- First line: integer `q`.
- Next `q` lines: `n`, `a`, `b`, `m`.

## Output Format

- One integer per query (the total sum).

## Constraints

- `1 <= q <= 2 * 10^5`.
- `0 <= n, a, b <= 10^{18}`.
- `1 <= m <= 10^{18}`.

## Clarifying Notes

- If `n = 0`, the sum is 0.
- The result can exceed $2^{63}-1$, but it will fit in an unsigned 64-bit integer or equivalent BigInt representation.

## Example Input

```
2
5 3 1 4
3 10 0 6
```

## Example Output

```
7
5
```
