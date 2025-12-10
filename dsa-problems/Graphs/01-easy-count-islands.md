# Social Network Circles

**Difficulty:** Easy
**Topic:** Graphs, DFS, Connected Components
**License:** Free to use for commercial purposes

## Problem Statement

A social media platform analyzes user connections to identify distinct communities. A "circle" is defined as a group of users who are connected directly or indirectly through friends.

Given a number of users `n` and a list of `connections` where each connection is a pair `[user_a, user_b]`, count the number of distinct social circles.

## Constraints

- `1 <= number of users <= 1000`
- `0 <= connections.length <= 5000`
- Users are numbered from 0 to n-1
- No duplicate connections

## Examples

### Example 1
```
Input: n = 7, connections = [[0, 5], [5, 2], [2, 0], [1, 3], [4, 6]]
Users: 0, 1, 2, 3, 4, 5, 6

Circles:
- Circle 1: 0-5-2 (Triangle connection)
- Circle 2: 1-3 (Pair)
- Circle 3: 4-6 (Pair)

Output: 3
```

### Example 2
```
Input: n = 5, connections = [[0, 4], [4, 1], [1, 3], [3, 2]]
Circles:
- Circle 1: 0-4-1-3-2 (All connected in a line)

Output: 1
```

### Example 3
```
Input: n = 4, connections = [[0, 1], [2, 3]]
Circles:
- Circle 1: 0-1
- Circle 2: 2-3

Output: 2
```

## Function Signature

### Python
```python
def count_social_circles(n: int, connections: list[list[int]]) -> int:
    pass
```

### JavaScript
```javascript
function countSocialCircles(n, connections) {
    // Your code here
}
```

### Java
```java
public int countSocialCircles(int n, int[][] connections) {
    // Your code here
}
```

## Hints

1. Build an adjacency list from the connections array
2. Use DFS or BFS to explore each connected component
3. Keep track of visited users to avoid counting them twice
4. Each time you start a new DFS/BFS, increment the circle counter
5. Time complexity: O(n + e), Space complexity: O(n + e)

## Tags
`graph` `dfs` `connected-components` `union-find` `easy`
