---
unique_problem_id: sorting_013
display_id: SORTING-013
slug: closest-pair-sorted-circular
version: 1.0.0
difficulty: Medium
topic_tags:
  - Sorting
  - Problem Solving
---

# Closest Pair in Sorted Circular Array

## Problem Description

Given a sorted circular array, find pair with sum closest to target (wrap-around allowed).

## Examples

- Input: `[4,5,1,2,3], target=7`
  - Output: `(4,3)`

## Constraints

`2 <= n <= 2 * 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] closestPairSortedCircular(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def closestPairSortedCircular(arr: List[int]) -> List[int]:
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
    vector<int> closestPairSortedCircular(vector<int>& arr) {
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

Find pivot; use two-pointer circular.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Closest Pair in Sorted Circular Array'?**

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
