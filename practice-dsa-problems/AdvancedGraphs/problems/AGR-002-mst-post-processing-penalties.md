---
problem_id: AGR_MST_POST_PROCESSING_PENALTIES__2495
display_id: NTB-AGR-2495
slug: mst-post-processing-penalties
title: "Minimum Spanning Tree with Post-Processing Penalties"
difficulty: Medium
difficulty_score: 50
topics:
  - Advanced Graphs
tags:
  - advanced-algorithms
  - advancedgraphs
  - algorithms
  - coding-interviews
  - data-structures
  - graph-theory
  - mst-post-processing-penalties
  - network-flow
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Minimum Spanning Tree with Post-Processing Penalties

## Problem Statement

You are given a connected, undirected graph with `n` nodes and `m` edges. Each edge has a base weight `w` and a penalty `p`.

Build a minimum spanning tree using **only the base weights** (standard Kruskal on `w`). After the MST is selected, the final cost is:

```
(sum of base weights in the MST) + (sum of penalties of the selected edges)
```

If the graph is not connected, output `-1`.

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v w p`

## Output Format

- Single integer: final cost after adding penalties, or `-1` if no spanning tree exists

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 200000`
- `1 <= u, v <= n`
- `-10^9 <= w, p <= 10^9`

## Clarifying Notes

- Edge selection is based **only** on base weight `w` (penalties do not affect the choice).
- Among edges with the same base weight, the algorithm must prioritize edges with a **smaller penalty** to ensure a unique answer.

## Example Input

```
4 5
1 2 1 5
2 3 2 0
3 4 1 1
1 4 3 0
2 4 4 10
```

## Example Output

```
10
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public long minSpanningTreeCostWithPenalties(int n, int m, List<Edge> edges) {
        // Your code here
        return -1;
    }

    public static class Edge {
        int u, v, w, p;
        public Edge(int u, int v, int w, int p) { this.u = u; this.v = v; this.w = w; this.p = p; }
    }
}
```

### Python

```python
from typing import List

class Edge:
    def __init__(self, u: int, v: int, w: int, p: int):
        self.u = u
        self.v = v
        self.w = w
        self.p = p

class Solution:
    def minSpanningTreeCostWithPenalties(self, n: int, m: int, edges: List[Edge]) -> int:
        # Your code here
        pass
```

### C++

```cpp
#include <vector>

struct Edge {
    int u, v, w, p;
};

class Solution {
public:
    long long minSpanningTreeCostWithPenalties(int n, int m, std::vector<Edge>& edges) {
        // Your code here
        return -1;
    }
};
```

### JavaScript

```javascript
class Solution {
  minSpanningTreeCostWithPenalties(n, m, edges) {
    // Your code here
    return -1;
  }
}
```
