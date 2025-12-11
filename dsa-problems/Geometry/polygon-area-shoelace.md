---
unique_problem_id: geometry_006
display_id: GEOMETRY-006
slug: polygon-area-shoelace
version: 1.0.0
difficulty: Easy
topic_tags:
  - Computational Geometry
  - Shoelace Formula
  - Polygon Area
  - Cross Product
  - Signed Area
---

# Polygon Area (Shoelace)

## Problem Description

Compute signed area of a simple polygon.

## Examples

- Example 1:
  - Input: [(0,0),(2,0),(2,2),(0,2)]
  - Output: 4
  - Explanation: Square with side 2. Area = 4.

- Example 2:
  - Input: [(0,0),(4,0),(2,3)]
  - Output: 6
  - Explanation: Triangle with base 4 and height 3. Area = 0.5 * 4 * 3 = 6.

- Example 3:
  - Input: [(0,0),(1,0),(1,1),(0,1)] (CCW)
  - Output: 1 (positive for CCW)
  - Explanation: Unit square, area = 1.

## Constraints

- n <= 10^5

## Function Signatures

### Java
```java
class Solution {
    public double polygonAreaShoelace(int[][] vertices) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List, Tuple

def polygon_area_shoelace(vertices: List[Tuple[int,int]]) -> float:
    """
    Compute polygon area using shoelace formula.
    
    Args:
        vertices: List of (x, y) vertices in order
    
    Returns:
        Area of polygon (always positive)
    """
    pass
```

### C++
```cpp
class Solution {
public:
    double polygonAreaShoelace(vector<vector<int>>& vertices) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n (number of vertices)
- Next n lines: x y

### Sample Input
```
4
0 0
2 0
2 2
0 2
```

## Hints

Shoelace formula: Area = 0.5 * |Σ(x_i * y_{i+1} - x_{i+1} * y_i)|. Sum over all edges, indices wrap around.

## Quiz

### Question 1
What is the shoelace formula?

A) A = Σ(x_i * y_i)  
B) A = 0.5 * |Σ(x_i * y_{i+1} - x_{i+1} * y_i)|  
C) A = Σ√((x_{i+1}-x_i)² + (y_{i+1}-y_i)²)  
D) A = max(x) * max(y)

**Correct Answer:** B

**Explanation:** Shoelace formula sums cross products of consecutive vertices, halved. Absolute value gives positive area.

### Question 2
What does the sign indicate?

A) Nothing  
B) Orientation: CCW = positive, CW = negative  
C) Error  
D) Convexity

**Correct Answer:** B

**Explanation:** Signed area is positive for CCW vertex ordering and negative for CW.

### Question 3
Time complexity?

A) O(1)  
B) O(n)  
C) O(n log n)  
D) O(n²)

**Correct Answer:** B

**Explanation:** Single pass through all n vertices.

### Question 4
Does it work for non-convex polygons?

A) No  
B) Yes  
C) Only for simple polygons  
D) Both B and C

**Correct Answer:** D

**Explanation:** Works for any simple (non-self-intersecting) polygon, convex or not.
