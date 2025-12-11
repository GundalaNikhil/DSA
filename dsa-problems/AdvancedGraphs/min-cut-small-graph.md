---
unique_problem_id: advgraph_001
display_id: ADVGRAPH-001
slug: min-cut-small-graph
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Network Flow
  - Minimum Cut
  - Max-Flow Min-Cut Theorem
  - Stoer-Wagner Algorithm
  - Global Min-Cut
---

# Minimum Cut in Small Graph

## Problem Description

Find the minimum cut value in an undirected weighted graph (global min-cut).

## Examples

- Example 1:
  - Input: `n=4`, `edges=[(0,1,2),(1,2,3),(2,3,1),(3,0,4),(0,2,1)]`
  - Output: Minimum cut = 3 (cutting edges (1,2) and (2,3) separates  graph)
- Example 2:
  - Input: `n=3`, `edges=[(0,1,5),(1,2,5),(2,0,5)]`
  - Output: Minimum cut = 10 (any two edges)
- Example 3:
  - Input: `n=5`, `edges=[(0,1,1),(1,2,1),(2,3,1),(3,4,1),(4,0,1)]`
  - Output: Minimum cut = 2

## Constraints

- `2 <= n <= 200` (number of vertices)
- `1 <= m <= 1000` (number of edges)
- `1 <= edge_weight <= 10^6`
- Graph is un directed and connected
- No self-loops or multiple edges

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public long minCutSmallGraph(int n, int[][] edges) {
        // edges[i] = {u, v, weight}
        // Use Stoer-Wagner algorithm for global min-cut
    }
}
```

### Python
```python
from typing import List, Tuple

def min_cut_small_graph(n: int, edges: List[Tuple[int, int, int]]) -> int:
    """
    Find the global minimum cut in an undirected weighted graph.
    
    Args:
        n: Number of vertices
        edges: List of undirected edges (u, v, weight)
    
    Returns:
        Minimum cut value
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
    ll minCutSmallGraph(int n, const vector<tuple<int,int,int>>& edges) {
        // Stoer-Wagner or run max flow for all pairs (slower)
    }
};
```

## Input Format

The input will be provided as:
- First line: Integers `n` (vertices) and `m` (edges)
- Next `m` lines: Three integers `u v w` representing an undirected edge

### Sample Input
```
4 5
0 1 2
1 2 3
2 3 1
3 0 4
0 2 1
```

## Hints

For small n, try all pairs as s-t and use max-flow, or use Stoer-Wagner algorithm.

## Quiz

### Question 1
What is the global min-cut problem?

A) Finding the minimum s-t cut for a specific source and sink  
B) Finding the minimum cut that separates any two parts of the graph (over all possible bipartitions)  
C) Finding the minimum spanning tree  
D) Finding the shortest path

**Correct Answer:** B

**Explanation:** The global min-cut finds the minimum-weight set of edges whose removal disconnects the graph, considering all possible bipartitions, not just a specific source-sink pair.

### Question 2
What is the time complexity of the Stoer-Wagner algorithm?

A) O(V³)  
B) O(V·E)  
C) O(E log V)  
D) O(V²)

**Correct Answer:** A

**Explanation:** The Stoer-Wagner algorithm runs in O(V³) or O(V²E) time depending on implementation, making it efficient for small graphs.

### Question 3
What theorem relates minimum cut to maximum flow?

A) Euler's Theorem  
B) Max-Flow Min-Cut Theorem  
C) König's Theorem  
D) Hall's Marriage Theorem

**Correct Answer:** B

**Explanation:** The Max-Flow Min-Cut Theorem states that in a network, the maximum flow from s to t equals the minimum capacity of an s-t cut.

### Question 4
For finding global min-cut by running max-flow for all pairs, what is the time complexity?

A) O(V² \u00b7 T_maxflow) where T_maxflow is time for one max-flow computation  
B) O(V \u00b7 E)  
C) O(E²)  
D) O(V³)

**Correct Answer:** A

**Explanation:** We need to run max-flow for all O(V²) pairs of vertices, so the total complexity is O(V² \u00b7 T_maxflow). For Dinic, this becomes O(V² \u00b7 V²E) = O(V⁴E).
