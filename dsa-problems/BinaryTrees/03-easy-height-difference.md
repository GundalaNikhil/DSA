# Skyscraper Skyline Analysis

**Difficulty:** Easy
**Topic:** Binary Trees, Tree Height
**License:** Free to use for commercial purposes

## Problem Statement

An architect is analyzing the design of a futuristic building shaped like a binary tree. They want to ensure structural balance by comparing the height of the left wing (left subtree) versus the right wing (right subtree).

Given the root of the binary tree representing the building, calculate the absolute difference between the height of the left subtree and the height of the right subtree.

Height is defined as the number of nodes along the longest path from the root to a leaf node.

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

Left wing height: 2 (30->20)
Right wing height: 1 (70)
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
Explanation: No left or right wings.
```

## Function Signature

### Python
```python
def wing_height_difference(root: TreeNode) -> int:
    pass
```

### JavaScript
```javascript
function wingHeightDifference(root) {
    // Your code here
}
```

### Java
```java
public int wingHeightDifference(TreeNode root) {
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
