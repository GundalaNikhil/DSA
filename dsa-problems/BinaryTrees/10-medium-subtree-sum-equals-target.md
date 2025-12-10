# Count Subtrees with Target Sum

**Difficulty:** Medium
**Topic:** Binary Trees, Subtree Sum
**License:** Free to use for commercial purposes

## Problem Statement

Given a binary tree and a target sum, count how many subtrees have a total sum equal to the target.

A subtree includes a node and all its descendants. Each node forms its own subtree.

## Constraints

- `1 <= number of nodes <= 2000`
- `-100 <= node.val <= 100`
- `-10000 <= target <= 10000`

## Examples

### Example 1
```
Input: root = [10, 5, 15, 3, 7, null, 18], target = 15
           10
          /  \
         5   15
        / \    \
       3   7   18

Subtree sums:
- Node 3: sum = 3
- Node 7: sum = 7
- Node 5 subtree: sum = 5+3+7 = 15 ✓
- Node 18: sum = 18
- Node 15 subtree: sum = 15+18 = 33
- Node 10 subtree: sum = 10+5+3+7+15+18 = 58

Output: 1
Explanation: Only subtree rooted at 5 has sum = 15
```

### Example 2
```
Input: root = [8, 4, 12, 2, 6, 10, 14], target = 12
             8
           /   \
          4    12
         / \   / \
        2  6 10 14

Subtree sums:
- Node 2: 2
- Node 6: 6
- Node 4: 4+2+6 = 12 ✓
- Node 10: 10
- Node 14: 14
- Node 12: 12+10+14 = 36
- Node 8: 8+4+2+6+12+10+14 = 56

Wait, single node 12 also = 12 ✓

Output: 2
Explanation: Subtree at node 4 (sum=12) and single node 12 (sum=12)
```

### Example 3
```
Input: root = [5, 5, 5], target = 5
        5
       / \
      5   5

Output: 3
Explanation: All three single-node subtrees have sum = 5
```

### Example 4
```
Input: root = [20, 10, 30, -5, 15], target = 20
          20
         /  \
       10   30
       / \
     -5  15

Subtree sums:
- Node -5: -5
- Node 15: 15
- Node 10: 10+(-5)+15 = 20 ✓
- Node 30: 30
- Node 20: 20+10+(-5)+15+30 = 70

Also single node 20 = 20 ✓

Output: 2
```

## Function Signature

### Python
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_subtrees_with_sum(root: TreeNode, target: int) -> int:
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

function countSubtreesWithSum(root, target) {
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

public int countSubtreesWithSum(TreeNode root, int target) {
    // Your code here
}
```

## Hints

1. Use post-order traversal (children first, then parent)
2. Calculate sum of each subtree recursively
3. For each node: subtree_sum = node.val + left_sum + right_sum
4. Check if subtree_sum equals target, increment counter
5. Return both the count and sum from each recursive call
6. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `subtree-sum` `recursion` `post-order` `medium`
