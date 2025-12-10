# Construction Project Timeline

**Difficulty:** Medium
**Topic:** Graphs, Topological Sort, DFS
**License:** Free to use for commercial purposes

## Problem Statement

A construction project consists of `n` phases. Some phases depend on others being completed first. A dependency `[A, B]` means phase A must be finished before phase B can start.

Given the list of `dependencies`, determine a valid linear order in which to complete the phases. If multiple valid orders exist, any one is acceptable. If no valid order exists (due to a cycle), return an empty list.

## Constraints

- `1 <= n <= 1000`
- `0 <= dependencies.length <= 5000`

## Examples

### Example 1
```
Input: n = 5, dependencies = [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4]]
Dependencies:
- 0 before 1
- 0 before 2
- 1 before 3
- 2 before 3
- 3 before 4

Output: [0, 1, 2, 3, 4] or [0, 2, 1, 3, 4]
```

### Example 2
```
Input: n = 3, dependencies = [[0, 1], [1, 2], [2, 0]]
Output: []
Explanation: Cycle 0->1->2->0.
```

### Example 3
```
Input: n = 6, dependencies = [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
Output: [5, 4, 2, 3, 1, 0]
Explanation: One valid topological sort.
```

## Function Signature

### Python
```python
def project_timeline(n: int, dependencies: list[list[int]]) -> list[int]:
    pass
```

### JavaScript
```javascript
function projectTimeline(n, dependencies) {
    // Your code here
}
```

### Java
```java
public int[] projectTimeline(int n, int[][] dependencies) {
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
