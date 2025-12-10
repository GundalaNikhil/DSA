# Chemical Reaction Chain

**Difficulty:** Medium
**Topic:** Binary Trees, Path Finding
**License:** Free to use for commercial purposes

## Problem Statement

A chemical process is modeled as a binary tree where each node represents a catalyst with a specific multiplication factor. A reaction starts at the root and follows a path down to a leaf node. The total reaction yield is the product of all catalyst factors along the path.

Given the root of the tree and a `target_yield`, determine if there exists any root-to-leaf path where the product of factors equals the `target_yield`.

Return `true` if such a path exists, `false` otherwise.

## Constraints

- `1 <= number of nodes <= 1000`
- `1 <= factor <= 20`
- `1 <= target_yield <= 10^9`

## Examples

### Example 1
```
Input: root = [2, 3, 5, 4, 2], target = 24
         2
        / \
       3   5
      / \
     4   2

Paths:
2->3->4 = 24 ✓
2->3->2 = 12
2->5 = 10

Output: true
```

### Example 2
```
Input: root = [3, 4, 5], target = 20
Output: false
Explanation: Paths are 3->4 (12) and 3->5 (15). Neither is 20.
```

### Example 3
```
Input: root = [10, 1, 2], target = 20
Output: true
Explanation: Path 10->2 gives product 20.
```

## Function Signature

### Python
```python
def has_reaction_path(root: TreeNode, target_yield: int) -> bool:
    pass
```

### JavaScript
```javascript
function hasReactionPath(root, targetYield) {
    // Your code here
}
```

### Java
```java
public boolean hasReactionPath(TreeNode root, int targetYield) {
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
