# Bridge Span Calculation

**Difficulty:** Hard
**Topic:** Binary Trees, Level Order Traversal
**License:** Free to use for commercial purposes

## Problem Statement

Civil engineers are designing a bridge support system modeled as a binary tree. They need to calculate the maximum horizontal span at any level of the structure.

The span (width) at a level is defined as the distance between the leftmost and rightmost non-null support pillars, including the empty spaces (null nodes) between them that would exist in a complete binary tree structure.

Return the maximum span found at any level.

## Constraints

- `1 <= number of pillars <= 3000`
- `-100 <= pillar.val <= 100`

## Examples

### Example 1
```
Input: root = [10, 20, 30, 40, null, null, 60]
           10
          /  \
        20   30
        /      \
      40       60

Level 0: width 1
Level 1: width 2 (20 to 30)
Level 2: width 4 (40, null, null, 60)

Output: 4
```

### Example 2
```
Input: root = [50, 40, 60]
Output: 2
Explanation: Level 1 has pillars 40 and 60. Width is 2.
```

### Example 3
```
Input: root = [100, null, 200, null, 300]
        100
          \
          200
            \
            300

Output: 1
Explanation: Each level has only 1 pillar. Max width is 1.
```

## Function Signature

### Python
```python
def max_bridge_span(root: TreeNode) -> int:
    pass
```

### JavaScript
```javascript
function maxBridgeSpan(root) {
    // Your code here
}
```

### Java
```java
public int maxBridgeSpan(TreeNode root) {
    // Your code here
}
```

## Hints

1. Use BFS with position tracking
2. Store (node, position) pairs in queue
3. For each level, track leftmost and rightmost positions
4. Width at level = rightmost_pos - leftmost_pos + 1
5. Be careful with large position values, use position normalization
6. Time complexity: O(n), Space complexity: O(w)

## Tags
`binary-tree` `breadth-first-search` `level-order` `width` `hard`
