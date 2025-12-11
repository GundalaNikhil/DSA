---
unique_problem_id: advgraph_014
display_id: ADVGRAPH-014
slug: k-shortest-loopless-paths
version: 1.0.0
difficulty: Hard
topic_tags:
  - Advanced Graphs
  - Shortest Paths
  - K Shortest Paths
  - Yen's Algorithm
  - Dijkstra's Algorithm
  - Path Finding
---

# K Shortest Paths (Loopless)

## Problem Description

Find the k shortest simple paths from s to t (length by edge weight) without cycles.

## Examples

- Example 1:
  - Input: `n=4`, `s=0`, `t=3`, `k=2`, `edges=[(0,1,1),(0,2,2),(1,3,1),(2,3,1)]`
  - Output: Paths: [0→1→3 (length 2), 0→2→3 (length 3)]
- Example 2:
  - Input: `n=3`, `s=0`, `t=2`, `k=3`, `edges=[(0,1,5),(1,2,3),(0,2,10)]`
  - Output: Paths: [0→1→2 (length 8), 0→2 (length 10)] (only 2 paths exist)
- Example 3:
  - Input: `n=5`, `s=0`, `t=4`, `k=1`, `edges=[(0,1,2),(1,2,3),(2,4,1),(0,3,10),(3,4,1)]`
  - Output: Path: [0→1→2→4 (length 6)]

## Constraints

- `2 <= n <= 1000` (number of vertices)
- `1 <= m <= 5000` (number of edges)
- `1 <= k <= 100` (number of paths to find)
- `1 <= edge_weight <= 10^6`
- Vertices are 0-indexed: `0 <= s, t < n`, `s ≠ t`

## Function Signatures

### Java
```java
import java.util.*;

class Solution {
    public List<Pair<List<Integer>, Long>> kShortestLooplessPaths(int n, int s, int t, int k, 
                                                                   int[][] edges) {
        // Return up to k shortest paths with their lengths
        // Use Yen's algorithm or similar
    }
}
```

### Python
```python
from typing import List, Tuple

def k_shortest_loopless_paths(n: int, s: int, t: int, k: int, 
                              edges: List[Tuple[int, int, int]]) -> List[Tuple[List[int], int]]:
    """
    Find k shortest simple paths from s to t.
    
    Args:
        n: Number of vertices
        s: Source vertex
        t: Target vertex
        k: Number of paths to find
        edges: List of directed edges (u, v, weight)
    
    Returns:
        List of (path, length) tuples for up to k shortest paths
    """
    pass
```

### C++
```cpp
#include <vector>
#include <utility>
using namespace std;
using ll = long long;

class Solution {
public:
    vector<pair<vector<int>, ll>> kShortestLooplessPaths(int n, int s, int t, int k,
                                                          const vector<tuple<int,int,int>>& edges) {
        // Yen's algorithm: iteratively find deviations from previous k-1 shortest paths
    }
};
```

## Input Format

The input will be provided as:
- First line: Integers `n`, `m`, `s`, `t`, `k`
- Next `m` lines: Three integers `u v w` representing directed edge with weight

### Sample Input
```
4 4 0 3 2
0 1 1
0 2 2
1 3 1
2 3 1
```

## Hints

Use Yen's algorithm: find shortest path, then iteratively find deviations.

## Quiz

### Question 1
What is the main idea behind Yen's algorithm for k shortest paths?

A) Run Dijkstra k times  
B) Iteratively find the next shortest path by considering deviations from previously found paths  
C) Use dynamic programming  
D) Find all paths and sort them

**Correct Answer:** B

**Explanation:** Yen's algorithm works by finding the shortest path first, then iteratively finding the next shortest path by systematically blocking parts of previous paths and finding deviations.

### Question 2
What is the time complexity of Yen's algorithm?

A) O(k·V·(E + V log V))  
B) O(E log E)  
C) O(V³)  
D) O(k·E)

**Correct Answer:** A

**Explanation:** Yen's algorithm runs k iterations, each involving up to V Dijkstra computations (one for each spur node), giving O(k·V·(E + V log V)) with a binary heap.

### Question 3
Why must the paths be loopless (simple)?

A) To reduce time complexity  
B) Because paths with loops can have arbitrarily many variations with different lengths  
C) To save memory  
D) It's not necessary

**Correct Answer:** B

**Explanation:** If loops were allowed, there could be infinitely many paths or the number of distinct path lengths could grow exponentially, making the k shortest paths problem ill-defined or trivial.

### Question 4
What data structure is typically used to maintain candidate paths in Yen's algorithm?

A) Stack  
B) Priority queue (min-heap) ordered by path length  
C) Hash map  
D) Array

**Correct Answer:** B

**Explanation:** A priority queue (min-heap) is used to efficiently retrieve the shortest candidate path in each iteration of Yen's algorithm.
