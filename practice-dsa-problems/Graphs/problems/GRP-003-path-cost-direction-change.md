---
problem_id: GRP_PATH_COST_DIRECTION_CHANGE__8546
display_id: NTB-GRP-8546
slug: path-cost-direction-change
title: "Path Cost with Direction Change Penalties"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
tags:
  - algorithms
  - coding-interviews
  - data-structures
  - graphs
  - path-cost-direction-change
  - search
  - shortest-paths
  - technical-interview-prep
  - traversal
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Path Cost with Direction Change Penalties

## Problem Statement

You are given a directed weighted graph with `n` nodes and `m` edges. Each edge has a compass direction in {N, E, S, W}.

You start at node `S`, initially facing direction `D₀`, and must reach node `T` with minimum total cost.

**Cost Rules:**

1. Edge traversal adds weight `w`.
2. Turn penalty is added based on direction change:
   - Same direction: +0
   - 90° turn: +penalty
   - 180° turn: +2 × penalty

## Input Format

- First line: `n`, `m`, `penalty`
- Second line: `S`, `T`, `D0` (Initial direction as N=0, E=1, S=2, W=3)
- Next `m` lines: `u v w direction`
  - `direction` is also encoded as 0, 1, 2, or 3.

## Output Format

- Single integer: Minimum total cost, or `-1` if unreachable.

## Constraints

- `2 <= n <= 10^5`
- `1 <= m <= 2^2*10^5`
- `0 <= penalty <= 10^6`
- `1 <= w <= 10^9`

## Clarifying Notes

- Turn steps = `min(|d1 - d2|, 4 - |d1 - d2|)`.
- Penalty added = `turn_steps * penalty`.
- The intended solution uses Dijkstra on states `(node, facing_dir)`.

## Example Input

```
4 5 10
1 4 0
1 2 5 0
2 3 5 1
3 4 5 2
1 3 20 1
2 4 15 2
```

## Example Output

```
35
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public long minPathCost(int n, int m, int penalty, int S, int T, int D0, int[][] edges) {
        // Your code here
        return -1;
    }
}
```

```python
import heapq

class Solution:
    def minPathCost(self, n: int, m: int, penalty: int, S: int, T: int, D0: int, edges: list[list[int]]) -> int:
        # Your code here
        return -1
```

```cpp
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long minPathCost(int n, int m, int penalty, int S, int T, int D0, vector<vector<int>>& edges) {
        // Your code here
        return -1;
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number} penalty
   * @param {number} S
   * @param {number} T
   * @param {number} D0
   * @param {number[][]} edges
   * @returns {number}
   */
  minPathCost(n, m, penalty, S, T, D0, edges) {
    // Your code here
    return -1;
  }
}
```
