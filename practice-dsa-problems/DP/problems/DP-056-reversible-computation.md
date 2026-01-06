---
problem_id: DP_REVERSIBLE_COMPUTATION__9348
display_id: NTB-DP-9348
slug: reversible-computation
title: "DP on Reversible Computation"
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
  - reversible-computation
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP on Reversible Computation

## Problem Statement

You have `n` steps and states `0..S-1`. Each action moves from state `u` to state `v` with cost `c`. Every action has a reverse action with cost `c_rev`.

Find the minimum total cost to start at state 0 and return to state 0 after exactly `n` steps.

## Input Format

- First line: integers `n`, `S`, `a`
- Next `a` lines: `u v c c_rev`

## Output Format

- Single integer: minimum cost, or `-1` if impossible

## Constraints

- `1 <= n <= 200`
- `1 <= S <= 50`
- `1 <= a <= 2000`

## Clarifying Notes

- Reverse actions are not automatic; you must choose them explicitly.

## Example Input

```
2 2 1
0 1 3 1
```

## Example Output

```
4
```

## Solution Stub

### Java

```java
class Solution {
    public long minCost(int n, int s, int a, int[][] actions) {
        // Implement here
        return -1;
    }
}
```

### Python

```python
class Solution:
    def minCost(self, n: int, s: int, a: int, actions: list[list[int]]) -> int:
        # Implement here
        return -1
```

### C++

```cpp
class Solution {
public:
    long long minCost(int n, int s, int a, vector<vector<int>>& actions) {
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
   * @param {number} s
   * @param {number} a
   * @param {number[][]} actions
   * @return {number}
   */
  minCost(n, s, a, actions) {
    // Implement here
    return -1;
  }
}
```
