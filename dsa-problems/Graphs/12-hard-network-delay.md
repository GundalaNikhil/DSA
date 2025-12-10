# Viral Meme Spread Time

**Difficulty:** Hard
**Topic:** Graphs, Dijkstra, BFS
**License:** Free to use for commercial purposes

## Problem Statement

A new meme is posted by a user (source node) on a social network. The meme spreads to connected users. Each connection has a specific "propagation delay" (time it takes for the user to see and repost).

Given `n` users, a list of `connections` where `[u, v, time]` means user `u` shares with user `v` in `time` units, and the `source_user` ID, find the minimum time required for *all* users in the network to receive the meme.

If it's impossible for everyone to see it (some users are disconnected), return -1.

## Constraints

- `1 <= n <= 1000`
- `1 <= connections.length <= 5000`
- Users are labeled from 1 to n
- `1 <= time <= 100`

## Examples

### Example 1
```
Input: n = 4, connections = [[1, 2, 5], [1, 3, 2], [2, 4, 2], [3, 4, 4]], source_user = 1

Spread:
- Time 0: User 1 posts.
- Time 2: User 3 sees it.
- Time 5: User 2 sees it.
- Time 6: User 4 sees it (via 3->4 takes 2+4=6? No, via 2->4 takes 5+2=7. So 6 is faster).
Wait, let's recheck:
1->3 (2s) -> 4 (4s) = Total 6s.
1->2 (5s) -> 4 (2s) = Total 7s.
So User 4 sees it at time 6.

Max time is 6.

Output: 6
```

### Example 2
```
Input: n = 3, connections = [[1, 2, 10]], source_user = 1
Output: -1
Explanation: User 3 never sees the meme.
```

### Example 3
```
Input: n = 2, connections = [[1, 2, 1], [2, 1, 1]], source_user = 2
Output: 1
Explanation: 2 shares with 1 in 1s.
```

## Function Signature

### Python
```python
def meme_spread_time(n: int, connections: list[list[int]], source_user: int) -> int:
    pass
```

### JavaScript
```javascript
function memeSpreadTime(n, connections, sourceUser) {
    // Your code here
}
```

### Java
```java
public int memeSpreadTime(int n, int[][] connections, int sourceUser) {
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
