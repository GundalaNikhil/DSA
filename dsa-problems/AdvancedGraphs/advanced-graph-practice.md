# Original Advanced Graphs & Flow Practice Set (16 Questions)

## 1) Minimum Cut on Small Graph
- Slug: min-cut-small-graph
- Difficulty: Medium
- Problem: Given an undirected weighted graph with n<=200 and m<=2000, compute the global minimum cut value.
- Hint: Use Stoer-Wagner algorithm.
- Example:
  - Input: n=4, edges [(0,1,1),(1,2,2),(2,3,1),(0,3,2)]
  - Output: 3

## 2) Max Flow With Vertex Capacities
- Slug: max-flow-vertex-capacity
- Difficulty: Medium
- Problem: Directed graph with edge capacities and vertex capacities. Compute max s-t flow respecting vertex limits.
- Hint: Split each vertex into in/out with an edge of vertex capacity; run Dinic/Edmonds-Karp.
- Constraints: n<=2000, m<=5000.
- Example:
  - Input: vertices 0..3, s=0, t=3, vertex caps [inf,3,2,inf], edges (0,1,3),(1,2,2),(2,3,3)
  - Output: 2

## 3) K Shortest Paths (Loopless)
- Slug: k-shortest-loopless-paths
- Difficulty: Medium
- Problem: Find the k shortest simple paths from s to t (length by edge weight) without cycles.
- Hint: Yen’s algorithm over Dijkstra for spur paths.
- Constraints: n<=500, k<=50.
- Example:
  - Input: graph 0-1 (1), 1-2 (1), 0-2 (3); k=2
  - Output: paths [0-1-2 length2, 0-2 length3]

## 4) All-Pairs Shortest Path With Negative Edges
- Slug: apsp-with-negatives
- Difficulty: Medium
- Problem: Given weighted directed graph (no negative cycles), compute all-pairs shortest paths.
- Hint: Johnson’s algorithm (Bellman-Ford + Dijkstra).
- Constraints: n<=2000, m<=5000.
- Example:
  - Input: n=3, edges (0,1,2),(1,2,-1),(0,2,4)
  - Output: dist[0][2]=1

## 5) Bridges and 2-Edge-Connected Components
- Slug: bridges-and-2ecc
- Difficulty: Medium
- Problem: Find all bridges and output 2-edge-connected components.
- Hint: DFS lowlink; union non-bridge edges.
- Constraints: n<=2e5, m<=2e5.
- Example:
  - Input: edges [(0,1),(1,2),(2,0),(2,3)]
  - Output: bridge (2,3); components {0,1,2}, {3}

## 6) Articulation Points and Biconnected Components
- Slug: articulation-and-bcc
- Difficulty: Medium
- Problem: Find articulation points and vertex-biconnected components in an undirected graph.
- Hint: Tarjan with stack of edges.
- Constraints: n<=2e5, m<=2e5.
- Example:
  - Input: edges [(0,1),(1,2),(2,0),(1,3)]
  - Output: AP={1}; BCCs: {0,1,2} and {1,3}

## 7) Eulerian Trail With Directed Edges
- Slug: eulerian-trail-directed
- Difficulty: Medium
- Problem: Determine if a directed graph has an Euler trail/path and output one if it exists.
- Hint: In/out degree check + Hierholzer.
- Constraints: n<=1e5, m<=2e5.
- Example:
  - Input: edges [(0,1),(1,2),(2,0)]
  - Output: path 0->1->2->0

## 8) Strongly Connected Components Compression
- Slug: scc-compression
- Difficulty: Easy-Medium
- Problem: Find SCCs and build the DAG of components (condensation graph).
- Hint: Kosaraju or Tarjan; then compress edges.
- Constraints: n<=2e5, m<=2e5.
- Example:
  - Input: edges [(0,1),(1,0),(1,2)]
  - Output: SCCs [{0,1},{2}], DAG edges [{0->1}]

