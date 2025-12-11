---
unique_problem_id: advgraph_009
display_id: ADVGRAPH-009
slug: bipartite-matching-node-capacity
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Bipartite Graphs
  - Maximum Matching
  - Node Capacities
  - Network Flow
  - Node Splitting
  - Dinic's Algorithm
  - Max Flow
---

# Maximum Matching with Node Capacities

## Problem Description

Bipartite graph (U,V,E), each node u in U has capacity capU[u] (max edges it can match), each v in V has capV[v]. Find a maximum feasible matching respecting capacities.

## Examples

- Example 1:
  - Input: `U={0,1}`, `V={2,3}`, `capsU=[1,2]`, `capsV=[1,1]`, `edges=[(0,2),(1,2),(1,3)]`
  - Output: Maximum matching size = 2
  - Explanation: Match (0,2) and (1,3). Cannot use (1,2) also because V[2] has capacity 1
- Example 2:
  - Input: `U={0,1,2}`, `V={3,4}`, `capsU=[2,1,1]`, `capsV=[2,2]`, `edges=[(0,3),(0,4),(1,3),(2,4)]`
  - Output: Maximum matching size = 4
  - Explanation: Node 0 can match to both 3 and 4 (capacity 2); total 4 edges used

## Constraints

- `1 <= |U| + |V| <= 100,000` (total nodes, where 1e5 means 1 × 10^5)
- `0 <= m <= 200,000` (number of edges, where 2e5 means 2 × 10^5)
- `1 <= capacity[u] <= 1000` for all nodes
- All nodes are 0-indexed within their partitions

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public int maxMatchingWithNodeCapacities(int[] capsU, int[] capsV, int[][] edges) {
        // edges[i] = {u, v} where u in U, v in V
        // Return maximum matching size respecting node capacities
    }
}
```

### Python
```python
from typing import List, Tuple

def max_matching_with_node_capacities(caps_u: List[int], caps_v: List[int], 
                                       edges: List[Tuple[int, int]]) -> int:
    """
    Find maximum matching respecting node capacities.
    
    Args:
        caps_u: Capacities for nodes in U partition
        caps_v: Capacities for nodes in V partition
        edges: Bipartite edges (u, v) where u in U, v in V
    
    Returns:
        Maximum matching size
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    int maxMatchingWithNodeCapacities(vector<int>& capsU, vector<int>& capsV, 
                                      vector<pair<int,int>>& edges) {
        // Use node splitting: split each node into in/out with capacity edge
        // Run max flow algorithm
    }
};
```

## Input Format

The input will be provided as:
- First line: Three integers `|U|`, `|V|`, `m` (sizes and edge count)
- Second line: `|U|` integers representing capacities of U nodes
- Third line: `|V|` integers representing capacities of V nodes
- Next `m` lines: Two integers `u v` representing edge from U[u] to V[v]

### Sample Input
```
2 2 3
1 2
1 1
0 2
1 2
1 3
```

## Hints

Convert to flow network with node splitting and run Dinic.

## Quiz

### Question 1
How do we reduce bipartite matching with node capacities to a standard max flow problem?

A) Add a super source and super sink  
B) Split each node into in-node and out-node with a capacity edge  
C) Use dynamic programming  
D) Apply Hopcroft-Karp directly

**Correct Answer:** B

**Explanation:** Each node is split into two: an in-node and out-node connected by an edge with capacity equal to the node's capacity. This converts node capacities to edge capacities.

### Question 2
What is the time complexity of solving this problem using Dinic's algorithm after node splitting?

A) O(V²E)  
B) O(E²)  
C) O(V·E)  
D) O((V+E) log V)

**Correct Answer:** A

**Explanation:** After node splitting, we have O(V) vertices and O(V+E) edges. Dinic's algorithm runs in O(V²E) time, which becomes O(V²(V+E)) in the worst case.

### Question 3
In the node-splitting technique, if node u has capacity c, what is the capacity of the edge from u_in to u_out?

A) 1  
B) Infinity  
C) c  
D) 0

**Correct Answer:** C

**Explanation:** The edge from u_in to u_out has capacity exactly c, representing the node's capacity constraint.

### Question 4
Can we use Hopcroft-Karp algorithm directly for bipartite matching with node capacities?

A) Yes, it works without modification  
B) No, it only works for unit capacities on edges  
C) Yes, but only if all capacities are 1  
D) No, node capacities must first be converted to edge capacities

**Correct Answer:** D

**Explanation:** Hopcroft-Karp is designed for standard bipartite matching. Node capacities must be converted to edge capacities via node splitting before applying any max flow algorithm.
