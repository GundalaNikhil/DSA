---
unique_problem_id: advgraph_010
display_id: ADVGRAPH-010
slug: bipartite-min-cost-vertex-cover
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Bipartite Graphs
  - Vertex Cover
  - Minimum Cost
  - Network Flow
  - Min-Cut
  - Max-Flow Min-Cut Theorem
  - König's Theorem
---

# Minimum Cost Vertex Cover in Bipartite Graph

## Problem Description

Bipartite graph with weights on vertices. Find vertex cover of minimum total weight.

## Examples

- Example 1:
  - Input: `weightsU=[3,1]`, `weightsV=[2,2]`, `edges=[(0,2),(1,2),(1,3)]`
  - Output: Minimum cost = 3 (select vertex 1 from U with weight 1, and vertex 3 from V with weight 2)
  - Explanation: This covers all edges: (1,2) covered by vertex 1, (1,3) covered by both, (0,2) covered by vertex 3
- Example 2:
  - Input: `weightsU=[5,4]`, `weightsV=[3,3,3]`, `edges=[(0,2),(0,3),(1,3),(1,4)]`
  - Output: Minimum cost = 6 (select vertices 3 and 4 from V, cost 3+3=6)
- Example 3:
  - Input: `weightsU=[10]`, `weightsV=[1,1,1]`, `edges=[(0,1),(0,2),(0,3)]`
  - Output: Minimum cost = 3 (select all V vertices)

## Constraints

- `1 <= |U| + |V| <= 100,000` (total nodes, where 1e5 means 1 × 10^5)
- `0 <= m <= 200,000` (number of edges, where 2e5 means 2 × 10^5)
- `1 <= weight[v] <= 10^9` for all vertices
- Graph is bipartite with edges only between U and V partitions

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public long minCostVertexCover(int[] weightsU, int[] weightsV, int[][] edges) {
        // Return minimum total weight of vertex cover
        // Use min-cut: source to U with cost, V to sink with cost, inf on edges
    }
}
```

### Python
```python
from typing import List, Tuple

def min_cost_vertex_cover(weights_u: List[int], weights_v: List[int], 
                          edges: List[Tuple[int, int]]) -> int:
    """
    Find minimum cost vertex cover in weighted bipartite graph.
    
    Args:
        weights_u: Weights of vertices in U partition
        weights_v: Weights of vertices in V partition  
        edges: Bipartite edges (u, v)
    
    Returns:
        Minimum total weight of vertex cover
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
    ll minCostVertexCover(vector<int>& weightsU, vector<int>& weightsV,
                          vector<pair<int,int>>& edges) {
        // Reduce to min-cut problem
        // sum(all weights) - max_flow gives min vertex cover cost
    }
};
```

## Input Format

The input will be provided as:
- First line: Three integers `|U|`, `|V|`, `m`
- Second line: `|U|` integers (weights of U vertices)
- Third line: `|V|` integers (weights of V vertices)
- Next `m` lines: Two integers `u v` (edge from U[u] to V[v])

### Sample Input
```
2 2 3
3 1
2 2
0 2
1 2
1 3
```

## Hints

Reduce to min-cut: add source to U with capacity weight, V to sink with weight, infinite capacities on edges.

## Quiz

### Question 1
How is the minimum cost vertex cover problem in a bipartite graph reduced to min-cut?

A) Add source to all vertices with infinite capacity  
B) Connect source to U with vertex weights, V to sink with vertex weights, and infinite capacity on original edges  
C) Use dynamic programming on the graph  
D) Apply greedy selection

**Correct Answer:** B

**Explanation:** We create a flow network: source → U vertices (capacity = weight), original edges (capacity = ∞), V vertices → sink (capacity = weight). The min-cut corresponds to min-cost vertex cover.

### Question 2
What theorem relates minimum vertex cover to maximum matching in unweighted bipartite graphs?

A) Hall's Marriage Theorem  
B) König's Theorem  
C) Menger's Theorem  
D) Max-Flow Min-Cut Theorem

**Correct Answer:** B

**Explanation:** König's Theorem states that in a bipartite graph, the size of minimum vertex cover equals the size of maximum matching.

### Question 3
Why are original graph edges given infinite capacity in the min-cut reduction?

A) To speed up computation  
B) To ensure they are never cut (forcing cuts only on source-U or V-sink edges)  
C) To maximize flow  
D) To minimize memory usage

**Correct Answer:** B

**Explanation:** Infinite capacity ensures original edges are never part of the min-cut. The cut must separate source from sink by cutting source-U or V-sink edges, which represent vertex selection.

### Question 4
What is the relationship between the min-cut value and the min-cost vertex cover?

A) They are equal  
B) Min-cut = sum of all weights - min-cost vertex cover  
C) Min-cost vertex cover = sum of all weights - min-cut  
D) They are unrelated

**Correct Answer:** A

**Explanation:** The min-cut value directly equals the minimum cost vertex cover. Vertices on the source side of the cut from U and sink side from V form the vertex cover.

### Question 5
For an unweighted bipartite graph, what is the time complexity to find minimum vertex cover?

A) O(V³)  
B) O(E√V) using Hopcroft-Karp  
C) O(E²)  
D) O(V²E)

**Correct Answer:** B

**Explanation:** For unweighted graphs, find maximum matching using Hopcroft-Karp in O(E√V), then apply König's theorem to construct the minimum vertex cover.
