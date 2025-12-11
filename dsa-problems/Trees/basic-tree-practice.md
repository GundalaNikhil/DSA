# Basic Tree Practice Set (15-18 Questions)

## 1) Campus Directory Traversal
- Slug: campus-directory-traversal
- Difficulty: Easy
- Problem: Given a binary tree, return its preorder, inorder, and postorder traversals as three separate lists.
- Constraints: `1 <= n <= 10^5`, node values fit in 32-bit int.
- Hint: Use recursion or explicit stacks; beware stack depth for skewed trees.
- Example:
  - Input: Tree with preorder `[4, 2, 1, 3, 6]`, inorder `[1, 2, 3, 4, 6]`
  - Output: Preorder `[4,2,1,3,6]`, Inorder `[1,2,3,4,6]`, Postorder `[1,3,2,6,4]`

## 2) Lab Tree Height
- Slug: lab-tree-height
- Difficulty: Easy
- Problem: Compute the height of a binary tree (edges on longest root-to-leaf path).
- Constraints: `0 <= n <= 10^5`.
- Hint: Recursively `1 + max(left, right)`; empty tree height is -1 or 0 by convention—state which you use.
- Example:
  - Input: Tree `5` with children `3` and `9`, and `3` has child `1`
  - Output: `2`

## 3) Garden Leaf Count
- Slug: garden-leaf-count
- Difficulty: Easy
- Problem: Count the number of leaf nodes in a binary tree.
- Constraints: `0 <= n <= 10^5`.
- Hint: Leaf when both children are null.
- Example:
  - Input: Tree `7` with children `4` and `8`; `4` has children `1` and `6`
  - Output: `3`

## 4) Seminar Level Order
- Slug: seminar-level-order
- Difficulty: Easy-Medium
- Problem: Return a list of levels for a binary tree (nodes from top to bottom, left to right).
- Constraints: `0 <= n <= 10^5`.
- Hint: BFS with a queue; track level size.
- Example:
  - Input: Tree `10` -> left `5`, right `12`, and `5` has child `7`
  - Output: `[[10],[5,12],[7]]`

## 5) Robotics Mirror Check with Colors
- Slug: robotics-mirror-check-colors
- Difficulty: Easy-Medium
- Problem: Each node has a value and a color bit (0/1). Determine if the tree is symmetric in structure and values, and also the multiset of colors on each mirrored level must match (but colors need not match node-for-node).
- Constraints: `0 <= n <= 10^5`.
- Hint: Compare mirrored nodes for value equality and collect colors per level; both structural mirror and level-color multisets must align.
- Example:
  - Input: Root `4`(0), children `2`(1) and `2`(1), grandchildren `1`(0),`3`(1) mirrored with swapped colors
  - Output: `true`

## 6) Lab Path Sum with Exactly One Turn
- Slug: lab-path-sum-one-turn
- Difficulty: Medium
- Problem: Given a target sum, determine if there exists a path from some node downwards that first moves only left, then only right (exactly one direction change allowed), ending at any node (not necessarily leaf), whose node values sum to target.
- Constraints: `0 <= n <= 10^5`, `-10^9 <= val <= 10^9`.
- Hint: Precompute prefix sums along left and right chains; DFS keeping hash maps of downward sums; check combinations at each pivot node.
- Example:
  - Input: Tree with root `5` left `3` (left `2`, right `1`), right `8`; target `9`
  - Output: `true` (path 3 -> 2 -> 1 with a turn)

## 7) Sports Dome Weighted Diameter
- Slug: sports-dome-weighted-diameter
- Difficulty: Medium
- Problem: Edges of the binary tree have non-negative weights. Find the maximum total edge weight on any path between two nodes.
- Constraints: `0 <= n <= 10^5`, edge weights `0..10^9`.
- Hint: DFS returning best downward path weight; update answer with sum of two child paths plus their edge weights.
- Example:
  - Input: Root `1` with left child `2` (edge 4) and right child `3` (edge 1); `2` has left `4` (edge 2)
  - Output: `6` (path 4-2-1-3)

## 8) Hostel Boundary Walk with Gaps
- Slug: hostel-boundary-walk-gaps
- Difficulty: Medium
- Problem: Same boundary walk but skip any boundary node whose value is negative; keep traversal order otherwise. Return the boundary list after skipping those nodes.
- Constraints: `1 <= n <= 10^5`, node values 32-bit int.
- Hint: Standard boundary collection; filter out negatives at each stage; avoid duplicates.
- Example:
  - Input: Tree `10` with left `-5` (child `2`) and right `15` (child `-20`)
  - Output: `[10,2,15]`

## 9) Campus Vertical Order
- Slug: campus-vertical-order
- Difficulty: Medium
- Problem: Return vertical order traversal of a binary tree (group by column from left to right, top to bottom).
- Constraints: `0 <= n <= 10^5`.
- Hint: BFS with column index; map column to list; track min/max column.
- Example:
  - Input: Root `3`, left `9`, right `8`, `8` has children `4` and `7`
  - Output: `[[9],[3,4],[8],[7]]`

