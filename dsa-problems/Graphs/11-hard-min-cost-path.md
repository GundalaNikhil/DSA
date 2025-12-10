# Interstellar Fuel Efficiency

**Difficulty:** Hard
**Topic:** Graphs, Dijkstra, Shortest Path
**License:** Free to use for commercial purposes

## Problem Statement

A spaceship needs to travel between star systems. The galaxy is mapped as a set of star systems connected by wormholes. Each wormhole has a specific fuel cost to traverse.

Given `n` star systems (labeled 0 to n-1), a list of `wormholes` where each is `[system_a, system_b, fuel_cost]`, a `start_system`, and a `destination_system`, find the minimum fuel required to complete the journey.

If the destination is unreachable, return -1.

## Constraints

- `1 <= number of systems <= 1000`
- `0 <= wormholes.length <= 5000`
- `1 <= fuel_cost <= 1000`
- Wormholes are bidirectional
- `0 <= start, destination < n`

## Examples

### Example 1
```
Input: n = 5, wormholes = [[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4], [2, 3, 8], [3, 4, 5]], start = 0, destination = 4

Routes:
- 0->1->3->4: 10+2+5 = 17
- 0->2->1->3->4: 3+4+2+5 = 14
- 0->2->3->4: 3+8+5 = 16

Output: 14
```

### Example 2
```
Input: n = 4, wormholes = [[0, 1, 5], [1, 2, 5], [0, 3, 20], [3, 2, 2]], start = 0, destination = 2

Routes:
- 0->1->2: 5+5 = 10
- 0->3->2: 20+2 = 22

Output: 10
```

### Example 3
```
Input: n = 3, wormholes = [[0, 1, 50]], start = 0, destination = 2
Output: -1
Explanation: System 2 is isolated.
```

## Function Signature

### Python
```python
def min_fuel_cost(n: int, wormholes: list[list[int]], start: int, destination: int) -> int:
    pass
```

### JavaScript
```javascript
function minFuelCost(n, wormholes, start, destination) {
    // Your code here
}
```

### Java
```java
public int minFuelCost(int n, int[][] wormholes, int start, int destination) {
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
