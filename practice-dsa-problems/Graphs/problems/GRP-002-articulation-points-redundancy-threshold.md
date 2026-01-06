---
problem_id: GRP_ARTICULATION_POINTS_REDUNDANCY_THRESHOLD__5926
display_id: NTB-GRP-5926
slug: articulation-points-redundancy-threshold
title: "Articulation Points with Redundancy Threshold"
difficulty: Medium
difficulty_score: 50
topics:
  - Graphs
tags:
  - algorithms
  - articulation-points-redundancy-threshold
  - coding-interviews
  - data-structures
  - graphs
  - search
  - shortest-paths
  - technical-interview-prep
  - traversal
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Articulation Points with Redundancy Threshold

## Problem Statement

You are given a connected, undirected graph with `n` nodes and `m` edges, and an integer percentage `X` (0 to 100). For a node `v`, remove `v` and all incident edges. Let the remaining graph split into components with sizes `s1, s2, ...` and let `s_max` be the largest component size.

Node `v` is **critical** if more than `X` percent of the remaining nodes are **not** in the largest component:

```
(n - 1 - s_max) * 100 > X * (n - 1)
```

Your task is to output all critical nodes in ascending order.

## Input Format

- First line: integers `n`, `m`, and `X`
- Next `m` lines: edges `u v`

## Output Format

- If there are no critical nodes, output a single line `0`.
- Otherwise, output:
  - First line: the number of critical nodes
  - Second line: their indices in ascending order, separated by spaces

## Constraints

- `1 <= n, m <= 200000`
- `0 <= X <= 100`
- `1 <= u, v <= n`

## Clarifying Notes

- The graph is connected before any removals.
- The intended solution uses articulation points (Tarjan) plus component size tracking.

## Example Input

```
5 4 40
1 2
2 3
3 4
3 5
```

## Example Output

```
1
3
```

## Solution Stub

```java
import java.util.*;

public class Solution {
    public List<Integer> findCriticalNodes(int n, int m, int X, int[][] edges) {
        // Your code here
        return new ArrayList<>();
    }
}
```

```python
class Solution:
    def findCriticalNodes(self, n: int, m: int, X: int, edges: list[list[int]]) -> list[int]:
        # Your code here
        return []
```

```cpp
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> findCriticalNodes(int n, int m, int X, vector<vector<int>>& edges) {
        // Your code here
        return {};
    }
};
```

```javascript
class Solution {
  /**
   * @param {number} n
   * @param {number} m
   * @param {number} X
   * @param {number[][]} edges
   * @returns {number[]}
   */
  findCriticalNodes(n, m, X, edges) {
    // Your code here
    return [];
  }
}
```
