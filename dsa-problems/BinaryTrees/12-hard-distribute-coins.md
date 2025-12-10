# Load Balancing Server Clusters

**Difficulty:** Hard
**Topic:** Binary Trees, Tree Traversal, Balancing
**License:** Free to use for commercial purposes

## Problem Statement

A network of servers is organized as a binary tree. Each server node currently holds a certain number of active tasks (represented by an integer). The system administrator wants to balance the load such that every server handles exactly 1 task.

In one operation, you can move 1 task from a server to its directly connected parent or child.

The total number of tasks in the entire network equals the number of servers (so a perfect balance is always possible).

Return the minimum number of move operations required to achieve this balance.

## Constraints

- `1 <= number of servers <= 500`
- `0 <= server.tasks <= 100`
- Total tasks = number of servers

## Examples

### Example 1
```
Input: root = [3, 0, 0]
        3
       / \
      0   0

Output: 2
Explanation:
- Server 3 has 2 extra tasks.
- Move 1 task to left child (1 op).
- Move 1 task to right child (1 op).
Total: 2 moves.
```

### Example 2
```
Input: root = [0, 3, 0]
        0
       / \
      3   0

Output: 3
Explanation:
- Left child (3 tasks) moves 2 tasks to root (2 ops).
- Root now has 2 tasks (0 original + 2 received).
- Root moves 1 task to right child (1 op).
Total: 3 moves.
```

### Example 3
```
Input: root = [1, 0, 2]
Output: 2
Explanation: Right child gives 1 to root. Root gives 1 to left child.
```

## Function Signature

### Python
```python
def balance_server_load(root: TreeNode) -> int:
    pass
```

### JavaScript
```javascript
function balanceServerLoad(root) {
    // Your code here
}
```

### Java
```java
public int balanceServerLoad(TreeNode root) {
    // Your code here
}
```

## Hints

1. Use post-order DFS (process children first)
2. For each node, calculate excess = tasks - 1 (what it needs/has extra)
3. A node needs to pass its excess to parent
4. Number of moves through an edge = |excess from that subtree|
5. Total moves = sum of absolute excess values from all subtrees
6. Time complexity: O(n), Space complexity: O(h)

## Tags
`binary-tree` `depth-first-search` `greedy` `balancing` `hard`
