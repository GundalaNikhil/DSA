---
problem_id: DP_CONDITIONAL_UNLOCKS__1809
display_id: NTB-DP-1809
slug: conditional-unlocks
title: "DP with Conditional Unlocks"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - conditional-unlocks
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

# DP with Conditional Unlocks

## Problem Statement

You have `n` steps and `a` actions. Each action has a requirement: it can be used only if a condition on cumulative_toggle count is met. You also have a toggle action that increments a counter.

Each step, choose either the toggle action or one of the regular actions that are currently unlocked. Maximize total reward.

## Input Format

- First line: integers `n`, `a`
- Second line: integer `toggle_reward`
- Next `a` lines: `reward req` where `req` is the minimum toggle count needed

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `0 <= toggle_reward <= 10^9`
- `0 <= req <= n`
- `-10^9 <= reward <= 10^9`

## Clarifying Notes

- Toggle count starts at 0 and increases by 1 when toggle is chosen.

## Example Input

```
3 2
0
5 1
8 2
```

## Example Output

```
13
```

## Solution Stub

### Java

```java
class Solution {
    public long maxReward(int n, int a, int toggleReward, int[][] actions) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, a: int, toggleReward: int, actions: list[list[int]]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxReward(int n, int a, int toggleReward, vector<vector<int>>& actions) {
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
   * @param {number} toggleReward
   * @param {number[][]} actions
   * @return {number}
   */
  maxReward(n, a, toggleReward, actions) {
    // Implement here
    return 0;
  }
}
```
