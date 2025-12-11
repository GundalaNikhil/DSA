---
unique_problem_id: graphbasic_011
display_id: GRAPHBASIC-011
slug: bridges-capacity-threshold
version: 1.0.0
difficulty: Medium
topic_tags:
  - Graph Basics
  - Problem Solving
---

# Bridges With Capacity Threshold

## Problem Description

Each edge has capacity c. An edge is critical if removing it increases the number of connected components AND its capacity is below threshold T. Find all such edges.

## Examples

- Input: edges (0-1 cap1),(1-2 cap5),(2-0 cap1),(1-3 cap2), T=3
  - Output: (1,3)

## Constraints

n<=1e5, m<=2e5.

## Function Signatures

### Java
```java
public class Solution {
    public int[] bridgesCapacityThreshold(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def bridgesCapacityThreshold(arr: List[int]) -> List[int]:
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
    vector<int> bridgesCapacityThreshold(vector<int>& arr) {
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

Standard bridge DFS, then filter by capacity < T.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Bridges With Capacity Threshold'?**

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

A) Graph Basics
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Graph Basics techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
