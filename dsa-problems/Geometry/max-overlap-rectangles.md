---
unique_problem_id: geometry_011
display_id: GEOMETRY-011
slug: max-overlap-rectangles
version: 1.0.0
difficulty: Medium
topic_tags:
  - Computational Geometry
  - Sweep Line
  - Segment Tree
  - Maximum Overlap
  - Event Processing
---

# Maximum Overlap of Rectangles

## Problem Description

Given axis-aligned rectangles, find maximum number overlapping at any point.

## Examples

- Example 1:
  - Input: rectangles [(0,0)-(2,2), (1,1)-(3,3), (2,0)-(4,2)]
  - Output: 2
  - Explanation: Maximum overlap of 2 rectangles at various points.

- Example 2:
  - Input: rectangles [(0,0)-(1,1), (2,2)-(3,3)]
  - Output: 1
  - Explanation: No overlap, each point covered by at most 1 rectangle.

- Example 3:
  - Input: rectangles [(0,0)-(10,10), (1,1)-(9,9), (2,2)-(8,8)]
  - Output: 3
  - Explanation: All three overlap at center region.

## Constraints

- Up to 10^5 rectangles

## Function Signatures

### Java
```java
class Solution {
    public int maxOverlapRectangles(int[][] rectangles) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List

def max_overlap_rectangles(rectangles: List[List[int]]) -> int:
    """
    Find maximum number of overlapping rectangles.
    
    Args:
        rectangles: List of [x1,y1,x2,y2]
    
    Returns:
        Maximum overlap count at any point
    """
    pass
```

### C++
```cpp
class Solution {
public:
    int maxOverlapRectangles(vector<vector<int>>& rectangles) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: n
- Next n lines: x1 y1 x2 y2

### Sample Input
```
3
0 0 2 2
1 1 3 3
2 0 4 2
```

## Hints

Sweep line + segment tree with lazy propagation. Track maximum coverage at any y-coordinate during sweep.

## Quiz

### Question 1
What info does the segment tree maintain?

A) Current coverage count for each y-interval  
B) Maximum coverage in any subinterval  
C) Both A and B  
D) Just the endpoints

**Correct Answer:** C

**Explanation:** Need to track coverage per interval (for updates) and maximum (for query).

### Question 2
What are the sweep events?

A) Only rectangle starts  
B) Rectangle left edge (add) and right edge (remove)  
C) All corners  
D) Random points

**Correct Answer:** B

**Explanation:** Left edges add coverage to y-interval; right edges remove it.

### Question 3
Time complexity?

A) O(n)  
B) O(n log n)  
C) O(n²)  
D) O(n log² n)

**Correct Answer:** B

**Explanation:** O(n log n) for sorting events, O(log n) per update with segment tree.

### Question 4
Can this be solved without coordinate compression?

A) Yes, always  
B) No, coordinates can be 10^9  
C) Sometimes  
D) Compression is optional

**Correct Answer:** B

**Explanation:** Coordinates up to 10^9 require compression to limit segment tree size.
