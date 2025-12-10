# Maze Solver

**Difficulty:** Easy
**Topic:** Graphs, BFS, DFS
**License:** Free to use for commercial purposes

## Problem Statement

A robot is navigating a maze represented as a graph. Rooms are nodes and corridors are edges. The robot starts at a specific room and needs to reach an exit room.

Given `n` rooms (labeled 0 to n-1), a list of `corridors` connecting them, a `start_room`, and an `exit_room`, determine if a path exists from start to exit.

Return `true` if the exit is reachable, `false` otherwise.

## Constraints

- `1 <= number of rooms <= 1000`
- `0 <= corridors.length <= 5000`
- `0 <= start_room, exit_room < n`

## Examples

### Example 1
```
Input: n = 6, corridors = [[0, 3], [3, 1], [1, 4], [4, 5], [5, 2]], start_room = 0, exit_room = 2
Output: true
Explanation: Path: 0 -> 3 -> 1 -> 4 -> 5 -> 2
```

### Example 2
```
Input: n = 5, corridors = [[0, 1], [1, 2], [3, 4]], start_room = 0, exit_room = 4
Output: false
Explanation: Rooms 0,1,2 are connected. Rooms 3,4 are connected. No path from 0 to 4.
```

### Example 3
```
Input: n = 4, corridors = [[0, 1], [1, 2], [2, 3], [3, 0]], start_room = 0, exit_room = 3
Output: true
Explanation: Rooms form a cycle. Can go 0 -> 3 directly (if bidirectional) or 0->1->2->3.
```

## Function Signature

### Python
```python
def can_escape_maze(n: int, corridors: list[list[int]], start_room: int, exit_room: int) -> bool:
    pass
```

### JavaScript
```javascript
function canEscapeMaze(n, corridors, startRoom, exitRoom) {
    // Your code here
}
```

### Java
```java
public boolean canEscapeMaze(int n, int[][] corridors, int startRoom, int exitRoom) {
    // Your code here
}
```

## Hints

1. Build an adjacency list from corridors
2. Use BFS or DFS starting from the start_room
3. Keep track of visited rooms to avoid infinite loops
4. If you reach the exit_room during traversal, return true
5. If traversal completes without finding exit, return false

## Tags
`graph` `bfs` `dfs` `path-finding` `easy`
