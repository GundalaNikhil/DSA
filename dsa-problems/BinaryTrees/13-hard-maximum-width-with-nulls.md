# Maximum Width Including Null Gaps

**Difficulty:** Hard
**Topic:** Binary Trees, Level Order Traversal
**License:** Free to use for commercial purposes

## Problem Statement

Find the maximum width of a binary tree, where width is measured as the distance between the leftmost and rightmost non-null nodes at any level, including the null gaps between them.

Use position indexing: root is at position 1, for any node at position `p`, its left child is at `2*p` and right child is at `2*p+1`.

Return the maximum width across all levels.

## Constraints

- `1 <= number of nodes <= 3000`
- `-100 <= node.val <= 100`

## Examples

### Example 1
```
Input: root = [10, 20, 30, 40, null, null, 60]
           10 (pos 1)
          /  \
        20   30 (pos 2, 3)
        /      \
      40       60 (pos 4, 7)

Level 0: positions [1], width = 1
Level 1: positions [2, 3], width = 3-2+1 = 2
Level 2: positions [4, 7], width = 7-4+1 = 4

Output: 4
Explanation: Level 2 has maximum width of 4 (including gaps)
```

### Example 2
```
Input: root = [50, 40, 60]
        50 (pos 1)
       /  \
     40   60 (pos 2, 3)

Level 0: width = 1
Level 1: width = 3-2+1 = 2

Output: 2
```

### Example 3
```
Input: root = [100, null, 200, null, 300]
        100 (pos 1)
          \
          200 (pos 3)
            \
            300 (pos 7)

Level 0: width = 1
Level 1: width = 1
Level 2: width = 1

Output: 1
```

### Example 4
```
Input: root = [25, 15, 35, 10, null, null, 40, 5]
              25 (pos 1)
            /    \
          15     35 (pos 2, 3)
          /        \
        10         40 (pos 4, 7)
        /
       5 (pos 8)

Level 2: positions [4, 7], width = 4
Level 3: positions [8], width = 1

Output: 4
```

## Function Signature

### Python
```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def width_of_tree(root: TreeNode) -> int:
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

function widthOfTree(root) {
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

public int widthOfTree(TreeNode root) {
    // Your code here
}
```

## Hints

1. Use BFS with position tracking
2. Store (node, position) pairs in queue
3. For each level, track leftmost and rightmost positions
4. Width at level = rightmost_pos - leftmost_pos + 1
5. Be careful with large position values, use position normalization
6. Time complexity: O(n), Space complexity: O(w)

## Tags
`binary-tree` `breadth-first-search` `level-order` `width` `hard`
