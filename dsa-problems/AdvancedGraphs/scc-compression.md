---
unique_problem_id: advgraph_008
display_id: ADVGRAPH-008
slug: scc-compression
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Advanced Graphs
  - Strongly Connected Components
  - Graph Condensation
  - Kosaraju's Algorithm
  - Tarjan's Algorithm
  - DAG
  - DFS
  - Graph Compression
---

# Strongly Connected Components Compression

## Problem Description

Find SCCs and build the DAG of components (condensation graph).

## Examples

- Example 1:
  - Input: `n=3`, `edges=[(0,1),(1,0),(1,2)]`
  - Output: SCCs = [{0,1},{2}]; DAG edges = [(SCC0, SCC1)]
  - Explanation: Vertices 0 and 1 form a cycle, vertex 2 is its own SCC
- Example 2:
  - Input: `n=5`, `edges=[(0,1),(1,2),(2,0),(1,3),(3,4),(4,3)]`
  - Output: SCCs = [{0,1,2},{3,4}]; DAG edges = [(SCC0, SCC1)]
- Example 3:
  - Input: `n=4`, `edges=[(0,1),(1,2),(2,3)]`
  - Output: SCCs = [{0},{1},{2},{3}]; DAG edges = [(0,1),(1,2),(2,3)]
  - Explanation: No cycles means each vertex is its own SCC

## Constraints

- `1 <= n <= 200,000` (number of vertices, where 2e5 means 2 × 10^5)
- `0 <= m <= 200,000` (number of directed edges)
- Vertices are 0-indexed: `0 <= u, v < n`
- Graph may have multiple SCCs and may not be fully connected

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    // Returns: (List of SCCs, List of condensation DAG edges)
    public Pair<List<Set<Integer>>, List<int[]>> sccCompression(int n, int[][] edges) {
        // Apply Kosaraju or Tarjan's algorithm
        // Build condensation graph from SCCs
    }
}
```

### Python
```python
from typing import List, Tuple, Set

def scc_compression(n: int, edges: List[Tuple[int, int]]) -> Tuple[List[Set[int]], List[Tuple[int, int]]]:
    """
    Find SCCs and build the condensation DAG.
    
    Args:
        n: Number of vertices
        edges: List of directed edges
    
    Returns:
        Tuple of (SCCs, condensation DAG edges)
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
    pair<vector<set<int>>, vector<pair<int,int>>> sccCompression(int n, 
                                                    const vector<pair<int,int>>& edges) {
        // Kosaraju: DFS + reverse DFS, or Tarjan with stack
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
1 0
1 2
```

## Hints

Kosaraju or Tarjan; then compress edges.

## Quiz

### Question 1
What is the time complexity of Kosaraju's and Tarjan's algorithms for finding SCCs?

A) O(V + E)  
B) O(V log V)  
C) O(V²)  
D) O(E log E)

**Correct Answer:** A

**Explanation:** Both Kosaraju's and Tarjan's algorithms perform DFS traversals, resulting in O(V + E) time complexity.

### Question 2
What is the key difference between Kosaraju's and Tarjan's SCC algorithms?

A) Time complexity  
B) Kosaraju uses two DFS passes(one on original, one on transposed graph), Tarjan uses one DFS with a stack  
C) Space complexity  
D) Tarjan only works on DAGs

**Correct Answer:** B

**Explanation:** Kosaraju's algorithm requires two DFS passes (one on the original graph and one on its transpose), while Tarjan's algorithm finds SCCs in a single DFS using lowlink values and a stack.

### Question 3
What property does the condensation graph (DAG of SCCs) always have?

A) It has cycles  
B) It is acyclic (DAG)  
C) It is a tree  
D) It is fully connected

**Correct Answer:** B

**Explanation:** The condensation graph is always a DAG (Directed Acyclic Graph) because edges only go between different SCCs, and by definition, there can be no cycles between SCCs.

### Question 4
In Kosaraju's algorithm, what is the purpose of processing vertices in decreasing order of finish time from the first DFS?

A) To improve time complexity  
B) To ensure we visit SCCs in topological order of the condensation DAG  
C) To reduce space usage  
D) It's not necessary, any order works

**Correct Answer:** B

**Explanation:** Processing vertices in decreasing order of finish time ensures that we process SCCs in reverse topological order, which allows us to correctly identify each SCC in the second DFS pass.
