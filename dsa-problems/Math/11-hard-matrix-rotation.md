# Robotic Arm End-Effector

**Difficulty:** Hard
**Topic:** Math, Geometry, Transformations
**License:** Free to use for commercial purposes

## Problem Statement

A robotic arm's end-effector is at position `(x, y)`. It rotates around the base `(0, 0)` by `degrees` counter-clockwise. Calculate the new position `(x', y')`.

Return coordinates rounded to 2 decimal places.

## Constraints

- `-1000 <= x, y <= 1000`
- `0 <= degrees <= 360`

## Examples

### Example 1
```
Input: x = 10, y = 0, degrees = 90
Output: [0.00, 10.00]
```

### Example 2
```
Input: x = 5, y = 5, degrees = 180
Output: [-5.00, -5.00]
```

### Example 3
```
Input: x = 10, y = 0, degrees = 45
Output: [7.07, 7.07]
Explanation: 10 * cos(45) = 7.07.
```

## Function Signature

### Python
```python
def rotate_effector(x: float, y: float, degrees: float) -> list[float]:
    pass
```

### JavaScript
```javascript
function rotateEffector(x, y, degrees) {
    // Your code here
}
```

### Java
```java
public double[] rotateEffector(double x, double y, double degrees) {
    // Your code here
}
```

## Hints
1. Convert degrees to radians
2. x' = x*cos(theta) - y*sin(theta)
3. y' = x*sin(theta) + y*cos(theta)

## Tags
`math` `geometry` `hard`
