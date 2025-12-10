# Flight Plan Generator

**Difficulty:** Medium
**Topic:** Graphs, DFS, Backtracking
**License:** Free to use for commercial purposes

## Problem Statement

An airline route planner needs to find all possible flight itineraries from a starting airport (ID 0) to a destination airport (ID n-1).

Given `n` airports and a list of direct `flights` (directed edges), return a list of all valid itineraries (paths) from airport 0 to airport n-1.

The flight network is guaranteed to be acyclic (no loops).

## Constraints

- `2 <= n <= 15`
- `0 <= flights.length <= 100`
- Graph is a DAG

## Examples

### Example 1
```
Input: n = 5, flights = [[0, 1], [0, 3], [1, 2], [3, 2], [2, 4]]
Output: [[0, 1, 2, 4], [0, 3, 2, 4]]
Explanation:
- Route 1: 0 -> 1 -> 2 -> 4
- Route 2: 0 -> 3 -> 2 -> 4
```

### Example 2
```
Input: n = 4, flights = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3]]
Output: [[0, 1, 2, 3], [0, 1, 3], [0, 2, 3]]
```

### Example 3
```
Input: n = 3, flights = [[0, 1], [1, 0]]
Output: []
Explanation: Wait, problem says DAG (acyclic), but if input had cycle it would be invalid.
Assuming valid DAG input:
Input: n = 3, flights = [[0, 1]]
Output: []
Explanation: No path to node 2.
```

## Function Signature

### Python
```python
def generate_flight_plans(n: int, flights: list[list[int]]) -> list[list[int]]:
    pass
```

### JavaScript
```javascript
function generateFlightPlans(n, flights) {
    // Your code here
}
```

### Java
```java
public List<List<Integer>> generateFlightPlans(int n, int[][] flights) {
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
