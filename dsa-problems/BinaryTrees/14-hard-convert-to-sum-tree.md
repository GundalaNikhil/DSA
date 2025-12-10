# Convert to Descendent Sum Tree

**Difficulty:** Hard
**Topic:** Binary Trees, Tree Transformation
**License:** Free to use for commercial purposes

## Problem Statement

Transform a binary tree into a sum tree where each node's value becomes the sum of all its descendants' original values (not including itself).

Leaf nodes become 0 (they have no descendants). Modify the tree in-place and return the root.

## Constraints

- `1 <= number of nodes <= 2500`
- `1 <= node.val <= 500`

## Examples

### Example 1
```
Input: root = [10, 5, 15, 2, 8]
         10
        /  \
       5   15
      / \
     2   8

After transformation:
         15 (sum of 5+2+8 = 15)
        /  \
      10    0
      / \
     0   0

Output: root of transformed tree
Explanation:
- Leaves 2, 8, 15 become 0
- Node 5: sum of descendants 2+8 = 10
- Node 10: sum of all descendants 5+2+8+15 = 30

Wait, let me recalculate:
- Node 5's descendants: 2, 8 → sum = 10
- Node 10's descendants: 5, 15, 2, 8 → sum = 30

Corrected:
         30
        /  \
      10    0
      / \
     0   0
```

### Example 2
```
Input: root = [20, 10, 30]
        20
       /  \
     10   30

After:
        40 (10+30)
       /  \
      0    0

Output: [40, 0, 0]
```

### Example 3
```
Input: root = [50]
Output: [0]
Explanation: Single node (leaf) becomes 0
```

### Example 4
```
Input: root = [100, 50, 150, 25, 75, 125, 175]
             100
           /     \
         50      150
        /  \    /   \
      25  75  125  175

Node 50's descendants: 25+75 = 100
Node 150's descendants: 125+175 = 300
Node 100's descendants: 50+25+75+150+125+175 = 600

After:
            600
           /   \
         100   300
        /  \ /   \
       0   0 0   0

Output: [600, 100, 300, 0, 0, 0, 0]
```

## Function Signature

### Python
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convert_to_sum_tree(root: TreeNode) -> TreeNode:
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

function convertToSumTree(root) {
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

public TreeNode convertToSumTree(TreeNode root) {
    // Your code here
}
```

## Hints

1. Use post-order traversal (process children first)
2. Create helper function that returns sum of subtree (including current node)
3. For each node: calculate left_sum + right_sum
4. Store original value, then set node.val = left_sum + right_sum
5. Return original_value + left_sum + right_sum to parent
6. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `tree-transformation` `post-order` `recursion` `hard`
