# Fragile Power Grid Lines

**Difficulty:** Hard
**Topic:** Graphs, DFS, Bridges
**License:** Free to use for commercial purposes

## Problem Statement

A power grid consists of `n` substations connected by transmission lines. A "fragile line" is a connection that, if it fails (is removed), would split the grid into disconnected islands, causing a blackout in some areas.

Find all such fragile lines (critical connections) in the grid.

Return the list of these connections.

## Constraints

- `1 <= n <= 1000`
- `n-1 <= connections.length <= 5000`
- Substations are numbered from 0 to n-1
- Grid is initially connected
- No duplicate connections

## Examples

### Example 1
```
Input: n = 5, connections = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4]]

Structure:
Triangle 0-1-2.
1 connects to 3.
3 connects to 4.

Fragile lines:
- [1, 3]: If removed, 3-4 is isolated.
- [3, 4]: If removed, 4 is isolated.
(0,1,2 are in a cycle, so lines between them are safe).

Output: [[1, 3], [3, 4]]
```

### Example 2
```
Input: n = 4, connections = [[0, 1], [1, 2], [2, 3]]
Output: [[0, 1], [1, 2], [2, 3]]
Explanation: Linear chain. All lines are critical.
```

### Example 3
```
Input: n = 3, connections = [[0, 1], [1, 2], [2, 0]]
Output: []
Explanation: A single cycle. No single line failure disconnects the grid.
```

## Function Signature

### Python
```python
def find_fragile_lines(n: int, connections: list[list[int]]) -> list[list[int]]:
    pass
```

### JavaScript
```javascript
function findFragileLines(n, connections) {
    // Your code here
}
```

### Java
```java
public List<List<Integer>> findFragileLines(int n, int[][] connections) {
    // Your code here
}
```

## Hints

1. This is a bridge-finding problem in graph theory
2. Use Tarjan's algorithm with DFS
3. Track discovery time and lowest reachable ancestor for each node
4. An edge is a bridge if there's no back edge bypassing it
5. Edge [u,v] is critical if low[v] > disc[u]

## Tags
`graph` `dfs` `bridges` `tarjan` `hard`
