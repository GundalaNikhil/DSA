---
problem_id: MTH_CONTENT_FILTER_SYSTEM__3485
display_id: NTB-MTH-3485
slug: content-filter-system
title: "Content Filter System"
difficulty: Medium
difficulty_score: 50
topics:
  - Math Advanced
tags:
  - advanced-math
  - algorithms
  - coding-interviews
  - content-filter-system
  - cryptography
  - data-structures
  - mathadvanced
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Content Filter System

## Problem Statement

A content moderation system filters out content IDs that are divisible by any of `k` blacklisted prime numbers. Given a range of IDs `[1, N]`, count how many IDs are "safe" (not divisible by any of the blacklisted primes).

## Input Format

- First line: integer `q`.
- For each query:
  - First line: `N` and `k`.
  - Second line: `k` distinct primes `p1, p2, ..., pk`.

## Output Format

- One integer per query (count of safe IDs).

## Constraints

- `1 <= q <= 10^3`.
- `1 <= N <= 10^{18}`.
- `1 <= k <= 20`.
- `2 <= pi <= 10^9`.

## Clarifying Notes

- An ID `x` is safe if `x % pi != 0` for all `i`.
- Watch for overflow when computing products of multiple primes.

## Example Input

```
2
10 2
2 5
20 3
2 3 5
```

## Example Output

```
4
6
```
