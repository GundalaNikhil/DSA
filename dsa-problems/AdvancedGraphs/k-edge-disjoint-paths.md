---
unique_problem_id: advgraph_013
display_id: ADVGRAPH-013
slug: k-edge-disjoint-paths
version: 1.0.0
difficulty: Hard
topic_tags:
  - Advanced Graphs
  - Network Flow
  - Edge-Disjoint Paths
  - Menger's Theorem
  - Max Flow
  - Graph Connectivity
---

# K-Edge-Disjoint Paths

## Problem Description

Determine if there exist k edge-disjoint paths from s to t in a directed graph; output yes/no.

## Examples

- Example 1:
  - Input: `n=4`, `s=0`, `t=3`, `k=2`, `edges=[(0,1),(1,3),(0,2),(2,3)]`
  - Output: Yes (2 edge-disjoint paths exist: 0→1→3 and 0→2→3)
- Example 2:
  - Input: `n=5`, `s=0`, `t=4`, `k=3`, `edges=[(0,1),(1,2),(2,4),(0,3),(3,4)]`
  - Output: No (only 2 edge-disjoint paths possible)
- Example 3:
  - Input: `n=3`, `s=0`, `t=2`, `k=1`, `edges=[(0,1),(1,2)]`
  - Output: Yes (one path: 0→1→2)

## Constraints

- `2 <= n <= 100,000` (number of vertices, where 1e5 means 1 × 10^5)
- `1 <= m <= 200,000` (number of edges, where 2e5 means 2 × 10^5)
- `1 <= k <= 10,000` (where 1e4 means 1 × 10^4)
- `0 <= s, t < n`, `s ≠ t`
- Vertices are 0-indexed

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public boolean hasKEdgeDisjointPaths(int n, int s, int t, int k, int[][] edges) {
        // Transform to max flow with unit capacities
        // Check if max flow >= k
    }
}
```

### Python
```python
from typing import List, Tuple

def has_k_edge_disjoint_paths(n: int, s: int, t: int, k: int, 
                               edges: List[Tuple[int, int]]) -> bool:
    """
    Check if k edge-disjoint paths exist from s to t.
    
    Args:
        n: Number of vertices
        s: Source vertex
        t: Sink vertex
        k: Number of required edge-disjoint paths
        edges: List of directed edges
    
    Returns:
        True if k edge-disjoint paths exist, False otherwise
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    bool hasKEdgeDisjointPaths(int n, int s, int t, int k, 
                               const vector<pair<int,int>>& edges) {
        // Build flow network with unit edge capacities
        // Run max flow algorithm and check if flow >= k
    }
};
```

## Input Format

The input will be provided as:
- First line: Integers `n`, `m`, `s`, `t`, `k`
- Next `m` lines: Two integers `u v` representing a directed edge

### Sample Input
```
4 4 0 3 2
0 1
1 3
0 2
2 3
```

## Hints

Transform to max flow with unit capacities.

## Quiz

### Question 1
What theorem directly relates to finding k edge-disjoint paths?

A) Euler's Theorem  
B) Menger's Theorem  
C) Hall's Marriage Theorem  
D) König's Theorem

**Correct Answer:** B

**Explanation:** Menger's Theorem states that the maximum number of edge-disjoint paths between two vertices equals the minimum edge cut separating them, which is exactly the max flow with unit capacities.

### Question 2
To check if k edge-disjoint paths exist, what should we do?

A) Run DFS k times  
B) Convert to max flow problem with unit edge capacities and check if max flow >= k  
C) Use Dijkstra's algorithm  
D) Find all cycles

**Correct Answer:** B

**Explanation:** Transform the problem to max flow by giving each edge unit capacity. The max flow value equals the maximum number of edge-disjoint paths by Menger's theorem.

### Question 3
What is the time complexity of solving this using max flow?

A) O(k·E)  
B) O(V²E) using Dinic  
C) O(E²)  
D) O(V³)

**Correct Answer:** B

**Explanation:** Using Dinic's or similar max flow algorithms gives O(V²E) time complexity for unit capacities, which can be improved to O(E√V) with specialized algorithms.

### Question 4
If we need node-disjoint paths instead of edge-disjoint paths, how should we modify the graph?

A) No modification needed  
B) Split each node into in-node and out-node with unit capacity edge  
C) Double all edge capacities  
D) Remove all cycles

**Correct Answer:** B

**Explanation:** To find node-disjoint paths, split each vertex (except s and t) into two vertices connected by a unit capacity edge, converting node constraints to edge constraints.
