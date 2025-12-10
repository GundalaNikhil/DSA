# Remove Nodes Below Threshold

**Difficulty:** Medium
**Topic:** Binary Trees, Tree Modification
**License:** Free to use for commercial purposes

## Problem Statement

Given a binary tree and a threshold value, remove all nodes whose values are less than the threshold. After removing, if a parent becomes a leaf (no children), keep it only if its value is >= threshold.

Return the root of the modified tree (or null if everything is removed).

## Constraints

- `0 <= number of nodes <= 3000`
- `1 <= node.val <= 500`
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

After removing nodes < 45:
         50
           \
           70
          /  \
        60   80

Output: root of modified tree [50, null, 70, 60, 80]
Explanation: Removed 30, 20, 40 (all < 45)
```

### Example 2
```
Input: root = [100, 80, 120, 60, 90], threshold = 95
          100
         /   \
       80    120
      /  \
    60   90

After removing < 95:
         100
           \
          120

Output: [100, null, 120]
```

### Example 3
```
Input: root = [25, 15, 35], threshold = 50
        25
       /  \
     15   35

Output: null
Explanation: All nodes are below threshold
```

### Example 4
```
Input: root = [75, 50, 100, 25, 60, 90, 110], threshold = 55
            75
          /    \
        50    100
       /  \   /  \
     25  60 90  110

After removing < 55:
         75
           \
          100
          /  \
        90  110

Also node 60 stays:
         75
        /  \
      60   100
          /  \
        90  110

Output: [75, 60, 100, null, null, 90, 110]
```

## Function Signature

### Python
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def prune_below_threshold(root: TreeNode, threshold: int) -> TreeNode:
    pass
```

### JavaScript
```javascript
class TreeNode {
    constructor(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function pruneBelowThreshold(root, threshold) {
    // Your code here
}
```

### Java
```java
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int v) { this.val = v; }
}

public TreeNode pruneBelowThreshold(TreeNode root, int threshold) {
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
