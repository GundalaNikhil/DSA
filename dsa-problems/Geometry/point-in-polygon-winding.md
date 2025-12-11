---
unique_problem_id: geometry_002
display_id: GEOMETRY-002
slug: point-in-polygon-winding
version: 1.0.0
difficulty: Medium
topic_tags:
  - Computational Geometry
  - Point in Polygon
  - Winding Number
  - Ray Casting
  - Polygon
---

# Point in Polygon (Winding)

## Problem Description

Determine if a point lies inside, outside, or on the boundary of a simple polygon using winding number.

## Examples

- Example 1:
  - Input: polygon [(0,0),(2,0),(2,2),(0,2)], point (1,1)
  - Output: `Inside`
  - Explanation: Point (1,1) is clearly inside the square.

- Example 2:
  - Input: polygon [(0,0),(2,0),(2,2),(0,2)], point (3,3)
  - Output: `Outside`
  - Explanation: Point (3,3) is outside the square.

- Example 3:
  - Input: polygon [(0,0),(2,0),(2,2),(0,2)], point (1,0)
  - Output: `Boundary`
  - Explanation: Point (1,0) lies on edge from (0,0) to (2,0).

## Constraints

- n <= 10^5

## Function Signatures

### Java
```java
class Solution {
    public String pointInPolygonWinding(int[][] polygon, int[] point) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List, Tuple

def point_in_polygon_winding(polygon: List[Tuple[int,int]], point: Tuple[int,int]) -> str:
    """
    Determine point location relative to polygon.
    
    Args:
        polygon: List of (x, y) vertices in order
        point: Query point (x, y)
    
    Returns:
        "Inside", "Outside", or "Boundary"
    """
    pass
```

### C++
```cpp
class Solution {
public:
    string pointInPolygonWinding(vector<vector<int>>& polygon, vector<int>& point) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n (polygon vertices)
- Next n lines: x y (vertex coordinates)
- Last line: query point x y

### Sample Input
```
4
0 0
2 0
2 2
0 2
1 1
```

## Hints

Winding number: sum of angles subtended by edges around the query point. Non-zero = inside, zero = outside. Or use ray casting: count edge crossings.

## Quiz

### Question 1
What is the winding number for a point inside?

A) 0  
B) Non-zero (typically ±1 for simple polygons)  
C) Greater than n  
D) Negative only

**Correct Answer:** B

**Explanation:** For simple polygons, winding number is ±1 for interior points (sign depends on polygon orientation).

### Question 2
What advantage does winding have over ray casting?

A) Faster  
B) Handles self-intersecting polygons  
C) Uses less memory  
D) Simpler implementation

**Correct Answer:** B

**Explanation:** Winding number naturally extends to complex (self-intersecting) polygons where ray casting may give ambiguous results.

### Question 3
Time complexity for n-vertex polygon?

A) O(1)  
B) O(n)  
C) O(n log n)  
D) O(n²)

**Correct Answer:** B

**Explanation:** We iterate through each edge once.

### Question 4
How to detect points on the boundary?

A) Winding number = 0.5  
B) Check if point lies on any edge segment  
C) Use tolerance  
D) Not possible with winding

**Correct Answer:** B

**Explanation:** Boundary cases need explicit edge-by-edge check since winding number theory assumes point is not on boundary.
