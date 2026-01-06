---
problem_id: DP_DP_WITH_MOMENTUM__4950
display_id: NTB-DP-4950
slug: dp-with-momentum
title: "DP with Momentum"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - dp-with-momentum
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Momentum

## Problem Statement

You have `n` steps and `a` actions. Choosing the same action consecutively builds momentum. Let `streak` be the number of consecutive uses of the current action (capped at `M`). The reward for using action `i` is:

```
reward = base_i + bonus_i * streak
```

Switching actions resets streak to 1 and also applies a switch penalty `P` (subtracted from reward).

Maximize total reward over `n` steps.

## Input Format

- First line: integers `n`, `a`, `M`, `P`
- Next `a` lines: `base_i bonus_i`

## Output Format

- Single integer: maximum total reward

## Constraints

- `1 <= n <= 200`
- `1 <= a <= 8`
- `1 <= M <= 10`
- `0 <= P <= 10^6`

## Clarifying Notes

- Streak is capped at `M`.

## Example Input

```
3 2 2 1
5 2
4 3
```

## Example Output

```
18
```

## Solution Stub

### Java

```java
class Solution {
    public long maxReward(int n, int a, int m, int p, int[][] actions) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, a: int, m: int, p: int, actions: list[list[int]]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxReward(int n, int a, int m, int p, vector<vector<int>>& actions) {
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
   * @param {number} m
   * @param {number} p
   * @param {number[][]} actions
   * @return {number}
   */
  maxReward(n, a, m, p, actions) {
    // Implement here
    return 0;
  }
}
```
