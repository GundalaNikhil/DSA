# Find All Routes

**Difficulty:** Medium
**Topic:** Graphs, DFS, Backtracking
**License:** Free to use for commercial purposes

## Problem Statement

Given a directed graph with n nodes (labeled 0 to n-1) and a list of edges, find all possible paths from node 0 to node n-1. Return all paths in any order.

Each path should be represented as a list of nodes visited in order. The graph is acyclic.

## Constraints

- `2 <= n <= 15`
- `0 <= edges.length <= 100`
- Graph is a DAG (no cycles)

## Examples

### Example 1
```
Input: n = 4, edges = [[0,1], [0,2], [1,3], [2,3]]

Graph:
  0
 / \
1   2
 \ /
  3

Paths from 0 to 3:
- [0, 1, 3]
- [0, 2, 3]

Output: [[0,1,3], [0,2,3]]
```

### Example 2
```
Input: n = 5, edges = [[0,1], [0,2], [1,3], [2,3], [3,4]]

Graph:
    0
   / \
  1   2
   \ /
    3
    |
    4

Paths: [0,1,3,4], [0,2,3,4]

Output: [[0,1,3,4], [0,2,3,4]]
```

### Example 3
```
Input: n = 3, edges = [[0,1], [1,2], [0,2]]

Graph:
0 → 1 → 2
 \     ↗

Paths: [0,1,2], [0,2]

Output: [[0,1,2], [0,2]]
```

### Example 4
```
Input: n = 2, edges = [[0,1]]

Simple path: 0 → 1

Output: [[0,1]]
```

## Function Signature

### Python
```python
def all_paths(n: int, edges: list[list[int]]) -> list[list[int]]:
    pass
```

### JavaScript
```javascript
function allPaths(n, edges) {
    // Your code here
}
```

### Java
```java
public List<List<Integer>> allPaths(int n, int[][] edges) {
    // Your code here
}
```

## Hints

1. Build adjacency list from edges
2. Use DFS with backtracking to explore all paths
3. Start from node 0 with an empty path
4. When you reach node n-1, add current path to result
5. Backtrack by removing last node and trying other options

## Tags
`graph` `dfs` `backtracking` `path-finding` `medium`
