# Fiber Optic Cable Layout

**Difficulty:** Hard
**Topic:** Graphs, Minimum Spanning Tree, Union-Find
**License:** Free to use for commercial purposes

## Problem Statement

A telecommunications company wants to lay fiber optic cables to connect `n` data centers. You are given a list of potential `connections`, where each connection `[center_a, center_b, cost]` represents the cost to lay a cable between two centers.

Find the minimum total cost required to connect all data centers together (directly or indirectly).

If it's impossible to connect all centers, return -1.

## Constraints

- `1 <= n <= 1000`
- `0 <= connections.length <= 5000`
- `1 <= cost <= 1000`

## Examples

### Example 1
```
Input: n = 4, connections = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]

MST Construction:
1. Edge [2, 3] cost 4. (Connects 2-3)
2. Edge [0, 3] cost 5. (Connects 0-3)
3. Edge [0, 2] cost 6. (Skip, 0 and 2 already connected via 3)
4. Edge [0, 1] cost 10. (Connects 1-0)

Total cost: 4 + 5 + 10 = 19.

Output: 19
```

### Example 2
```
Input: n = 3, connections = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
Edges sorted: [0,2,1], [1,2,3], [0,1,5]
1. [0,2] cost 1.
2. [1,2] cost 3.
All connected. Total 4.

Output: 4
```

### Example 3
```
Input: n = 4, connections = [[0, 1, 1], [2, 3, 1]]
Output: -1
Explanation: Two disconnected components.
```

## Function Signature

### Python
```python
def min_cable_cost(n: int, connections: list[list[int]]) -> int:
    pass
```

### JavaScript
```javascript
function minCableCost(n, connections) {
    // Your code here
}
```

### Java
```java
public int minCableCost(int n, int[][] connections) {
    // Your code here
}
```

## Hints

1. Use Kruskal's algorithm: sort edges by cost
2. Use Union-Find data structure to detect cycles
3. Add edges one by one if they don't create a cycle
4. Stop when you have n-1 edges (or all edges processed)
5. If final count < n-1 edges, graph is disconnected

## Tags
`graph` `minimum-spanning-tree` `kruskal` `union-find` `hard`
