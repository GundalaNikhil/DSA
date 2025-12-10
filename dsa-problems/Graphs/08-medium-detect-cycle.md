# Find Circular Dependency

**Difficulty:** Medium
**Topic:** Graphs, DFS, Cycle Detection
**License:** Free to use for commercial purposes

## Problem Statement

You have a list of tasks where some tasks depend on others. A dependency is represented as [A, B] meaning task A must be completed before task B. Check if there is a circular dependency.

Return true if a circular dependency exists, false otherwise. A circular dependency means task A depends on B, B depends on C, and C depends on A (directly or indirectly).

## Constraints

- `1 <= number of tasks <= 1000`
- `0 <= dependencies.length <= 5000`
- Tasks are numbered from 0 to n-1

## Examples

### Example 1
```
Input: n = 4, dependencies = [[0,1], [1,2], [2,3]]

0 → 1 → 2 → 3

Output: false
Explanation: Linear dependency chain, no cycle
```

### Example 2
```
Input: n = 3, dependencies = [[0,1], [1,2], [2,0]]

0 → 1 → 2 → 0 (cycle!)

Output: true
Explanation: Task 0 depends on 1, 1 depends on 2, 2 depends on 0 = circular
```

### Example 3
```
Input: n = 5, dependencies = [[0,1], [0,2], [1,3], [2,3], [3,4]]

    0
   / \
  1   2
   \ /
    3
    |
    4

Output: false
Explanation: DAG (Directed Acyclic Graph), no cycles
```

### Example 4
```
Input: n = 4, dependencies = [[0,1], [1,2], [2,1]]

0 → 1 ⇄ 2 (cycle between 1 and 2)

Output: true
```

## Function Signature

### Python
```python
def has_circular_dependency(n: int, dependencies: list[list[int]]) -> bool:
    pass
```

### JavaScript
```javascript
function hasCircularDependency(n, dependencies) {
    // Your code here
}
```

### Java
```java
public boolean hasCircularDependency(int n, int[][] dependencies) {
    // Your code here
}
```

## Hints

1. Build a directed graph from dependencies
2. Use DFS with three states: unvisited, visiting, visited
3. If you encounter a node in "visiting" state, there's a cycle
4. Mark node as "visiting" when entering, "visited" when leaving
5. Alternative: Use topological sort (Kahn's algorithm)

## Tags
`graph` `dfs` `cycle-detection` `directed-graph` `medium`
