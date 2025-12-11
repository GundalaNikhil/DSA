---
unique_problem_id: advgraph_011
display_id: ADVGRAPH-011
slug: dinic-with-scaling
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Network Flow
  - Maximum Flow
  - Dinic's Algorithm
  - Capacity Scaling
  - Blocking Flow
  - Level Graph
---

# Dinic With Scaling

## Problem Description

Implement max flow with capacity scaling to improve on large capacities.

## Examples

- Example 1:
  - Input: `n=4`, `s=0`, `t=3`, `edges=[(0,1,10),(0,2,5),(1,3,7),(2,3,8)]`
  - Output: Maximum flow = 12
  - Explanation: Send 7 through 0→1→3 and 5 through 0→2→3
- Example 2:
  - Input: `n=6`, `s=0`, `t=5`, `edges=[(0,1,16),(0,2,13),(1,2,10),(1,3,12),(2,1,4),(2,4,14),(3,2,9),(3,5,20),(4,3,7),(4,5,4)]`
  - Output: Maximum flow = 23

## Constraints

- `2 <= n <= 5000` (number of vertices)
- `1 <= m <= 20,000` (number of edges, where 2e4 means 2 × 10^4)
- `0 <= capacity <= 10^9` for each edge
- Vertices are 0-indexed
- Source `s` and sink `t` are distinct vertices

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public long maxFlowDinicScaling(int n, int s, int t, int[][] edges) {
        // edges[i] = {u, v, capacity}
        // Implement Dinic's algorithm with capacity scaling
    }
}
```

### Python
```python
from typing import List, Tuple

def max_flow_dinic_scaling(n: int, s: int, t: int, edges: List[Tuple[int, int, int]]) -> int:
    """
    Compute maximum flow using Dinic's algorithm with capacity scaling.
    
    Args:
        n: Number of vertices
        s: Source vertex
        t: Sink vertex
        edges: List of directed edges (u, v, capacity)
    
    Returns:
        Maximum flow value
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;
using ll = long long;

class Solution {
public:
    ll maxFlowDinicScaling(int n, int s, int t, const vector<tuple<int,int,int>>& edges) {
        // Build level graph and find blocking flows with scaling
    }
};
```

## Input Format

The input will be provided as:
- First line: Integers `n` (vertices), `m` (edges), `s` (source), `t` (sink)
- Next `m` lines: Three integers `u v cap` representing directed edge with capacity

### Sample Input
```
4 4 0 3
0 1 10
0 2 5
1 3 7
2 3 8
```

## Hints

Use capacity scaling: process edges with capacity ≥ Δ for decreasing powers of 2.

## Quiz

### Question 1
What is the time complexity of standard Dinic's algorithm?

A) O(V²E)  
B) O(VE²)  
C) O(E²)  
D) O(V³)

**Correct Answer:** A

**Explanation:** Dinic's algorithm runs in O(V²E) time by building at most V level graphs and running DFS to find blocking flows.

### Question 2
What does capacity scaling improve in Dinic's algorithm?

A) Space complexity  
B) Handling of large capacity values  
C) Graph connectivity  
D) Number of vertices

**Correct Answer:** B

**Explanation:** Capacity scaling processes edges in decreasing order of capacity magnitude, improving performance when capacities are large by reducing the number of augmenting paths needed.

### Question 3
What is a blocking flow in Dinic's algorithm?

A) A flow that uses all edges  
B) A flow in the level graph where every path from s to t contains at least one saturated edge  
C) A flow with value 0  
D) The maximum flow in the graph

**Correct Answer:** B

**Explanation:** A blocking flow is a flow in the level graph such that no more flow can be pushed from source to sink without using edges backward or outside the level graph.

### Question 4
How many times is the level graph reconstructed in Dinic's algorithm?

A) Once  
B) At most E times  
C) At most V times  
D) Exactly log(max_capacity) times

**Correct Answer:** C

**Explanation:** The distance from source to sink in the level graph increases by at least 1 after each blocking flow, so at most V level graphs are constructed.
