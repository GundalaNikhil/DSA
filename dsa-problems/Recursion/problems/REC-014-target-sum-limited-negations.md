---
problem_id: REC_TARGET_SUM_LIMITED_NEGATIONS__8206
display_id: REC-014
slug: target-sum-limited-negations
title: "Target Sum With Limited Negations"
difficulty: Medium
difficulty_score: 49
topics:
  - Recursion
  - Backtracking
  - DP
tags:
  - recursion
  - target-sum
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# REC-014: Target Sum With Limited Negations

## Problem Statement

Given an array `nums`, assign each number either `+` or `-` so that the total equals `target`. You may negate at most `K` numbers.

Return the number of valid sign assignments.

![Problem Illustration](../images/REC-014/problem-illustration.png)

## Input Format

- First line: integers `n`, `K`, and `target`
- Second line: `n` space-separated integers `nums[i]`

## Output Format

- Single integer: number of valid assignments

## Constraints

- `1 <= n <= 20`
- `0 <= K <= n`
- `|nums[i]| <= 20`
- `|target| <= 10^9`

## Example

**Input:**

```
3 1 2
1 2 3
```

**Output:**

```
2
```

**Explanation:**

Valid assignments include `+1 +2 -3` and `-1 +2 +3`.

![Example Visualization](../images/REC-014/example-1.png)

## Notes

- Track position, current sum, and negations used
- Use recursion with pruning or memoization
- The search space is size `2^n`
- Count all assignments that meet constraints

## Related Topics

Backtracking, Target Sum, Recursion

---

## Solution Template
### Java


### Python


### C++


### JavaScript

