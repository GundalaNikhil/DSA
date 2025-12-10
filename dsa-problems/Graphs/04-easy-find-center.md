# Find Star Graph Center

**Difficulty:** Easy
**Topic:** Graphs, Graph Properties
**License:** Free to use for commercial purposes

## Problem Statement

A star graph is a graph where one central node is connected to all other nodes, and there are no other connections. Given the edges of a star graph, find the center node.

The graph is guaranteed to be a star graph with n nodes. Return the ID of the center node.

## Constraints

- `3 <= n <= 1000`
- `edges.length == n - 1`
- Graph is guaranteed to be a star
- Nodes are numbered from 1 to n

## Examples

### Example 1
```
Input: edges = [[1,2], [2,3], [2,4]]

Graph structure:
  1
   \
    2 (center)
   / \
  3   4

Output: 2
Explanation: Node 2 is connected to all other nodes
```

### Example 2
```
Input: edges = [[5,1], [5,2], [5,3], [5,4]]

Graph:
    1
    |
2 - 5 - 4
    |
    3

Output: 5
```

### Example 3
```
Input: edges = [[1,3], [2,3], [4,3]]

Graph:
  1
   \
    3 (center)
   / \
  2   4

Output: 3
```

### Example 4
```
Input: edges = [[7,8], [7,9]]

Graph:
  8 - 7 - 9

Output: 7
```

## Function Signature

### Python
```python
def find_center(edges: list[list[int]]) -> int:
    pass
```

### JavaScript
```javascript
function findCenter(edges) {
    // Your code here
}
```

### Java
```java
public int findCenter(int[][] edges) {
    // Your code here
}
```

## Hints

1. The center node appears in every edge
2. Check the first two edges - the center must be in both
3. Compare edges[0] and edges[1] to find the common node
4. Alternatively, count degrees - center has degree n-1
5. Time complexity: O(1) with edge comparison, O(n) with degree counting

## Tags
`graph` `star-graph` `properties` `easy`
