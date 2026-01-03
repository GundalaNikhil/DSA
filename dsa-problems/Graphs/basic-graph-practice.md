# Basic Graph Practice Set (15-18 Questions)

## 1) Campus Map BFS
- Slug: campus-map-bfs
- Difficulty: Easy
- Problem: Given an undirected unweighted graph (n nodes, adjacency list), perform BFS starting from node 0 and return visit order.
- Constraints: `1 <= n <= 10^5`, `0 <= edges <= 2*10^5`.
- Hint: Use a queue and visited array.
- Example:
  - Input: `n=4`, edges `[(0,1),(0,2),(1,3)]`
  - Output: `[0,1,2,3]`

## 2) Lab Network DFS
- Slug: lab-network-dfs
- Difficulty: Easy
- Problem: Perform DFS preorder on an undirected graph starting from node 0; return visited nodes in order.
- Constraints: Same as above.
- Hint: Recursive or stack-based; mark visited.
- Example:
  - Input: `n=5`, edges `[(0,1),(0,2),(1,4)]`
  - Output: `[0,1,4,2]`

## 3) Hostel Components Count
- Slug: hostel-components-count
- Difficulty: Medium
- Problem: Count connected components in an undirected graph.
- Constraints: `1 <= n <= 10^5`, `0 <= edges <= 2*10^5`.
- Hint: Iterate all nodes; BFS/DFS if unvisited.
- Example:
  - Input: `n=5`, edges `[(0,1),(2,3)]`
  - Output: `3`

## 4) Seminar Bipartite Check with Locked Nodes
- Slug: seminar-bipartite-check-locked
- Difficulty: Medium
- Problem: Some nodes are pre-colored either group A or group B and cannot change. Determine if the undirected graph can be colored to satisfy bipartite constraints while respecting locked nodes.
- Constraints: `1 <= n <= 10^5`, locked array length n with values {0=unlocked,1=force A,2=force B}.
- Hint: BFS/DFS coloring; if a locked node conflicts with its forced color, fail early.
- Example:
  - Input: `n=4`, edges `[(0,1),(1,2),(2,3),(3,0)]`, locked `[1,0,2,0]`
  - Output: `true`

## 5) Robotics Cycle Detector
- Slug: robotics-cycle-detector
- Difficulty: Medium
- Problem: Detect if an undirected graph contains any cycle.
- Constraints: `1 <= n <= 10^5`.
- Hint: DFS with parent tracking; back-edge indicates cycle.
- Example:
  - Input: `n=3`, edges `[(0,1),(1,2),(2,0)]`
  - Output: `true`

## 6) Lab Directed Cycle Check
- Slug: lab-directed-cycle-check
- Difficulty: Medium
- Problem: Given a directed graph, detect if it has a cycle.
- Constraints: `1 <= n <= 10^5`.
- Hint: DFS with recursion stack or Kahn’s topological sort; back-edge or leftover nodes indicates cycle.
- Example:
  - Input: `n=4`, edges `[(0,1),(1,2),(2,1),(2,3)]`
  - Output: `true`

## 7) Course Plan with Mandatory Pairs
- Slug: course-plan-mandatory-pairs
- Difficulty: Medium
- Problem: You are given prerequisites as a DAG and also pairs of courses that must appear adjacent (in any order) in the schedule. Produce a topological ordering that respects adjacency pairs if possible; otherwise return empty.
- Constraints: `1 <= n <= 10^5`, `0 <= edges <= 2*10^5`, `0 <= pairs <= 10^5`.
- Hint: First contract each adjacency pair into a super-node if it doesn’t violate prerequisites; then run Kahn’s on the contracted graph while expanding pairs appropriately.
- Example:
  - Input: `n=4`, edges `[(0,2),(1,2)]`, pairs `[(2,3)]`
  - Output: A valid order `[0,1,2,3]` (2 and 3 adjacent)

## 8) Shuttle Shortest Stops
- Slug: shuttle-shortest-stops
- Difficulty: Medium
- Problem: In an unweighted graph, find the shortest distance (edges) from a source `s` to all nodes.
- Constraints: `1 <= n <= 10^5`.
- Hint: BFS distances initialized to -1; distance of source is 0.
- Example:
  - Input: `n=5`, edges `[(0,1),(1,2),(0,3)]`, `s=0`
  - Output: `[0,1,2,1, -1]`

## 9) City Toll Dijkstra
- Slug: city-toll-dijkstra
- Difficulty: Medium
- Problem: Given a weighted directed graph with non-negative weights, compute single-source shortest paths.
- Constraints: `1 <= n <= 10^5`, `0 <= edges <= 2*10^5`, weights `<= 10^9`.
- Hint: Use Dijkstra with min-heap; store (dist,node).
- Example:
  - Input: `n=4`, edges `0->1 (2)`, `0->2 (5)`, `1->3 (4)`, `2->3 (1)`, `s=0`
  - Output: `[0,2,5,6]`

## 10) Battery Archipelago Analyzer
- Slug: battery-archipelago-analyzer
- Difficulty: Medium
- Problem: A grid stores elevation integers. Cells with elevation `> 0` are land, `0` is shallow water, `-1` is a bridge tile that does not count as land but connects land components 4-directionally. Count how many distinct land masses remain if bridges are removed, and also report the size of the largest land mass after bridges are removed.
- Constraints: `1 <= r,c <= 400`.
- Hint: First treat only `>0` as land to label components; bridges connect components but are not counted in size. Use BFS/DFS and a set union step over bridges.
- Example:
  - Input: `[[2,-1,3],[0,-1,0],[1,0,4]]`
  - Output: `Components = 2, Largest = 3`

