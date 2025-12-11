---
unique_problem_id: mathadvanced_011
display_id: MATHADVANCED-011
slug: minimal-polynomial-matrix
version: 1.0.0
difficulty: Hard
topic_tags:
  - Advanced Math
  - Problem Solving
---

# Minimal Polynomial of Matrix (Krylov)

## Problem Description

Compute minimal polynomial of an n x n matrix using Krylov sequence and Berlekamp-Massey on vector sequence.

## Examples

- Input: 2x2 matrix [[1,1],[0,1]]
  - Output: minimal polynomial (x-1)^2

## Constraints

n<=200.

## Function Signatures

### Java
```java
public class Solution {
    public int[] minimalPolynomialMatrix(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def minimalPolynomialMatrix(arr: List[int]) -> List[int]:
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
    vector<int> minimalPolynomialMatrix(vector<int>& arr) {
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
**What is the space complexity of an efficient solution to 'Minimal Polynomial of Matrix (Krylov)'?**

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

A) Advanced Math
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Advanced Math techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
