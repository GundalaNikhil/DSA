---
unique_problem_id: geometry_009
display_id: GEOMETRY-009
slug: half-plane-intersection
version: 1.0.0
difficulty: Hard
topic_tags:
  - Computational Geometry
  - Half-Plane Intersection
  - Linear Programming
  - Convex Region
  - Sorting by Angle
---

# Half-Plane Intersection

## Problem Description

Given half-planes, compute intersection polygon or report empty.

## Examples

- Example 1:
  - Input: Half-planes x>=0, x<=1, y>=0, y<=1
  - Output: Square [(0,0),(1,0),(1,1),(0,1)]
  - Explanation: Intersection of four half-planes forms a unit square.

- Example 2:
  - Input: Half-planes x>=0, x<=(-1)
  - Output: Empty
  - Explanation: No point satisfies both x>=0 and x<=-1.

- Example 3:
  - Input: Three half-planes forming a triangle
  - Output: Triangle vertices

## Constraints

- Up to 10^5 half-planes

## Function Signatures

### Java
```java
class Solution {
    public int[][] halfPlaneIntersection(double[][] halfPlanes) {
        // Implementation here (each half-plane as [a,b,c] for ax+by<=c)
    }
}
```

### Python
```python
from typing import List, Tuple, Optional

def half_plane_intersection(half_planes: List[Tuple[float,float,float]]) -> Optional[List[Tuple[float,float]]]:
    """
    Compute intersection of half-planes.
    
    Args:
        half_planes: List of (a, b, c) for ax + by <= c
    
    Returns:
        List of vertices of intersection polygon, or None if empty
    """
    pass
```

### C++
```cpp
class Solution {
public:
    vector<vector<double>> halfPlaneIntersection(vector<vector<double>>& halfPlanes) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n
- Next n lines: a b c (representing ax + by <= c)

### Sample Input
```
4
1 0 1
-1 0 0
0 1 1
0 -1 0
```

## Hints

Sort half-planes by angle. Use incremental algorithm with deque to maintain current intersection boundary. Remove dominated half-planes.

## Quiz

### Question 1
What shape is the intersection of half-planes?

A) Always a triangle  
B) Convex polygon or empty  
C) Can be non-convex  
D) Always bounded

**Correct Answer:** B

**Explanation:** Intersection of half-planes is always convex (possibly empty or unbounded).

### Question 2
Time complexity of the algorithm?

A) O(n)  
B) O(n log n)  
C) O(n²)  
D) O(n³)

**Correct Answer:** B

**Explanation:** Sort by angle O(n log n), then linear pass with deque O(n).

### Question 3
Why sort by angle?

A) For ordering  
B) Adjacent half-planes in sorted order form consecutive boundary edges  
C) Random order works too  
D) For numerical stability

**Correct Answer:** B

**Explanation:** Sorting by angle of the half-plane normal allows processing in order around the polygon.

### Question 4
What is a "dominated" half-plane?

A) One that contributes no boundary  
B) One parallel and outside another  
C) One that can be removed  
D) All of the above

**Correct Answer:** D

**Explanation:** A dominated half-plane is made redundant by others and doesn't affect the intersection.
