---
problem_id: DP_SHADOW_ACCOUNTING__4305
display_id: NTB-DP-4305
slug: shadow-accounting
title: "DP with Shadow Accounting"
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
  - shadow-accounting
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Shadow Accounting

## Problem Statement

Each action has a primary reward `r_i` and a shadow cost `s_i`. The shadow balance starts at 0 and must never drop below 0. When you take an action, shadow balance changes by `s_i`.

Maximize total primary reward over `n` steps.

## Input Format

- First line: integers `n`, `a`
- Next `a` lines: `r_i s_i`

## Output Format

- Single integer: maximum total reward, or `-1` if impossible

## Constraints

- `1 <= n <= 200`
- `1 <= a <= 20`
- `-10 <= s_i <= 10`
- `-10^9 <= r_i <= 10^9`
- Shadow balance is capped at 200 for DP.

## Clarifying Notes

- If an action would make shadow balance negative, it cannot be chosen.

## Example Input

```
3 2
5 -1
2 1
```

## Example Output

```
9
```

## Solution Stub

### Java

```java
class Solution {
    public long maxReward(int n, int a, int[][] actions) {
        // Implement here
        return -1;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, a: int, actions: list[list[int]]) -> int:
        # Implement here
        return -1
```

### C++

```cpp
class Solution {
public:
    long long maxReward(int n, int a, vector<vector<int>>& actions) {
        // Implement here
        return -1;
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
    return -1;
  }
}
```
