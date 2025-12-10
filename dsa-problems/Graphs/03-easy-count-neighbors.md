# Count Direct Connections

**Difficulty:** Easy
**Topic:** Graphs, Graph Representation
**License:** Free to use for commercial purposes

## Problem Statement

You have a network of computers where some computers are directly connected. Given a list of connections and a specific computer ID, count how many other computers are directly connected to it.

Only count direct connections, not connections through other computers.

## Constraints

- `1 <= number of computers <= 1000`
- `0 <= connections.length <= 5000`
- `0 <= target < n`
- Connections are bidirectional

## Examples

### Example 1
```
Input: n = 6, connections = [[0,1], [0,2], [1,3], [2,4], [3,5]], target = 0

Computer 0's direct connections: 1, 2

Output: 2
Explanation: Computer 0 is directly connected to computers 1 and 2
```

### Example 2
```
Input: n = 5, connections = [[0,1], [1,2], [2,3], [3,4]], target = 2

Computer 2's direct connections: 1, 3

Output: 2
```

### Example 3
```
Input: n = 4, connections = [[0,1], [0,2], [0,3]], target = 0

Computer 0's direct connections: 1, 2, 3

Output: 3
Explanation: Computer 0 is connected to all other computers
```

### Example 4
```
Input: n = 5, connections = [[1,2], [3,4]], target = 0

Computer 0's direct connections: none

Output: 0
Explanation: Computer 0 has no connections
```

## Function Signature

### Python
```python
def count_neighbors(n: int, connections: list[list[int]], target: int) -> int:
    pass
```

### JavaScript
```javascript
function countNeighbors(n, connections, target) {
    // Your code here
}
```

### Java
```java
public int countNeighbors(int n, int[][] connections, int target) {
    // Your code here
}
```

## Hints

1. Build an adjacency list or use a simple counter
2. For each connection [a, b], both a and b are neighbors
3. If connection contains target, increment count
4. Remember connections are bidirectional
5. Time complexity: O(e), Space complexity: O(n)

## Tags
`graph` `adjacency-list` `counting` `easy`
