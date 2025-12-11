# Flooded Campus Min Cost With Free Cells

## Problem Metadata
- **unique_problem_id**: `dp_009`
- **display_id**: `DP-009`
- **slug**: `flooded-campus-min-cost-free`
- **version**: `1.0.0`
- **difficulty**: `Medium`
- **topic_tags**: `["Dynamic Programming", "Grid", "Optimization", "Path Finding"]`

## Problem Title
Flooded Campus Min Cost With Free Cells

## Problem Description
You are given an `m × n` grid where each cell `grid[i][j]` has a traversal cost. You start at the top-left corner (0, 0) and want to reach the bottom-right corner (m-1, n-1). You can only move right or down.

You have a special ability: you can choose up to `f` cells to traverse for free (cost becomes 0 for those cells). Find the minimum total cost to reach the destination.

## Examples

### Example 1
**Input:**
```
grid = [[5, 3],
        [4, 1]]
f = 1
```

**Output:**
```
4
```

**Explanation:**
- Path without using free: 5 → 3 → 1 = 9
- Path using free on cell (0,1): 5 → 0 → 1 = 6
- Path using free on cell (1,0): 5 → 4 → 1 = 10 (worse)
- Best path: Start 5, go down to 4, then right to 1: 5 → 4 → 1 = 10... wait that's not 4.

Let me recalculate:
- We start at (0,0) with cost 5
- Option 1: Right to (0,1) cost 3, then down to (1,1) cost 1 → total: 5+3+1=9
- With 1 free cell on (0,1): 5+0+1 = 6
- With 1 free cell on (0,0): 0+3+1 = 4 ✓

**Corrected Explanation:** Make cell (0,0) free: 0 + 3 + 1 = 4.

### Example 2
**Input:**
```
grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]
f = 2
```

**Output:**
```
3
```

**Explanation:**
- Optimal path: (0,0) → (0,1) → (0,2) → (1,2) → (2,2)
- Costs: 1 + 3 + 1 + 1 + 1 = 7
- Make (0,1) and (1,2) free: 1 + 0 + 1 + 0 + 1 = 3

## Constraints
- `1 <= m, n <= 200`
- `0 <= cost[i][j] <= 10^4`
- `0 <= f <= 10`
- You must include the starting and ending cell costs in your calculation

## Function Signatures

### Java
```java
class Solution {
    public int minCostWithFreeCells(int[][] grid, int f) {
        // Your code here
    }
}
```

### Python
```python
class Solution:
    def minCostWithFreeCells(self, grid: List[List[int]], f: int) -> int:
        # Your code here
        pass
```

### C++
```cpp
class Solution {
public:
    int minCostWithFreeCells(vector<vector<int>>& grid, int f) {
        // Your code here
    }
};
```

## Input Format
```
Line 1: Three space-separated integers: m (rows), n (columns), f (free cells)
Next m lines: n space-separated integers representing grid costs
```

### Sample Input
```
2 2 1
5 3
4 1
```

## Hints
- Use 3D DP: dp[i][j][k] = minimum cost to reach (i,j) having used k free cells
- State transition: From (i,j) go to (i+1,j) or (i,j+1)
  - Without using free: dp[i+1][j][k] = dp[i][j][k] + grid[i+1][j]
  - Using free: dp[i+1][j][k+1] = dp[i][j][k] + 0
- Base case: dp[0][0][0] = grid[0][0] or dp[0][0][1] = 0 if we use free on start
- Answer: min(dp[m-1][n-1][k]) for k = 0 to f
- Time complexity: O(m × n × f)

## Related Topics Quiz

### Question 1
What is the time complexity of the DP solution?
- A) O(m × n)
- B) O(m × n × f)
- C) O(m × n × f²)
- D) O(m + n + f)

**Answer:** B) O(m × n × f) - Three dimensions: position (m×n) and free cells used (f).

### Question 2
Why do we need a third dimension (k) in our DP state?
- A) To count the number of paths
- B) To track how many free cells we've used
- C) To store the minimum cost
- D) To avoid cycles

**Answer:** B) To track how many free cells we've used - We need to ensure we don't exceed f free cells.

### Question 3
Is it always optimal to use all f free cells?
- A) Yes, more free cells always reduce cost
- B) No, if some cells have cost 0, using free on them is wasteful
- C) Yes, but only in larger grids
- D) It doesn't matter

**Answer:** B) No, if some cells have cost 0, using free on them is wasteful - We should save free cells for high-cost cells.

### Question 4
What should dp[0][0][0] represent?
- A) Cost of starting cell
- B) 0 (no cost at start)
- C) Minimum cost to reach start
- D) Number of paths

**Answer:** A) Cost of starting cell - We must pay the cost of the starting cell unless we use a free cell on it.

### Question 5
Can we optimize space complexity?
- A) No, we need all three dimensions
- B) Yes, to O(n × f) by processing row by row
- C) Yes, to O(1) always
- D) Only if f = 0

**Answer:** B) Yes, to O(n × f) by processing row by row - We only need current and previous row, not all m rows.
