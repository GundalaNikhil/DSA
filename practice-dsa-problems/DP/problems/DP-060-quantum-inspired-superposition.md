---
problem_id: DP_QUANTUM_INSPIRED_SUPERPOSITION__3908
display_id: NTB-DP-3908
slug: quantum-inspired-superposition
title: "DP with Quantum-Inspired Superposition"
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
  - quantum-inspired-superposition
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Quantum-Inspired Superposition

## Problem Statement

Your system has two possible states `A` and `B` with amplitudes `(x, y)` (integers). Each action applies a linear transform:

```
(x', y') = (a*x + b*y, c*x + d*y)
```

At a measurement step, the state collapses to `A` if `x >= y`, otherwise to `B`. After collapse, amplitudes reset to `(1,0)` for `A` or `(0,1)` for `B`.

You must choose actions over `n` steps, and you may measure at any step. Reward is 1 each time the system collapses to `A` and 0 otherwise. Maximize total reward.

## Input Format

- First line: integers `n` and `a`
- Next `a` lines: `a b c d` (transform matrix)

## Output Format

- Single integer: maximum reward

## Constraints

- `1 <= n <= 30`
- `1 <= a <= 6`
- `-5 <= a,b,c,d <= 5`

## Clarifying Notes

- You may measure at most once per step (either measure or apply a transform).
- This is deterministic; collapse rule is based on `x` and `y`.

## Example Input

```
2 1
1 1 0 1
```

## Example Output

```
2
```

## Solution Stub

### Java

```java
class Solution {
    public int maxReward(int n, int a, int[][] transforms) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, a: int, transforms: list[list[int]]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    int maxReward(int n, int a, vector<vector<int>>& transforms) {
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
   * @param {number[][]} transforms
   * @return {number}
   */
  maxReward(n, a, transforms) {
    // Implement here
    return 0;
  }
}
```