## 11) Library Fire With Exhaustion
- Slug: library-fire-with-exhaustion
- Difficulty: Medium
- Problem: Grid cells are `0` empty, `1` wall, `2` fire source with stamina `s` (given in a parallel grid). Each minute, active fire cells spread to their 4 neighbors and their stamina decreases by 1; when a cell’s stamina reaches 0 it stops spreading further but stays burning. Compute minutes until no new cells ignite; if any empty cell never burns, return -1.
- Constraints: `1 <= r,c <= 200`, stamina values `1..10`.
- Hint: Multi-source BFS carrying remaining stamina; only enqueue neighbors while stamina > 0 and neighbor not wall/burning.
- Example:
  - Input grid: `[[2,0],[0,0]]`, stamina grid: `[[2,0],[0,0]]`
  - Output: `2`

## 12) Exam Seating Rooms with VIP Isolation
- Slug: exam-seating-rooms-vip
- Difficulty: Medium
- Problem: An undirected graph shows students who must sit together. VIP nodes (given) cannot be in the same component as any other VIP. Remove the minimum number of edges to ensure no component contains more than one VIP. Return the resulting maximum component size after removals.
- Constraints: `1 <= n <= 10^5`, `0 <= edges <= 2*10^5`.
- Hint: Run DSU; when an edge would merge two components each containing a VIP, skip that edge; track component sizes.
- Example:
  - Input: `n=5`, edges `[(0,1),(1,2),(3,4)]`, VIPs `{2,3}`
  - Output: `3` (edge (3,4) allowed; largest component size 3)

## 13) Robotics Bridges
- Slug: robotics-bridges
- Difficulty: Medium
- Problem: In an undirected graph, find all bridges (edges whose removal increases components).
- Constraints: `1 <= n <= 10^5`.
- Hint: Use Tarjan DFS with discovery/low times.
- Example:
  - Input: `n=5`, edges `[(0,1),(1,2),(2,0),(1,3),(3,4)]`
  - Output: `[(1,3),(3,4)]`

## 14) Lab Articulation Points
- Slug: lab-articulation-points
- Difficulty: Medium
- Problem: Find all articulation points in an undirected graph.
- Constraints: `1 <= n <= 10^5`.
- Hint: Tarjan with root child count rule.
- Example:
  - Input: `n=5`, edges `[(0,1),(1,2),(2,0),(1,3),(3,4)]`
  - Output: `[1,3]`

## 15) Shuttle Seating Assignment Feasibility
- Slug: shuttle-seating-assignment-feasibility
- Difficulty: Medium
- Problem: Given time constraints between tasks as directed edges (u before v), determine if a valid ordering exists and count how many nodes have zero in-degree in the final ordering step.
- Constraints: `1 <= n <= 10^5`.
- Hint: Run Kahn’s; if processed count < n, cycle exists; track in-degree zero pops.
- Example:
  - Input: `n=4`, edges `[(0,2),(1,2),(2,3)]`
  - Output: Ordering possible; zero in-degree pops were 2 (nodes 0 and 1 initially)

## 16) Campus Carpool Pairing
- Slug: campus-carpool-pairing
- Difficulty: Medium
- Problem: Given an undirected graph, find if there is any cycle of length 2 or more; if none, it is a forest; return true/false for being a forest.
- Constraints: `1 <= n <= 10^5`.
- Hint: Union-Find detecting existing parent connections.
- Example:
  - Input: `n=3`, edges `[(0,1),(1,2)]`
  - Output: `true`

## 17) Festival Maze Shortest Path
- Slug: festival-maze-shortest-path
- Difficulty: Medium
- Problem: Grid contains one start `S`, one exit `E`, at least one food stall `F`, walls `#`, and open cells `.`. You may move 4-directionally through non-wall cells. You must visit any food stall at least once before exiting. Find the minimum steps from `S` to `E` that satisfy the visit rule, or `-1` if impossible.
- Constraints: `1 <= r,c <= 400`; at least one `F`; `S` and `E` exist; total cells `<= 1.6 * 10^5`.
- Hint: BFS on state `(r,c,seenFood)` where `seenFood` is 0/1; first time a stall is reached flip the flag.
- Example:
  - Input:
    ```
    S F .
    # # E
    . F .
    ```
  - Output: `4` (path S→F(0,1)→(0,2)→(1,2)→E)

## 18) Robotics Weighted Reachability
- Slug: robotics-weighted-reachability
- Difficulty: Medium
- Problem: Given a weighted undirected graph and threshold `T`, count how many nodes are reachable from node 0 using only edges with weight <= T.
- Constraints: `1 <= n <= 10^5`, `1 <= edges <= 2*10^5`.
- Hint: BFS/DFS on filtered edges; or sort edges and union-find all with weight<=T then count component size of node 0.
- Example:
  - Input: `n=5`, edges `[(0,1,3),(1,2,7),(0,3,2),(3,4,5)]`, `T=4`
  - Output: `3` (nodes 0,1,3)
