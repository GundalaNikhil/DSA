# Height Difference Between Subtrees

**Difficulty:** Easy
**Topic:** Binary Trees, Tree Height
**License:** Free to use for commercial purposes

## Problem Statement

Given a binary tree, find the absolute difference between the heights of the left and right subtrees of the root.

Height of a tree is the longest path from root to any leaf. Return the absolute difference.

## Constraints

- `0 <= number of nodes <= 4000`
- `-200 <= node.val <= 200`

## Examples

### Example 1
```
Input: root = [50, 30, 70, 20, 40]
         50
        /  \
      30    70
     /  \
   20   40

Left subtree height: 2 (50→30→20)
Right subtree height: 1 (50→70)
Output: 1
Explanation: |2 - 1| = 1
```

### Example 2
```
Input: root = [100, 50, 150, 25, null, null, 175, 12]
            100
           /   \
         50    150
        /        \
      25        175
     /
   12

Left height: 3, Right height: 2
Output: 1
```

### Example 3
```
Input: root = [10]
Output: 0
Explanation: No left or right subtree, both heights are 0
```

### Example 4
```
Input: root = [60, 40, 80, 30, 50, 70, 90, 20]
            60
          /    \
        40      80
       /  \    /  \
     30   50  70  90
    /
  20

Left height: 3, Right height: 2
Output: 1
```

## Function Signature

### Python
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height_difference(root: TreeNode) -> int:
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

function heightDifference(root) {
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

public int heightDifference(TreeNode root) {
    // Your code here
}
```

## Hints

1. Create a helper function to calculate height of a tree
2. Height of null tree is 0
3. Height of tree = 1 + max(left_height, right_height)
4. Calculate height of left and right subtrees of root
5. Return absolute difference
6. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `tree-height` `recursion` `easy`
