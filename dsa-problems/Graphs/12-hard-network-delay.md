# Signal Broadcasting Time

**Difficulty:** Hard
**Topic:** Graphs, Dijkstra, BFS
**License:** Free to use for commercial purposes

## Problem Statement

You have n network nodes. A signal is sent from a source node and propagates through the network. Each connection has a delay time. Find the minimum time for all nodes to receive the signal.

If some nodes cannot receive the signal, return -1.

## Constraints

- `1 <= n <= 1000`
- `1 <= connections.length <= 5000`
- Nodes are labeled from 1 to n
- `connections[i] = [from, to, delay]`
- `1 <= delay <= 100`

## Examples

### Example 1
```
Input: n = 4, connections = [[1,2,2], [1,3,4], [2,4,3], [3,4,1]], source = 1

Signal propagation:
- Time 0: Node 1 sends signal
- Time 2: Node 2 receives (via 1→2)
- Time 4: Node 3 receives (via 1→3)
- Time 5: Node 4 receives first via 1→2→4 OR at time 5 via 1→3→4

All nodes received by time 5

Output: 5
```

### Example 2
```
Input: n = 3, connections = [[1,2,1]], source = 1

Nodes 1 and 2 are connected, but node 3 is isolated

Output: -1
Explanation: Node 3 cannot receive the signal
```

### Example 3
```
Input: n = 5, connections = [[1,2,1], [2,3,2], [1,4,4], [3,4,1], [4,5,3]], source = 1

All nodes reachable from 1
Time to reach each:
- Node 1: 0
- Node 2: 1
- Node 3: 3
- Node 4: 4
- Node 5: 7

Output: 7
```

### Example 4
```
Input: n = 2, connections = [[1,2,10], [2,1,5]], source = 2

Starting from node 2:
- Node 1 receives at time 5

Output: 5
```

## Function Signature

### Python
```python
def network_delay(n: int, connections: list[list[int]], source: int) -> int:
    pass
```

### JavaScript
```javascript
function networkDelay(n, connections, source) {
    // Your code here
}
```

### Java
```java
public int networkDelay(int n, int[][] connections, int source) {
    // Your code here
}
```

## Hints

1. Find shortest time to reach each node from source (Dijkstra)
2. The answer is the maximum of all shortest times
3. If any node is unreachable, return -1
4. Use priority queue to process nodes in order of arrival time
5. Track visited nodes and minimum arrival times

## Tags
`graph` `dijkstra` `shortest-path` `broadcasting` `hard`
