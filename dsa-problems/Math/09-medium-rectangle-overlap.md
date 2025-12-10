# Rectangle Overlap Area

**Difficulty:** Medium
**Topic:** Math, Geometry, Rectangles
**License:** Free to use for commercial purposes

## Problem Statement

Two rectangles are placed on a 2D coordinate plane. Each rectangle is defined by its bottom-left corner `(x1, y1)` and top-right corner `(x2, y2)`, where `x1 < x2` and `y1 < y2`.

Calculate the area of overlap between the two rectangles. If they don't overlap, return 0.

## Constraints

- `-1000 <= x1 < x2 <= 1000`
- `-1000 <= y1 < y2 <= 1000`
- Coordinates are integers

## Examples

### Example 1
```
Input:
  Rectangle A: (0, 0), (4, 4)
  Rectangle B: (2, 2), (6, 6)
Output: 4
Explanation:
  Overlap region: (2, 2) to (4, 4)
  Width = 4 - 2 = 2, Height = 4 - 2 = 2
  Area = 2 × 2 = 4
```

### Example 2
```
Input:
  Rectangle A: (0, 0), (3, 3)
  Rectangle B: (5, 5), (8, 8)
Output: 0
Explanation: Rectangles don't overlap.
```

### Example 3
```
Input:
  Rectangle A: (0, 0), (5, 5)
  Rectangle B: (1, 1), (4, 4)
Output: 9
Explanation:
  Rectangle B is completely inside Rectangle A.
  Overlap area = 3 × 3 = 9
```

### Example 4
```
Input:
  Rectangle A: (0, 0), (10, 10)
  Rectangle B: (5, 0), (15, 10)
Output: 50
Explanation:
  Overlap region: (5, 0) to (10, 10)
  Width = 5, Height = 10
  Area = 5 × 10 = 50
```

### Example 5
```
Input:
  Rectangle A: (-5, -5), (0, 0)
  Rectangle B: (-3, -3), (3, 3)
Output: 9
Explanation:
  Overlap region: (-3, -3) to (0, 0)
  Width = 3, Height = 3
  Area = 3 × 3 = 9
```

## Function Signature

### Python
```python
def calculate_overlap_area(ax1: int, ay1: int, ax2: int, ay2: int,
                          bx1: int, by1: int, bx2: int, by2: int) -> int:
    pass
```

### JavaScript
```javascript
function calculateOverlapArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2) {
    // Your code here
}
```

### Java
```java
public int calculateOverlapArea(int ax1, int ay1, int ax2, int ay2,
                               int bx1, int by1, int bx2, int by2) {
    // Your code here
}
```

## Hints

1. Find the overlapping rectangle's coordinates
2. Overlap left edge: max(ax1, bx1)
3. Overlap right edge: min(ax2, bx2)
4. Overlap bottom edge: max(ay1, by1)
5. Overlap top edge: min(ay2, by2)
6. If left >= right or bottom >= top, no overlap exists
7. Area = width × height = (right - left) × (top - bottom)
8. Time complexity: O(1), Space complexity: O(1)

## Tags
`math` `geometry` `rectangles` `coordinate-geometry` `medium`
