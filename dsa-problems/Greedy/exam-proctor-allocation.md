---
unique_problem_id: greedy_008
display_id: GREEDY-008
slug: exam-proctor-allocation
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Greedy
  - Problem Solving
---

# Exam Proctor Allocation

## Problem Description

Intervals of exams `[start,end]` need proctors. Each proctor can handle up to `r` overlapping exams at once. Find min number of proctors needed.

## Examples

- Input: `[(0,10),(5,7),(6,9)]`, `r=2`
  - Output: `2`

## Constraints

`1 <= n <= 10^5`, `1 <= r <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] examProctorAllocation(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def examProctorAllocation(arr: List[int]) -> List[int]:
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
    vector<int> examProctorAllocation(vector<int>& arr) {
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

Sweep-line counts overlaps; proctors = ceil(maxOverlap / r).

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Exam Proctor Allocation'?**

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

A) Greedy
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Greedy techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
