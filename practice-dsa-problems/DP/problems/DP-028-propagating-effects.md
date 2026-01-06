---
problem_id: DP_PROPAGATING_EFFECTS__5041
display_id: NTB-DP-5041
slug: propagating-effects
title: "DP with Propagating Effects"
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
  - optimization
  - propagating-effects
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Propagating Effects

## Problem Statement

You have `n` steps and `a` actions. Action `i` yields immediate reward `r_i` and creates a propagating effect of strength `e_i` that lasts `d_i` steps. On each future step while active, the effect adds `e_i` to the reward of whatever action you take. Multiple effects add together.

Maximize total reward after `n` steps.

## Input Format

- First line: integers `n` and `a`
- Next `a` lines: `r_i e_i d_i`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 30`
- `1 <= a <= 6`
- `0 <= r_i, e_i <= 50`
- `0 <= d_i <= 5`

## Clarifying Notes

- Effects apply starting from the next step.
- State tracks the multiset of active effect timers.

## Example Input

```
3 2
5 2 1
3 1 2
```

## Example Output

```
13
```

## Solution Stub

### Java

```java
class Solution {
    public long maxReward(int n, int a, int[][] actions) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, a: int, actions: list[list[int]]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxReward(int n, int a, vector<vector<int>>& actions) {
        // Implement here
        return 0;
    }
};
```

### JavaScript

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} a
   * @param {number[][]} actions
   * @return {number}
   */
  maxReward(n, a, actions) {
    // Implement here
    return 0;
  }
}
```
