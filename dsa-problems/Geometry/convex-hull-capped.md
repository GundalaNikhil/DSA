---
unique_problem_id: geometry_005
display_id: GEOMETRY-005
slug: convex-hull-capped
version: 1.0.0
difficulty: Medium
topic_tags:
  - Computational Geometry
  - Problem Solving
---

# Convex Hull with Interior Caps

## Problem Description

Compute convex hull of a set of points, but discard any hull vertex whose interior angle is less than a given threshold `theta` (in degrees). Return the capped hull in CCW order.

## Examples

- Input: points [(0,0),(1,1),(2,0),(1,-1)], theta=60
  - Output: capped hull (may remove sharp vertices if below threshold)

## Constraints

n <= 10^5, 0 < theta < 180.

## Function Signatures

### Java
```java
public class Solution {
    public int[] convexHullCapped(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def convexHullCapped(arr: List[int]) -> List[int]:
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
    vector<int> convexHullCapped(vector<int>& arr) {
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

No hints available.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Convex Hull with Interior Caps'?**

A) O(1)
B) O(n)
C) O(n log n)
D) O(n^2)

**Correct Answer:** B

**Explanation:** The solution requires additional space proportional to the input size for preprocessing or storage.

### Question 2
**What technique is most applicable to solve this problem efficiently?**

A) Two pointers
B) Divide and conquer
C) Dynamic programming
D) Greedy approach

**Correct Answer:** A

**Explanation:** The problem can be efficiently solved using the two-pointer technique.

### Question 3
**Which algorithmic paradigm does this problem primarily belong to?**

A) Computational Geometry
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Computational Geometry techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