## 10) Auditorium Top View
- Slug: auditorium-top-view
- Difficulty: Medium
- Problem: Return the top view of a binary tree (first node visible in each vertical column from above).
- Constraints: `0 <= n <= 10^5`.
- Hint: BFS with column map storing first occurrence.
- Example:
  - Input: Root `1`, left `2`, right `3`, `2` has right `4`, `3` has left `5`
  - Output: `[2,1,3]`

## 11) Lab Bottom View with Shadow Limit
- Slug: lab-bottom-view-shadow-limit
- Difficulty: Medium
- Problem: Return the bottom view but ignore any node deeper than depth `D` (0-indexed). Only consider nodes at depth <= D when choosing the bottom-most node per vertical column.
- Constraints: `0 <= n <= 10^5`, `0 <= D <= 10^5`.
- Hint: BFS with column map storing the deepest (<=D) seen node; skip nodes beyond D entirely.
- Example:
  - Input: Root `1`, left `2` (left `4`), right `3` (right `5`), `D=1`
  - Output: `[2,1,3]`

## 12) Robotics LCA with Blocked Nodes
- Slug: robotics-lca-blocked
- Difficulty: Medium
- Problem: Some nodes are blocked and cannot be used as part of the path. Given two target nodes that are not blocked, find their lowest common ancestor that is also not blocked; if all common ancestors are blocked, return `null`.
- Constraints: `1 <= n <= 10^5`.
- Hint: Postorder DFS returning presence of targets and ignoring blocked subtrees; only count an ancestor if unblocked.
- Example:
  - Input: Tree `6` with children `2` and `8`; `2` has children `1` and `4`; blocked node `6`; targets `1` and `4`
  - Output: `2`

## 13) Auditorium BST Validate
- Slug: auditorium-bst-validate
- Difficulty: Medium
- Problem: Determine if a binary tree is a valid BST (left < node < right for all nodes).
- Constraints: `0 <= n <= 10^5`, values fit in 64-bit.
- Hint: Carry min/max bounds in DFS.
- Example:
  - Input: Tree root `5`, left `1`, right `7` with children `6` and `8`
  - Output: `true`

## 14) Campus BST Insert & Search
- Slug: campus-bst-insert-search
- Difficulty: Easy-Medium
- Problem: Implement insertion and search in a BST and return inorder after insertions.
- Constraints: `0 <= n <= 10^5`.
- Hint: Standard BST walk; duplicates go to right or ignore—state rule.
- Example:
  - Input: Insert `4,2,6,1,3`, search `5`
  - Output: Inorder `[1,2,3,4,6]`, Search result `false`

## 15) Shuttle BST Kth Smallest in Range
- Slug: shuttle-bst-kth-smallest-range
- Difficulty: Medium
- Problem: Given a BST, an integer range `[L,R]`, and integer `k`, return the k-th smallest value that lies within `[L,R]` (1-indexed among the filtered set). If fewer than `k` values exist in the range, return -1.
- Constraints: `1 <= n <= 10^5`, values fit in 64-bit, `1 <= k <= n`.
- Hint: Inorder traversal skipping nodes outside range; decrement k only on in-range nodes.
- Example:
  - Input: BST inorder `[2,4,5,7,9]`, range `[4,8]`, `k=2`
  - Output: `5`

## 16) Robotics Balance Check
- Slug: robotics-balance-check
- Difficulty: Medium
- Problem: Check if a binary tree is height-balanced (for every node, height diff <= 1).
- Constraints: `0 <= n <= 10^5`.
- Hint: Postorder returning height and balance flag; short-circuit on imbalance.
- Example:
  - Input: Root `1` with left chain `2->3` and right `4`
  - Output: `false`

## 17) Lab Tree Right View
- Slug: lab-tree-right-view
- Difficulty: Easy-Medium
- Problem: Return the list of nodes visible from the right side of the binary tree.
- Constraints: `0 <= n <= 10^5`.
- Hint: BFS level order taking the last node each level; or DFS right-first by depth.
- Example:
  - Input: Root `10`, left `6` (child `7`), right `14`
  - Output: `[10,14,7]`

## 18) Seminar Opposite-Parity Ancestor Gap
- Slug: seminar-opposite-parity-ancestor-gap
- Difficulty: Medium
- Problem: For each node, consider only ancestors at a depth parity different from the node (one even, one odd). Find the maximum absolute difference between a node value and any such opposite-parity ancestor.
- Constraints: `0 <= n <= 10^5`.
- Hint: DFS carrying two pairs of min/max by parity; update answer using the opposite parity bucket.
- Example:
  - Input: Root `8`, left `3` (child `1`), right `10` (child `14`)
  - Output: `11` (node 14 vs ancestor 3 of opposite parity)
