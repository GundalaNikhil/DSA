---
unique_problem_id: advgraph_007
display_id: ADVGRAPH-007
slug: eulerian-trail-directed
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Eulerian Path
  - Eulerian Circuit
  - Directed Graphs
  - Hierholzer's Algorithm
  - Graph Traversal
  - Degree Conditions
---

# Eulerian Trail With Directed Edges

## Problem Description

Determine if a directed graph has an Euler trail/path and output one if it exists.

## Examples

- Example 1:
  - Input: `n=3`, `edges=[(0,1),(1,2),(2,0)]`
  - Output: Euler circuit exists: [0,1,2,0]
  - Explanation: All vertices have in-degree = out-degree, forms a circuit
- Example 2:
  - Input: `n=4`, `edges=[(0,1),(1,2),(1,3),(2,3)]`
  - Output: Euler path exists: [0,1,2,3] or [0,1,3,2] (edges: 0→1→2→3)
  - Explanation: Vertex 0 has out-degree - in-degree = 1, vertex 3 has in-degree - out-degree = 1
- Example 3:
  - Input: `n=3`, `edges=[(0,1),(2,1)]`
  - Output: No Euler path exists
  - Explanation: Graph is not connected in underlying undirected sense

## Constraints

- `1 <= n <= 100,000` (number of vertices, where 1e5 means 1 × 10^5)
- `0 <= m <= 200,000` (number of edges, where 2e5 means 2 × 10^5)
- Vertices are 0-indexed: `0 <= u, v < n`
- Graph may have isolated vertices

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public List<Integer> eulerianTrailDirected(int n, int[][] edges) {
        // Check degree conditions and use Hierholzer's algorithm
        // Return vertex sequence of Euler path/circuit, or empty if none exists
    }
}
```

### Python
```python
from typing import List, Tuple, Optional

def eulerian_trail_directed(n: int, edges: List[Tuple[int, int]]) -> Optional[List[int]]:
    """
    Find an Eulerian path or circuit in a directed graph.
    
    Args:
        n: Number of vertices
        edges: List of directed edges
    
    Returns:
        Vertex sequence of Euler path/circuit, or None if it doesn't exist
    """
    pass
```

### C++
```cpp
#include <vector>
#include <optional>
using namespace std;

class Solution {
public:
    optional<vector<int>> eulerianTrailDirected(int n, const vector<pair<int,int>>& edges) {
        // Check: in-degree = out-degree for all, or exactly one +1 and one -1
        // Use Hierholzer's algorithm with stack
    }
};
```

## Input Format

The input will be provided as:
- First line: Integers `n` (vertices) and `m` (edges)
- Next `m` lines: Two integers `u v` representing a directed edge

### Sample Input
```
3 3
0 1
1 2
2 0
```

## Hints

In/out degree check + Hierholzer.

## Quiz

### Question 1
What is the necessary condition for an Eulerian circuit in a directed graph?

A) All vertices have the same degree  
B) All vertices have in-degree equal to out-degree  
C) Graph is a tree  
D) Graph is bipartite

**Correct Answer:** B

**Explanation:** For an Eulerian circuit to exist in a directed graph, every vertex must have equal in-degree and out-degree.

### Question 2
What is the condition for an Eulerian path (but not circuit) in a directed graph?

A) All vertices have in-degree = out-degree  
B) Exactly one vertex has (out-degree - in-degree) = 1, exactly one has (in-degree - out-degree) = 1, all others have in-degree = out-degree  
C) At most two vertices have odd degree  
D) Graph has no cycles

**Correct Answer:** B

**Explanation:** For an Eulerian path, there must be a start vertex with one extra outgoing edge and an end vertex with one extra incoming edge.

### Question 3
What is the time complexity of Hierholzer's algorithm for finding an Eulerian path?

A) O(V + E)  
B) O(V²)  
C) O(E²)  
D) O(V·E)

**Correct Answer:** A

**Explanation:** Hierholzer's algorithm visits each edge exactly once, making it O(V + E) time complexity.

### Question 4
What additional condition must be checked besides degree conditions?

A) Graph must be a tree  
B) Graph must be strongly connected (considering only vertices with edges)  
C) Graph must be planar  
D) No condition needed

**Correct Answer:** B

**Explanation:** Besides degree conditions, the graph must be connected in the sense that all vertices with nonzero degree must be in the same weakly connected component.
