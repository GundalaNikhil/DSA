# Flip Values at Alternate Levels

**Difficulty:** Medium
**Topic:** Binary Trees, Level Order Traversal
**License:** Free to use for commercial purposes

## Problem Statement

Given a binary tree, flip all node values at alternate levels. Flipping means negating the value (multiply by -1).

Flip levels 1, 3, 5, ... (odd levels). Keep levels 0, 2, 4, ... (even levels) unchanged.

Return the root of the modified tree.

## Constraints

- `1 <= number of nodes <= 3000`
- `-200 <= node.val <= 200`

## Examples

### Example 1
```
Input: root = [10, 20, 30, 40, 50, 60, 70]
           10          Level 0 (keep)
          /  \
        20   30        Level 1 (flip)
       /  \ /  \
     40  50 60 70      Level 2 (keep)

After flipping:
           10
          /  \
       -20   -30
       /  \ /  \
     40  50 60 70

Output: [10, -20, -30, 40, 50, 60, 70]
```

### Example 2
```
Input: root = [5, 10, 15]
        5            Level 0 (keep)
       / \
     10  15          Level 1 (flip)

After flipping:
        5
       / \
    -10  -15

Output: [5, -10, -15]
```

### Example 3
```
Input: root = [100]
Output: [100]
Explanation: Only level 0, no flipping needed
```

### Example 4
```
Input: root = [50, 25, 75, 12, 37, 62, 87, 6, 18]
              50            Level 0 (keep)
            /    \
          25     75         Level 1 (flip)
         /  \   /  \
       12  37 62  87       Level 2 (keep)
       / \
      6  18                Level 3 (flip)

After flipping:
              50
            /    \
         -25     -75
         /  \   /  \
       12  37 62  87
       / \
     -6  -18

Output: [50, -25, -75, 12, 37, 62, 87, -6, -18]
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

def flip_alternate_levels(root: TreeNode) -> TreeNode:
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

function flipAlternateLevels(root) {
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

public TreeNode flipAlternateLevels(TreeNode root) {
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
