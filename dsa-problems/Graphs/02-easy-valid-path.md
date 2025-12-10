# Check If Path Exists

**Difficulty:** Easy
**Topic:** Graphs, BFS, DFS
**License:** Free to use for commercial purposes

## Problem Statement

You have a map with cities and roads. Each road connects two cities. Check if you can travel from a start city to a destination city using the available roads.

Return true if a path exists, false otherwise.

## Constraints

- `1 <= number of cities <= 1000`
- `0 <= roads.length <= 5000`
- Cities are numbered from 0 to n-1
- `0 <= start, destination < n`

## Examples

### Example 1
```
Input: n = 5, roads = [[0,1], [1,2], [2,3], [3,4]], start = 0, destination = 4

Cities and connections:
0 - 1 - 2 - 3 - 4

Output: true
Explanation: Can travel 0→1→2→3→4
```

### Example 2
```
Input: n = 6, roads = [[0,1], [1,2], [3,4]], start = 0, destination = 5

Connections:
0 - 1 - 2
3 - 4
5 (isolated)

Output: false
Explanation: City 5 is not connected to city 0
```

### Example 3
```
Input: n = 3, roads = [[0,1], [1,2], [2,0]], start = 0, destination = 2

Output: true
Explanation: Can go 0→1→2 or 0→2 directly
```

### Example 4
```
Input: n = 1, roads = [], start = 0, destination = 0

Output: true
Explanation: Start and destination are the same city
```

## Function Signature

### Python
```python
def has_path(n: int, roads: list[list[int]], start: int, destination: int) -> bool:
    pass
```

### JavaScript
```javascript
function hasPath(n, roads, start, destination) {
    // Your code here
}
```

### Java
```java
public boolean hasPath(int n, int[][] roads, int start, int destination) {
    // Your code here
}
```

## Hints

1. Build an adjacency list from roads
2. Use BFS or DFS starting from the start city
3. Keep track of visited cities to avoid infinite loops
4. If you reach the destination during traversal, return true
5. If traversal completes without finding destination, return false

## Tags
`graph` `bfs` `dfs` `path-finding` `easy`
