# Dungeon Crawler Loot

**Difficulty:** Hard
**Topic:** Arrays, Dynamic Programming, Backtracking
**License:** Free to use for commercial purposes

## Problem Statement

A hero navigates through a dungeon grid to collect loot. The grid contains:

- Positive integers: gold coins (collect when visited)
- Negative integers: traps (health cost to pass through)
- Zero: empty corridor (safe to pass)

The hero starts at the top-left corner `(0, 0)` and must reach the bottom-right corner `(m-1, n-1)`. The hero can only move right or down. Find the maximum total value (gold minus trap damage) the hero can achieve.

If multiple paths have the same value, return the maximum value achievable.

## Constraints

- `1 <= dungeon.length, dungeon[0].length <= 100`
- `-1000 <= dungeon[i][j] <= 1000`
- Hero always starts at `(0, 0)` and ends at `(m-1, n-1)`

## Examples

### Example 1

```
Input: dungeon = [
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
Input: dungeon = [
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
Input: dungeon = [[5]]
Output: 5
Explanation: Only one cell, collect its value.
```

### Example 4

```
Input: dungeon = [
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
def max_loot_value(dungeon: list[list[int]]) -> int:
    pass
```

### JavaScript

```javascript
function maxLootValue(dungeon) {
  // Your code here
}
```

### Java

```java
public int maxLootValue(int[][] dungeon) {
    // Your code here
}
```

## Hints

1. Use dynamic programming: dp[i][j] = maximum value to reach cell (i, j)
2. For each cell, it can be reached from top (i-1, j) or left (i, j-1)
3. dp[i][j] = dungeon[i][j] + max(dp[i-1][j], dp[i][j-1])
4. Handle the first row and first column as base cases
5. The answer is dp[m-1][n-1]
6. Time complexity: O(m × n), Space complexity: O(m × n) or O(n) with optimization

## Tags

`array` `dynamic-programming` `matrix` `path-finding` `hard`
