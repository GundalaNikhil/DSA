---
unique_problem_id: geometry_014
display_id: GEOMETRY-014
slug: angle-sorting-polar
version: 1.0.0
difficulty: Easy
topic_tags:
  - Computational Geometry
  - Polar Coordinates
  - Angle Sorting
  - atan2
  - Comparator
---

# Angle Sorting for Polar Order

## Problem Description

Sort points by polar angle around origin; tie by distance.

## Examples

- Example 1:
  - Input: [(1,0), (1,1), (0,1)]
  - Output: [(1,0), (1,1), (0,1)]
  - Explanation: Angles: 0°, 45°, 90°. Already sorted.

- Example 2:
  - Input: [(0,1), (1,0), (-1,0)]
  - Output: [(1,0), (0,1), (-1,0)]
  - Explanation: Sorted by angle: 0°, 90°, 180°.

- Example 3:
  - Input: [(2,0), (1,0)]
  - Output: [(1,0), (2,0)]
  - Explanation: Same angle (0°), sort by distance.

## Constraints

- n <= 10^5

## Function Signatures

### Java
```java
class Solution {
    public int[][] angleSortingPolar(int[][] points) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List, Tuple

def angle_sorting_polar(points: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    """
    Sort points by polar angle around origin.
    
    Args:
        points: List of (x, y) coordinates
    
    Returns:
        Points sorted by angle, then by distance
    """
    pass
```

### C++
```cpp
class Solution {
public:
    vector<vector<int>> angleSortingPolar(vector<vector<int>>& points) {
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
1 0
1 1
0 1
```

## Hints

Use atan2(y, x) for angle computation. Or use cross product for comparison without computing actual angles (avoids floating point).

## Quiz

### Question 1
Why use atan2 instead of atan(y/x)?

A) Faster  
B) Handles all quadrants correctly, avoids division by zero  
C) Returns degrees  
D) No difference

**Correct Answer:** B

**Explanation:** atan2(y,x) handles the full range [-π, π] and all quadrants, avoiding division issues.

### Question 2
How to avoid floating point issues?

A) Use integer cross product for comparisons  
B) Multiply by 1000  
C) Round results  
D) Can't avoid

**Correct Answer:** A

**Explanation:** Cross product sign determines relative angle ordering. No floating point needed.

### Question 3
What if a point is at the origin?

A) It has angle 0  
B) Undefined angle - handle specially  
C) It has angle π  
D) Skip it

**Correct Answer:** B

**Explanation:** Origin has no well-defined angle. Often sorted first or handled as special case.

### Question 4
Time complexity?

A) O(n)  
B) O(n log n)  
C) O(n²)  
D) O(1)

**Correct Answer:** B

**Explanation:** Sorting dominates at O(n log n).
