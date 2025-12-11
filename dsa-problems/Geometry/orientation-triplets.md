---
unique_problem_id: geometry_001
display_id: GEOMETRY-001
slug: orientation-triplets
version: 1.0.0
difficulty: Easy
topic_tags:
  - Computational Geometry
  - Cross Product
  - Orientation Test
  - Collinearity
  - Triangle Area
---

# Orientation of Triplets

## Problem Description

Given three points, determine if they are collinear, clockwise, or counterclockwise.

## Examples

- Example 1:
  - Input: (0,0), (1,1), (2,0)
  - Output: `Clockwise`
  - Explanation: Cross product (1-0)*(0-0) - (0-0)*(2-0) = 1*0 - 0*2 = 0? No, let's recalculate: (p2-p1) × (p3-p1) = (1,1)×(2,0) relative to origin at p1. (1)(0) - (1)(2) = -2 < 0 = Clockwise.

- Example 2:
  - Input: (0,0), (1,1), (2,2)
  - Output: `Collinear`
  - Explanation: All points on line y=x. Cross product = 0.

- Example 3:
  - Input: (0,0), (2,0), (1,1)
  - Output: `Counterclockwise`
  - Explanation: Cross product (2)(1) - (0)(1) = 2 > 0 = CCW.

## Constraints

- Coordinates in [-10^9, 10^9]

## Function Signatures

### Java
```java
class Solution {
    public String orientationTriplets(int[] p1, int[] p2, int[] p3) {
        // Implementation here
    }
}
```

### Python
```python
from typing import Tuple

def orientation_triplets(p1: Tuple[int,int], p2: Tuple[int,int], p3: Tuple[int,int]) -> str:
    """
    Determine orientation of three points.
    
    Args:
        p1, p2, p3: Three points as (x, y) tuples
    
    Returns:
        "Collinear", "Clockwise", or "Counterclockwise"
    """
    pass
```

### C++
```cpp
class Solution {
public:
    string orientationTriplets(vector<int>& p1, vector<int>& p2, vector<int>& p3) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- Three lines, each with x y coordinates

### Sample Input
```
0 0
1 1
2 0
```

## Hints

Compute cross product of vectors (p2-p1) and (p3-p1). If > 0: CCW, < 0: CW, = 0: collinear. Use long long to avoid overflow.

## Quiz

### Question 1
What does the cross product sign indicate?

A) Distance between points  
B) Orientation (CW/CCW/collinear)  
C) Angle magnitude  
D) Area

**Correct Answer:** B

**Explanation:** The sign of cross product determines relative orientation: positive = CCW, negative = CW, zero = collinear.

### Question 2
Why use long long for computation?

A) Faster  
B) Avoid integer overflow when multiplying large coordinates  
C) Required by geometry  
D) Cleaner code

**Correct Answer:** B

**Explanation:** Coordinates up to 10^9 when multiplied can exceed int range (10^18 vs ~2*10^9).

### Question 3
What is the formula for 2D cross product?

A) x1*y2 + x2*y1  
B) (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)  
C) x1*x2 + y1*y2  
D) sqrt((x2-x1)² + (y2-y1)²)

**Correct Answer:** B

**Explanation:** Cross product of vectors (a,b) and (c,d) is ad - bc. For points, translate to common origin first.

### Question 4
What is the time complexity?

A) O(1)  
B) O(n)  
C) O(n²)  
D) O(log n)

**Correct Answer:** A

**Explanation:** Just a few arithmetic operations regardless of coordinate size.
