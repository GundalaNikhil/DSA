# Minimum Distance Between Cities

**Difficulty:** Medium
**Topic:** Graphs, BFS, Shortest Path
**License:** Free to use for commercial purposes

## Problem Statement

You have a network of cities connected by roads. Each road takes 1 unit of time to travel. Find the shortest travel time from a start city to a destination city.

If no path exists between the cities, return -1.

## Constraints

- `1 <= number of cities <= 1000`
- `0 <= roads.length <= 5000`
- `0 <= start, destination < n`
- Roads are bidirectional

## Examples

### Example 1
```
Input: n = 6, roads = [[0,1], [1,2], [0,3], [3,4], [4,5], [2,5]], start = 0, destination = 5

Paths:
- 0→1→2→5 (length 3)
- 0→3→4→5 (length 3)

Output: 3
```

### Example 2
```
Input: n = 5, roads = [[0,1], [1,2], [3,4]], start = 0, destination = 4

No path exists between 0 and 4

Output: -1
```

### Example 3
```
Input: n = 4, roads = [[0,1], [1,2], [2,3], [0,3]], start = 0, destination = 3

Paths:
- 0→3 (length 1) - direct
- 0→1→2→3 (length 3)

Output: 1
Explanation: Direct path is shortest
```

### Example 4
```
Input: n = 3, roads = [[0,1], [1,2]], start = 2, destination = 2

Output: 0
Explanation: Start and destination are the same
```

## Function Signature

### Python
```python
def shortest_distance(n: int, roads: list[list[int]], start: int, destination: int) -> int:
    pass
```

### JavaScript
```javascript
function shortestDistance(n, roads, start, destination) {
    // Your code here
}
```

### Java
```java
public int shortestDistance(int n, int[][] roads, int start, int destination) {
    // Your code here
}
```

## Hints

1. Use BFS (breadth-first search) for shortest path in unweighted graphs
2. Start from the start city and explore level by level
3. Track distance for each city as you visit it
4. When you reach destination, return its distance
5. Time complexity: O(n + e), Space complexity: O(n)

## Tags
`graph` `bfs` `shortest-path` `unweighted` `medium`
