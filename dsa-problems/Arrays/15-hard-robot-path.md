# Robot Warehouse Navigator

**Difficulty:** Hard
**Topic:** Arrays, Dynamic Programming, Backtracking
**License:** Free to use for commercial purposes

## Problem Statement

A warehouse robot navigates through a 2D grid to collect packages. The grid contains:
- Positive integers: package values (collect when visited)
- Negative integers: obstacles (energy cost to pass through)
- Zero: empty space (free to pass)

The robot starts at the top-left corner `(0, 0)` and must reach the bottom-right corner `(m-1, n-1)`. The robot can only move right or down. Find the maximum total value the robot can collect minus the energy costs paid.

If multiple paths have the same value, return the maximum value achievable.

## Constraints

- `1 <= grid.length, grid[0].length <= 100`
- `-1000 <= grid[i][j] <= 1000`
- Robot always starts at `(0, 0)` and ends at `(m-1, n-1)`

## Examples

### Example 1
```
Input: grid = [
  [5,   3,  2],
  [1,  -2,  3],
  [2,   1,  4]
]
Output: 14
Explanation:
  Optimal path: (0,0)→(0,1)→(0,2)→(1,2)→(2,2)
  Values: 5 + 3 + 2 + 3 + 4 = 17
  Costs: 0 (no negative values on this path)
  Total: 17

  Alternative path: (0,0)→(1,0)→(2,0)→(2,1)→(2,2)
  Values: 5 + 1 + 2 + 1 + 4 = 13
  Total: 13

  Another path through obstacle: (0,0)→(1,0)→(1,1)→(1,2)→(2,2)
  Values: 5 + 1 + (-2) + 3 + 4 = 11
  Total: 11

  Maximum: 17

  Wait, let me recalculate the first path:
  Path: (0,0)→(0,1)→(0,2)→(1,2)→(2,2)
  Values collected: grid[0][0] + grid[0][1] + grid[0][2] + grid[1][2] + grid[2][2]
  = 5 + 3 + 2 + 3 + 4 = 17 ✓

  But expected output is 14, not 17. Let me check if I misunderstood the problem.

  Oh, maybe the starting position value is not collected? Let me re-read...
  "collect when visited" suggests we do collect the starting position.

  Or maybe the ending position isn't collected? Let me try:
  5 + 3 + 2 + 3 = 13 (without ending position)

  Still not 14. Let me try different interpretation.

  Maybe the robot starts with the value at (0,0) already counted?
  Or maybe there's a different optimal path?

  Let me recalculate assuming we DON'T count the starting position:
  Path: (0,0)→(0,1)→(0,2)→(1,2)→(2,2)
  Values: 3 + 2 + 3 + 4 = 12 (skipping 5)

  That's 12, not 14.

  Let me try: DO count start, DON'T count end:
  5 + 3 + 2 + 3 = 13

  Still not 14.

  Let me try a completely different path:
  (0,0)→(1,0)→(1,1)→(2,1)→(2,2)
  Values: 5 + 1 + (-2) + 1 + 4 = 9

  Or: (0,0)→(0,1)→(1,1)→(2,1)→(2,2)
  Values: 5 + 3 + (-2) + 1 + 4 = 11

  Or: (0,0)→(0,1)→(1,1)→(1,2)→(2,2)
  Values: 5 + 3 + (-2) + 3 + 4 = 13

  Or: (0,0)→(1,0)→(2,0)→(2,1)→(2,2)
  Values: 5 + 1 + 2 + 1 + 4 = 13

  I can't get 14 with any path. Let me change the expected output to 17.
```

### Example 1 (corrected)
```
Input: grid = [
  [5,   3,  2],
  [1,  -2,  3],
  [2,   1,  4]
]
Output: 17
Explanation:
  Optimal path: (0,0)→(0,1)→(0,2)→(1,2)→(2,2)
  Values: 5 + 3 + 2 + 3 + 4 = 17
```

### Example 2
```
Input: grid = [
  [10, -5],
  [-3,  8]
]
Output: 10
Explanation:
  Path 1: (0,0)→(0,1)→(1,1) = 10 + (-5) + 8 = 13
  Path 2: (0,0)→(1,0)→(1,1) = 10 + (-3) + 8 = 15

  Maximum: 15

  Wait, expected is 10 but I calculated 15. Let me reconsider.

  Oh! Maybe we don't collect the destination value? Let me try:
  Path 2: 10 + (-3) = 7 (without destination)

  That's 7, not 10.

  Maybe only the start is collected?
  That would be 10 for path 1 or path 2.

  That makes sense! The robot starts at (0,0) and that's the only value collected by default,
  and we track the total value collected along the path.

  Actually, this doesn't make sense for a "collection" problem. Let me reconsider entirely.

  Standard interpretation: collect all values on the path including start and end.
  Path 1: 10 + (-5) + 8 = 13
  Path 2: 10 + (-3) + 8 = 15
  Max = 15

  I'll change the expected output to 15.
```

### Example 2 (corrected)
```
Input: grid = [
  [10, -5],
  [-3,  8]
]
Output: 15
Explanation:
  Path 1: (0,0)→(0,1)→(1,1) = 10 + (-5) + 8 = 13
  Path 2: (0,0)→(1,0)→(1,1) = 10 + (-3) + 8 = 15

  Maximum: 15
```

### Example 3
```
Input: grid = [[5]]
Output: 5
Explanation: Only one cell, collect its value.
```

### Example 4
```
Input: grid = [
  [1, 2, 3],
  [4, 5, 6]
]
Output: 21
Explanation:
  Optimal path: (0,0)→(0,1)→(0,2)→(1,2)
  Values: 1 + 2 + 3 + 6 = 12

  Or: (0,0)→(1,0)→(1,1)→(1,2)
  Values: 1 + 4 + 5 + 6 = 16

  Maximum: 16

  But expected is 21. Let me recalculate...

  What if we can go: (0,0)→(0,1)→(1,1)→(1,2)?
  Values: 1 + 2 + 5 + 6 = 14

  Or: (0,0)→(1,0)→(1,1)→(0,1)? No, can't go up.

  I can't reach 21 with any valid path. Let me change to 16.
```

### Example 4 (corrected)
```
Input: grid = [
  [1, 2, 3],
  [4, 5, 6]
]
Output: 16
Explanation:
  Optimal path: (0,0)→(1,0)→(1,1)→(1,2)
  Values: 1 + 4 + 5 + 6 = 16
```

## Function Signature

### Python
```python
def max_collection_value(grid: list[list[int]]) -> int:
    pass
```

### JavaScript
```javascript
function maxCollectionValue(grid) {
    // Your code here
}
```

### Java
```java
public int maxCollectionValue(int[][] grid) {
    // Your code here
}
```

## Hints

1. Use dynamic programming: dp[i][j] = maximum value to reach cell (i, j)
2. For each cell, it can be reached from top (i-1, j) or left (i, j-1)
3. dp[i][j] = grid[i][j] + max(dp[i-1][j], dp[i][j-1])
4. Handle the first row and first column as base cases
5. The answer is dp[m-1][n-1]
6. Time complexity: O(m × n), Space complexity: O(m × n) or O(n) with optimization

## Tags
`array` `dynamic-programming` `matrix` `path-finding` `hard`
