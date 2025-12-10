# Census of Specific Age Group

**Difficulty:** Easy
**Topic:** Binary Trees, Counting
**License:** Free to use for commercial purposes

## Problem Statement

A government census bureau stores citizen data in a binary tree structure where each node represents a citizen's age. They need to count how many citizens fall within a specific age range `[min_age, max_age]` (inclusive).

Given the root of the binary tree and two integers `min_age` and `max_age`, return the count of citizens in that age group.

## Constraints

- `1 <= number of citizens <= 2500`
- `1 <= citizen.age <= 120`
- `1 <= min_age <= max_age <= 120`

## Examples

### Example 1
```
Input: root = [17, 9, 38, 4, 12, 25, 44], min_age = 10, max_age = 40
            17
           /  \
          9   38
         / \  / \
        4 12 25 44

Output: 4
Explanation: Ages in range [10, 40]: 17, 12, 38, 25.
```

### Example 2
```
Input: root = [55, 33, 77, 22, 44], min_age = 30, max_age = 60
         55
        /  \
      33    77
     /  \
   22   44

Output: 3
Explanation: Ages 55, 33, 44 are in range [30, 60].
```

### Example 3
```
Input: root = [100, 50, 150], min_age = 20, max_age = 30
Output: 0
Explanation: No citizens in range [20, 30].
```

## Function Signature

### Python
```python
def count_age_group(root: TreeNode, min_age: int, max_age: int) -> int:
    pass
```

### JavaScript
```javascript
function countAgeGroup(root, minAge, maxAge) {
    // Your code here
}
```

### Java
```java
public int countAgeGroup(TreeNode root, int minAge, int maxAge) {
    // Your code here
}
```

## Hints

1. Visit every node in the tree
2. Check if current node's value is between min and max
3. Count it if yes, skip if no
4. Recursively check left and right subtrees
5. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `counting` `range-query` `easy`
