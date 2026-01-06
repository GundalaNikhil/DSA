---
problem_id: DP_COMPOSITIONAL_STATE__5091
display_id: NTB-DP-5091
slug: compositional-state
title: "DP with Compositional State"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - compositional-state
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

# DP with Compositional State

## Problem Statement

Your state is a pair `(x, y)` where `x` in `[0..X]` and `y` in `[0..Y]`. Each action updates `x` and `y` by different deltas and yields reward `r`.

Find the maximum total reward after exactly `n` steps, starting from `(0, 0)` and staying within bounds.

## Input Format

- First line: integers `n`, `X`, `Y`, `a`
- Next `a` lines: `dx dy r`

## Output Format

- Single integer: maximum total reward, or `-1` if impossible

## Constraints

- `1 <= n <= 200`
- `0 <= X, Y <= 50`
- `-10^9 <= r <= 10^9`

## Clarifying Notes

- `dx` and `dy` can be negative but bounds must be respected.

## Example Input

```
2 2 2 2
1 0 3
0 1 4
```

## Example Output

```
7
```

## Solution Stub

### Java

```java
class Solution {
    public long maxReward(int n, int x, int y, int a, int[][] actions) {
        // Implement here
        return -1;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, x: int, y: int, a: int, actions: list[list[int]]) -> int:
        # Implement here
        return -1
```

### C++

```cpp
class Solution {
public:
    long long maxReward(int n, int x, int y, int a, vector<vector<int>>& actions) {
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
   * @param {number} x
   * @param {number} y
   * @param {number} a
   * @param {number[][]} actions
   * @return {number}
   */
  maxReward(n, x, y, a, actions) {
    // Implement here
    return -1;
  }
}
```
