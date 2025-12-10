# Matrix Coordinate Rotation

**Difficulty:** Hard
**Topic:** Math, Geometry, Transformations
**License:** Free to use for commercial purposes

## Problem Statement

Given a point `(x, y)` on a 2D coordinate plane and an angle `theta` in degrees, rotate the point around the origin `(0, 0)` counterclockwise by the given angle. Return the new coordinates rounded to 2 decimal places.

Rotation formulas:
- x' = x × cos(θ) - y × sin(θ)
- y' = x × sin(θ) + y × cos(θ)

## Constraints

- `-1000 <= x, y <= 1000`
- `0 <= theta <= 360`
- Return coordinates as `[newX, newY]` rounded to 2 decimal places

## Examples

### Example 1
```
Input: x = 1, y = 0, theta = 90
Output: [0.00, 1.00]
Explanation: Point (1, 0) rotated 90° counterclockwise becomes (0, 1).
```

### Example 2
```
Input: x = 3, y = 4, theta = 180
Output: [-3.00, -4.00]
Explanation: 180° rotation flips the point to opposite quadrant.
```

### Example 3
```
Input: x = 5, y = 0, theta = 45
Output: [3.54, 3.54]
Explanation:
  x' = 5 × cos(45°) - 0 × sin(45°) = 5 × 0.707 = 3.535 ≈ 3.54
  y' = 5 × sin(45°) + 0 × cos(45°) = 5 × 0.707 = 3.535 ≈ 3.54
```

### Example 4
```
Input: x = 10, y = 10, theta = 270
Output: [10.00, -10.00]
Explanation: 270° counterclockwise (or 90° clockwise).
```

### Example 5
```
Input: x = 0, y = 5, theta = 0
Output: [0.00, 5.00]
Explanation: 0° rotation means no change.
```

## Function Signature

### Python
```python
def rotate_point(x: float, y: float, theta: float) -> list[float]:
    pass
```

### JavaScript
```javascript
function rotatePoint(x, y, theta) {
    // Your code here
}
```

### Java
```java
public double[] rotatePoint(double x, double y, double theta) {
    // Your code here
}
```

## Hints

1. Convert theta from degrees to radians: radians = theta × π / 180
2. Use trigonometric functions: cos() and sin()
3. Apply rotation formulas
4. Round results to 2 decimal places
5. Handle edge cases like theta = 0, 90, 180, 270, 360
6. Time complexity: O(1), Space complexity: O(1)

## Tags
`math` `geometry` `rotation` `trigonometry` `transformation` `hard`
