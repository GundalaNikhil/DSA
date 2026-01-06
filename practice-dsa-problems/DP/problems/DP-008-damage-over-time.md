---
problem_id: DP_DAMAGE_OVER_TIME__3651
display_id: NTB-DP-3651
slug: damage-over-time
title: "DP with Damage Over Time"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - damage-over-time
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

# DP with Damage Over Time

## Problem Statement

You have `n` turns and `a` actions. Action `i` applies immediate damage `d_i` and a DoT effect that lasts `t_i` turns, dealing `s_i` damage per turn.

DoT effects stack independently. At each turn, all active effects deal damage before the new action is chosen.

Maximize total damage after `n` turns.

## Input Format

- First line: integers `n` and `a`
- Next `a` lines: `d_i t_i s_i`

## Output Format

- Single integer: maximum total damage

## Constraints

- `1 <= n <= 25`
- `1 <= a <= 6`
- `0 <= d_i, s_i <= 50`
- `0 <= t_i <= 5`

## Clarifying Notes

- Effects with `t_i = 0` have only immediate damage.
- State tracks remaining durations of active effects (capped by `t_i`).

## Example Input

```
2 2
3 1 2
1 2 1
```

## Example Output

```
7
```

## Solution Stub

### Java

```java
class Solution {
    public long maxTotalDamage(int n, int a, int[][] actions) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxTotalDamage(self, n: int, a: int, actions: list[list[int]]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxTotalDamage(int n, int a, vector<vector<int>>& actions) {
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
  maxTotalDamage(n, a, actions) {
    // Implement here
    return 0;
  }
}
```
