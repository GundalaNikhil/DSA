# Original Graph Basics Practice Set (16 Questions)

## 1) BFS Shortest Path Unweighted
- Slug: bfs-shortest-path-unweighted
- Difficulty: Easy
- Problem: Given unweighted undirected graph, compute shortest path length from s to all nodes.
- Constraints: n<=1e5, m<=2e5.
- Example:
  - Input: n=4, edges [(0,1),(1,2),(0,3)]
  - Output: dist from 0 = [0,1,2,1]

## 2) DFS Connected Components
- Slug: dfs-connected-components
- Difficulty: Easy
- Problem: Count connected components in undirected graph; label nodes.
- Constraints: n<=1e5.
- Example:
  - Input: edges [(0,1),(2,3)]
  - Output: 2 components

## 3) Dijkstra with Binary Heap
- Slug: dijkstra-binary-heap
- Difficulty: Medium
- Problem: Single-source shortest paths with non-negative weights.
- Constraints: n<=1e5, m<=2e5.
- Example:
  - Input: edges (0->1,1), (1->2,2), (0->2,5)
  - Output: dist[0]=0, dist[2]=3

## 4) Bellman-Ford Negative Edges
- Slug: bellman-ford
- Difficulty: Medium
- Problem: Shortest paths with possible negative edges; detect negative cycle reachable from s.
- Constraints: n<=1e4, m<=5e4.
- Example:
  - Input: edges (0->1,-1),(1->0,-1)
  - Output: negative cycle

## 5) Topological Sort (Kahn)
- Slug: topo-sort-kahn
- Difficulty: Easy-Medium
- Problem: Given DAG, output one topological order.
- Constraints: n<=1e5.
- Example:
  - Input: edges (0->1),(1->2)
  - Output: [0,1,2]

## 6) Detect Cycle in Directed Graph
- Slug: detect-cycle-directed
- Difficulty: Easy-Medium
- Problem: Determine if directed graph has a cycle using DFS colors or Kahn.
- Constraints: n<=1e5.
- Example:
  - Input: edges (0->1),(1->2),(2->0)
  - Output: true

## 7) MST Kruskal
- Slug: mst-kruskal
- Difficulty: Medium
- Problem: Compute MST weight of undirected weighted graph using Kruskal.
- Constraints: n<=1e5, m<=2e5.
- Example:
  - Input: edges (0-1,1),(1-2,2),(0-2,3)
  - Output: MST weight 3

## 8) MST Prim
- Slug: mst-prim
- Difficulty: Medium
- Problem: Compute MST weight using Prim with min-heap.
- Constraints: connected graph, n<=1e5.
- Example:
  - Input: same as above
  - Output: 3

## 9) Bipartite Check BFS
- Slug: bipartite-check-bfs
- Difficulty: Easy-Medium
- Problem: Check if undirected graph is bipartite; output one 2-coloring or report odd cycle.
- Constraints: n<=1e5.
- Example:
  - Input: triangle graph
  - Output: not bipartite

## 10) Articulation Points (DFS)
- Slug: articulation-points-basic
- Difficulty: Medium
- Problem: Find all articulation points in undirected graph.
- Constraints: n<=1e5, m<=2e5.
- Example:
  - Input: edges (0-1),(1-2),(2-0),(1-3)
  - Output: {1}

## 11) Bridges (DFS)
- Slug: bridges-basic
- Difficulty: Medium
- Problem: Find all bridges in undirected graph.
- Constraints: n<=1e5.
- Example:
  - Input: edges (0-1),(1-2),(2-0),(1-3)
  - Output: (1,3)

## 12) Disjoint Set Union Basics
- Slug: dsu-basics
- Difficulty: Easy
- Problem: Support union and find queries; detect connectivity online.
- Constraints: n<=2e5.
- Example:
  - Input: union(0,1), union(2,3), query(0,3)
  - Output: false

## 13) 2-SAT Satisfiability
- Slug: two-sat
- Difficulty: Medium
- Problem: Given clauses (xi or yj), determine satisfiability and output assignment if exists using implication graph + SCC.
- Constraints: variables<=1e5, clauses<=2e5.
- Example:
  - Input: (x1 or x2), (!x1 or !x2)
  - Output: satisfiable assignment x1=true,x2=false

## 14) Shortest Path in DAG
- Slug: shortest-path-dag
- Difficulty: Easy-Medium
- Problem: Given weighted DAG, compute shortest paths from s via topo order.
- Constraints: n<=1e5, m<=2e5.
- Example:
  - Input: edges (0->1,1),(1->2,2)
  - Output: dist[2]=3

## 15) Floyd-Warshall All-Pairs
- Slug: floyd-warshall
- Difficulty: Medium
- Problem: APSP for n<=500 using Floyd-Warshall; detect negative cycles.
- Constraints: n<=500.
- Example:
  - Input: 3-node graph
  - Output: distance matrix

## 16) Euler Tour of Tree (Array Flatten)
- Slug: euler-tour-flatten
- Difficulty: Medium
- Problem: Given rooted tree, produce entry/exit times to flatten subtree ranges for segment tree use.
- Constraints: n<=2e5.
- Example:
  - Input: root 1 with children 2,3
  - Output: tin/tout arrays
