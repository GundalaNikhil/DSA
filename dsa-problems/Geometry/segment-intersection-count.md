---
unique_problem_id: geometry_003
display_id: GEOMETRY-003
slug: segment-intersection-count
version: 1.0.0
difficulty: Medium
topic_tags:
  - Computational Geometry
  - Sweep Line
  - Segment Intersection
  - Balanced BST
  - Event-Driven
---

# Segment Intersection Count

## Problem Description

Given `m` line segments, count how many pairs intersect (including touching).

## Examples

- Example 1:
  - Input: segments [(0,0)-(2,2), (0,2)-(2,0)]
  - Output: 1
  - Explanation: The two segments cross at (1,1).

- Example 2:
  - Input: segments [(0,0)-(1,0), (2,0)-(3,0)]
  - Output: 0
  - Explanation: No intersection - segments are separated.

- Example 3:
  - Input: segments [(0,0)-(2,0), (1,0)-(3,0)]
  - Output: 1
  - Explanation: Segments overlap from (1,0) to (2,0) - counts as intersection.

## Constraints

- m <= 2 * 10^5

## Function Signatures

### Java
```java
class Solution {
    public int segmentIntersectionCount(int[][][] segments) {
        // Implementation here
    }
}
```

### Python
```python
from typing import List, Tuple

def segment_intersection_count(segments: List[Tuple[Tuple[int,int], Tuple[int,int]]]) -> int:
    """
    Count pairs of intersecting segments.
    
    Args:
        segments: List of ((x1,y1), (x2,y2)) segments
    
    Returns:
        Number of intersecting pairs
    """
    pass
```

### C++
```cpp
class Solution {
public:
    int segmentIntersectionCount(vector<vector<vector<int>>>& segments) {
        // Implementation here
    }
};
```

## Input Format

The input will be provided as:
- First line: m (number of segments)
- Next m lines: x1 y1 x2 y2

### Sample Input
```
2
0 0 2 2
0 2 2 0
```

## Hints

Sweep line algorithm with balanced tree. Events: segment start, end, intersection. For each event, check neighboring segments in sweep status for potential new intersections.

## Quiz

### Question 1
Why is O(n²) brute force too slow here?

A) It's not too slow  
B) m can be 2*10^5, so m² = 4*10^10 operations  
C) Memory issues  
D) Brute force doesn't work

**Correct Answer:** B

**Explanation:** Checking all pairs in O(m²) is too slow for m=2*10^5. Sweep line achieves O((m+k) log m) where k is intersection count.

### Question 2
What is the key insight of sweep line?

A) Only nearby segments in sweep order can intersect  
B) Process all segments at once  
C) Ignore horizontal segments  
D) Use brute force in local regions

**Correct Answer:** A

**Explanation:** As we sweep, only adjacent segments in the vertical order can potentially intersect next.

### Question 3
What data structure maintains sweep status?

A) Array  
B) Stack  
C) Balanced BST (like TreeSet)  
D) Hash map

**Correct Answer:** C

**Explanation:** We need ordered structure with O(log n) insert/delete/neighbor-queries. Balanced BST fits perfectly.

### Question 4
What events are processed?

A) Only segment starts  
B) Left endpoints, right endpoints, intersections  
C) Only intersections  
D) Random points

**Correct Answer:** B

**Explanation:** Start events add segments to status; end events remove; intersection events swap order and check new neighbors.
