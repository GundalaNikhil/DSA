# Find Level with Maximum Average

**Difficulty:** Medium
**Topic:** Binary Trees, Level Order Traversal
**License:** Free to use for commercial purposes

## Problem Statement

Given a binary tree, calculate the average value of nodes at each level. Return the level number (starting from 0) that has the highest average.

If multiple levels have the same maximum average, return the smallest level number.

## Constraints

- `1 <= number of nodes <= 4000`
- `-1000 <= node.val <= 1000`

## Examples

### Example 1
```
Input: root = [20, 10, 30, 5, 15, 25, 40]
           20           Level 0: avg = 20
          /  \
        10   30        Level 1: avg = (10+30)/2 = 20
       /  \  /  \
      5  15 25  40     Level 2: avg = (5+15+25+40)/4 = 21.25

Output: 2
Explanation: Level 2 has highest average of 21.25
```

### Example 2
```
Input: root = [50, 60, 40, 70, 50, 30, 50]
            50         Level 0: avg = 50
           /  \
         60   40       Level 1: avg = (60+40)/2 = 50
        /  \ /  \
      70  50 30 50    Level 2: avg = (70+50+30+50)/4 = 50

Output: 0
Explanation: All levels have same average, return smallest level (0)
```

### Example 3
```
Input: root = [100, 200, 50]
         100          Level 0: avg = 100
        /   \
      200   50        Level 1: avg = (200+50)/2 = 125

Output: 1
Explanation: Level 1 has higher average
```

### Example 4
```
Input: root = [15, 18, 12, 20, 16, 10, 14, 22]
              15           Level 0: avg = 15
            /    \
          18     12        Level 1: avg = 15
         /  \   /  \
       20  16 10  14      Level 2: avg = 15
       /
     22                   Level 3: avg = 22

Output: 3
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

def max_average_level(root: TreeNode) -> int:
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

function maxAverageLevel(root) {
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

public int maxAverageLevel(TreeNode root) {
    // Your code here
}
```

## Hints

1. Use BFS to process tree level by level
2. For each level, calculate sum and count of nodes
3. Average = sum / count
4. Track maximum average and its level number
5. Time complexity: O(n), Space complexity: O(w) where w is max width

## Tags
`binary-tree` `breadth-first-search` `level-order` `average` `medium`
