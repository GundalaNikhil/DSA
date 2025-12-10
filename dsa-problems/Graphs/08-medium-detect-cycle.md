# Deadlock Detection System

**Difficulty:** Medium
**Topic:** Graphs, DFS, Cycle Detection
**License:** Free to use for commercial purposes

## Problem Statement

An operating system resource manager tracks processes waiting for resources held by other processes. This dependency is represented as `[Process A, Process B]`, meaning Process A is waiting for Process B.

A "deadlock" occurs if there is a circular chain of dependencies (e.g., A waits for B, B waits for A).

Given `n` processes and a list of `waits_for` dependencies, determine if a deadlock exists in the system.

Return `true` if a deadlock (cycle) is detected, `false` otherwise.

## Constraints

- `1 <= number of processes <= 1000`
- `0 <= dependencies.length <= 5000`
- Processes are numbered from 0 to n-1

## Examples

### Example 1
```
Input: n = 5, waits_for = [[0, 2], [2, 4], [4, 1], [1, 3]]
Output: false
Explanation: 0->2->4->1->3. No cycle.
```

### Example 2
```
Input: n = 4, waits_for = [[0, 1], [1, 2], [2, 3], [3, 1]]
Output: true
Explanation: Cycle: 1->2->3->1.
```

### Example 3
```
Input: n = 3, waits_for = [[0, 1], [1, 2], [0, 2]]
Output: false
Explanation: 0 waits for 1 and 2. 1 waits for 2. No circular waiting.
```

## Function Signature

### Python
```python
def detect_deadlock(n: int, waits_for: list[list[int]]) -> bool:
    pass
```

### JavaScript
```javascript
function detectDeadlock(n, waitsFor) {
    // Your code here
}
```

### Java
```java
public boolean detectDeadlock(int n, int[][] waitsFor) {
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
