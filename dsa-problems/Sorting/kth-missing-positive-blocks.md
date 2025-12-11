---
unique_problem_id: sorting_002
display_id: SORTING-002
slug: kth-missing-positive-blocks
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Sorting
  - Problem Solving
---

# Kth Missing Positive with Blocks

## Problem Description

Sorted array of unique positives `arr`, and queries of form `(k, blockSize)` where missing numbers are counted in blocks of size blockSize (i.e., skip ahead by blockSize when counting missing). For each query, find the k-th missing number under that counting scheme.

## Examples

- Input: `arr=[2,3,7], query (k=3, block=2)`
  - Output: `9` (missing numbers counted as 1,4,5,6,8,9,... in blocks of 2)

## Constraints

`1 <= n <= 10^5`, `1 <= q <= 10^5`, `1 <= blockSize <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] kthMissingPositiveBlocks(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def kthMissingPositiveBlocks(arr: List[int]) -> List[int]:
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
    vector<int> kthMissingPositiveBlocks(vector<int>& arr) {
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

Precompute standard missing counts; adjust by block factor.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Kth Missing Positive with Blocks'?**

A) O(n)
B) O(n log n)
C) O(n^2)
D) O(1)

**Correct Answer:** A

**Explanation:** The optimal solution can be achieved in linear time by processing the array in a single pass.

### Question 2
**Which data structure would be most suitable for this problem?**

A) Array/List
B) Hash Map
C) Tree
D) Graph

**Correct Answer:** A

**Explanation:** An array or list is the primary data structure needed for this problem.

### Question 3
**Which algorithmic paradigm does this problem primarily belong to?**

A) Sorting
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Sorting techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
