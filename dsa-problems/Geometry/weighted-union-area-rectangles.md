---
unique_problem_id: geometry_010
display_id: GEOMETRY-010
slug: weighted-union-area-rectangles
version: 1.0.0
difficulty: Medium
topic_tags:
  - Computational Geometry
  - Sweep Line
  - Segment Tree
  - Rectangle Union
  - Coordinate Compression
---

# Line Sweep Weighted Union Area

## Problem Description

Given axis-aligned rectangles each with an integer weight, compute the area covered by rectangles where the cumulative weight is at least `W` (threshold). Rectangles can overlap; count area only where sum of weights >= W.

## Examples

- Example 1:
  - Input: rectangles [(0,0)-(2,2,w=1), (1,1)-(3,3,w=2)], W=2
  - Output: 4
  - Explanation: Overlap region (1,1)-(2,2) has weight 3 (area 1). Region (1,1)-(2,3) and (1,1)-(3,2) have weight 2. Total area >= W.

- Example 2:
  - Input: rectangles [(0,0)-(1,1,w=1)], W=2
  - Output: 0
  - Explanation: Only weight 1 everywhere, below threshold.

- Example 3:
  - Input: rectangles [(0,0)-(2,2,w=5)], W=3
  - Output: 4
  - Explanation: Entire rectangle has weight 5 >= 3.

## Constraints

- Up to 10^5 rectangles
- |weight| <= 10^6
- 1 <= W <= 10^6

## Function Signatures

### Java
```java
class Solution {
    public long weightedUnionAreaRectangles(int[][] rectangles, int W) {
        // rectangles[i] = [x1,y1,x2,y2,weight]
        // Implementation here
    }
}
```

### Python
```python
from typing import List

def weighted_union_area_rectangles(rectangles: List[List[int]], W: int) -> int:
    """
    Compute area where cumulative weight >= W.
    
    Args:
        rectangles: List of [x1,y1,x2,y2,weight]
        W: Weight threshold
    
    Returns:
        Total area meeting threshold
    """
    pass
```

### C++
```cpp
class Solution {
public:
    long long weightedUnionAreaRectangles(vector<vector<int>>& rectangles, int W) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n W
- Next n lines: x1 y1 x2 y2 weight

### Sample Input
```
2 2
0 0 2 2 1
1 1 3 3 2
```

## Hints

Sweep x-coordinate. For each x-interval, use segment tree on y to track coverage weight. Query for total y-length where weight >= W.

## Quiz

### Question 1
How is this different from simple rectangle union?

A) Overlaps count multiple times  
B) Only count area where sum of overlapping weights >= W  
C) Weights are ignored  
D) No difference

**Correct Answer:** B

**Explanation:** Standard union counts area covered at least once. Here we threshold by cumulative weight.

### Question 2
Why coordinate compression?

A) Reduces memory  
B) Allows discrete sweep events  
C) Segment tree operates on compressed coordinates  
D) All of the above

**Correct Answer:** D

**Explanation:** Coordinates up to 10^9 need compression to fit in segment tree with O(n) nodes.

### Question 3
What does the segment tree track?

A) Y-intervals and their cumulative weight  
B) Number of rectangles  
C) Area directly  
D) X-coordinates

**Correct Answer:** A

**Explanation:** At each x-position, segment tree tracks weight at each y-interval and can query total length with weight >= W.

### Question 4
Time complexity?

A) O(n)  
B) O(n log n)  
C) O(n² log n)  
D) O(n²)

**Correct Answer:** B

**Explanation:** O(n log n) events, each processed in O(log n) with segment tree.
