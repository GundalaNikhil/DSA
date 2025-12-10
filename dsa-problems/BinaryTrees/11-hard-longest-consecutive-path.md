# Hiking Trail Elevation Streak

**Difficulty:** Hard
**Topic:** Binary Trees, Path Finding
**License:** Free to use for commercial purposes

## Problem Statement

A mountain hiking area is mapped as a binary tree where each node represents a checkpoint with a specific elevation. A "consecutive hike" is a path where the elevation increases by exactly 1 meter at each step (e.g., 100 -> 101 -> 102). The path can go from a parent checkpoint to a child checkpoint.

Given the root of the elevation map, find the length of the longest consecutive hike path.

## Constraints

- `1 <= number of checkpoints <= 3000`
- `1 <= elevation <= 1000`

## Examples

### Example 1
```
Input: root = [10, 8, 12, 7, 9, 11, 13]
            10
           /  \
          8   12
         / \  / \
        7  9 11 13

Longest consecutive hikes:
- 7->8 (length 2)
- 8->9 (length 2)
- 11->12->13 (length 3)

Output: 3
Explanation: The path 11->12->13 represents a consecutive elevation gain.
```

### Example 2
```
Input: root = [50, 49, 51, 48, null, null, 52]
           50
          /  \
        49   51
        /      \
      48       52

Output: 5
Explanation: Path 48->49->50->51->52 forms a sequence of length 5.
```

### Example 3
```
Input: root = [100, 200, 300]
Output: 1
Explanation: No consecutive sequence exists.
```

## Function Signature

### Python
```python
def longest_elevation_streak(root: TreeNode) -> int:
    pass
```

### JavaScript
```javascript
function longestElevationStreak(root) {
    // Your code here
}
```

### Java
```java
public int longestElevationStreak(TreeNode root) {
    // Your code here
}
```

## Hints

1. At each node, track consecutive length from parent
2. If child.val == parent.val + 1, length = parent_length + 1
3. Else length = 1
4. Track global maximum
5. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `depth-first-search` `path-finding` `consecutive` `hard`
