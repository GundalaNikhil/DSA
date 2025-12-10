# Total Salary of Departments

**Difficulty:** Easy
**Topic:** Binary Trees, Tree Traversal
**License:** Free to use for commercial purposes

## Problem Statement

A company organizes departments as a binary tree. Each node has a salary budget number. Find the total salary budget of all departments combined.

Simply add up all the numbers in the tree.

## Constraints

- `1 <= number of nodes <= 3000`
- `1000 <= node.val <= 100000`

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
Explanation: Sum all nodes = 85000
```

### Example 3
```
Input: root = [50000]
Output: 50000
Explanation: Only one department
```

### Example 4
```
Input: root = [40000, 18000, 22000, 9000, 11000, 13000, 19000]
            40000
           /     \
       18000     22000
       /   \     /    \
    9000 11000 13000 19000

Output: 132000
```

## Function Signature

### Python
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def total_salary(root: TreeNode) -> int:
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

function totalSalary(root) {
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

public int totalSalary(TreeNode root) {
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
