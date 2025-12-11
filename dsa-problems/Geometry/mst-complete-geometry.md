---
unique_problem_id: geometry_016
display_id: GEOMETRY-016
slug: mst-complete-geometry
version: 1.0.0
difficulty: Hard
topic_tags:
  - Computational Geometry
  - Manhattan MST
  - Euclidean MST
  - Sweep Line
  - Union Find
---

# Minimum Spanning Tree on Complete Graph by Geometry

## Problem Description

Given points, MST of complete graph with edge weight as Manhattan distance. Compute MST weight efficiently.

## Examples

- Example 1:
  - Input: [(0,0),(2,2),(3,0)]
  - Output: 6
  - Explanation: Connect (0,0)-(3,0) (dist 3) and (3,0)-(2,2) (dist 1+2=3). Total = 6? Or (0,0)-(2,2)=4, (2,2)-(3,0)=1+2=3. Total=7. Best: (0,0)-(3,0)=3, (3,0)-(2,2)=3. Total=6.

- Example 2:
  - Input: [(0,0),(1,0),(0,1)]
  - Output: 2
  - Explanation: Connect with total Manhattan distance 2.

- Example 3:
  - Input: [(0,0),(10,10)]
  - Output: 20
  - Explanation: Only edge has Manhattan distance |10-0| + |10-0| = 20.

## Constraints

- n <= 2 * 10^5

## Function Signatures

### Java
```java
class Solution {
    public long mstCompleteGeometry(int[][] points) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List, Tuple

def mst_complete_geometry(points: List[Tuple[int,int]]) -> int:
    """
    Compute MST weight for complete graph with Manhattan distances.
    
    Args:
        points: List of (x, y) coordinates
    
    Returns:
        Total MST weight
    """
    pass
```

### C++
```cpp
class Solution {
public:
    long long mstCompleteGeometry(vector<vector<int>>& points) {
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
2 2
3 0
```

## Hints

Manhattan MST trick: transform to 8 directional neighbors (4 regions after merging). For each direction, use sweep line to find candidates. O(n log n) total edges, then Kruskal's.

## Quiz

### Question 1
Why can't we use O(n²) approach for large n?

A) Memory  
B) Time: 4*10^10 edges too slow  
C) Precision  
D) No reason

**Correct Answer:** B

**Explanation:** With n=2*10^5, O(n²) = 4*10^10 operations, way too slow.

### Question 2
How many candidate edges per point in Manhattan MST?

A) n-1  
B) O(1) per region, ~8 total  
C) log n  
D) sqrt(n)

**Correct Answer:** B

**Explanation:** In each of 8 octants, we only need the closest point. This gives O(n) total candidate edges.

### Question 3
What transformation is used?

A) None  
B) Coordinate rotation/transformation to handle different regions  
C) Log transformation  
D) Fourier transform

**Correct Answer:** B

**Explanation:** Transform coordinates (e.g., (x,y) → (x+y, x-y)) to handle different directional regions uniformly.

### Question 4
Final complexity?

A) O(n log n)  
B) O(n²)  
C) O(n)  
D) O(n² log n)

**Correct Answer:** A

**Explanation:** O(n log n) for sorting/sweep in each region, O(n log n) candidate edges, O(n log n) for Kruskal's.
