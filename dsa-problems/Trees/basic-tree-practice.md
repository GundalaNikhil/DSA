# Basic Tree Practice Set (15-18 Questions)

## 1) Campus Directory Multi-Tree Comparison

- Slug: campus-directory-multi-tree
- Difficulty: Medium
- Problem: Given two binary trees T1 and T2, return their preorder, inorder, and postorder traversals. Then determine if they are structurally identical (ignoring values) and if any two of the six traversals match exactly.
- Constraints: `1 <= n <= 10^5`, node values fit in 32-bit int.
- Hint: Generate all six traversals; compare structures recursively; match lists pairwise.
- Example:
  - Input: T1 preorder `[4,2,1,3,6]`, T2 preorder `[7,5,2,8,9]`
  - Output: T1 traversals, T2 traversals, structurally_identical=true, matching_traversals=["inorder"]

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

## 4) Seminar Level Order Odd-Depth Only

- Slug: seminar-level-order-odd
- Difficulty: Medium
- Problem: Return level order lists but include only nodes at odd depths (root at depth 0). Preserve order within those levels.
- Constraints: `0 <= n <= 10^5`.
- Hint: BFS with depth tracking; skip even-depth nodes in output but still traverse their children.
- Example:
  - Input: Tree `10` -> left `5`, right `12`, and `5` has child `7`
  - Output: `[[5,12]]`

## 5) Robotics Mirror Check with Colors

- Slug: robotics-mirror-check-colors
- Difficulty: Medium
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

## 9) Campus Vertical Order With Weight Priority

- Slug: campus-vertical-order-weight
- Difficulty: Medium
- Problem: Each node has a value and weight. Return vertical order groups where nodes are sorted within each column by: (1) depth ascending, (2) weight descending (tie-breaker), (3) value ascending (final tie-breaker). Only include columns where total weight >= threshold W.
- Constraints: `0 <= n <= 10^5`, `1 <= weight[i] <= 10^6`, `0 <= W <= 10^9`.
- Hint: BFS storing (column, depth, weight, value); group by column; filter by total weight; multi-key sort.
- Example:
  - Input: Root `3`(w=5), left `9`(w=2), right `8`(w=3), `8` has children `4`(w=1) and `7`(w=4), W=5
  - Output: `[[3,8],[7]]` (column with 9 has weight 2 < 5, excluded)

## 10) Auditorium Top View With Height Bonus

- Slug: auditorium-top-view-height
- Difficulty: Medium
- Problem: For each column, choose the node with smallest depth; if multiple at same depth, choose the one with largest value. Return columns left to right.
- Constraints: `0 <= n <= 10^5`.
- Hint: BFS with column and depth; update when depth smaller or equal but value larger.
- Example:
  - Input: Root `1`, left `2`, right `3`, `2` has right `4`, `3` has left `5`
  - Output: `[4,1,5]`

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

## 13) Auditorium BST Validate with Gap

- Slug: auditorium-bst-validate-gap
- Difficulty: Medium
- Problem: Validate BST with an extra rule: difference between parent and child must be at least `G` (strict). Return false if any edge violates gap or BST order.
- Constraints: `0 <= n <= 10^5`, values 64-bit, `G >= 0`.
- Hint: DFS with min/max and track parent value to enforce gap.
- Example:
  - Input: root 5, left 1, right 7, G=2
  - Output: true

## 14) Campus BST Insert & Search

- Slug: campus-bst-insert-search
- Difficulty: Medium
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

## 16) Robotics Balance Check with Weight Limit

- Slug: robotics-balance-check-weight
- Difficulty: Medium
- Problem: Each node has weight w. Tree is balanced if height diff <=1 AND total weight difference between left/right subtrees <= `W` at every node. Return true/false.
- Constraints: `0 <= n <= 10^5`, weights up to 1e9, `W` given.
- Hint: Postorder returning (height, weight sum, balanced flag).
- Example:
  - Input: weights [1,2,1], W=1
  - Output: true

## 17) Lab Tree Right View with Skips

- Slug: lab-tree-right-view-skips
- Difficulty: Medium
- Problem: Return right view but skip any node whose value is negative; if a level has only skipped nodes, omit that level.
- Constraints: `0 <= n <= 10^5`.
- Hint: BFS level order; take rightmost non-negative.
- Example:
  - Input: Root `10`, left `-6` (child `7`), right `14`
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
