---
unique_problem_id: arrays_012
display_id: ARRAYS-012
slug: longest-zero-sum-even
version: 1.0.0
difficulty: Medium
topic_tags:
  - Arrays
  - Hash Map
  - Prefix Sum
---

# Longest Zero-Sum Even Length

## Problem Description

Find the maximum even length of a subarray with sum zero.

## Examples

### Example 1
- Input: `[1, -1, 3, -3, 2]`
- Output: `4`
- Explanation: Subarray [1, -1, 3, -3] from indices 0 to 3 has sum = 0 and length = 4 (even). This is the longest even-length zero-sum subarray.

### Example 2
- Input: `[2, -2, 4, -4, 1, -1]`
- Output: `6`
- Explanation: The entire array sums to 0 and has length 6 (even). This is the longest possible.

### Example 3
- Input: `[1, 2, 3, -3, -2, -1]`
- Output: `6`
- Explanation: The entire array: 1+2+3-3-2-1 = 0, length = 6 (even).

### Example 4
- Input: `[5, -5, 2, -2, 3]`
- Output: `4`
- Explanation: Two possible subarrays: [5, -5, 2, -2] (length 4) or [5, -5] (length 2) plus [2, -2] (length 2). The maximum even length is 4.

### Example 5
- Input: `[1, 2, 3]`
- Output: `0`
- Explanation: No subarray with zero sum exists. Return 0.

## Constraints

- `1 <= n <= 2 * 10^5` (array length)
- `-10^9 <= arr[i] <= 10^9` (array elements)
- Must find even-length subarray (length 2, 4, 6, etc.)
- If no zero-sum subarray with even length exists, return 0
- Time limit: 2 seconds per test case

## Function Signatures

### Java
```java
public class Solution {
    public int[] longestZeroSumEven(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def longestZeroSumEven(arr: List[int]) -> List[int]:
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
    vector<int> longestZeroSumEven(vector<int>& arr) {
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

Prefix sums with hashmap of first index for each parity bucket.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Longest Zero-Sum Even Length'?**

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
