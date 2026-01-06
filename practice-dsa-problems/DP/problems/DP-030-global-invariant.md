---
problem_id: DP_GLOBAL_INVARIANT__1732
display_id: NTB-DP-1732
slug: global-invariant
title: "DP with Global Invariant"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - dp
  - global-invariant
  - memoization
  - optimization
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Global Invariant

## Problem Statement

You must choose one value per step from a set of actions. Each action `i` adds `v_i` to a running sum and yields reward `r_i`. After `n` steps, the running sum must satisfy `sum % M = 0`.

Maximize total reward while respecting the invariant.

## Input Format

- First line: integers `n`, `a`, `M`
- Next `a` lines: `v_i r_i`

## Output Format

- Single integer: maximum total reward, or `-1` if impossible

## Constraints

- `1 <= n <= 2000`
- `1 <= a <= 20`
- `1 <= M <= 2000`
- `-10^9 <= v_i, r_i <= 10^9`

## Clarifying Notes

- The invariant is checked only at the end.

## Example Input

```
3 2 5
2 4
3 1
```

## Example Output

```
6
```

## Solution Stub

### Java

```java
class Solution {
    public long maxReward(int n, int a, int m, int[][] actions) {
        // Implement here
        return -1;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, a: int, m: int, actions: list[list[int]]) -> int:
        # Implement here
        return -1
```

### C++

```cpp
class Solution {
public:
    long long maxReward(int n, int a, int m, vector<vector<int>>& actions) {
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
   * @param {number} m
   * @param {number[][]} actions
   * @return {number}
   */
  maxReward(n, a, m, actions) {
    // Implement here
    return -1;
  }
}
```
