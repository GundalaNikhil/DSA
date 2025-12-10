# Family Tree Heritage Search

**Difficulty:** Easy
**Topic:** Binary Trees, Level Order Traversal
**License:** Free to use for commercial purposes

## Problem Statement

A genealogist is analyzing a family tree. Two family members are considered "cousins" if they are in the same generation (same depth level from the ancestor root) but have different parents.

Given the root of the family tree and the IDs of two members `member1` and `member2`, determine if they are cousins.

Return `true` if they are cousins, `false` otherwise.

## Constraints

- `2 <= number of members <= 2000`
- `1 <= member.id <= 100`
- All member IDs are unique
- Both target members exist in the tree

## Examples

### Example 1
```
Input: root = [50, 30, 70, 20, 40, 60, 80], member1 = 20, member2 = 60
           50
          /  \
        30    70
       /  \  /  \
     20  40 60  80

Output: true
Explanation: Both 20 and 60 are at generation 2, but have different parents (30 and 70).
```

### Example 2
```
Input: root = [50, 30, 70, 20, 40], member1 = 20, member2 = 40
         50
        /  \
      30    70
     /  \
   20   40

Output: false
Explanation: Both at generation 2, but same parent (30). They are siblings, not cousins.
```

### Example 3
```
Input: root = [10, 5, 15, 3, 7, 12, 18], member1 = 3, member2 = 18
           10
         /    \
        5     15
       / \   /  \
      3   7 12  18

Output: true
Explanation: Different generations? No, both at generation 2. Different parents (5 and 15). Cousins.
```

## Function Signature

### Python
```python
def are_cousins(root: TreeNode, member1: int, member2: int) -> bool:
    pass
```

### JavaScript
```javascript
function areCousins(root, member1, member2) {
    // Your code here
}
```

### Java
```java
public boolean areCousins(TreeNode root, int member1, int member2) {
    // Your code here
}
```

## Hints

1. Find the depth and parent of each target node
2. Use BFS or DFS to track level and parent
3. Two nodes are cousins if: same depth AND different parents
4. Store (depth, parent) for each node as you search
5. Time complexity: O(n), Space complexity: O(n)

## Tags
`binary-tree` `breadth-first-search` `level-order` `easy`
