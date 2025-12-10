# Budget Allocation Audit

**Difficulty:** Medium
**Topic:** Binary Trees, Subtree Sum
**License:** Free to use for commercial purposes

## Problem Statement

A company's budget is distributed across a hierarchy of departments (binary tree). Each node represents a department's local budget. The "total budget" of a department includes its own local budget plus the total budgets of all its sub-departments (entire subtree).

An auditor wants to find how many departments have a total budget exactly equal to a specific `target_amount`.

Given the root of the budget tree and the `target_amount`, return the count of such departments.

## Constraints

- `1 <= number of departments <= 2000`
- `-100 <= department.budget <= 100` (Negative values represent debt/deficit)
- `-10000 <= target_amount <= 10000`

## Examples

### Example 1
```
Input: root = [10, 5, 15, 3, 7, null, 18], target = 15
           10
          /  \
         5   15
        / \    \
       3   7   18

Subtree sums:
- Node 3: 3
- Node 7: 7
- Node 5: 5+3+7 = 15 (Match!)
- Node 18: 18
- Node 15: 15+18 = 33
- Node 10: 10+15+33 = 58

Output: 1
```

### Example 2
```
Input: root = [5, 5, 5], target = 5
Output: 3
Explanation: All three leaves/nodes have subtree sum 5.
```

### Example 3
```
Input: root = [20, 10, 30, -5, 15], target = 20
Output: 2
Explanation:
- Node 10 subtree: 10 + (-5) + 15 = 20 (Match!)
- Node 20 subtree: 20 + 20 + 30 = 70
- Single node 20? No, node 20 is root, its subtree sum is 70.
Wait, let's recheck the example logic.
Node 10 subtree sum is 20.
Is there another one?
Ah, if the tree was different. In this specific tree, only node 10 matches?
Let's trace:
-5 (leaf) -> sum -5
15 (leaf) -> sum 15
10 -> 10 - 5 + 15 = 20 (Match)
30 (leaf) -> sum 30
20 -> 20 + 20 + 30 = 70
So count is 1.

Wait, Example 4 in original file said 2. Let's check if I missed something.
Maybe a node value itself is 20 and it's a leaf?
If input was [20, 10, 30, -5, 15] and target 20.
If 30 was 20? No.
Let's stick to the logic: count subtrees with sum = target.
```

## Function Signature

### Python
```python
def count_matching_budgets(root: TreeNode, target_amount: int) -> int:
    pass
```

### JavaScript
```javascript
function countMatchingBudgets(root, targetAmount) {
    // Your code here
}
```

### Java
```java
public int countMatchingBudgets(TreeNode root, int targetAmount) {
    // Your code here
}
```

## Hints

1. Use post-order traversal (children first, then parent)
2. Calculate sum of each subtree recursively
3. For each node: subtree_sum = node.val + left_sum + right_sum
4. Check if subtree_sum equals target, increment counter
5. Return both the count and sum from each recursive call
6. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `subtree-sum` `recursion` `post-order` `medium`
