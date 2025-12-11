---
unique_problem_id: geometry_005
display_id: GEOMETRY-005
slug: convex-hull-capped
version: 1.0.0
difficulty: Medium
topic_tags:
  - Computational Geometry
  - Convex Hull
  - Angle Filtering
  - Graham Scan
  - Andrew's Algorithm
---

# Convex Hull with Interior Caps

## Problem Description

Compute convex hull of a set of points, but discard any hull vertex whose interior angle is less than a given threshold `theta` (in degrees). Return the capped hull in CCW order.

## Examples

- Example 1:
  - Input: points [(0,0),(1,1),(2,0),(1,-1)], theta=60
  - Output: Capped hull with sharp vertices removed
  - Explanation: Compute full hull first, then filter vertices by angle threshold.

- Example 2:
  - Input: points [(0,0),(4,0),(2,3)], theta=30
  - Output: [(0,0),(4,0),(2,3)] (all angles >= 30°)
  - Explanation: Standard triangle hull, all angles above threshold retained.

- Example 3:
  - Input: points collinear [(0,0),(1,0),(2,0)], theta=90
  - Output: [(0,0),(2,0)]
  - Explanation: Collinear points have 180° angle, well above threshold.

## Constraints

- n <= 10^5
- 0 < theta < 180

## Function Signatures

### Java
```java
class Solution {
    public int[][] convexHullCapped(int[][] points, double theta) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List, Tuple

def convex_hull_capped(points: List[Tuple[int,int]], theta: float) -> List[Tuple[int,int]]:
    """
    Compute convex hull with angle-based vertex filtering.
    
    Args:
        points: List of (x, y) coordinates
        theta: Minimum interior angle threshold in degrees
    
    Returns:
        List of hull vertices in CCW order
    """
    pass
```

### C++
```cpp
class Solution {
public:
    vector<vector<int>> convexHullCapped(vector<vector<int>>& points, double theta) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n theta
- Next n lines: x y

### Sample Input
```
4 60
0 0
1 1
2 0
1 -1
```

## Hints

First compute standard convex hull. Then iterate through hull vertices and compute interior angle at each. Remove vertices with angle < theta (may need multiple passes until stable).

## Quiz

### Question 1
How to compute interior angle at a vertex?

A) Use arctan  
B) Cross product gives sine of angle  
C) Dot product gives cosine, use arccos  
D) Both B and C work

**Correct Answer:** D

**Explanation:** Dot product of vectors gives |a||b|cos(θ), and cross product gives |a||b|sin(θ). Either can compute the angle.

### Question 2
What is time complexity of standard convex hull?

A) O(n)  
B) O(n log n)  
C) O(n²)  
D) O(n³)

**Correct Answer:** B

**Explanation:** Dominated by sorting. Graham scan and Andrew's algorithm are O(n log n).

### Question 3
After removing a vertex, do adjacent angles change?

A) No  
B) Yes, must recheck neighbors  
C) Sometimes  
D) Only for collinear points

**Correct Answer:** B

**Explanation:** Removing a vertex changes the angle at both neighboring vertices. May need iterative passes.

### Question 4
What if theta = 0?

A) No vertices removed  
B) All vertices removed  
C) Error  
D) Only collinear removed

**Correct Answer:** A

**Explanation:** All angles >= 0°, so no vertices are filtered out.
