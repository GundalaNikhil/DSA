# Distribute Coins to Make Equal

**Difficulty:** Hard
**Topic:** Binary Trees, Tree Traversal, Balancing
**License:** Free to use for commercial purposes

## Problem Statement

Given a binary tree where each node has some coins (can be 0, 1, or more), distribute the coins so that every node has exactly 1 coin. In one move, you can move 1 coin from a node to its parent or child.

The total number of coins in the tree equals the number of nodes (so distribution is always possible).

Return the minimum number of moves required.

## Constraints

- `1 <= number of nodes <= 500`
- `0 <= node.coins <= 100`
- Total coins = number of nodes

## Examples

### Example 1
```
Input: root = [3, 0, 0]
        3
       / \
      0   0

Output: 2
Explanation:
- Move 1 coin from root to left child (1 move)
- Move 1 coin from root to right child (1 move)
Total: 2 moves
```

### Example 2
```
Input: root = [0, 3, 0]
        0
       / \
      3   0

Output: 3
Explanation:
- Move 1 coin from left child to root (1 move)
- Move 1 coin from root to right child (1 move)
- Move 1 coin from left child to root (1 move)
Total: 3 moves
```

### Example 3
```
Input: root = [1, 0, 2]
        1
       / \
      0   2

Output: 2
Explanation:
- Move 1 coin from right child to root (1 move)
- Move 1 coin from root to left child (1 move)
Total: 2 moves
```

### Example 4
```
Input: root = [2, 1, 0, 0, 3]
          2
         / \
        1   0
       / \
      0   3

Output: 4
Explanation:
- Node with 3 coins needs to give away 2 coins
- Node with 0 needs to receive 1 coin
- Multiple moves through the tree
Total: 4 moves
```

## Function Signature

### Python
```python
class TreeNode:
    def __init__(self, coins=0, left=None, right=None):
        self.coins = coins
        self.left = left
        self.right = right

def distribute_coins(root: TreeNode) -> int:
    pass
```

### JavaScript
```javascript
class TreeNode {
    constructor(coins, left = null, right = null) {
        this.coins = coins;
        this.left = left;
        this.right = right;
    }
}

function distributeCoins(root) {
    // Your code here
}
```

### Java
```java
class TreeNode {
    int coins;
    TreeNode left;
    TreeNode right;
    TreeNode(int c) { this.coins = c; }
}

public int distributeCoins(TreeNode root) {
    // Your code here
}
```

## Hints

1. Use post-order DFS (process children first)
2. For each node, calculate excess = coins - 1 (what it needs/has extra)
3. A node needs to pass its excess to parent
4. Number of moves through an edge = |excess from that subtree|
5. Total moves = sum of absolute excess values from all subtrees
6. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `depth-first-search` `greedy` `balancing` `hard`
