# Difference Between Even and Odd Values

**Difficulty:** Easy
**Topic:** Binary Trees, Tree Traversal
**License:** Free to use for commercial purposes

## Problem Statement

Given a binary tree, calculate the sum of all even-valued nodes minus the sum of all odd-valued nodes.

Return (sum of even values) - (sum of odd values).

## Constraints

- `1 <= number of nodes <= 3500`
- `1 <= node.val <= 200`

## Examples

### Example 1
```
Input: root = [13, 8, 19, 6, 11]
         13
        /  \
       8   19
      / \
     6  11

Even values: 8, 6 → sum = 14
Odd values: 13, 19, 11 → sum = 43
Output: 14 - 43 = -29
```

### Example 2
```
Input: root = [24, 16, 32, 8]
         24
        /  \
      16   32
      /
     8

Even values: 24, 16, 32, 8 → sum = 80
Odd values: none → sum = 0
Output: 80 - 0 = 80
```

### Example 3
```
Input: root = [7, 3, 9, 1, 5]
        7
       / \
      3   9
     / \
    1   5

Even values: none → sum = 0
Odd values: 7, 3, 9, 1, 5 → sum = 25
Output: 0 - 25 = -25
```

### Example 4
```
Input: root = [18, 7, 24, 3, 10, 20, 28]
            18
          /    \
        7      24
       / \    /  \
      3  10  20  28

Even: 18, 24, 10, 20, 28 → sum = 100
Odd: 7, 3 → sum = 10
Output: 100 - 10 = 90
```

## Function Signature

### Python
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def even_odd_difference(root: TreeNode) -> int:
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

function evenOddDifference(root) {
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

public int evenOddDifference(TreeNode root) {
    // Your code here
}
```

## Hints

1. Visit all nodes and check if value is even or odd
2. Keep two running sums: one for even, one for odd
3. Check if number is even using modulo: num % 2 == 0
4. Return even_sum - odd_sum at the end
5. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `tree-traversal` `even-odd` `easy`
