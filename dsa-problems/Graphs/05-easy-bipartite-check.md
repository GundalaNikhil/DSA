# Check Two Group Division

**Difficulty:** Easy
**Topic:** Graphs, Bipartite, BFS
**License:** Free to use for commercial purposes

## Problem Statement

You need to divide people into two groups (A and B) such that no two people in the same group are connected. Given the connections between people, check if such a division is possible.

Return true if you can divide everyone into two groups following the rule, false otherwise.

## Constraints

- `1 <= number of people <= 1000`
- `0 <= connections.length <= 5000`
- People are numbered from 0 to n-1

## Examples

### Example 1
```
Input: n = 4, connections = [[0,1], [1,2], [2,3]]

Arrangement:
Group A: 0, 2
Group B: 1, 3

0 - 1 - 2 - 3
A   B   A   B

Output: true
Explanation: Alternating groups work perfectly
```

### Example 2
```
Input: n = 3, connections = [[0,1], [1,2], [2,0]]

Triangle:
  0
 / \
1---2

Output: false
Explanation: Cannot divide a triangle into two groups with this rule
If 0 is in A, then 1 and 2 must be in B, but 1 and 2 are connected
```

### Example 3
```
Input: n = 4, connections = [[0,1], [2,3]]

Groups:
Group A: 0, 2
Group B: 1, 3

Output: true
Explanation: Two separate pairs, easy to divide
```

### Example 4
```
Input: n = 5, connections = [[0,1], [1,2], [3,4]]

Groups:
Group A: 0, 2, 3
Group B: 1, 4

Output: true
```

## Function Signature

### Python
```python
def can_divide_groups(n: int, connections: list[list[int]]) -> bool:
    pass
```

### JavaScript
```javascript
function canDivideGroups(n, connections) {
    // Your code here
}
```

### Java
```java
public boolean canDivideGroups(int n, int[][] connections) {
    // Your code here
}
```

## Hints

1. This is a bipartite graph check problem
2. Use BFS or DFS with 2-coloring approach
3. Start coloring a node with color 0, its neighbors with color 1
4. If you encounter a neighbor with the same color, return false
5. Handle disconnected components by checking all unvisited nodes

## Tags
`graph` `bipartite` `bfs` `two-coloring` `easy`
