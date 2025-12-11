---
unique_problem_id: bitwise_012
display_id: BITWISE-012
slug: distinct-subarray-xors
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - Problem Solving
---

# Distinct Subarray XORs

## Problem Description

Compute how many distinct XOR results appear among all subarrays.

## Examples

- Input: `a=[1,2,3]`
  - Output: `6`

## Constraints

`1 <= n <= 10^4`, `0 <= a[i] <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] distinctSubarrayXors(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def distinctSubarrayXors(arr: List[int]) -> List[int]:
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
    vector<int> distinctSubarrayXors(vector<int>& arr) {
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

Trie of prefix XORs; count unique XORs via set of results per prefix incremental.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Distinct Subarray XORs'?**

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
