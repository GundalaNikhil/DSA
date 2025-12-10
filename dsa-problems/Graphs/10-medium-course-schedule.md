# Task Completion Order

**Difficulty:** Medium
**Topic:** Graphs, Topological Sort, DFS
**License:** Free to use for commercial purposes

## Problem Statement

You need to complete n tasks numbered from 0 to n-1. Some tasks have prerequisites - you must finish certain tasks before starting others. Given the prerequisites, return any valid order to complete all tasks.

If it's impossible to complete all tasks (due to circular dependencies), return an empty array.

## Constraints

- `1 <= n <= 1000`
- `0 <= prerequisites.length <= 5000`
- `prerequisites[i] = [a, b]` means task a must be done before task b

## Examples

### Example 1
```
Input: n = 4, prerequisites = [[1,0], [2,0], [3,1], [3,2]]

Dependencies:
- Task 0 must be done before tasks 1 and 2
- Tasks 1 and 2 must be done before task 3

Valid order: [0, 1, 2, 3] or [0, 2, 1, 3]

Output: [0, 1, 2, 3]
```

### Example 2
```
Input: n = 2, prerequisites = [[1,0], [0,1]]

Task 0 needs task 1
Task 1 needs task 0
→ Circular dependency!

Output: []
```

### Example 3
```
Input: n = 5, prerequisites = [[1,0], [2,1], [3,2], [4,3]]

Linear chain: 0 → 1 → 2 → 3 → 4

Output: [0, 1, 2, 3, 4]
```

### Example 4
```
Input: n = 3, prerequisites = []

No dependencies, any order works

Output: [0, 1, 2] (or any permutation)
```

## Function Signature

### Python
```python
def task_order(n: int, prerequisites: list[list[int]]) -> list[int]:
    pass
```

### JavaScript
```javascript
function taskOrder(n, prerequisites) {
    // Your code here
}
```

### Java
```java
public int[] taskOrder(int n, int[][] prerequisites) {
    // Your code here
}
```

## Hints

1. This is a topological sort problem
2. Build adjacency list and track in-degrees
3. Use Kahn's algorithm: start with nodes having 0 in-degree
4. Process nodes level by level, reducing in-degrees
5. If you can't process all n nodes, there's a cycle

## Tags
`graph` `topological-sort` `dfs` `bfs` `medium`
