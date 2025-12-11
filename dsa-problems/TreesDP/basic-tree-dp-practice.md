# Original Tree DP & LCA Practice Set (16 Questions)

## 1) Lowest Common Ancestor (Binary Lifting)
- Slug: lca-binary-lifting
- Difficulty: Easy-Medium
- Problem: Preprocess rooted tree for O(log n) LCA queries.
- Constraints: n<=2e5, q<=2e5.
- Example:
  - Input: tree 1-2,1-3; query LCA(2,3)
  - Output: 1

## 2) Tree Diameter DP
- Slug: tree-diameter-dp
- Difficulty: Easy-Medium
- Problem: Compute tree diameter using two DFS or DP of heights.
- Constraints: n<=2e5.
- Example:
  - Input: path of length 3
  - Output: 3

## 3) Subtree Sum and Size
- Slug: subtree-sum-size
- Difficulty: Easy
- Problem: For each node, compute sum and size of its subtree.
- Constraints: n<=2e5, values |a[i]|<=1e9.
- Example:
  - Input: tree 1-2,1-3, values [1,2,3]
  - Output: subtree sums [6,2,3]

## 4) Rerooting for Weighted Distance Variance
- Slug: rerooting-weighted-variance
- Difficulty: Medium
- Problem: Each node i has weight w[i]. Find node minimizing the weighted sum of squared distances to all nodes: sum(w[j] * dist(i,j)^2). Use rerooting DP adapted for squared terms.
- Constraints: n<=2e5, w[i] <= 10^6.
- Example:
  - Input: line 1-2-3 with w=[1,2,1]
  - Output: node 2 (weighted variance smallest)

## 5) Max Path Sum with Length Limit
- Slug: max-path-sum-length-limit
- Difficulty: Medium
- Problem: Node values may be negative; find maximum path sum where the path uses at most `L` edges.
- Constraints: n<=2e5, 1<=L<=n-1.
- Hint: DP keeping top two best downward paths by length; combine within length limit.
- Example:
  - Input: values [1,-2,3] edges 1-2,1-3, L=2
  - Output: 4 (path 1-3)

## 6) Tree DP for Vertex Cover
- Slug: tree-vertex-cover
- Difficulty: Medium
- Problem: Minimum vertex cover on tree via DP (include/exclude).
- Constraints: n<=2e5.
- Example:
  - Input: chain of 3
  - Output: cover size 1 (middle)

## 7) Distance-2 Independent Set on Tree
- Slug: tree-independent-set-distance2
- Difficulty: Medium
- Problem: Choose nodes with maximum total weight such that any two chosen nodes are at distance at least 3 (no adjacency and no common neighbor).
- Constraints: n<=2e5, weights up to 1e9.
- Hint: DP with states: choose node, choose child, or skip neighborhood.
- Example:
  - Input: chain weights [1,2,3]
  - Output: 3 (pick node3 only)

## 8) Tree Coloring (DP with k colors)
- Slug: tree-coloring-k
- Difficulty: Medium
- Problem: Count colorings of tree with k colors where adjacent nodes differ, modulo MOD.
- Constraints: n<=1e5, k<=1e5.
- Example:
  - Input: chain of 2, k=3
  - Output: 6

## 9) Path Queries with Euler + RMQ
- Slug: path-queries-rmq
- Difficulty: Medium
- Problem: Preprocess Euler tour depth array; answer LCA via RMQ; then compute distance between nodes quickly.
- Constraints: n<=2e5, q<=2e5.
- Example:
  - Input: tree 1-2,1-3; dist(2,3)
  - Output: 2

## 10) Tree DP for Number of Paths of Length K
- Slug: tree-paths-length-k
- Difficulty: Medium
- Problem: Count unordered pairs of nodes at distance exactly K using centroid decomposition or DFS with counts.
- Constraints: n<=2e5, K<=1e5.
- Example:
  - Input: path of 3 nodes, K=2
  - Output: 1

## 11) Heavy-Light Decomposition Basics
- Slug: heavy-light-basics
- Difficulty: Medium
- Problem: Decompose tree into chains for path queries (sum or max) with segment tree.
- Constraints: n<=2e5.
- Example:
  - Input: path queries for sum on edges
  - Output: correct sums

## 12) Binary Lifting for K-th Ancestor with Color Filter
- Slug: kth-ancestor-color-filter
- Difficulty: Medium
- Problem: Each node has a color. Preprocess to answer: given node v, color c, and k, find the k-th ancestor of v (in ancestor order) whose color equals c; return -1 if fewer than k such ancestors exist.
- Constraints: n<=2e5, q<=2e5.
- Hint: Binary lifting with per-color jump tables on compressed colors; or offline queries with Euler tour + Fenwick.
- Example:
  - Input: tree 1-2,1-3 with colors [red,blue,red]; query node3, color red, k=1 -> 1

## 13) DP on Tree for Max Matching
- Slug: tree-max-matching
- Difficulty: Medium
- Problem: Find maximum matching in a tree via DP.
- Constraints: n<=2e5.
- Example:
  - Input: path of 4
  - Output: matching size 2

## 14) Centroid Decomposition for Path Value Queries
- Slug: centroid-decomp-path-values
- Difficulty: Hard
- Problem: Given weighted tree, support updates of node values and queries for minimum distance + value to a marked node using centroid decomposition.
- Constraints: n<=2e5, q<=2e5.
- Example:
  - Input: toggle mark nodes, query min distance to mark
  - Output: sequence of answers

## 15) DP for Subtree LIS on Tree
- Slug: subtree-lis-tree
- Difficulty: Hard
- Problem: For each node, compute length of LIS of values along path from root to that node.
- Constraints: n<=2e5.
- Hint: Use multiset or Fenwick with coordinate compression during DFS.
- Example:
  - Input: tree 1-2,1-3 with values [2,1,3]
  - Output: [1,1,2]? Actually LIS to node1=1, node2=1, node3=2

## 16) Tree Flatten with Subtree Updates
- Slug: tree-flatten-subtree-updates
- Difficulty: Medium
- Problem: Flatten tree by Euler tour; support range add on subtree and point query on node value.
- Constraints: n<=2e5, q<=2e5.
- Example:
  - Input: initial values [1,2,3], add +1 to subtree of root, query node2
  - Output: node2 value 3
