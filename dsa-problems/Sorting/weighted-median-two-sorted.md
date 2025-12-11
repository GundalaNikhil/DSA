---
unique_problem_id: sorting_009
display_id: SORTING-009
slug: weighted-median-two-sorted
version: 1.0.0
difficulty: Medium
topic_tags:
  - Sorting
  - Problem Solving
---

# Weighted Median of Two Sorted Arrays

## Problem Description

Two sorted arrays A and B come with weights wA and wB (positive integers). Treat each element of A as repeated wA times and each of B as repeated wB times. Return the median of the multiset without expanding it.

## Examples

- Input: `A=[1,3], B=[2,7], wA=1, wB=2`
  - Expanded multiset (conceptual): `[1, 3, 2, 2, 7, 7]` → sorted: `[1, 2, 2, 3, 7, 7]`
  - Total count = 6 (even), median = average of 3rd and 4th = (2+3)/2 = 2.5
  - Output: `2.5`

## Constraints

`1 <= n,m <= 10^5`, `1 <= wA,wB <= 10^6`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] weightedMedianTwoSorted(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def weightedMedianTwoSorted(arr: List[int]) -> List[int]:
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
    vector<int> weightedMedianTwoSorted(vector<int>& arr) {
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

Binary search on value space using prefix counts; similar to kth order statistic on weighted arrays.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Weighted Median of Two Sorted Arrays'?**

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

A) Sorting
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Sorting techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
