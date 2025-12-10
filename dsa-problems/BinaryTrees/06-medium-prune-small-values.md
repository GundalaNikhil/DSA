# Orchard Harvest Optimization

**Difficulty:** Medium
**Topic:** Binary Trees, Tree Modification
**License:** Free to use for commercial purposes

## Problem Statement

An automated gardening bot manages a fruit orchard organized as a binary tree structure. Each node represents a branch section with a certain fruit yield value.

To optimize growth, the bot needs to prune "weak" branches. A branch node is considered weak if its yield is strictly less than a given `threshold`.

The pruning rules are:
1. If a node's yield is less than `threshold` AND it has no children (leaf node), it should be removed.
2. This process applies recursively: if a parent becomes a leaf after its children are removed, and its yield is also low, it should also be removed.
3. If a node has a low yield but still has at least one surviving child branch, it must be kept to support that branch.

Given the root of the tree and the `threshold`, return the root of the pruned tree.

## Constraints

- `0 <= number of nodes <= 3000`
- `1 <= node.yield <= 500`
- `1 <= threshold <= 500`

## Examples

### Example 1
```
Input: root = [50, 30, 70, 20, 40, 60, 80], threshold = 45
           50
          /  \
        30    70
       /  \  /  \
     20  40 60  80

Output: [50, null, 70, 60, 80]
Explanation:
- Leaves 20 and 40 are < 45, so removed.
- Node 30 becomes a leaf. Since 30 < 45, it is also removed.
- Leaves 60 and 80 are >= 45, kept.
- Node 70 is kept.
- Root 50 is kept.
```

### Example 2
```
Input: root = [100, 80, 120, 60, 90], threshold = 95
          100
         /   \
       80    120
      /  \
    60   90

Output: [100, null, 120]
Explanation:
- 60 and 90 removed (< 95).
- 80 becomes leaf, removed (< 95).
- 120 kept.
```

### Example 3
```
Input: root = [25, 15, 35], threshold = 50
Output: []
Explanation: All nodes are below threshold. Entire tree pruned.
```

## Function Signature

### Python
```python
def optimize_orchard(root: TreeNode, threshold: int) -> TreeNode:
    pass
```

### JavaScript
```javascript
function optimizeOrchard(root, threshold) {
    // Your code here
}
```

### Java
```java
public TreeNode optimizeOrchard(TreeNode root, int threshold) {
    // Your code here
}
```

## Hints

1. Use post-order traversal (process children first, then parent)
2. Recursively prune left and right subtrees first
3. After pruning children, check if current node should be removed
4. Remove current if: value < threshold AND no children remain
5. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `tree-modification` `recursion` `medium`
