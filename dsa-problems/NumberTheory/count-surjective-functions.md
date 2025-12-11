---
unique_problem_id: numbertheory_016
display_id: NUMBERTHEORY-016
slug: count-surjective-functions
version: 1.0.0
difficulty: Medium
topic_tags:
  - Number Theory
  - Problem Solving
---

# Count Surjective Functions

## Problem Description

Count surjective functions from an n-element set to a k-element set (n,k up to 30). Return result modulo `MOD`.

## Examples

- Input: `n=3, k=2`
  - Output: `6` (onto functions from 3 elements to 2)

## Constraints

`1 <= k <= n <= 30`, `MOD=10^9+7`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] countSurjectiveFunctions(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def countSurjectiveFunctions(arr: List[int]) -> List[int]:
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
    vector<int> countSurjectiveFunctions(vector<int>& arr) {
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

Inclusion-exclusion: k! * S(n,k) or sum (-1)^i C(k,i) (k-i)^n.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Count Surjective Functions'?**

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

A) Number Theory
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Number Theory techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
