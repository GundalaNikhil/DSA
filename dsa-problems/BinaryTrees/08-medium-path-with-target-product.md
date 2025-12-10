# Path with Target Product

**Difficulty:** Medium
**Topic:** Binary Trees, Path Finding
**License:** Free to use for commercial purposes

## Problem Statement

Given a binary tree and a target number, find if there exists any path from root to leaf where the product (multiplication) of all node values equals the target.

Return `true` if such a path exists, `false` otherwise.

## Constraints

- `1 <= number of nodes <= 1000`
- `1 <= node.val <= 20`
- `1 <= target <= 10^9`

## Examples

### Example 1
```
Input: root = [5, 2, 6, 3, 4], target = 120
         5
        / \
       2   6
      / \
     3   4

Paths:
5→2→3 = 30
5→2→4 = 40
5→6 = 30

Output: false
Explanation: No path multiplies to 120
```

### Example 2
```
Input: root = [3, 4, 5, 2, 6], target = 72
         3
        / \
       4   5
      / \
     2   6

Paths:
3→4→2 = 24
3→4→6 = 72 ✓
3→5 = 15

Output: true
Explanation: Path 3→4→6 has product 72
```

### Example 3
```
Input: root = [10, 1, 2], target = 20
        10
       /  \
      1    2

Paths:
10→1 = 10
10→2 = 20 ✓

Output: true
```

### Example 4
```
Input: root = [7, 3, 11, 2, 4, 5, 6], target = 1155
             7
           /   \
          3    11
         / \   / \
        2  4  5  6

Paths products:
7→3→2 = 42
7→3→4 = 84
7→11→5 = 385
7→11→6 = 462

Output: false
Explanation: None multiply to 1155
```

## Function Signature

### Python
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path_with_product(root: TreeNode, target: int) -> bool:
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

function hasPathWithProduct(root, target) {
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

public boolean hasPathWithProduct(TreeNode root, int target) {
    // Your code here
}
```

## Hints

1. Use DFS to explore all root-to-leaf paths
2. Track running product as you go down
3. When you reach a leaf, check if product equals target
4. Be careful with integer overflow for large products
5. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `depth-first-search` `path-finding` `product` `medium`
