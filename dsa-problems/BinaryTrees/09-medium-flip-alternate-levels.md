# Mirror Dimension Rift

**Difficulty:** Medium
**Topic:** Binary Trees, Level Order Traversal
**License:** Free to use for commercial purposes

## Problem Statement

A glitch in the multiverse has caused alternate dimensions to flip their polarity. The multiverse is represented as a binary tree.
- Level 0 (Root) is stable (Normal).
- Level 1 is unstable (Flipped).
- Level 2 is stable (Normal).
- Level 3 is unstable (Flipped).
- And so on...

"Flipped" means the energy value of the node is negated (multiplied by -1).

Given the root of the tree, apply this dimension rift effect and return the modified tree.

## Constraints

- `1 <= number of nodes <= 3000`
- `-200 <= node.val <= 200`

## Examples

### Example 1
```
Input: root = [10, 20, 30, 40, 50, 60, 70]
           10          (Level 0: Normal)
          /  \
        20   30        (Level 1: Flipped)
       /  \ /  \
     40  50 60 70      (Level 2: Normal)

Output: [10, -20, -30, 40, 50, 60, 70]
```

### Example 2
```
Input: root = [5, 10, 15]
Output: [5, -10, -15]
```

### Example 3
```
Input: root = [100]
Output: [100]
```

## Function Signature

### Python
```python
def apply_dimension_rift(root: TreeNode) -> TreeNode:
    pass
```

### JavaScript
```javascript
function applyDimensionRift(root) {
    // Your code here
}
```

### Java
```java
public TreeNode applyDimensionRift(TreeNode root) {
    // Your code here
}
```

## Hints

1. Use BFS to process tree level by level
2. Track current level number (starting from 0)
3. For odd levels, negate all node values
4. For even levels, keep values as they are
5. Time complexity: O(n), Space complexity: O(w) where w is max width

## Tags
`binary-tree` `breadth-first-search` `level-order` `modification` `medium`
