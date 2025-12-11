---
unique_problem_id: geometry_008
display_id: GEOMETRY-008
slug: minimum-enclosing-circle
version: 1.0.0
difficulty: Medium
topic_tags:
  - Computational Geometry
  - Minimum Enclosing Circle
  - Randomized Algorithm
  - Welzl Algorithm
  - Circle Construction
---

# Minimum Enclosing Circle

## Problem Description

Find the smallest circle enclosing all points.

## Examples

- Example 1:
  - Input: [(0,0),(1,0),(0,1)]
  - Output: center (0.5,0.5), radius ~0.707
  - Explanation: Circle centered at (0.5,0.5) with radius √0.5 encloses all three points.

- Example 2:
  - Input: [(0,0),(2,0)]
  - Output: center (1,0), radius 1
  - Explanation: Two points define a circle with diameter as the line segment.

- Example 3:
  - Input: [(0,0)]
  - Output: center (0,0), radius 0
  - Explanation: Single point is trivially enclosed.

## Constraints

- n <= 2 * 10^5

## Function Signatures

### Java
```java
class Solution {
    public double[] minimumEnclosingCircle(int[][] points) {
        // Returns [centerX, centerY, radius]
        // Implementation here
    }
}
```

### Python
```python
from typing import List, Tuple

def minimum_enclosing_circle(points: List[Tuple[int,int]]) -> Tuple[float, float, float]:
    """
    Find smallest enclosing circle.
    
    Args:
        points: List of (x, y) coordinates
    
    Returns:
        Tuple of (center_x, center_y, radius)
    """
    pass
```

### C++
```cpp
class Solution {
public:
    vector<double> minimumEnclosingCircle(vector<vector<int>>& points) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n
- Next n lines: x y

### Sample Input
```
3
0 0
1 0
0 1
```

## Hints

Welzl's randomized incremental algorithm: expected O(n). Base cases: 0-3 points on boundary define the circle. Add points incrementally with random order.

## Quiz

### Question 1
How many points define the minimum enclosing circle boundary?

A) Always n  
B) At most 3  
C) Exactly 2  
D) At least 4

**Correct Answer:** B

**Explanation:** A circle is defined by at most 3 points (circumcircle of triangle, or 2 points as diameter).

### Question 2
Expected time complexity of Welzl's algorithm?

A) O(n)  
B) O(n log n)  
C) O(n²)  
D) O(n³)

**Correct Answer:** A

**Explanation:** Randomized order gives expected O(n) time, though worst case is O(n²).

### Question 3
What if a point is outside the current circle?

A) Ignore it  
B) It must be on the new boundary; recurse  
C) Restart from scratch  
D) Double the radius

**Correct Answer:** B

**Explanation:** A point outside the current MEC must lie on the boundary of the true MEC. Recurse with this point fixed on boundary.

### Question 4
What is the base case for 2 boundary points?

A) Any circle through them  
B) Circle with them as diameter  
C) Smallest circle tangent to both  
D) Depends on position

**Correct Answer:** B

**Explanation:** Two points define the smallest enclosing circle as the one with them as endpoints of a diameter.
