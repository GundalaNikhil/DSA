# Circle Intersection Area

**Difficulty:** Hard
**Topic:** Math, Geometry, Circles
**License:** Free to use for commercial purposes

## Problem Statement

Two circles are defined on a 2D plane. Circle 1 has center `(x1, y1)` and radius `r1`. Circle 2 has center `(x2, y2)` and radius `r2`.

Calculate the area of intersection between the two circles. If the circles don't intersect, return 0.

## Constraints

- `-1000 <= x1, x2, y1, y2 <= 1000`
- `1 <= r1, r2 <= 1000`
- Return area rounded to 2 decimal places

## Examples

### Example 1
```
Input: x1=0, y1=0, r1=2, x2=3, y2=0, r2=2
Output: 3.48
Explanation:
  Distance between centers = 3
  Circles overlap partially
  Intersection area ≈ 3.48
```

### Example 2
```
Input: x1=0, y1=0, r1=1, x2=0, y2=0, r2=1
Output: 3.14
Explanation:
  Both circles are identical (same center and radius)
  Intersection area = π × r² ≈ 3.14
```

### Example 3
```
Input: x1=0, y1=0, r1=1, x2=5, y2=0, r2=1
Output: 0.00
Explanation:
  Distance between centers = 5
  Sum of radii = 2
  Circles don't intersect (too far apart)
```

### Example 4
```
Input: x1=0, y1=0, r1=5, x2=0, y2=0, r2=2
Output: 12.57
Explanation:
  Circle 2 is completely inside Circle 1
  Intersection area = area of smaller circle = π × 2² ≈ 12.57
```

### Example 5
```
Input: x1=0, y1=0, r1=3, x2=4, y2=0, r2=3
Output: 7.25
Explanation:
  Distance = 4, both radii = 3
  Partial overlap with intersection area ≈ 7.25
```

## Function Signature

### Python
```python
def circle_intersection_area(x1: float, y1: float, r1: float,
                             x2: float, y2: float, r2: float) -> float:
    pass
```

### JavaScript
```javascript
function circleIntersectionArea(x1, y1, r1, x2, y2, r2) {
    // Your code here
}
```

### Java
```java
public double circleIntersectionArea(double x1, double y1, double r1,
                                    double x2, double y2, double r2) {
    // Your code here
}
```

## Hints

1. Calculate distance between centers: d = √((x2-x1)² + (y2-y1)²)

2. Check for special cases:
   - If d >= r1 + r2: circles don't intersect, return 0
   - If d <= |r1 - r2|: one circle inside another, return π × (smaller radius)²

3. For partial overlap, use the formula:
   - A = r1² × arccos((d² + r1² - r2²)/(2dr1)) +
        r2² × arccos((d² + r2² - r1²)/(2dr2)) -
        0.5 × √((-d+r1+r2)(d+r1-r2)(d-r1+r2)(d+r1+r2))

4. Use math constants and functions: π, arccos, sqrt
5. Time complexity: O(1), Space complexity: O(1)

## Tags
`math` `geometry` `circles` `intersection` `trigonometry` `hard`
