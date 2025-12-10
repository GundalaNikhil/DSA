# Floor Tile Pattern Counter

**Difficulty:** Medium
**Topic:** Math, Pattern Recognition, Sequences
**License:** Free to use for commercial purposes

## Problem Statement

A floor designer creates tile patterns where each row has an increasing number of tiles based on a specific pattern:
- Row 1: 3 tiles
- Row 2: 7 tiles
- Row 3: 11 tiles
- Row 4: 15 tiles
- Pattern: Each row has 4 more tiles than the previous row

Given `n` rows, calculate the total number of tiles needed for the entire pattern.

## Constraints

- `1 <= n <= 100000`

## Examples

### Example 1
```
Input: n = 1
Output: 3
Explanation: Only row 1 with 3 tiles.
```

### Example 2
```
Input: n = 3
Output: 21
Explanation: Row 1: 3, Row 2: 7, Row 3: 11. Total = 3 + 7 + 11 = 21 tiles.
```

### Example 3
```
Input: n = 5
Output: 55
Explanation: 3 + 7 + 11 + 15 + 19 = 55 tiles.
```

### Example 4
```
Input: n = 10
Output: 210
Explanation: Sum of arithmetic sequence: 3, 7, 11, 15, 19, 23, 27, 31, 35, 39 = 210.
```

## Function Signature

### Python
```python
def count_floor_tiles(n: int) -> int:
    pass
```

### JavaScript
```javascript
function countFloorTiles(n) {
    // Your code here
}
```

### Java
```java
public int countFloorTiles(int n) {
    // Your code here
}
```

## Hints

1. This is an arithmetic sequence with first term a₁ = 3 and common difference d = 4
2. The nth term formula: aₙ = a₁ + (n-1) × d = 3 + (n-1) × 4
3. Sum of arithmetic sequence: S = n × (a₁ + aₙ) / 2
4. Or use: S = n × (2a₁ + (n-1)d) / 2
5. Avoid loops for large n - use the formula directly
6. Time complexity: O(1), Space complexity: O(1)

## Tags
`math` `arithmetic-sequence` `patterns` `series-sum` `medium`
