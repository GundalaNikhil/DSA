---
unique_problem_id: geometry_012
display_id: GEOMETRY-012
slug: largest-empty-circle-rect
version: 1.0.0
difficulty: Medium
topic_tags:
  - Computational Geometry
  - Voronoi Diagram
  - Empty Circle
  - Candidate Centers
  - Brute Force Optimization
---

# Largest Empty Circle Inside Rectangle

## Problem Description

Given points inside a bounding rectangle, find the largest empty circle fully contained in the rectangle and not covering any point.

## Examples

- Example 1:
  - Input: rect (0,0)-(4,4), points [(1,1),(3,1)]
  - Output: radius 1.5
  - Explanation: Circle centered at (2,2.5) with radius ~1.5 avoids both points.

- Example 2:
  - Input: rect (0,0)-(2,2), points [(1,1)]
  - Output: radius ~1
  - Explanation: Largest empty circle touches one point and a rectangle edge.

- Example 3:
  - Input: rect (0,0)-(10,10), no points
  - Output: radius 5
  - Explanation: Circle fills the rectangle, center (5,5), radius 5.

## Constraints

- n <= 2000

## Function Signatures

### Java
```java
class Solution {
    public double largestEmptyCircleRect(int[] rect, int[][] points) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List, Tuple

def largest_empty_circle_rect(rect: Tuple[int,int,int,int], points: List[Tuple[int,int]]) -> float:
    """
    Find radius of largest empty circle in rectangle.
    
    Args:
        rect: (x1, y1, x2, y2) bounding rectangle
        points: List of (x, y) obstacle points
    
    Returns:
        Maximum radius of empty circle
    """
    pass
```

### C++
```cpp
class Solution {
public:
    double largestEmptyCircleRect(vector<int>& rect, vector<vector<int>>& points) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: x1 y1 x2 y2 (rectangle)
- Second line: n
- Next n lines: x y (points)

### Sample Input
```
0 0 4 4
2
1 1
3 1
```

## Hints

Candidate centers lie on Voronoi vertices or edges, or rectangle edges. For n<=2000, can use O(n²) or O(n² log n) approaches.

## Quiz

### Question 1
Where can the optimal center be located?

A) Any random point  
B) Voronoi vertices, Voronoi edges, or rectangle boundary  
C) Only at existing points  
D) Center of rectangle

**Correct Answer:** B

**Explanation:** Optimal empty circle touches multiple obstacles or boundary. Center is on Voronoi diagram.

### Question 2
What is the Voronoi diagram?

A) Partition of plane into regions closest to each point  
B) A triangulation  
C) The convex hull  
D) Random subdivision

**Correct Answer:** A

**Explanation:** Voronoi tessellation divides the plane so each cell contains points closest to one site.

### Question 3
Time complexity for brute force approach?

A) O(n)  
B) O(n log n)  
C) O(n²) or O(n² log n)  
D) O(n³)

**Correct Answer:** C

**Explanation:** With n<=2000, checking O(n²) candidate centers (Voronoi vertices from point pairs) is feasible.

### Question 4
Why must the circle be "fully contained"?

A) Partial circles don't count  
B) Circle cannot extend beyond rectangle boundary  
C) It's a constraint of the problem  
D) All of the above

**Correct Answer:** D

**Explanation:** The problem requires the empty circle to lie entirely within the bounding rectangle.
