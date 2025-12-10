# Count Nodes at Distance K from Any Leaf

**Difficulty:** Hard
**Topic:** Binary Trees, Distance Calculation
**License:** Free to use for commercial purposes

## Problem Statement

Given a binary tree and an integer `k`, count how many nodes are at exactly distance `k` from at least one leaf node.

Distance is measured by counting edges in the path. A node can be at distance `k` from multiple leaves, but count it only once.

## Constraints

- `1 <= number of nodes <= 2000`
- `-100 <= node.val <= 100`
- `0 <= k <= 10`

## Examples

### Example 1
```
Input: root = [50, 30, 70, 20, 40], k = 1
         50
        /  \
      30    70
     /  \
   20   40

Leaves: 20, 40, 70
Nodes at distance 1 from leaves:
- Node 30 (distance 1 from leaves 20 and 40)
- Node 50 (distance 1 from leaf 70)

Output: 2
Explanation: Nodes 30 and 50 are at distance 1 from some leaf
```

### Example 2
```
Input: root = [100, 80, 120, 60, 90], k = 2
          100
         /   \
       80    120
      /  \
    60   90

Leaves: 60, 90, 120
Nodes at distance 2:
- Node 100 (distance 2 from leaves 60 and 90)

Output: 1
```

### Example 3
```
Input: root = [10, 5, 15], k = 0
        10
       /  \
      5   15

Leaves: 5, 15
Nodes at distance 0 from leaves: 5, 15 themselves

Output: 2
```

### Example 4
```
Input: root = [25, 20, 30, 18, 22, 28, 32, 16], k = 3
              25
            /    \
          20     30
         /  \   /  \
       18  22 28  32
       /
     16

Leaves: 16, 22, 28, 32
Checking distance 3:
- From leaf 16: going up 3 levels reaches node 25
- Other leaves are at depth 2, so distance 3 goes above root

Output: 1
Explanation: Only node 25 is at distance 3 from leaf 16
```

## Function Signature

### Python
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_at_distance_from_leaf(root: TreeNode, k: int) -> int:
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

function countAtDistanceFromLeaf(root, k) {
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

public int countAtDistanceFromLeaf(TreeNode root, int k) {
    // Your code here
}
```

## Hints

1. For each leaf, mark all ancestors at distance k
2. Track path from root to current node during DFS
3. When you reach a leaf, check if k-th ancestor exists in path
4. Use a Set to store unique nodes at distance k
5. Time complexity: O(n * h), Space complexity: O(n)

## Tags
`binary-tree` `depth-first-search` `distance` `path-tracking` `hard`
