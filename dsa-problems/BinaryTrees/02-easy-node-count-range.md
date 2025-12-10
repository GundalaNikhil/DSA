# Count Nodes in Range

**Difficulty:** Easy
**Topic:** Binary Trees, Counting
**License:** Free to use for commercial purposes

## Problem Statement

Given a binary tree and two numbers `min` and `max`, count how many nodes have values between `min` and `max` (inclusive).

Return the count of nodes whose value is >= min AND <= max.

## Constraints

- `1 <= number of nodes <= 2500`
- `1 <= node.val <= 500`
- `1 <= min <= max <= 500`

## Examples

### Example 1
```
Input: root = [17, 9, 38, 4, 12, 25, 44], min = 10, max = 40
            17
           /  \
          9   38
         / \  / \
        4 12 25 44

Output: 4
Explanation: Nodes with values in [10, 40]: 17, 12, 38, 25
```

### Example 2
```
Input: root = [55, 33, 77, 22, 44], min = 30, max = 60
         55
        /  \
      33    77
     /  \
   22   44

Output: 3
Explanation: Nodes 55, 33, 44 are in range [30, 60]
```

### Example 3
```
Input: root = [100, 50, 150], min = 200, max = 300
        100
       /   \
     50    150

Output: 0
Explanation: No nodes in range [200, 300]
```

### Example 4
```
Input: root = [8, 3, 11, 1, 6, 9, 14], min = 5, max = 12
           8
         /   \
        3    11
       / \   / \
      1   6 9  14

Output: 4
Explanation: Nodes 8, 6, 11, 9 are in range [5, 12]
```

## Function Signature

### Python
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_in_range(root: TreeNode, min_val: int, max_val: int) -> int:
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

function countInRange(root, minVal, maxVal) {
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

public int countInRange(TreeNode root, int minVal, int maxVal) {
    // Your code here
}
```

## Hints

1. Visit every node in the tree
2. Check if current node's value is between min and max
3. Count it if yes, skip if no
4. Recursively check left and right subtrees
5. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `counting` `range-query` `easy`
