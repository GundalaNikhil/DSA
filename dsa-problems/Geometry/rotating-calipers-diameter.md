---
unique_problem_id: geometry_007
display_id: GEOMETRY-007
slug: rotating-calipers-diameter
version: 1.0.0
difficulty: Medium
topic_tags:
  - Computational Geometry
  - Rotating Calipers
  - Convex Hull
  - Diameter
  - Farthest Pair
---

# Rotating Calipers Diameter

## Problem Description

Given convex polygon, find farthest pair of vertices (diameter squared).

## Examples

- Example 1:
  - Input: Square [(0,0),(1,0),(1,1),(0,1)]
  - Output: 2
  - Explanation: Diagonal distance² = 1² + 1² = 2.

- Example 2:
  - Input: Triangle [(0,0),(3,0),(1.5,2)]
  - Output: 9
  - Explanation: Distance from (0,0) to (3,0) = 3, squared = 9.

- Example 3:
  - Input: Regular hexagon
  - Output: Diameter² across opposite vertices

## Constraints

- n <= 10^5

## Function Signatures

### Java
```java
class Solution {
    public long rotatingCalipersDiameter(int[][] polygon) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List, Tuple

def rotating_calipers_diameter(polygon: List[Tuple[int,int]]) -> int:
    """
    Find squared diameter of convex polygon.
    
    Args:
        polygon: Convex polygon vertices in CCW order
    
    Returns:
        Maximum squared distance between any two vertices
    """
    pass
```

### C++
```cpp
class Solution {
public:
    long long rotatingCalipersDiameter(vector<vector<int>>& polygon) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n
- Next n lines: x y (vertices in order)

### Sample Input
```
4
0 0
1 0
1 1
0 1
```

## Hints

Rotating calipers: two parallel lines "sandwich" the polygon. Rotate around, tracking antipodal pairs. Diameter is found among antipodal points.

## Quiz

### Question 1
Why does rotating calipers work in O(n)?

A) Magic  
B) Each caliper point advances monotonically; total advances = O(n)  
C) Only checks endpoints  
D) Parallel processing

**Correct Answer:** B

**Explanation:** As one caliper edge advances, the antipodal point also advances monotonically around the hull. Total work is O(n).

### Question 2
What is an antipodal pair?

A) Adjacent vertices  
B) Vertices with parallel supporting lines  
C) Random pair  
D) Collinear vertices

**Correct Answer:** B

**Explanation:** Antipodal points are those where parallel tangent lines can touch the polygon at both points.

### Question 3
Does this require convex hull preprocessing?

A) No  
B) Yes, if input isn't already convex hull  
C) Sometimes  
D) Only for n > 1000

**Correct Answer:** B

**Explanation:** Rotating calipers assume convex polygon. If given arbitrary points, first compute convex hull.

### Question 4
Why return squared distance?

A) Avoid floating point  
B) Faster  
C) Same ordering  
D) All of the above

**Correct Answer:** D

**Explanation:** Squared distance is exact integer, faster to compute, and has same comparison ordering.
