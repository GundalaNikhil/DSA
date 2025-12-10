# Minimum Cost Travel Route

**Difficulty:** Hard
**Topic:** Graphs, Dijkstra, Shortest Path
**License:** Free to use for commercial purposes

## Problem Statement

You have a network of cities connected by toll roads. Each road has a specific cost to travel. Find the minimum total cost to travel from a start city to a destination city.

If no path exists, return -1.

## Constraints

- `1 <= number of cities <= 1000`
- `0 <= roads.length <= 5000`
- `1 <= cost <= 1000` for each road
- Roads are bidirectional
- `0 <= start, destination < n`

## Examples

### Example 1
```
Input: n = 5, roads = [[0,1,4], [0,2,1], [2,1,2], [1,3,5], [2,3,8], [3,4,3]], start = 0, destination = 4

Paths and costs:
- 0→1→3→4: cost = 4+5+3 = 12
- 0→2→1→3→4: cost = 1+2+5+3 = 11
- 0→2→3→4: cost = 1+8+3 = 12

Output: 11
```

### Example 2
```
Input: n = 4, roads = [[0,1,10], [1,2,20], [0,3,50], [3,2,5]], start = 0, destination = 2

Paths:
- 0→1→2: cost = 10+20 = 30
- 0→3→2: cost = 50+5 = 55

Output: 30
```

### Example 3
```
Input: n = 3, roads = [[0,1,100]], start = 0, destination = 2

No path exists between 0 and 2

Output: -1
```

### Example 4
```
Input: n = 6, roads = [[0,1,2], [1,2,3], [0,3,10], [3,4,2], [4,5,1], [2,5,4]], start = 0, destination = 5

Best path: 0→1→2→5 = 2+3+4 = 9

Output: 9
```

## Function Signature

### Python
```python
def min_cost_path(n: int, roads: list[list[int]], start: int, destination: int) -> int:
    pass
```

### JavaScript
```javascript
function minCostPath(n, roads, start, destination) {
    // Your code here
}
```

### Java
```java
public int minCostPath(int n, int[][] roads, int start, int destination) {
    // Your code here
}
```

## Hints

1. Use Dijkstra's algorithm for weighted shortest path
2. Maintain a priority queue with (cost, node) pairs
3. Track minimum cost to reach each node
4. Always expand the node with smallest cost first
5. Time complexity: O((n+e) log n), Space complexity: O(n+e)

## Tags
`graph` `dijkstra` `shortest-path` `weighted-graph` `hard`
