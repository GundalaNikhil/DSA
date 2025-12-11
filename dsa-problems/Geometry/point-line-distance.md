---
unique_problem_id: geometry_013
display_id: GEOMETRY-013
slug: point-line-distance
version: 1.0.0
difficulty: Easy
topic_tags:
  - Computational Geometry
  - Distance
  - Projection
  - Line Segment
  - Vector Math
---

# Point-Line Distance

## Problem Description

Compute shortest distance from point to line segment.

## Examples

- Example 1:
  - Input: segment (0,0)-(2,0), point (1,1)
  - Output: 1
  - Explanation: Projection of (1,1) onto segment is (1,0). Distance = 1.

- Example 2:
  - Input: segment (0,0)-(2,0), point (-1,0)
  - Output: 1
  - Explanation: Point projects before segment start. Closest is (0,0). Distance = 1.

- Example 3:
  - Input: segment (0,0)-(2,0), point (1,0)
  - Output: 0
  - Explanation: Point is on the segment.

## Constraints

- Coordinates in [-10^9, 10^9]

## Function Signatures

### Java
```java
class Solution {
    public double pointLineDistance(int[] p1, int[] p2, int[] point) {
        // Implementation here
    }
}
```

### Python
```python
from typing import Tuple

def point_line_distance(segment_start: Tuple[int,int], segment_end: Tuple[int,int], point: Tuple[int,int]) -> float:
    """
    Compute distance from point to line segment.
    
    Args:
        segment_start: (x, y) segment start
        segment_end: (x, y) segment end
        point: (x, y) query point
    
    Returns:
        Shortest distance
    """
    pass
```

### C++
```cpp
class Solution {
public:
    double pointLineDistance(vector<int>& p1, vector<int>& p2, vector<int>& point) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: x1 y1 x2 y2 (segment)
- Second line: px py (point)

### Sample Input
```
0 0 2 0
1 1
```

## Hints

Project point onto infinite line. If projection falls within segment, use perpendicular distance. Otherwise, use distance to nearer endpoint.

## Quiz

### Question 1
What are the three cases for point-segment distance?

A) Always use perpendicular  
B) Projection before segment, on segment, after segment  
C) Only endpoints matter  
D) Depends on segment length

**Correct Answer:** B

**Explanation:** Check where projection falls: before start (use start), after end (use end), or between (use perpendicular distance).

### Question 2
How to compute the projection parameter t?

A) Dot product divided by squared length  
B) Cross product  
C) Segment length  
D) Point coordinates

**Correct Answer:** A

**Explanation:** t = dot(P-A, B-A) / |B-A|². Clamp t to [0,1] for segment.

### Question 3
Time complexity?

A) O(1)  
B) O(n)  
C) O(log n)  
D) O(n²)

**Correct Answer:** A

**Explanation:** Just arithmetic operations, constant time.

### Question 4
Does it work for zero-length segments (point)?

A) No  
B) Yes, reduce to point-point distance  
C) Error  
D) Undefined

**Correct Answer:** B

**Explanation:** If segment has zero length, it's a point. Distance is just point-to-point.
