---
problem_id: AGR_OFFLINE_DYNAMIC_CONNECTIVITY_ROLLBACK_DSU__4349
display_id: NTB-AGR-4349
slug: offline-dynamic-connectivity-rollback-dsu
title: "Offline Dynamic Connectivity with Rollback DSU"
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
  - network-flow
  - offline-dynamic-connectivity-rollback-dsu
  - technical-interview-prep
premium: false
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# Offline Dynamic Connectivity with Rollback DSU

## Problem Statement

You are given an undirected graph with `n` nodes and a sequence of `q` operations. The graph changes over time by adding and removing edges. For each query, determine whether two nodes are connected at that time.

Operations:

- `ADD u v`: add the edge `(u, v)`.
- `REM u v`: remove the edge `(u, v)`.
- `ASK u v`: output whether `u` and `v` are connected in the current graph.

Edges are identified by unordered pairs. An edge will not be added twice without being removed in between, and every `REM` refers to an active edge.

You must answer the queries in order using a rollback DSU with stack-based undo (offline dynamic connectivity).

## Input Format

- First line: integers `n` and `q`
- Next `q` lines: operations in the format above

## Output Format

- For each `ASK` operation, output `YES` or `NO` on its own line

## Constraints

- `1 <= n, q <= 200000`
- `1 <= u, v <= n`

## Clarifying Notes

- The problem is offline: you can read all operations before producing outputs.
- A correct solution uses a segment tree over time with rollback DSU.
- Edge endpoints can be given in any order; treat `(u, v)` the same as `(v, u)`.

## Example Input

```
4 7
ADD 1 2
ADD 2 3
ASK 1 3
REM 2 3
ASK 1 3
ADD 3 4
ASK 1 4
```

## Example Output

```
YES
NO
NO
```

## Solution Stubs

### Java

```java
import java.util.*;

public class Solution {
    public List<String> solveDynamicConnectivity(int n, int q, List<GraphOp> ops) {
        // Your code here
        return new ArrayList<>();
    }

    public static class GraphOp {
        String type;
        int u, v;
        public GraphOp(String type, int u, int v) { this.type = type; this.u = u; this.v = v; }
    }
}
```

### Python

```python
from typing import List

class GraphOp:
    def __init__(self, type: str, u: int, v: int):
        self.type = type
        self.u = u
        self.v = v

class Solution:
    def solveDynamicConnectivity(self, n: int, q: int, ops: List[GraphOp]) -> List[str]:
        # Your code here
        pass
```

### C++

```cpp
#include <string>
#include <vector>

struct GraphOp {
    std::string type;
    int u, v;
};

class Solution {
public:
    std::vector<std::string> solveDynamicConnectivity(int n, int q, std::vector<GraphOp>& ops) {
        // Your code here
        return {};
    }
};
```

### JavaScript

```javascript
class Solution {
  solveDynamicConnectivity(n, q, ops) {
    // Your code here
    return [];
  }
}
```
