---
unique_problem_id: advgraph_002
display_id: ADVGRAPH-002
slug: max-flow-vertex-capacity
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Network Flow
  - Maximum Flow
  - Vertex Capacities
  - Node Splitting
  - Dinic's Algorithm
  - Edmonds-Karp
---

# Max Flow With Vertex Capacities

## Problem Description

Directed graph with edge capacities and vertex capacities. Compute max s-t flow respecting vertex limits.

## Examples

- Example 1:
  - Input: `n=4`, `s=0`, `t=3`, `vertexCaps=[INF,3,2,INF]`, `edges=[(0,1,5),(1,2,4),(2,3,5)]`
  - Output: Maximum flow = 2
  - Explanation: Flow is limited by vertex 2's capacity of 2
- Example 2:
  - Input: `n=4`, `s=0`, `t=3`, `vertexCaps=[INF,5,5,INF]`, `edges=[(0,1,3),(0,2,2),(1,3,3),(2,3,2)]`
  - Output: Maximum flow = 5
- Example 3:
  - Input: `n=3`, `s=0`, `t=2`, `vertexCaps=[INF,1,INF]`, `edges=[(0,1,10),(1,2,10)]`
  - Output: Maximum flow = 1 (limited by vertex 1's capacity)

## Constraints

- `2 <= n <= 2000` (number of vertices)
- `1 <= m <= 5000` (number of edges)
- `1 <= edge capacity, vertex capacity <= 10^9`
- Vertices are 0-indexed: `0 <= s, t < n`, `s ≠ t`
- Source and sink typically have infinite capacity
- Use INF or a large value (e.g., 10^9) to represent infinite capacity

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public long maxFlowVertexCapacity(int n, int s, int t, long[] vertexCaps, int[][] edges) {
        // edges[i] = {u, v, capacity}
        // Split vertices and run max flow algorithm
    }
}
```

### Python
```python
from typing import List, Tuple

def max_flow_vertex_capacity(n: int, s: int, t: int, vertex_caps: List[int],
                             edges: List[Tuple[int, int, int]]) -> int:
    """
    Compute maximum flow with vertex capacity constraints.
    
    Args:
        n: Number of vertices
        s: Source vertex
        t: Sink vertex
        vertex_caps: Capacity for each vertex (use large value for INF)
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
    ll maxFlowVertexCapacity(int n, int s, int t, const vector<ll>& vertexCaps,
                            const vector<tuple<int,int,ll>>& edges) {
        // Node splitting: v -> v_in and v_out with edge (v_in, v_out, capacity)
        // Run Dinic or Edmonds-Karp
    }
};
```

## Input Format

The input will be provided as:
- First line: Integers `n`, `m`, `s`, `t`
- Second line: `n` integers representing vertex capacities  
- Next `m` lines: Three integers `u v cap` representing directed edge

### Sample Input
```
4 3 0 3
1000000000 3 2 1000000000
0 1 5
1 2 4
2 3 5
```

## Hints

Split each vertex into in/out with an edge of vertex capacity; run Dinic/Edmonds-Karp.

## Quiz

### Question 1
How do we handle vertex capacities in a flow network?

A) Ignore them and use edge capacities only  
B) Split each vertex v into v_in and v_out, connected by an edge with capacity equal to vertex capacity  
C) Reduce all edge capacities  
D) Use dynamic programming

**Correct Answer:** B

**Explanation:** Vertex capacities are converted to edge capacities by splitting each vertex into an in-node and out-node connected by an edge with the vertex's capacity.

### Question 2
After node splitting, what is the number of vertices and edges in the transformed graph?

A) V vertices, E edges  
B) 2V vertices, E + V edges  
C) V vertices, 2E edges  
D) 2V vertices, 2E edges

**Correct Answer:** B

**Explanation:** Each original vertex is split into 2, giving 2V vertices. Original E edges remain, and V new edges are added for the split vertices, giving E + V edges.

### Question 3
Which vertices should NOT be split in the transformation?

A) All vertices must be split  
B) Only source and sink should not be split (or given infinite internal capacity)  
C) Vertices with degree 1  
D) Vertices on the longest path

**Correct Answer:** B

**Explanation:** The source and sink typically should not have capacity constraints, so they either aren't split or are given infinite capacity on their internal edge.

### Question 4
What is the time complexity after transforming to standard max flow?

A) O(V²)  
B) O((2V)²(E+V)) = O(V²E) using Dinic  
C) O(E²)  
D) O(V³)

**Correct Answer:** B

**Explanation:** After transformation, we have 2V vertices and E+V edges. Using Dinic's algorithm gives O(V²E) complexity.
