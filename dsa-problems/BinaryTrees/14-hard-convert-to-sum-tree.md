# Accumulated Radiation Exposure

**Difficulty:** Hard
**Topic:** Binary Trees, Tree Transformation
**License:** Free to use for commercial purposes

## Problem Statement

A sensor network is deployed in a hazardous zone. Each sensor (node) measures local radiation. However, radiation accumulates upwards. Scientists want to transform the data map such that each sensor reports the total radiation measured by all sensors in its sub-zone (descendants), excluding its own original measurement.

Leaf sensors (with no sub-zone) will report 0.

Modify the tree in-place to reflect these accumulated values and return the root.

## Constraints

- `1 <= number of sensors <= 2500`
- `1 <= sensor.val <= 500`

## Examples

### Example 1
```
Input: root = [10, 5, 15, 2, 8]
         10
        /  \
       5   15
      / \
     2   8

After transformation:
         30
        /  \
      10    0
      / \
     0   0

Explanation:
- Leaves 2, 8, 15 become 0.
- Node 5 becomes 2 + 8 = 10.
- Node 10 becomes 5 + 2 + 8 + 15 = 30.
```

### Example 2
```
Input: root = [20, 10, 30]
Output: [40, 0, 0]
Explanation: Root becomes 10 + 30 = 40. Leaves become 0.
```

### Example 3
```
Input: root = [50]
Output: [0]
```

## Function Signature

### Python
```python
def accumulate_radiation(root: TreeNode) -> TreeNode:
    pass
```

### JavaScript
```javascript
function accumulateRadiation(root) {
    // Your code here
}
```

### Java
```java
public TreeNode accumulateRadiation(TreeNode root) {
    // Your code here
}
```

## Hints

1. Use post-order traversal (process children first)
2. Create helper function that returns sum of subtree (including current node)
3. For each node: calculate left_sum + right_sum
4. Store original value, then set node.val = left_sum + right_sum
5. Return original_value + left_sum + right_sum to parent
6. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `tree-transformation` `post-order` `recursion` `hard`
