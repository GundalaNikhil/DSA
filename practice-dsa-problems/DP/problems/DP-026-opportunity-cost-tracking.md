---
problem_id: DP_OPPORTUNITY_COST_TRACKING__1624
display_id: NTB-DP-1624
slug: opportunity-cost-tracking
title: "DP with Opportunity Cost Tracking"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - memoization
  - opportunity-cost-tracking
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Opportunity Cost Tracking

## Problem Statement

You have `n` steps and `a` actions with rewards `r_i`. At each step, choosing action `i` incurs opportunity cost equal to:

```
max_reward - r_i
```

where `max_reward` is the maximum reward among all actions for that step (constant across steps). The total opportunity cost must not exceed `B`.

Maximize total reward.

## Input Format

- First line: integers `n`, `a`, `B`
- Second line: `a` integers: rewards `r_1..r_a`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `1 <= a <= 50`
- `0 <= B <= 10^6`
- `-10^6 <= r_i <= 10^6`

## Clarifying Notes

- Opportunity cost uses the same `max_reward` for every step.

## Example Input

```
3 3 2
5 4 1
```

## Example Output

```
14
```
