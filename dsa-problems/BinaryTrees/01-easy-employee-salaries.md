# Galactic Resource Collection

**Difficulty:** Easy
**Topic:** Binary Trees, Tree Traversal
**License:** Free to use for commercial purposes

## Problem Statement

A space mining corporation has set up outposts on various planets, organized in a hierarchical binary tree structure. Each node represents an outpost, and the value represents the amount of rare minerals collected there.

The headquarters needs to calculate the total amount of minerals collected from all outposts combined.

Given the root of the binary tree, return the sum of all mineral values.

## Constraints

- `1 <= number of outposts <= 3000`
- `1000 <= outpost.minerals <= 100000`

## Examples

### Example 1
```
Input: root = [45000, 23000, 67000]
       45000
       /    \
   23000    67000

Output: 135000
Explanation: 45000 + 23000 + 67000 = 135000
```

### Example 2
```
Input: root = [30000, 15000, 20000, 8000, 12000]
          30000
         /     \
      15000    20000
      /   \
   8000  12000

Output: 85000
Explanation: Sum of all outposts = 85000
```

### Example 3
```
Input: root = [50000]
Output: 50000
Explanation: Only one outpost.
```

## Function Signature

### Python
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def total_minerals(root: TreeNode) -> int:
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

function totalMinerals(root) {
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

public int totalMinerals(TreeNode root) {
    // Your code here
}
```

## Hints

1. Visit every node in the tree
2. Add each node's value to a running total
3. Use recursion: total = current + left_total + right_total
4. Base case: null node contributes 0
5. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `tree-traversal` `recursion` `easy`
