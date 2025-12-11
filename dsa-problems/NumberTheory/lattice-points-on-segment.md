---
unique_problem_id: numbertheory_008
display_id: NUMBERTHEORY-008
slug: lattice-points-on-segment
version: 1.0.0
difficulty: Easy
topic_tags:
  - Number Theory
  - Problem Solving
---

# Counting Lattice Points On Segment

## Problem Description

Given endpoints (x1,y1),(x2,y2) integer coordinates, count integer lattice points on the closed segment.

## Examples

- Input: `(0,0),(6,4)`
  - Output: `3` (points at (0,0),(3,2),(6,4))

## Constraints

`|coords| <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] latticePointsOnSegment(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def latticePointsOnSegment(arr: List[int]) -> List[int]:
    """
    Solve the problem.

    Args:
        arr: Input array

    Returns:
        Result array
    """
    pass
```

### C++
```cpp
class Solution {
public:
    vector<int> latticePointsOnSegment(vector<int>& arr) {
        // Implementation here
        return {};
    }
};
```

## Input Format

The input will be provided as:
- First line: Integer n (size of array)
- Second line: n space-separated integers representing the array

### Sample Input
```
5
1 2 3 4 5
```

## Hints

gcd of differences + 1.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Counting Lattice Points On Segment'?**

A) O(n)
B) O(n log n)
C) O(n^2)
D) O(1)

**Correct Answer:** A

**Explanation:** The optimal solution can be achieved in linear time by processing the array in a single pass.

### Question 2
**Which data structure would be most suitable for this problem?**

A) Array/List
B) Hash Map
C) Tree
D) Graph

**Correct Answer:** A

**Explanation:** An array or list is the primary data structure needed for this problem.

### Question 3
**Which algorithmic paradigm does this problem primarily belong to?**

A) Number Theory
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Number Theory techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
