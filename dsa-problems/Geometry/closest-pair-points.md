---
unique_problem_id: geometry_004
display_id: GEOMETRY-004
slug: closest-pair-points
version: 1.0.0
difficulty: Medium
topic_tags:
  - Computational Geometry
  - Divide and Conquer
  - Closest Pair
  - Euclidean Distance
  - Sorting
---

# Closest Pair of Points

## Problem Description

Given points in 2D, find squared distance of closest pair.

## Examples

- Example 1:
  - Input: [(0,0), (3,4), (1,1)]
  - Output: 2
  - Explanation: Distance from (0,0) to (1,1) is √2, squared = 2.

- Example 2:
  - Input: [(0,0), (1,0), (0,1)]
  - Output: 1
  - Explanation: Distance (0,0)-(1,0) or (0,0)-(0,1) is 1, squared = 1.

- Example 3:
  - Input: [(0,0), (10,10)]
  - Output: 200
  - Explanation: Only two points. Distance² = 100 + 100 = 200.

## Constraints

- n <= 2 * 10^5

## Function Signatures

### Java
```java
class Solution {
    public long closestPairPoints(int[][] points) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List, Tuple

def closest_pair_points(points: List[Tuple[int, int]]) -> int:
    """
    Find squared distance of closest pair of points.
    
    Args:
        points: List of (x, y) coordinates
    
    Returns:
        Minimum squared Euclidean distance between any two points
    """
    pass
```

### C++
```cpp
class Solution {
public:
    long long closestPairPoints(vector<vector<int>>& points) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n (number of points)
- Next n lines: x y

### Sample Input
```
3
0 0
3 4
1 1
```

## Hints

Divide and conquer: split by x-coordinate, solve left/right recursively, then check pairs crossing the middle strip (width = current min distance).

## Quiz

### Question 1
Why return squared distance?

A) Faster computation  
B) Avoids floating point imprecision  
C) Same comparison semantics  
D) All of the above

**Correct Answer:** D

**Explanation:** Squared distance is easier to compute (no sqrt), uses exact integers, and has same ordering as actual distance.

### Question 2
Time complexity of divide and conquer approach?

A) O(n)  
B) O(n log n)  
C) O(n²)  
D) O(n log² n)

**Correct Answer:** B or D

**Explanation:** With careful implementation and pre-sorting, O(n log n) is achievable. Simple implementations are O(n log² n).

### Question 3
Why is the strip check O(n)?

A) Magic  
B) Only O(1) points per point in strip fit within delta distance  
C) We skip most points  
D) Random sampling

**Correct Answer:** B

**Explanation:** In the strip of width delta, points sorted by y have at most ~6-8 potential neighbors within delta distance (packing argument).

### Question 4
Brute force complexity?

A) O(n)  
B) O(n log n)  
C) O(n²)  
D) O(2^n)

**Correct Answer:** C

**Explanation:** Checking all pairs takes O(n²) comparisons.
