---
unique_problem_id: advgraph_015
display_id: ADVGRAPH-015
slug: directed-cycle-basis
version: 1.0.0
difficulty: Hard
topic_tags:
  - Advanced Graphs
  - Cycle Basis
  - Directed Graphs
  - DFS
  - Spanning Forest
  - Graph Theory
  - Fundamental Cycles
---

# Directed Cycle Basis

## Problem Description

Given a directed graph, find a basis of simple cycles (over GF(2) incidence) of minimal size (m - n + c). Output the cycles.

## Examples

- Example 1:
  - Input: `n=4`, `edges=[(0,1),(1,2),(2,0),(1,3),(3,1)]`
  - Output: Cycles = [[0,1,2,0], [1,3,1]]
  - Explanation: Two fundamental cycles form the basis
- Example 2:
  - Input: `n=5`, `edges=[(0,1),(1,2),(2,3),(3,4),(4,2)]`
  - Output: Cycles = [[2,3,4,2]]
  - Explanation: Only one cycle in the graph

## Constraints

- `1 <= n <= 500` (number of vertices)
- `1 <= m <= 2000` (number of edges, where 2e3 means 2 × 10^3)
- Vertices are 0-indexed: `0 <= u, v < n`
- Graph may have multiple connected components

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public List<List<Integer>> directedCycleBasis(int n, int[][] edges) {
        // Return list of cycles, each cycle is a list of vertices
        // Build spanning forest, add back-edges to form fundamental cycles
    }
}
```

### Python
```python
from typing import List, Tuple

def directed_cycle_basis(n: int, edges: List[Tuple[int, int]]) -> List[List[int]]:
    """
    Find a fundamental cycle basis for the directed graph.
    
    Args:
        n: Number of vertices
        edges: List of directed edges
    
    Returns:
        List of cycles, each represented as a list of vertices
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> directedCycleBasis(int n, const vector<pair<int,int>>& edges) {
        // DFS to build spanning forest
        // For each back edge, trace cycle using parent pointers
    }
};
```

## Input Format

The input will be provided as:
- First line: Integers `n` (vertices) and `m` (edges)
- Next `m` lines: Two integers `u v` representing a directed edge

### Sample Input
```
4 5
0 1
1 2
2 0
1 3
3 1
```

## Hints

Build spanning forest; add back edges to recover cycles via parent pointers.

## Quiz

### Question 1
What is the size of a minimal cycle basis in a directed graph with n vertices, m edges, and c connected components?

A) m - n  
B) m - n + c  
C) n - c  
D) m

**Correct Answer:** B

**Explanation:** The cycle space dimension for a graph with n vertices, m edges, and c components is m - n + c. This is the minimum number of fundamental cycles needed.

### Question 2
How are fundamental cycles identified during DFS?

A) By detecting all edges  
B) By identifying back edges (edges to ancestors in DFS tree) and tracing the path back  
C) By using BFS  
D) By sorting edges

**Correct Answer:** B

**Explanation:** During DFS, back edges (edges pointing to an ancestor in the DFS tree) indicate cycles. The cycle can be traced by following parent pointers from the descendant back to the ancestor.

### Question 3
What is the time complexity of finding a cycle basis using DFS?

A) O(V + E)  
B) O(V²)  
C) O(E²)  
D) O(V·E)

**Correct Answer:** A

**Explanation:** DFS traversal takes O(V + E) time, and tracing each fundamental cycle takes time proportional to the cycle length, which sums to O(V + E) overall.

### Question 4
In a DAG (Directed Acyclic Graph), how many cycles are in the cycle basis?

A) n - 1  
B) 0  
C) m  
D) n

**Correct Answer:** B

**Explanation:** A DAG has no cycles by definition, so the cycle basis is empty (size 0).
