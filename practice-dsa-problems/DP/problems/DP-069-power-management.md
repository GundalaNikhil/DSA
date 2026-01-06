---
problem_id: DP_POWER_MANAGEMENT__9221
display_id: NTB-DP-9221
slug: power-management
title: "Power Management DP"
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
  - power-management
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Power Management DP

## Problem Statement

You have system states `1..s`. Each state has power draw `p_i`. Transitioning from state `i` to `j` costs `c_{i,j}`. At each time step, you must be in a state that satisfies required performance `req_t` (each state has performance `perf_i`).

Minimize total energy cost over `n` steps.

## Input Format

- First line: integers `n` and `s`
- Second line: `s` integers: power `p_i`
- Third line: `s` integers: performance `perf_i`
- Next `s` lines: `s` integers: transition costs
- Last line: `n` integers: requirements `req_t`

## Output Format

- Single integer: minimum total cost, or `-1` if impossible

## Constraints

- `1 <= n <= 2000`
- `1 <= s <= 50`
- `0 <= costs <= 10^6`

## Clarifying Notes

- Total cost is sum of power per step plus transition costs.

## Example Input

```
2 2
3 1
5 2
0 2
2 0
3 1
```

## Example Output

```
6
```

## Solution Stub

```java
public class Solution {
    public long minEnergyCost(int n, int s, int[] power, int[] performance, int[][] transitionCosts, int[] requirements) {
        // Your code here
        return 0;
    }
}
```

```python
class Solution:
    def minEnergyCost(self, n: int, s: int, power: list[int], performance: list[int], transitionCosts: list[list[int]], requirements: list[int]) -> int:
        # Your code here
        return 0
```

```cpp
class Solution {
public:
    long long minEnergyCost(int n, int s, vector<int>& power, vector<int>& performance, vector<vector<int>>& transitionCosts, vector<int>& requirements) {
        // Your code here
        return 0;
    }
};
```

```javascript
class Solution {
  minEnergyCost(n, s, power, performance, transitionCosts, requirements) {
    // Your code here
    return 0;
  }
}
```