## 9) Maximum Matching in Bipartite Graph
- Slug: bipartite-maximum-matching
- Difficulty: Medium
- Problem: Given bipartite graph (U,V,E), find maximum matching size and an example matching.
- Hint: Hopcroft-Karp.
- Constraints: |U|+|V| <= 1e5, m<=2e5.
- Example:
  - Input: U={0,1}, V={2,3}, edges (0,2),(1,2),(1,3)
  - Output: size 2, matching {(0,2),(1,3)}

## 10) Minimum Vertex Cover in Bipartite Graph
- Slug: bipartite-min-vertex-cover
- Difficulty: Medium
- Problem: Given a maximum matching, compute a minimum vertex cover using Kőnig’s theorem.
- Hint: BFS/DFS alternating paths from unmatched U vertices.
- Constraints: same as above.
- Example:
  - Input: same graph as matching example
  - Output: cover size 2 (vertices 1 and 2)

## 11) Dinic With Scaling
- Slug: dinic-with-scaling
- Difficulty: Medium
- Problem: Implement max flow with capacity scaling to improve on large capacities.
- Constraints: n<=5000, m<=2e4.
- Example:
  - Input: small network (0->1 cap10, 0->2 cap5, 1->3 cap7, 2->3 cap8)
  - Output: max flow 12

## 12) Minimum-Cost Flow With Demands
- Slug: mincost-flow-demands
- Difficulty: Hard
- Problem: Some edges have lower/upper bounds and costs. Nodes have supply/demand. Determine feasible flow and minimum cost if feasible.
- Hint: Convert to circulation with super source/sink; use potentials + SPFA/Dijkstra for min cost flow.
- Constraints: n<=500, m<=2000.
- Example:
  - Input: demands: s supply 5, t demand 5; edge s->t lower 2 upper 5 cost 1
  - Output: feasible, cost 5

## 13) K-Edge-Disjoint Paths
- Slug: k-edge-disjoint-paths
- Difficulty: Hard
- Problem: Determine if there exist k edge-disjoint paths from s to t in a directed graph; output yes/no.
- Hint: Transform to max flow with unit capacities.
- Constraints: n<=1e5, m<=2e5, k<=1e4.
- Example:
  - Input: s=0, t=3, edges (0,1),(1,3),(0,2),(2,3)
  - Output: yes for k=2

## 14) Tree Diameter With Edge Removal
- Slug: tree-diameter-after-removal
- Difficulty: Medium
- Problem: Given a tree, for each edge, compute the diameter of the graph if that edge is removed (two components). Return the maximum of these diameters.
- Hint: Precompute subtree heights and reroot; for each edge, diameter = max(diam(component1), diam(component2)).
- Constraints: n<=2e5.
- Example:
  - Input: tree edges (0-1,1-2,1-3)
  - Output: 2

## 15) Directed Cycle Basis
- Slug: directed-cycle-basis
- Difficulty: Hard
- Problem: Given a directed graph, find a basis of simple cycles (over GF(2) incidence) of minimal size (m - n + c). Output the cycles.
- Hint: Build spanning forest; add back edges to recover cycles via parent pointers.
- Constraints: n<=500, m<=2000.
- Example:
  - Input: edges (0->1,1->2,2->0,1->3,3->1)
  - Output: cycles [0-1-2-0,1-3-1]

## 16) Offline Lowest Common Ancestor with Modifications
- Slug: offline-lca-with-mods
- Difficulty: Hard
- Problem: Given a rooted tree, process operations: add edge (temporarily connecting two nodes), remove that added edge, and LCA queries between nodes considering currently active extra edges. Answer queries offline.
- Hint: Use DSU rollback on Euler tour intervals; segment tree over time for edge activations; LCA via binary lifting on base tree plus DSU connectivity.
- Constraints: n<=2e5, events<=2e5.
- Example:
  - Input: base tree edges (0-1,1-2,1-3); add extra edge (2-3) active during certain queries; query LCA(2,3) during active phase.
  - Output: LCA becomes 2 or 3 when edge makes them directly connected? Actually with extra edge, treat as connectivity query; answer 1 when only tree edges active.
