---
problem_id: DP_CLIMB_CRACKED_MAXJ__7314
display_id: DP-001
slug: staircase-cracked-steps-maxjump
title: "Staircase With Cracked Steps and Max Jump"
difficulty: Medium
difficulty_score: 52
topics:
  - Dynamic Programming
  - Sliding Window
  - Counting
tags:
  - dp
  - dynamic-programming
  - sliding-window
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-001: Staircase With Cracked Steps and Max Jump

## Problem Statement

You are climbing a staircase with `n` steps (numbered `1` to `n`). You start at step `0` (ground) and want to reach step `n`.

From any step `i`, you may jump to `i+1`, `i+2`, ..., `i+J` (as long as you do not go past `n`).

Some steps are **cracked** and you **cannot land** on them (but you may jump over them).

Your task is to count the number of distinct ways to reach step `n`, modulo `1_000_000_007`.

![Problem Illustration](../images/DP-001/problem-illustration.png)

## Input Format

- First line: two integers `n` and `J`
- Second line: integer `m` = number of cracked steps
- Third line: `m` space-separated integers denoting cracked step indices

## Output Format

Print one integer: the number of ways to reach step `n` modulo `1_000_000_007`.

## Constraints

- `1 <= n <= 100000`
- `1 <= J <= 50`
- `0 <= m <= 100000`
- Cracked indices are in range `1..n` (if `n` is cracked, answer is `0`)

## Example

**Input:**
```
4 3
1
2
```

**Output:**
```
3
```

**Explanation:**

Cracked step: `{2}` (cannot land on step 2).

Valid paths from step 0 to step 4 using jumps up to 3:

- `0 -> 1 -> 3 -> 4`
- `0 -> 1 -> 4`
- `0 -> 3 -> 4`

So the answer is `3`.

![Example Visualization](../images/DP-001/example-1.png)

## Notes

- You may jump **over** cracked steps; you just cannot land on them.
- Use modulo `1_000_000_007` because the number of ways grows very fast.
- If step `n` is cracked, the answer is `0` because you cannot land on the destination.

## Related Topics

Dynamic Programming, Sliding Window, Counting

---

## Solution Template

### Java


### Python


### C++


### JavaScript


