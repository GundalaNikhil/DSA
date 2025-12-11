---
unique_problem_id: arrays_014
display_id: ARRAYS-014
slug: boarding-order-fixed-ones
version: 1.0.0
difficulty: Medium
topic_tags:
  - Arrays
  - Problem Solving
---

# Boarding Order With Fixed Ones

## Problem Description

Array contains only 0s,1s,2s. All 1s are already in correct relative order and must not move. Sort the array (0s before 1s before 2s) while keeping 1s in place.

## Examples

- Input: `[2,1,0,2,0,1]`
  - Output: `[0,1,0,1,2,2]`

## Constraints

`1 <= n <= 2 * 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] boardingOrderFixedOnes(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def boardingOrderFixedOnes(arr: List[int]) -> List[int]:
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
    vector<int> boardingOrderFixedOnes(vector<int>& arr) {
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

Two-pass to fill 0s from left skipping 1s, then fill 2s from right skipping 1s.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Boarding Order With Fixed Ones'?**

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

A) Arrays
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Arrays techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
