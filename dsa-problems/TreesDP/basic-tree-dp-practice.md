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

## 4) Rerooting for Best Root
- Slug: rerooting-best-root
- Difficulty: Medium
- Problem: Find node minimizing sum of distances to all nodes using rerooting DP.
- Constraints: n<=2e5.
- Example:
  - Input: star with center 1
  - Output: center is best

## 5) Max Path Sum in Tree
- Slug: max-path-sum-tree
- Difficulty: Medium
- Problem: Node values may be negative; find max sum of any path (not necessarily root).
- Constraints: n<=2e5.
- Example:
  - Input: values [1,-2,3] with edges 1-2,1-3
  - Output: 4 (path 2-1-3? values 1-2+3=2? Actually 1+3=4)

## 6) Tree DP for Vertex Cover
- Slug: tree-vertex-cover
- Difficulty: Medium
- Problem: Minimum vertex cover on tree via DP (include/exclude).
- Constraints: n<=2e5.
- Example:
  - Input: chain of 3
  - Output: cover size 1 (middle)

## 7) Independent Set on Tree
- Slug: tree-independent-set
- Difficulty: Medium
- Problem: Max weight independent set on tree.
- Constraints: n<=2e5, weights up to 1e9.
- Example:
  - Input: chain weights [1,2,3]
  - Output: 4 (nodes 1 and 3)

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

## 12) Binary Lifting for K-th Ancestor
- Slug: kth-ancestor-binary-lifting
- Difficulty: Medium
- Problem: Preprocess to answer k-th ancestor query for any node.
- Constraints: n<=2e5.
- Example:
  - Input: node 3, k=1 => parent
  - Output: parent id

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
