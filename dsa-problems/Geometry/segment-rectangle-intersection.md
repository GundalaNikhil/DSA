---
unique_problem_id: geometry_015
display_id: GEOMETRY-015
slug: segment-rectangle-intersection
version: 1.0.0
difficulty: Medium
topic_tags:
  - Computational Geometry
  - Line Clipping
  - Cohen-Sutherland
  - Liang-Barsky
  - Rectangle Intersection
---

# Segment-Rectangle Intersection

## Problem Description

Determine if a line segment intersects or lies within an axis-aligned rectangle.

## Examples

- Example 1:
  - Input: segment (-1,1)-(1,1), rect (0,0)-(2,2)
  - Output: true
  - Explanation: Segment enters rectangle from left at (0,1).

- Example 2:
  - Input: segment (3,3)-(4,4), rect (0,0)-(2,2)
  - Output: false
  - Explanation: Segment entirely outside rectangle.

- Example 3:
  - Input: segment (1,1)-(1.5,1.5), rect (0,0)-(2,2)
  - Output: true
  - Explanation: Segment entirely inside rectangle.

## Constraints

- Coordinates in [-10^9, 10^9]

## Function Signatures

### Java
```java
class Solution {
    public boolean segmentRectangleIntersection(int[] segment, int[] rect) {
        // segment = [x1,y1,x2,y2], rect = [rx1,ry1,rx2,ry2]
        // Implementation here
    }
}
```

### Python
```python
from typing import Tuple

def segment_rectangle_intersection(segment: Tuple[int,int,int,int], rect: Tuple[int,int,int,int]) -> bool:
    """
    Check if segment intersects rectangle.
    
    Args:
        segment: (x1, y1, x2, y2) line segment
        rect: (x1, y1, x2, y2) rectangle bounds
    
    Returns:
        True if segment intersects or is inside rectangle
    """
    pass
```

### C++
```cpp
class Solution {
public:
    bool segmentRectangleIntersection(vector<int>& segment, vector<int>& rect) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: x1 y1 x2 y2 (segment)
- Second line: rx1 ry1 rx2 ry2 (rectangle)

### Sample Input
```
-1 1 1 1
0 0 2 2
```

## Hints

Use Liang-Barsky or Cohen-Sutherland line clipping. Compute intersection with each edge; check if any clipped segment remains.

## Quiz

### Question 1
What is Cohen-Sutherland algorithm?

A) Sorting algorithm  
B) Line clipping algorithm using region codes  
C) Polygon triangulation  
D) Shortest path

**Correct Answer:** B

**Explanation:** Cohen-Sutherland uses 4-bit region codes to efficiently clip lines against rectangles.

### Question 2
What are the three possible outcomes?

A) Only inside or outside  
B) Segment entirely inside, entirely outside, or crossing boundary  
C) Always crossing  
D) Cannot determine

**Correct Answer:** B

**Explanation:** The segment can be fully contained, fully outside, or cross the rectangle boundary.

### Question 3
Liang-Barsky advantage over Cohen-Sutherland?

A) Simpler  
B) Computes intersection directly using parametric form, fewer iterations  
C) Works in 3D  
D) No advantage

**Correct Answer:** B

**Explanation:** Liang-Barsky uses parametric equations, often more efficient for single intersection.

### Question 4
Time complexity?

A) O(1)  
B) O(n)  
C) O(log n)  
D) O(n²)

**Correct Answer:** A

**Explanation:** Fixed number of edge checks and calculations.
