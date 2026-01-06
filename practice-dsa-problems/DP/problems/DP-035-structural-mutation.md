---
problem_id: DP_STRUCTURAL_MUTATION__3777
display_id: NTB-DP-3777
slug: structural-mutation
title: "DP with Structural Mutation"
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
  - structural-mutation
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP with Structural Mutation

## Problem Statement

You traverse a graph of `m` nodes for `n` steps. Each action moves along an edge and yields reward. Some edges are **fragile** and disappear permanently after being used once.

Maximize total reward.

## Input Format

- First line: integers `n`, `m`, `e`
- Next `e` lines: `u v reward fragile` (fragile is 0 or 1)

## Output Format

- Single integer: maximum total reward starting from node 1

## Constraints

- `1 <= n <= 20`
- `1 <= m <= 12`
- `1 <= e <= 50`
- `-10^9 <= reward <= 10^9`

## Clarifying Notes

- You can traverse an edge in either direction only if it exists.
- State includes current node and which fragile edges remain.

## Example Input

```
3 3 3
1 2 5 1
2 3 4 0
1 3 2 1
```

## Example Output

```
11
```

## Solution Stub

### Java

```java
class Solution {
    public long maxReward(int n, int m, int e, int[][] edges) {
        // Implement here
        return 0;
    }
}
```

### Python

```python
class Solution:
    def maxReward(self, n: int, m: int, e: int, edges: list[list[int]]) -> int:
        # Implement here
        return 0
```

### C++

```cpp
class Solution {
public:
    long long maxReward(int n, int m, int e, vector<vector<int>>& edges) {
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
   * @param {number} m
   * @param {number} e
   * @param {number[][]} edges
   * @return {number}
   */
  maxReward(n, m, e, edges) {
    // Implement here
    return 0;
  }
}
```
