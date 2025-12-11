---
unique_problem_id: hashing_013
display_id: HASHING-013
slug: 2d-rolling-hash
version: 1.0.0
difficulty: Medium
topic_tags:
  - Hashing
  - Problem Solving
---

# 2D Rolling Hash for Matrix Match

## Problem Description

Given matrix `A` and smaller matrix `B`, determine if `B` appears in `A` as a submatrix using 2D rolling hash.

## Examples

- Input: A 3x3 with rows [1 2 3; 4 5 6; 7 8 9], B 2x2 [5 6; 8 9]
  - Output: true

## Constraints

`1 <= n,m <= 1000`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] 2dRollingHash(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def 2dRollingHash(arr: List[int]) -> List[int]:
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
    vector<int> 2dRollingHash(vector<int>& arr) {
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
**What is the space complexity of an efficient solution to '2D Rolling Hash for Matrix Match'?**

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

A) Hashing
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Hashing techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
