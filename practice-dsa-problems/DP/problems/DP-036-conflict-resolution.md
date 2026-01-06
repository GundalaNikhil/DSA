---
problem_id: DP_CONFLICT_RESOLUTION__7613
display_id: NTB-DP-7613
slug: conflict-resolution
title: "DP with Conflict Resolution"
difficulty: Medium
difficulty_score: 50
topics:
  - Dynamic Programming
tags:
  - algorithms
  - coding-interviews
  - conflict-resolution
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

# DP with Conflict Resolution

## Problem Statement

You have a DAG with a unique start node `S` and end node `T`. Each edge has a reward. When multiple paths merge at a node, their requirements (bitmasks) are combined by AND. A path is valid if its final requirement mask equals `target_mask`.

Find the maximum reward among valid paths from `S` to `T`.

## Input Format

- First line: integers `n`, `m`, `b`
- Second line: integers `S`, `T`, `target_mask` (0..(1<<b)-1)
- Next `m` lines: `u v reward mask` (mask is the requirement bitmask for the edge)

## Output Format

- Single integer: maximum reward, or `-1` if no valid path

## Constraints

- `1 <= n <= 200`
- `1 <= m <= 5000`
- `1 <= b <= 10`

## Clarifying Notes

- Requirements along a path are combined by bitwise AND.

## Example Input

```
3 2 2
1 3 1
1 2 5 3
2 3 4 1
```

## Example Output

```
9
```

## Solution Stub

### Java

```java
class Solution {
    public long maxReward(int n, int m, int b, int s, int t, int targetMask, int[][] edges) {
        // Implement here
        return -1;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, m: int, b: int, s: int, t: int, targetMask: int, edges: list[list[int]]) -> int:
        # Implement here
        return -1
```

### C++

```cpp
class Solution {
public:
    long long maxReward(int n, int m, int b, int s, int t, int targetMask, vector<vector<int>>& edges) {
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
   * @param {number} m
   * @param {number} b
   * @param {number} s
   * @param {number} t
   * @param {number} targetMask
   * @param {number[][]} edges
   * @return {number}
   */
  maxReward(n, m, b, s, t, targetMask, edges) {
    // Implement here
    return -1;
  }
}
```
