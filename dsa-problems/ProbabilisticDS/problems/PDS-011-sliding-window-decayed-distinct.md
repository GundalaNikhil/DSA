---
problem_id: PDS_SLIDING_WINDOW_DECAYED_DISTINCT__5072
display_id: PDS-011
slug: sliding-window-decayed-distinct
title: "Sliding Window Distinct with Exponential Decay"
difficulty: Medium
difficulty_score: 56
topics:
  - Probabilistic Data Structures
  - Sliding Window
  - Decay
tags:
  - probabilistic-ds
  - sliding-window
  - decay
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PDS-011: Sliding Window Distinct with Exponential Decay

## Problem Statement

Estimate a decayed distinct count using the last-seen time of each distinct item. Given current time `T`, decay factor `lambda`, and last-seen timestamps `t_i`, compute:

```
Estimate = sum exp(-lambda * (T - t_i))
```

![Problem Illustration](../images/PDS-011/problem-illustration.png)

## Input Format

- First line: integer `T`, real `lambda`, and integer `m`
- Second line: `m` integers (last-seen times)

## Output Format

- Single floating-point number: decayed distinct estimate

## Constraints

- `0 <= T <= 10^9`
- `0 < lambda <= 1`
- `1 <= m <= 100000`
- `0 <= t_i <= T`

## Example

**Input:**

```
10 0.1 3
10 8 5
```

**Output:**

```
2.425261
```

**Explanation:**

exp(0) + exp(-0.2) + exp(-0.5) = 2.425261.

![Example Visualization](../images/PDS-011/example-1.png)

## Notes

- Use double precision
- Accept answers with absolute error <= 1e-6
- Time complexity: O(m)

## Related Topics

Exponential Decay, Sliding Window, Distinct Counting

---

## Solution Template

### Java


### Python


### C++


### JavaScript

