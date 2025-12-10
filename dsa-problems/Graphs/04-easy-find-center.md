# Central Server Identification

**Difficulty:** Easy
**Topic:** Graphs, Graph Properties
**License:** Free to use for commercial purposes

## Problem Statement

A network topology is designed as a star graph, where one central server is connected to every other client node, and client nodes are not connected to each other.

Given the list of `connections` in this network, identify the ID of the central server.

The network is guaranteed to be a valid star topology with `n` nodes (labeled 1 to n).

## Constraints

- `3 <= n <= 1000`
- `connections.length == n - 1`

## Examples

### Example 1
```
Input: connections = [[3, 1], [3, 2], [3, 4], [3, 5]]
Output: 3
Explanation: Node 3 connects to 1, 2, 4, 5. It is the center.
```

### Example 2
```
Input: connections = [[1, 2], [2, 3], [4, 2]]
Output: 2
Explanation: Node 2 is the common node in all edges.
```

### Example 3
```
Input: connections = [[10, 1], [10, 5], [10, 20]]
Output: 10
```

## Function Signature

### Python
```python
def find_central_server(connections: list[list[int]]) -> int:
    pass
```

### JavaScript
```javascript
function findCentralServer(connections) {
    // Your code here
}
```

### Java
```java
public int findCentralServer(int[][] connections) {
    // Your code here
}
```

## Hints

1. The center node appears in every edge
2. Check the first two edges - the center must be in both
3. Compare edges[0] and edges[1] to find the common node
4. Time complexity: O(1)

## Tags
`graph` `star-graph` `properties` `easy`
