# Check if Two Nodes are Cousins

**Difficulty:** Easy
**Topic:** Binary Trees, Level Order Traversal
**License:** Free to use for commercial purposes

## Problem Statement

Two nodes are cousins if they are at the same level (same distance from root) but have different parents.

Given a binary tree and two node values, check if they are cousins. Return `true` if they are cousins, `false` otherwise.

## Constraints

- `2 <= number of nodes <= 2000`
- `1 <= node.val <= 100`
- All node values are unique
- Both target nodes exist in the tree

## Examples

### Example 1
```
Input: root = [50, 30, 70, 20, 40, 60, 80], node1 = 20, node2 = 60
           50
          /  \
        30    70
       /  \  /  \
     20  40 60  80

Output: true
Explanation: Both 20 and 60 are at level 2, but have different parents (30 and 70)
```

### Example 2
```
Input: root = [50, 30, 70, 20, 40], node1 = 20, node2 = 40
         50
        /  \
      30    70
     /  \
   20   40

Output: false
Explanation: Both at level 2, but same parent (30)
```

### Example 3
```
Input: root = [10, 5, 15, 3, 7, 12, 18], node1 = 3, node2 = 18
           10
         /    \
        5     15
       / \   /  \
      3   7 12  18

Output: true
Explanation: Different levels - 3 at level 2, 18 at level 2, different parents
```

### Example 4
```
Input: root = [25, 15, 35, null, 18], node1 = 18, node2 = 35
         25
        /  \
      15   35
        \
        18

Output: false
Explanation: 35 is at level 1, 18 is at level 2 - different levels
```

## Function Signature

### Python
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def are_cousins(root: TreeNode, node1: int, node2: int) -> bool:
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

function areCousins(root, node1, node2) {
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

public boolean areCousins(TreeNode root, int node1, int node2) {
    // Your code here
}
```

## Hints

1. Find the depth and parent of each target node
2. Use BFS or DFS to track level and parent
3. Two nodes are cousins if: same depth AND different parents
4. Store (depth, parent) for each node as you search
5. Time complexity: O(n), Space complexity: O(n)

## Tags
`binary-tree` `breadth-first-search` `level-order` `easy`
