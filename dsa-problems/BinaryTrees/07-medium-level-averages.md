# Corporate Hierarchy Salary Analysis

**Difficulty:** Medium
**Topic:** Binary Trees, Level Order Traversal
**License:** Free to use for commercial purposes

## Problem Statement

A corporation wants to analyze salary distribution across different levels of its hierarchy. The organization is represented as a binary tree where the root is the CEO, and children are subordinates. Each node contains the salary of that employee.

Calculate the average salary for each level of the hierarchy. Return the level number (0-indexed, where CEO is level 0) that has the highest average salary. If there is a tie, return the smallest level number.

## Constraints

- `1 <= number of employees <= 4000`
- `1000 <= salary <= 100000`

## Examples

### Example 1
```
Input: root = [20000, 10000, 30000, 5000, 15000, 25000, 40000]
           20k
          /   \
       10k    30k
       / \    / \
     5k 15k 25k 40k

Level 0 avg: 20000
Level 1 avg: (10000+30000)/2 = 20000
Level 2 avg: (5000+15000+25000+40000)/4 = 21250

Output: 2
Explanation: Level 2 has the highest average salary.
```

### Example 2
```
Input: root = [50000, 60000, 40000]
Level 0 avg: 50000
Level 1 avg: (60000+40000)/2 = 50000

Output: 0
Explanation: Tie between level 0 and 1. Return lowest level 0.
```

### Example 3
```
Input: root = [100000, 200000, 50000]
Level 0 avg: 100000
Level 1 avg: 125000

Output: 1
```

## Function Signature

### Python
```python
def highest_average_salary_level(root: TreeNode) -> int:
    pass
```

### JavaScript
```javascript
function highestAverageSalaryLevel(root) {
    // Your code here
}
```

### Java
```java
public int highestAverageSalaryLevel(TreeNode root) {
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
