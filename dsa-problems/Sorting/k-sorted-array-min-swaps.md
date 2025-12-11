---
unique_problem_id: sorting_006
display_id: SORTING-006
slug: k-sorted-array-min-swaps
version: 1.0.0
difficulty: Medium
topic_tags:
  - Sorting
  - Problem Solving
---

# K-Sorted Array Minimum Swaps

## Problem Description

An array is k-sorted if every element is at most k positions away from its sorted position. Given such an array and k, find min swaps to fully sort it.

## Examples

- Input: `[3,1,2], k=2`
  - Output: `2`

## Constraints

`1 <= n <= 2 * 10^5`, `0 <= k < n`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] kSortedArrayMinSwaps(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def kSortedArrayMinSwaps(arr: List[int]) -> List[int]:
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
    vector<int> kSortedArrayMinSwaps(vector<int>& arr) {
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

Use indexed positions after sorting; count cycles within windows.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'K-Sorted Array Minimum Swaps'?**

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
