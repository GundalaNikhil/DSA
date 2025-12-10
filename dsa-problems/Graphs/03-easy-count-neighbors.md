# Influencer Reach

**Difficulty:** Easy
**Topic:** Graphs, Graph Representation
**License:** Free to use for commercial purposes

## Problem Statement

In an influencer marketing platform, users follow each other. We want to measure the "direct reach" of a specific influencer.

Given a network of `n` users and a list of `follows` (where `[A, B]` means A and B follow each other - bidirectional for simplicity in this model), count how many direct followers a specific `target_user` has.

## Constraints

- `1 <= number of users <= 1000`
- `0 <= follows.length <= 5000`
- `0 <= target_user < n`

## Examples

### Example 1
```
Input: n = 7, follows = [[0, 2], [0, 5], [1, 3], [2, 4], [5, 6], [0, 6]], target_user = 0
Output: 3
Explanation: User 0 is connected to 2, 5, and 6.
```

### Example 2
```
Input: n = 4, follows = [[1, 2], [2, 3], [3, 1]], target_user = 0
Output: 0
Explanation: User 0 has no connections.
```

### Example 3
```
Input: n = 5, follows = [[0, 1], [0, 2], [0, 3], [0, 4]], target_user = 0
Output: 4
Explanation: User 0 is the hub, connected to everyone.
```

## Function Signature

### Python
```python
def count_direct_followers(n: int, follows: list[list[int]], target_user: int) -> int:
    pass
```

### JavaScript
```javascript
function countDirectFollowers(n, follows, targetUser) {
    // Your code here
}
```

### Java
```java
public int countDirectFollowers(int n, int[][] follows, int targetUser) {
    // Your code here
}
```

## Hints

1. Build an adjacency list or use a simple counter
2. For each connection [a, b], both a and b are neighbors
3. If connection contains target, increment count
4. Time complexity: O(e), Space complexity: O(n)

## Tags
`graph` `adjacency-list` `counting` `easy`
