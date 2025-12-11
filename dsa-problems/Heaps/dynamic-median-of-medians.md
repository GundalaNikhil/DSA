---
unique_problem_id: heaps_009
display_id: HEAPS-009
slug: dynamic-median-of-medians
version: 1.0.0
difficulty: Medium
topic_tags:
  - Heaps
  - Problem Solving
---

# Dynamic Median of Medians

## Problem Description

Maintain medians of disjoint groups; queries ask for median of current group medians after inserts and merges of groups.

## Examples

- Input: create group A with [1,3], group B with [2]; merge A,B; query median-of-medians
  - Output: 2

## Constraints

groups <= 10^5.

## Function Signatures

### Java
```java
public class Solution {
    public int[] dynamicMedianOfMedians(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def dynamicMedianOfMedians(arr: List[int]) -> List[int]:
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
    vector<int> dynamicMedianOfMedians(vector<int>& arr) {
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

Heaps per group; global heap of medians.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Dynamic Median of Medians'?**

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

A) Heaps
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Heaps techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
