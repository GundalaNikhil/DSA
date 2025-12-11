---
unique_problem_id: advgraph_005
display_id: ADVGRAPH-005
slug: bridges-and-2ecc
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Graph Connectivity
  - Bridges
  - 2-Edge-Connected Components
  - Tarjan's Algorithm
  - DFS
  - Lowlink Values
  - Cut Edges
---

# Bridges and 2-Edge-Connected Components

## Problem Description

Find all bridges and output 2-edge-connected components.

## Examples

- Example 1:
  - Input: `n=4`, `edges=[(0,1),(1,2),(2,0),(2,3)]`
  - Output: Bridges = {(2,3)}; 2-ECCs: {0,1,2}, {3}
  - Explanation: Edge (2,3) is a bridge because removing it disconnects vertex 3
- Example 2:
  - Input: `n=6`, `edges=[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,3)]`
  - Output: Bridges = {(2,3)}; 2-ECCs: {0,1,2}, {3,4,5}
- Example 3:
  - Input: `n=5`, `edges=[(0,1),(1,2),(2,3),(3,4)]`
  - Output: Bridges = {(0,1),(1,2),(2,3),(3,4)}; 2-ECCs: {0}, {1}, {2}, {3}, {4}
  - Explanation: In a tree, every edge is a bridge

## Constraints

- `1 <= n <= 200,000` (number of vertices, where 2e5 means 2 × 10^5)
- `0 <= m <= 200,000` (number of edges)
- Graph is undirected and may have multiple connected components
- No self-loops or multiple edges
- Vertices are 0-indexed: `0 <= u, v < n`

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    // Returns: (List of bridge edges, List of 2-ECCs)
    public Pair<List<int[]>, List<Set<Integer>>> bridgesAnd2ecc(int n, int[][] edges) {
        // Apply Tarjan's algorithm with DFS
        // Return bridges and 2-edge-connected components
    }
}
```

### Python
```python
from typing import List, Tuple, Set

def bridges_and_2ecc(n: int, edges: List[Tuple[int, int]]) -> Tuple[List[Tuple[int, int]], List[Set[int]]]:
    """
    Find bridges and 2-edge-connected components.
    
    Args:
        n: Number of vertices
        edges: List of undirected edges
    
    Returns:
        Tuple of (bridges, 2-edge-connected components)
    """
    pass
```

### C++
```cpp
#include <vector>
#include <set>
using namespace std;

class Solution {
public:
    pair<vector<pair<int,int>>, vector<set<int>>> bridgesAnd2ecc(int n, 
                                                     const vector<pair<int,int>>& edges) {
        // Tarjan's DFS with lowlink values
        // Union non-bridge edges for 2-ECCs
    }
};
```

## Input Format

The input will be provided as:
- First line: Integers `n` (vertices) and `m` (edges)
- Next `m` lines: Two integers `u v` representing an undirected edge

### Sample Input
```
4 4
0 1
1 2
2 0
2 3
```

## Hints

DFS lowlink; union non-bridge edges.

## Quiz

### Question 1
What is the time complexity of finding all bridges using Tarjan's algorithm?

A) O(n²)  
B) O(n + m)  
C) O(n log n)  
D) O(m log m)

**Correct Answer:** B

**Explanation:** Tarjan's algorithm performs a single DFS traversal, visiting each vertex and edge once, resulting in O(n + m) time complexity.

### Question 2
An edge (u, v) is a bridge if and only if:

A) u and v have the same lowlink value  
B) There is no back edge from the subtree of v to an ancestor of u  
C) The degree of u or v is 1  
D) (u, v) is part of a cycle

**Correct Answer:** B

**Explanation:** An edge (u, v) is a bridge if there's no alternative path from v's subtree back to u or its ancestors, meaning low[v] > disc[u].

### Question 3
What is a 2-edge-connected component?

A) A maximal subgraph with at least 2 edges  
B) A maximal subgraph where every pair of vertices has at least 2 edge-disjoint paths  
C) A subgraph with exactly 2 connected components  
D) A tree with 2 edges

**Correct Answer:** B

**Explanation:** A 2-edge-connected component is a maximal set of vertices where any two vertices remain connected even after removing any single edge.

### Question 4
How do we find 2-edge-connected components after identifying bridges?

A) Remove all bridges and find connected components  
B) Use BFS from each vertex  
C) Apply Dijkstra's algorithm  
D) Use dynamic programming

**Correct Answer:** A

**Explanation:** After finding all bridges, removing them from the graph and finding connected components in the remaining graph gives the 2-edge-connected components.

### Question 5
In a tree with n vertices, how many bridges are there?

A) 0  
B) n - 1  
C) n  
D) n - 2

**Correct Answer:** B

**Explanation:** A tree with n vertices has exactly n-1 edges, and all edges in a tree are bridges since removing any edge disconnects the tree.
