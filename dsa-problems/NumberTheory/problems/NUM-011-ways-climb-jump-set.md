---
problem_id: NUM_WAYS_CLIMB_JUMP_SET__7681
display_id: NUM-011
slug: ways-climb-jump-set
title: "Ways to Climb With Jumps Set"
difficulty: Medium
difficulty_score: 48
topics:
  - Number Theory
  - Dynamic Programming
  - Combinatorics
tags:
  - number-theory
  - dp
  - combinatorics
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# NUM-011: Ways to Climb With Jumps Set

## Problem Statement

You are climbing `n` stairs. You may take jumps only from a given set `J`. Count the number of distinct ways to reach exactly stair `n`, modulo `1000000007`.

![Problem Illustration](../images/NUM-011/problem-illustration.png)

## Input Format

- First line: integers `n` and `m` (size of set J)
- Second line: `m` integers (the jump sizes)

## Output Format

- Single integer: number of ways modulo `1000000007`

## Constraints

- `1 <= n <= 100000`
- `1 <= m <= 20`
- `1 <= J[i] <= 100000`

## Example

**Input:**

```
4 2
1 3
```

**Output:**

```
3
```

**Explanation:**

Ways: 1+1+1+1, 1+3, 3+1.

![Example Visualization](../images/NUM-011/example-1.png)

## Notes

- DP: dp[i] = sum(dp[i-j]) for j in J and i >= j
- Base: dp[0] = 1
- Time complexity: O(n * m)
- Space complexity: O(n)

## Related Topics

Dynamic Programming, Modular Counting

---

## Solution Template

### Java


### Python


### C++


### JavaScript

