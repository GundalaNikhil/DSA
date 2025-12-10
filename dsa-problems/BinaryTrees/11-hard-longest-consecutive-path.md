# Longest Consecutive Sequence Path

**Difficulty:** Hard
**Topic:** Binary Trees, Path Finding
**License:** Free to use for commercial purposes

## Problem Statement

Given a binary tree, find the longest path where node values form a consecutive sequence (each value is exactly 1 more than the previous). The path can go through parent-child relationships in any direction.

For example: 5→6→7 or 10→9→8 are valid consecutive sequences.

Return the length of the longest consecutive path.

## Constraints

- `1 <= number of nodes <= 3000`
- `1 <= node.val <= 1000`

## Examples

### Example 1
```
Input: root = [10, 8, 12, 7, 9, 11, 13]
            10
           /  \
          8   12
         / \  / \
        7  9 11 13

Longest consecutive sequences:
- 7→8 (length 2)
- 8→9 (length 2)
- 11→12→13 (length 3) ✓
- 10→11→12→13 (not consecutive, 10 to 11 jump)

Wait, let me reconsider: 11→12→13 is 3 nodes
Actually from 10: 10→11 is consecutive, then 11→12, then 12→13
So: 10→11→12→13 could be length 4 if they're connected

In this tree: 11→12→13 gives length 3

Output: 3
```

### Example 2
```
Input: root = [50, 49, 51, 48, null, null, 52]
           50
          /  \
        49   51
        /      \
      48       52

Sequences:
- 48→49→50→51→52 (length 5) ✓

Output: 5
Explanation: Path goes 48→49→50→51→52
```

### Example 3
```
Input: root = [100, 200, 300]
         100
        /   \
      200   300

Output: 1
Explanation: No consecutive sequences, each node is its own sequence
```

### Example 4
```
Input: root = [25, 24, 26, 23, null, null, 27, 22]
             25
           /    \
         24     26
         /        \
       23         27
       /
     22

Sequences:
- 22→23→24→25→26→27 (length 6) ✓

Output: 6
```

## Function Signature

### Python
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def longest_consecutive(root: TreeNode) -> int:
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

function longestConsecutive(root) {
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

public int longestConsecutive(TreeNode root) {
    // Your code here
}
```

## Hints

1. At each node, track both increasing and decreasing consecutive lengths
2. For each node, get increasing/decreasing lengths from left and right children
3. If child.val = parent.val + 1, it extends increasing sequence
4. If child.val = parent.val - 1, it extends decreasing sequence
5. Maximum path through a node = inc_from_left + dec_from_right + 1 (or vice versa)
6. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `depth-first-search` `path-finding` `consecutive` `hard`
