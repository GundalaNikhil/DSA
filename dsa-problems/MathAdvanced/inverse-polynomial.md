---
unique_problem_id: mathadvanced_003
display_id: MATHADVANCED-003
slug: inverse-polynomial
version: 1.0.0
difficulty: Hard
topic_tags:
  - Advanced Math
  - Problem Solving
---

# Inverse Polynomial Mod x^n

## Problem Description

Given polynomial P(x) with P[0]!=0 modulo prime, compute Q(x) such that P*Q ≡ 1 mod x^n.

## Examples

- Input: P=[1,1] (1+x), n=3
  - Output: Q=[1,-1,1] (mod prime)

## Constraints

n up to 1e5.

## Function Signatures

### Java
```java
public class Solution {
    public int[] inversePolynomial(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def inversePolynomial(arr: List[int]) -> List[int]:
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
    vector<int> inversePolynomial(vector<int>& arr) {
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

Newton iteration with NTT.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Inverse Polynomial Mod x^n'?**

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
