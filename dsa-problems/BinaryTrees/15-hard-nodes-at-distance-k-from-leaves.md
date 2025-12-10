# Fire Spread Risk Analysis

**Difficulty:** Hard
**Topic:** Binary Trees, Distance Calculation
**License:** Free to use for commercial purposes

## Problem Statement

A forest is modeled as a binary tree. Leaf nodes represent potential fire sources (dry bushes). A fire safety algorithm needs to identify all zones (nodes) that are at a specific risk distance `k` from any fire source.

Count how many nodes are exactly at distance `k` from at least one leaf node.

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

Leaves (Fire Sources): 20, 40, 70
Nodes at distance 1:
- Node 30 (dist 1 from 20 and 40)
- Node 50 (dist 1 from 70)

Output: 2
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
- Node 100 (dist 2 from 60 and 90)

Output: 1
```

### Example 3
```
Input: root = [10, 5, 15], k = 0
Output: 2
Explanation: Leaves themselves are at distance 0.
```

## Function Signature

### Python
```python
def count_risk_zones(root: TreeNode, k: int) -> int:
    pass
```

### JavaScript
```javascript
function countRiskZones(root, k) {
    // Your code here
}
```

### Java
```java
public int countRiskZones(TreeNode root, int k) {
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
