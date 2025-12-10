# Minimum Cost Network Connection

**Difficulty:** Hard
**Topic:** Graphs, Minimum Spanning Tree, Union-Find
**License:** Free to use for commercial purposes

## Problem Statement

You need to connect n cities with cables. You have a list of possible cable connections, each with a cost. Find the minimum total cost to connect all cities together.

If it's impossible to connect all cities, return -1.

## Constraints

- `1 <= n <= 1000`
- `0 <= cables.length <= 5000`
- `cables[i] = [city1, city2, cost]`
- `1 <= cost <= 1000`

## Examples

### Example 1
```
Input: n = 4, cables = [[0,1,2], [0,2,5], [1,2,3], [1,3,6], [2,3,4]]

Possible spanning trees:
Choose edges: [0,1], [1,2], [2,3] = cost 2+3+4 = 9
Or: [0,1], [0,2], [2,3] = cost 2+5+4 = 11

Minimum: 9

Output: 9
```

### Example 2
```
Input: n = 3, cables = [[0,1,10], [0,2,15], [1,2,20]]

Need 2 edges to connect 3 cities:
Choose: [0,1] and [0,2] = 10+15 = 25
Or: [0,1] and [1,2] = 10+20 = 30
Or: [0,2] and [1,2] = 15+20 = 35

Output: 25
```

### Example 3
```
Input: n = 4, cables = [[0,1,1], [2,3,2]]

Two separate components: {0,1} and {2,3}
Cannot connect all cities

Output: -1
```

### Example 4
```
Input: n = 5, cables = [[0,1,3], [0,2,4], [1,2,2], [1,3,5], [2,3,3], [3,4,1]]

Build MST:
- Add [3,4] cost 1
- Add [1,2] cost 2
- Add [0,1] cost 3
- Add [2,3] cost 3
Total: 1+2+3+3 = 9

Output: 9
```

## Function Signature

### Python
```python
def min_cost_connect(n: int, cables: list[list[int]]) -> int:
    pass
```

### JavaScript
```javascript
function minCostConnect(n, cables) {
    // Your code here
}
```

### Java
```java
public int minCostConnect(int n, int[][] cables) {
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
