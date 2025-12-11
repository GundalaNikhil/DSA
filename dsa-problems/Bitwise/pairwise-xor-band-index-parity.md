---
unique_problem_id: bitwise_004
display_id: BITWISE-004
slug: pairwise-xor-band-index-parity
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - Problem Solving
---

# Pairwise XOR in Band With Index Parity

## Problem Description

Given array `a` and integers `L, U`, count pairs `(i,j)` with `i<j` and `(i+j)` even such that `L <= (a[i] XOR a[j]) <= U`.

## Examples

- Input: `a=[2,3,1,7], L=1, U=4`
  - Output: `3` (pairs (0,1):1, (0,2):3, (1,3):4)

## Constraints

`1 <= n <= 10^5`, `0 <= a[i] <= 10^9`, `0 <= L <= U <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] pairwiseXorBandIndexParity(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def pairwiseXorBandIndexParity(arr: List[int]) -> List[int]:
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
    vector<int> pairwiseXorBandIndexParity(vector<int>& arr) {
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

Maintain two separate bitwise tries (even-sum parity vs odd-sum parity index pairs) as you sweep; query counts in range [L,U] using two bound queries.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Pairwise XOR in Band With Index Parity'?**

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

A) Bitwise
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Bitwise techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
