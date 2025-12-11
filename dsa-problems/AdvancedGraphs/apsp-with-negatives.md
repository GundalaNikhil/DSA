---
unique_problem_id: advgraph_004
display_id: ADVGRAPH-004
slug: apsp-with-negatives
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Shortest Paths
  - All-Pairs Shortest Path (APSP)
  - Johnson's Algorithm
  - Bellman-Ford Algorithm
  - Dijkstra's Algorithm
  - Floyd-Warshall Algorithm
  - Negative Edge Weights
  - Graph Reweighting
  - Vertex Potentials
---

# All-Pairs Shortest Path With Negative Edges

## Problem Description

Given weighted directed graph (no negative cycles), compute all-pairs shortest paths.

## Examples

- Example 1:
  - Input: `n=3`, `edges=[(0,1,2),(1,2,-1),(0,2,4)]`
  - Output: `dist[0][2]=1`, full matrix:
    ```
    [0, 2, 1]
    [INF, 0, -1]
    [INF, INF, 0]
    ```
- Example 2:
  - Input: `n=4`, `edges=[(0,1,1),(1,2,-2),(2,3,3),(3,1,2)]`
  - Output (one row): `dist[0]=[0,1,-1,2]` (no negative cycles, but a reweight is needed)
- Example 3:
  - Input: `n=5`, `edges=[(0,1,5),(1,2,-3),(2,3,2),(0,3,7),(3,4,1),(1,4,6)]`
  - Output: `dist[0]=[0,5,2,4,5]`, `dist[1]=[INF,0,-3,-1,0]`, ...
  - Explanation: Shortest path from 0 to 2 is 0→1→2 with cost 5+(-3)=2
- Example 4:
  - Input: `n=2`, `edges=[(0,1,-5)]`
  - Output:
    ```
    [0, -5]
    [INF, 0]
    ```

## Constraints

- `1 <= n <= 2000` (number of nodes)
- `0 <= m <= 5000` (number of edges, where 5000 = 5 × 10^3)
- Edge weights: `-10^9 <= w <= 10^9` (i.e., -1,000,000,000 to 1,000,000,000)
- Graph has **no negative-weight cycles** (guaranteed in input)
- All nodes are 0-indexed: `0 <= u, v < n`
- Use 64-bit integers (long long in C++/Java, int in Python) for accumulated distances to avoid overflow

## Function Signatures

### Java
```java
class Solution {
    // edges: list of {u,v,w}, 0-indexed, n nodes
    public long[][] apspWithNegatives(int n, int[][] edges) {
        // return n x n matrix, INF represented by Long.MAX_VALUE/4
    }
}
```

### Python
```python
from typing import List, Tuple

def apsp_with_negatives(n: int, edges: List[Tuple[int, int, int]]) -> List[List[int]]:
    """Return n x n distance matrix; use a large sentinel for INF."""
    ...
```

### C++
```cpp
using ll = long long;
const ll INF = (1LL<<60);

vector<vector<ll>> apspWithNegatives(int n, const vector<tuple<int,int,int>>& edges) {
    // implement Johnson or Floyd–Warshall depending on density
}
```

## Input Format

The input will be provided as:
- First line: Integers `n` (nodes) and `m` (edges).
- Next `m` lines: `u v w` describing a directed edge `u -> v` with weight `w`.

### Sample Input
```
3 3
0 1 2
1 2 -1
0 2 4
```

### Sample Output
```
0 2 1
INF 0 -1
INF INF 0
```

## Hints

Johnson’s algorithm (Bellman-Ford + Dijkstra).

## Quiz

### Question 1
For a sparse graph with `n` up to 2000 and `m` up to 5000, which APSP approach is typically most efficient?

A) Floyd–Warshall  
B) `n` times Bellman–Ford  
C) Johnson’s algorithm (1 Bellman–Ford + `n` Dijkstras)  
D) BFS from every node

**Correct Answer:** C

### Question 2
In Johnson’s algorithm, why is Bellman–Ford run once at the start?

A) To detect/handle negative cycles and compute vertex potentials  
B) To initialize Dijkstra’s priority queue  
C) To compress SCCs  
D) To remove parallel edges

**Correct Answer:** A

### Question 3
After reweighting edges with Bellman–Ford potentials, what property holds for all edges `(u,v)` with weight `w'`?

A) `w'` can still be negative  
B) `w'` is guaranteed non-negative  
C) `w'` is guaranteed positive  
D) `w'` becomes zero

**Correct Answer:** B

### Question 4
For dense graphs with `n <= 500`, which APSP algorithm is simplest and efficient enough?

A) Johnson’s  
B) BFS  
C) Floyd–Warshall  
D) Repeated DFS

**Correct Answer:** C

### Question 5
What is the time complexity of Johnson's algorithm for a graph with `n` nodes and `m` edges?

A) O(n³)  
B) O(n² log n + nm)  
C) O(nm log n)  
D) O(n·m + n²·log n)

**Correct Answer:** D

**Explanation:** Johnson's runs Bellman-Ford once in O(nm), then n Dijkstra runs in O(n²·log n) using binary heap (or O(n²+nm) with Fibonacci heap).

### Question 6
If the graph has no negative edges, what is the most efficient algorithm for APSP on a sparse graph?

A) Johnson's algorithm  
B) Floyd-Warshall  
C) Run Dijkstra from each vertex  
D) Run BFS from each vertex

**Correct Answer:** C

**Explanation:** Without negative edges, Johnson's reweighting step becomes unnecessary, so running Dijkstra n times is optimal for sparse graphs.
