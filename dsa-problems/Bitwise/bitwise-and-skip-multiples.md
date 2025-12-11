---
unique_problem_id: bitwise_003
display_id: BITWISE-003
slug: bitwise-and-skip-multiples
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - Problem Solving
---

# Bitwise AND Skipping Multiples

## Problem Description

Given `L, R, m`, compute the bitwise AND of all numbers in `[L,R]` that are NOT divisible by `m`. If no numbers remain, return `-1`.

## Examples

- Input: `L=10, R=15, m=3`
  - Output: `8` (numbers 10,11,13,14,15 AND to 8)

## Constraints

`0 <= L <= R <= 10^12`, `1 <= m <= 10^6`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] bitwiseAndSkipMultiples(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def bitwiseAndSkipMultiples(arr: List[int]) -> List[int]:
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
    vector<int> bitwiseAndSkipMultiples(vector<int>& arr) {
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

Identify contiguous spans of allowed numbers; AND short-circuits to 0 if spans cross powers of two boundaries.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Bitwise AND Skipping Multiples'?**

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
