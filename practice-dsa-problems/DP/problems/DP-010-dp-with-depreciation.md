---
problem_id: DP_DP_WITH_DEPRECIATION__6366
display_id: NTB-DP-6366
slug: dp-with-depreciation
title: "DP with Depreciation"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - dp-with-depreciation
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Depreciation

## Problem Statement

You have `n` days and a budget `B`. Each day `i` offers an asset with price `p_i` and initial value `v_i`. If bought on day `i`, its value on day `j >= i` becomes:

```
max(0, v_i - d * (j - i))
```

You may buy at most one asset per day and hold all purchases. Maximize total value at day `n` without exceeding budget `B`.

## Input Format

- First line: integers `n`, `B`, `d`
- Next `n` lines: `p_i v_i`

## Output Format

- Single integer: maximum total value at day `n`

## Constraints

- `1 <= n <= 200`
- `0 <= B <= 20000`
- `0 <= d <= 1000`
- `0 <= p_i, v_i <= 10^6`

## Clarifying Notes

- Budget is total spend across all days.

## Example Input

```
2 5 1
3 5
2 3
```

## Example Output

```
6
```
