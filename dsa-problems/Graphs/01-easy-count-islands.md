# Count Connected Groups

**Difficulty:** Easy
**Topic:** Graphs, DFS, Connected Components
**License:** Free to use for commercial purposes

## Problem Statement

You have a list of friendships where each pair represents two people who are friends. Friends of friends are also considered connected. Count how many separate friend groups exist.

For example, if A is friends with B, and B is friends with C, then A, B, and C form one group even though A and C are not direct friends.

## Constraints

- `1 <= number of people <= 1000`
- `0 <= friendships.length <= 5000`
- Each person is represented by a number from 0 to n-1
- No duplicate friendships in the input

## Examples

### Example 1
```
Input: n = 6, friendships = [[0,1], [1,2], [3,4]]
People: 0, 1, 2, 3, 4, 5

Groups:
- Group 1: 0-1-2 (all connected)
- Group 2: 3-4
- Group 3: 5 (alone)

Output: 3
```

### Example 2
```
Input: n = 5, friendships = [[0,1], [2,3], [3,4]]

Groups:
- Group 1: 0-1
- Group 2: 2-3-4

Output: 2
```

### Example 3
```
Input: n = 4, friendships = []

Groups:
- 0 alone
- 1 alone
- 2 alone
- 3 alone

Output: 4
Explanation: No friendships means everyone is in their own group
```

### Example 4
```
Input: n = 3, friendships = [[0,1], [1,2], [2,0]]

Groups:
- Group 1: 0-1-2 (all connected in a cycle)

Output: 1
```

## Function Signature

### Python
```python
def count_groups(n: int, friendships: list[list[int]]) -> int:
    pass
```

### JavaScript
```javascript
function countGroups(n, friendships) {
    // Your code here
}
```

### Java
```java
public int countGroups(int n, int[][] friendships) {
    // Your code here
}
```

## Hints

1. Build an adjacency list from the friendships array
2. Use DFS or BFS to explore each connected component
3. Keep track of visited people to avoid counting them twice
4. Each time you start a new DFS/BFS, increment the group counter
5. Time complexity: O(n + e), Space complexity: O(n + e)

## Tags
`graph` `dfs` `connected-components` `union-find` `easy`
