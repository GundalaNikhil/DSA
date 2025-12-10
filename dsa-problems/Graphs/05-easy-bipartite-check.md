# Team Rivalry Separation

**Difficulty:** Easy
**Topic:** Graphs, Bipartite, BFS
**License:** Free to use for commercial purposes

## Problem Statement

A tournament organizer needs to split players into two rival teams (Team Red and Team Blue). However, certain pairs of players have a rivalry history and cannot be on the same team.

Given `n` players and a list of `rivalries` (pairs of players who cannot be teammates), determine if it is possible to split all players into two teams such that no two rivals are on the same team.

Return `true` if a valid split is possible, `false` otherwise.

## Constraints

- `1 <= number of players <= 1000`
- `0 <= rivalries.length <= 5000`
- Players are numbered from 0 to n-1

## Examples

### Example 1
```
Input: n = 5, rivalries = [[0, 3], [3, 1], [1, 4], [4, 2]]
Output: true
Explanation:
- Team Red: 0, 1, 2
- Team Blue: 3, 4
Check:
0-3 (Red-Blue) OK
3-1 (Blue-Red) OK
1-4 (Red-Blue) OK
4-2 (Blue-Red) OK
```

### Example 2
```
Input: n = 3, rivalries = [[0, 1], [1, 2], [2, 0]]
Output: false
Explanation: Cycle of length 3 (triangle). Impossible to split into 2 teams.
```

### Example 3
```
Input: n = 6, rivalries = [[0, 5], [1, 4], [2, 3]]
Output: true
Explanation: 3 disjoint pairs. Can easily split.
```

## Function Signature

### Python
```python
def can_split_teams(n: int, rivalries: list[list[int]]) -> bool:
    pass
```

### JavaScript
```javascript
function canSplitTeams(n, rivalries) {
    // Your code here
}
```

### Java
```java
public boolean canSplitTeams(int n, int[][] rivalries) {
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
