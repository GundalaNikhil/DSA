---
problem_id: PRB_EXPECTED_STEPS_RANDOM_WALK_1D__3079
display_id: PRB-002
slug: expected-steps-random-walk-1d
title: "Expected Steps Random Walk 1D"
difficulty: Medium
difficulty_score: 50
topics:
  - Probability
  - Random Walk
  - Linear Equations
tags:
  - probability
  - random-walk
  - dp
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# PRB-002: Expected Steps Random Walk 1D

## Problem Statement

A random walk starts at position 0 on the integer line. Each step moves +1 with probability `p`, and -1 with probability `1-p`. The walk stops when it reaches `+a` or `-b` (absorbing boundaries). Compute the expected number of steps until absorption.

![Problem Illustration](../images/PRB-002/problem-illustration.png)

## Input Format

- Single line: integers `a`, `b`, and real `p`

## Output Format

- Single floating-point number: expected steps

## Constraints

- `1 <= a, b <= 200`
- `0 < p < 1`

## Example

**Input:**

```
2 1 0.5
```

**Output:**

```
2
```

**Explanation:**

For a symmetric walk with boundaries at +2 and -1, the expected time to absorption from 0 is 2.

![Example Visualization](../images/PRB-002/example-1.png)

## Notes

- Use DP or solve linear equations for states in [-b+1, a-1]
- Accept answers with absolute error <= 1e-6
- Time complexity: O((a+b)^2) for equation solving

## Related Topics

Random Walk, Expected Value, Linear Systems

---

## Solution Template

### Java


### Python


### C++


### JavaScript

