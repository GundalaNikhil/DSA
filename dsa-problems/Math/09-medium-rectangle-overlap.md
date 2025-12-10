# Land Plot Encroachment

**Difficulty:** Medium
**Topic:** Math, Geometry, Rectangles
**License:** Free to use for commercial purposes

## Problem Statement

Two land plots are defined by their bottom-left `(x1, y1)` and top-right `(x2, y2)` coordinates. Determine the area of encroachment (overlap) between Plot A and Plot B.

Return 0 if no overlap.

## Constraints

- Coordinates are integers between -1000 and 1000.

## Examples

### Example 1
```
Input:
Plot A: (0, 0) to (10, 10)
Plot B: (5, 5) to (15, 15)
Output: 25
Explanation: Overlap is box from (5,5) to (10,10). 5x5 = 25.
```

### Example 2
```
Input:
Plot A: (0, 0) to (2, 2)
Plot B: (3, 3) to (5, 5)
Output: 0
```

### Example 3
```
Input:
Plot A: (0, 0) to (5, 5)
Plot B: (2, 0) to (3, 5)
Output: 5
Explanation: B is a vertical strip inside A. Width 1, Height 5. Area 5.
```

## Function Signature

### Python
```python
def calculate_encroachment(ax1: int, ay1: int, ax2: int, ay2: int,
                          bx1: int, by1: int, bx2: int, by2: int) -> int:
    pass
```

### JavaScript
```javascript
function calculateEncroachment(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) {
    // Your code here
}
```

### Java
```java
public int calculateEncroachment(int ax1, int ay1, int ax2, int ay2,
                                int bx1, int by1, int bx2, int by2) {
    // Your code here
}
```

## Hints
1. Overlap x-range: max(ax1, bx1) to min(ax2, bx2)
2. Overlap y-range: max(ay1, by1) to min(ay2, by2)
3. If min < max in both dimensions, area = dx * dy

## Tags
`math` `geometry` `medium`
