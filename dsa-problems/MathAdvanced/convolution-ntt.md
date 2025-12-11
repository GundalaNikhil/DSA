---
unique_problem_id: mathadvanced_002
display_id: MATHADVANCED-002
slug: convolution-ntt
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Math
  - Problem Solving
---

# Convolution Mod Prime Using NTT

## Problem Description

Perform convolution under a suitable NTT prime (e.g., 998244353). Handle padding to power of two.

## Examples

- Input: A=[1,1,1], B=[1,2]
  - Output: [1,3,3,2]

## Constraints

length up to 1e5.

## Function Signatures

### Java
```java
public class Solution {
    public int[] convolutionNtt(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def convolutionNtt(arr: List[int]) -> List[int]:
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
    vector<int> convolutionNtt(vector<int>& arr) {
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
**What is the space complexity of an efficient solution to 'Convolution Mod Prime Using NTT'?**

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
