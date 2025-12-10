# Spiral Matrix Path Sum

**Difficulty:** Hard
**Topic:** Arrays, Matrix, Simulation
**License:** Free to use for commercial purposes

## Problem Statement

A robot starts at the center of a 2D grid and moves in a spiral pattern (right → down → left → up, expanding outward). The grid contains integers, and the robot collects values as it moves. Given a matrix and the number of steps `k`, calculate the sum of all values the robot collects in its first `k` steps.

The robot starts at the center position (if the matrix has odd dimensions) or the center-most position (for even dimensions, use `[rows//2, cols//2]` as starting point).

The spiral pattern: Start moving right (1 step), then down (1 step), then left (2 steps), then up (2 steps), then right (3 steps), and so on, increasing the step count for every two direction changes.

## Constraints

- `1 <= matrix.length, matrix[0].length <= 100`
- `-1000 <= matrix[i][j] <= 1000`
- `1 <= k <= matrix.length × matrix[0].length`

## Examples

### Example 1
```
Input:
matrix = [
  [1,  2,  3],
  [4,  5,  6],
  [7,  8,  9]
]
k = 5

Output: 35
Explanation:
  Start at center [1,1] (value = 5)
  Spiral path: [1,1]→[1,2]→[2,2]→[2,1]→[2,0]
  Values collected: 5, 6, 9, 8, 7
  Sum: 5 + 6 + 9 + 8 + 7 = 35
```

### Example 2
```
Input:
matrix = [
  [5, 10, 15],
  [20, 25, 30],
  [35, 40, 45]
]
k = 7

Output: 200
Explanation:
  Start at center [1,1] (value = 25)
  Spiral: [1,1]→[1,2]→[2,2]→[2,1]→[2,0]→[1,0]→[0,0]
  Values: 25, 30, 45, 40, 35, 20, 5
  Sum: 25 + 30 + 45 + 40 + 35 + 20 + 5 = 200
```

### Example 3
```
Input:
matrix = [[100]]
k = 1

Output: 100
Explanation: Only one cell, robot collects 100.
```

## Function Signature

### Python
```python
def spiral_path_sum(matrix: list[list[int]], k: int) -> int:
    pass
```

### JavaScript
```javascript
function spiralPathSum(matrix, k) {
    // Your code here
}
```

### Java
```java
public int spiralPathSum(int[][] matrix, int k) {
    // Your code here
}
```

## Hints

1. Find the starting position (center of matrix)
2. Implement spiral movement: right, down, left, up with increasing step sizes
3. Track visited cells to avoid revisiting
4. Handle boundary conditions carefully
5. Stop when k cells have been visited
6. Use direction vectors: [(0,1), (1,0), (0,-1), (-1,0)]
7. Pattern: move 1 step right, 1 down, 2 left, 2 up, 3 right, 3 down, ...

## Tags
`array` `matrix` `simulation` `spiral` `hard`
