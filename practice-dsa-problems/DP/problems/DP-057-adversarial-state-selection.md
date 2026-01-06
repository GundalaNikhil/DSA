---
problem_id: DP_ADVERSARIAL_STATE_SELECTION__1766
display_id: NTB-DP-1766
slug: adversarial-state-selection
title: "DP with Adversarial State Selection"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - adversarial-state-selection
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Adversarial State Selection

## Problem Statement

At each step you choose an action. The adversary then chooses the next state from a set of possible outcomes for that action. You receive the reward associated with the chosen transition. The adversary aims to minimize your total reward.

Compute the maximum reward you can guarantee after `n` steps starting from state 1.

## Input Format

- First line: integers `n`, `s`, `a`
- Next `a` blocks:
  - integer `k` (number of possible outcomes)
  - `k` lines: `from to reward`

## Output Format

- Single integer: maximum guaranteed reward

## Constraints

- `1 <= n <= 100`
- `1 <= s <= 50`
- Total transitions <= 2000

## Clarifying Notes

- This is a minimax DP: adversary picks the worst outcome for you.

## Example Input

```
2 2 1
2
1 1 3
1 2 1
```

## Example Output

```
2
```
