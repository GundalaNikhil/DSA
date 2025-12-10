# Drone Search Pattern

**Difficulty:** Hard
**Topic:** Arrays, Matrix, Simulation
**License:** Free to use for commercial purposes

## Problem Statement

A search-and-rescue drone is deployed at the center of a grid-based search area to find a missing target. The drone follows a spiral search pattern (Right -> Down -> Left -> Up, expanding outward) to scan sectors. Each sector in the grid has a "probability score" indicating the likelihood of finding the target.

Given a 2D grid `probabilities` and an integer `k`, calculate the total probability score accumulated by the drone after scanning its first `k` sectors.

The drone starts at the center position. If the grid has even dimensions, use `[rows//2, cols//2]` as the starting point.

The spiral pattern: Start moving right (1 step), then down (1 step), then left (2 steps), then up (2 steps), then right (3 steps), and so on.

## Constraints

- `1 <= probabilities.length, probabilities[0].length <= 100`
- `-1000 <= probabilities[i][j] <= 1000`
- `1 <= k <= probabilities.length × probabilities[0].length`

## Examples

### Example 1
```
Input:
probabilities = [
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
probabilities = [
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
probabilities = [[100]]
k = 1

Output: 100
Explanation: Only one sector, drone collects 100.
```

## Function Signature

### Python
```python
def drone_search_score(probabilities: list[list[int]], k: int) -> int:
    pass
```

### JavaScript
```javascript
function droneSearchScore(probabilities, k) {
    // Your code here
}
```

### Java
```java
public int droneSearchScore(int[][] probabilities, int k) {
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

## Tags
`array` `matrix` `simulation` `spiral` `hard`
