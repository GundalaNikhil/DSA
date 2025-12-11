---
unique_problem_id: advgraph_006
display_id: ADVGRAPH-006
slug: articulation-and-bcc
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Graph Connectivity
  - Articulation Points
  - Biconnected Components
  - Tarjan's Algorithm
  - DFS
  - Lowlink Values
  - Cut Vertices
  - Block-Cut Tree
---

# Articulation Points and Biconnected Components

## Problem Description

Find articulation points and vertex-biconnected components in an undirected graph.

## Examples

- Example 1:
  - Input: `n=4`, `edges=[(0,1),(1,2),(2,0),(1,3)]`
  - Output: Articulation Points = {1}; BCCs: {0,1,2} and {1,3}
  - Explanation: Removing vertex 1 disconnects the graph, making it an articulation point
- Example 2:
  - Input: `n=6`, `edges=[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,3)]`
  - Output: Articulation Points = {2,3}; BCCs: {0,1,2}, {2,3}, {3,4,5}
- Example 3:
  - Input: `n=5`, `edges=[(0,1),(1,2),(2,3),(3,4)]`
  - Output: Articulation Points = {1,2,3}; BCCs: {0,1}, {1,2}, {2,3}, {3,4}
  - Explanation: In a path graph, all internal vertices are articulation points

## Constraints

- `1 <= n <= 200,000` (number of vertices, where 2e5 means 2 × 10^5)
- `0 <= m <= 200,000` (number of edges)
- Graph is undirected and may have multiple connected components
- No self-loops or multiple edges between same pair of vertices
- Vertices are 0-indexed: `0 <= u, v < n`

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    // Returns a pair: (List of articulation points, List of BCCs)
    // Each BCC is represented as a List<Integer> of vertices
    public Pair<List<Integer>, List<List<Integer>>> articulationAndBcc(int n, int[][] edges) {
        // Build adjacency list and apply Tarjan's algorithm
        // Return articulation points and biconnected components
    }
}
```

### Python
```python
from typing import List, Tuple, Set

def articulation_and_bcc(n: int, edges: List[Tuple[int, int]]) -> Tuple[Set[int], List[Set[int]]]:
    """
    Find articulation points and biconnected components.
    
    Args:
        n: Number of vertices
        edges: List of undirected edges (u, v)
    
    Returns:
        Tuple of (articulation_points, biconnected_components)
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
    // Returns pair: (articulation points, BCCs)
    pair<set<int>, vector<set<int>>> articulationAndBcc(int n, const vector<pair<int,int>>& edges) {
        // Tarjan's algorithm with edge stack
        // Return APs and BCCs
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
1 3
```

## Hints

Tarjan with stack of edges.

## Quiz

### Question 1
What is the time complexity of Tarjan's algorithm for finding articulation points and BCCs?

A) O(n²)  
B) O(n + m)  
C) O(n log n)  
D) O(m log m)

**Correct Answer:** B

**Explanation:** Tarjan's algorithm performs a single DFS traversal visiting each vertex and edge once, resulting in O(n + m) time.

### Question 2
What data structure is essential for tracking biconnected components during Tarjan's algorithm?

A) Priority queue  
B) Hash map  
C) Stack of edges  
D) Binary search tree

**Correct Answer:** C

**Explanation:** A stack of edges is maintained during DFS. When an articulation point is found, edges are popped to form a BCC.

### Question 3
In an undirected graph, a vertex `v` is an articulation point if:

A) Its degree is greater than 2  
B) Removing it increases the number of connected components  
C) It has a self-loop  
D) It is the vertex with maximum degree

**Correct Answer:** B

**Explanation:** An articulation point (or cut vertex) is one whose removal increases the number of connected components in the graph.

### Question 4
For a tree with `n` vertices, how many articulation points are there?

A) 0  
B) n - 2  
C) n - 1  
D) All non-leaf vertices

**Correct Answer:** D

**Explanation:** In a tree, every non-leaf vertex is an articulation point because removing it disconnects its subtree from the rest.

### Question 5
What does the "lowlink" value represent in Tarjan's algorithm?

A) The depth of a vertex in DFS  
B) The lowest discovery time reachable from a vertex's subtree  
C) The number of children of a vertex  
D) The degree of a vertex

**Correct Answer:** B

**Explanation:** The lowlink value of vertex v is the minimum discovery time of any vertex reachable from v through its DFS subtree, including back edges.
