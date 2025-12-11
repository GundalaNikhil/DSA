---
unique_problem_id: advgraph_003
display_id: ADVGRAPH-003
slug: offline-lca-with-mods
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Trees
  - Lowest Common Ancestor (LCA)
  - Offline Queries
  - Tarjan's Offline LCA
  - Union-Find
  - DFS
---

# Offline Lowest Common Ancestor with Modifications

## Problem Description

Given a rooted tree, process operations: add edge (temporarily connecting two nodes), remove that added edge, and LCA queries between nodes considering currently active extra edges. Answer queries offline.

## Examples

- Example 1:
  - Input: `n=5`, tree edges `[(0,1),(0,2),(1,3),(1,4)]`, queries `[(3,4),(2,4),(3,2)]`
  - Output: LCAs = [1, 0, 0]
  - Explanation: LCA(3,4)=1, LCA(2,4)=0, LCA(3,2)=0
- Example 2:
  - Input: `n=7`, tree edges `[(0,1),(1,2),(1,3),(3,4),(3,5),(5,6)]`, queries `[(2,4),(4,6),(2,6)]`
  - Output: LCAs = [1, 3, 1]

## Constraints

- `1 <= n <= 100,000` (number of vertices, where 1e5 means 1 × 10^5)
- `n-1` edges (tree structure)
- `1 <= q <= 100,000` (number of LCA queries)
- Vertices are 0-indexed: `0 <= u, v < n`
- Root is typically vertex 0 (can be any vertex)

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public int[] offlineLCA(int n, int[][] edges, int[][] queries) {
        // Use Tarjan's offline LCA algorithm with Union-Find
        // Return array of LCA results for each query
    }
}
```

### Python
```python
from typing import List, Tuple

def offline_lca(n: int, edges: List[Tuple[int, int]], 
                queries: List[Tuple[int, int]]) -> List[int]:
    """
    Answer multiple LCA queries offline using Tarjan's algorithm.
    
    Args:
        n: Number of vertices (tree nodes)
        edges: Tree edges (n-1 edges)
        queries: List of LCA queries (u, v)
    
    Returns:
        List of LCA answers corresponding to each query
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> offlineLCA(int n, const vector<pair<int,int>>& edges,
                          const vector<pair<int,int>>& queries) {
        // DFS with Union-Find to process queries in O(n + q \u00b7 α(n))
    }
};
```

## Input Format

The input will be provided as:
- First line: Integers `n` (vertices) and `q` (queries)
- Next `n-1` lines: Two integers `u v` representing tree edge
- Next `q` lines: Two integers `u v` representing LCA query

### Sample Input
```
5 3
0 1
0 2
1 3
1 4
3 4
2 4
3 2
```

## Hints

Use Tarjan's offline LCA algorithm combining DFS with Union-Find for efficient batch processing.

## Quiz

### Question 1
What is the time complexity of Tarjan's offline LCA algorithm?

A) O(n + q)  
B) O((n + q) \u00b7 α(n)) where α is the inverse Ackermann function  
C) O(n \u00b7 q)  
D) O(n²)

**Correct Answer:** B

**Explanation:** Tarjan's offline LCA uses DFS in O(n) and Union-Find operations for q queries in O(q\u00b7α(n)), where α is the inverse Ackermann function (effectively constant).

### Question 2
Why is this algorithm called "offline"?

A) It doesn't use the internet  
B) All queries must be known in advance before processing  
C) It works on disconnected graphs  
D) It processes one query at a time

**Correct Answer:** B

**Explanation:** The algorithm is "offline" because it requires knowing all queries beforehand, allowing it to process them together during a single DFS traversal for better efficiency.

### Question 3
What data structure is essential for Tarjan's offline LCA?

A) Priority queue  
B) Stack  
C) Union-Find (Disjoint Set Union)  
D) Binary search tree

**Correct Answer:** C

**Explanation:** Tarjan's algorithm uses Union-Find to merge sets of visited nodes and quickly determine the LCA when both nodes of a query have been visited.

### Question 4
For online LCA queries (answering one at a time without knowing future queries), what preprocessing technique is commonly used?

A) No preprocessing needed  
B) Binary lifting or Euler tour with RMQ  
C) Topological sort  
D) Bellman-Ford

**Correct Answer:** B

**Explanation:** For online LCA, techniques like binary lifting (O(log n) per query after O(n log n) preprocessing) or Euler tour with Range Minimum Query are used.
