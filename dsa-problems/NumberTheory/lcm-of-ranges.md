---
unique_problem_id: numbertheory_007
display_id: NUMBERTHEORY-007
slug: lcm-of-ranges
version: 1.0.0
difficulty: Medium
topic_tags:
  - Number Theory
  - Problem Solving
---

# LCM of Ranges

## Problem Description

Given array `a`, for each query `[l,r]` (small length <= 20), compute `lcm(a[l..r])` modulo `MOD`.

## Examples

- Input: `a=[2,6,3], query [0,1], MOD=1000000007`
  - Output: `6`

## Constraints

`1 <= n <= 2 * 10^5`, `1 <= a[i], MOD <= 10^9+7`, `r-l <= 20`, `1 <= q <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] lcmOfRanges(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def lcmOfRanges(arr: List[int]) -> List[int]:
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
    vector<int> lcmOfRanges(vector<int>& arr) {
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

Prime-factorize on the fly for short ranges; track max exponents.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'LCM of Ranges'?**

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
