# Radar Coverage Overlap

**Difficulty:** Hard
**Topic:** Math, Geometry, Circles
**License:** Free to use for commercial purposes

## Problem Statement

Two radar stations have coverage areas defined by circles (center x, y and radius r). Calculate the area of overlap between the two radar coverages.

## Constraints

- Coordinates and radii are integers.

## Examples

### Example 1
```
Input: x1=0, y1=0, r1=10, x2=10, y2=0, r2=10
Output: 122.84
Explanation: Partial overlap.
```

### Example 2
```
Input: x1=0, y1=0, r1=5, x2=20, y2=0, r2=5
Output: 0.00
Explanation: Too far apart.
```

### Example 3
```
Input: x1=0, y1=0, r1=10, x2=0, y2=0, r2=5
Output: 78.54
Explanation: Inner circle fully inside. Area = pi * 5^2 = 78.54.
```

## Function Signature

### Python
```python
def radar_overlap_area(x1: float, y1: float, r1: float,
                       x2: float, y2: float, r2: float) -> float:
    pass
```

### JavaScript
```javascript
function radarOverlapArea(x1, y1, r1, x2, y2, r2) {
    // Your code here
}
```

### Java
```java
public double radarOverlapArea(double x1, double y1, double r1,
                               double x2, double y2, double r2) {
    // Your code here
}
```

## Hints
1. Check distance between centers
2. Use circle intersection area formula

## Tags
`math` `geometry` `hard`
