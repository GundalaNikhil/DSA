# Find Network Bottlenecks

**Difficulty:** Hard
**Topic:** Graphs, DFS, Bridges
**License:** Free to use for commercial purposes

## Problem Statement

You have a computer network with n servers connected by cables. A critical connection is a cable whose removal would disconnect the network into multiple parts. Find all critical connections.

Return the list of critical connections in any order.

## Constraints

- `1 <= n <= 1000`
- `n-1 <= connections.length <= 5000`
- Servers are numbered from 0 to n-1
- Network is initially connected
- No duplicate connections

## Examples

### Example 1
```
Input: n = 4, connections = [[0,1], [1,2], [2,0], [1,3]]

Network:
  0---1---3
   \ /
    2

Critical connections: [[1,3]]
Explanation: Removing [1,3] disconnects server 3 from the rest
The triangle [0,1,2] has redundant paths, so no edge there is critical
```

### Example 2
```
Input: n = 5, connections = [[0,1], [1,2], [2,3], [3,4]]

Linear chain: 0-1-2-3-4

Output: [[0,1], [1,2], [2,3], [3,4]]
Explanation: Every connection is critical (removing any breaks the chain)
```

### Example 3
```
Input: n = 6, connections = [[0,1], [1,2], [2,0], [1,3], [3,4], [4,5], [5,3]]

Network has triangle [0,1,2] and triangle [3,4,5]
Connected by edge [1,3]

Critical: [[1,3]]
```

### Example 4
```
Input: n = 2, connections = [[0,1]]

Output: [[0,1]]
Explanation: Only one connection, must be critical
```

## Function Signature

### Python
```python
def critical_connections(n: int, connections: list[list[int]]) -> list[list[int]]:
    pass
```

### JavaScript
```javascript
function criticalConnections(n, connections) {
    // Your code here
}
```

### Java
```java
public List<List<Integer>> criticalConnections(int n, int[][] connections) {
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
