---
unique_problem_id: heaps_015
display_id: HEAPS-015
slug: median-two-heaps-merge
version: 1.0.0
difficulty: Medium
topic_tags:
  - Heaps
  - Problem Solving
---

# Median of Two Heaps After Merge

## Problem Description

Two heaps (one max, one min) each contain some numbers. Merge them and report median without flattening all numbers.

## Examples

- Input: heap1 [1,3] (max-heap), heap2 [2,4] (min-heap)
  - Output: 2.5

## Constraints

total size <= 2 * 10^5.

## Function Signatures

### Java
```java
public class Solution {
    public int[] medianTwoHeapsMerge(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def medianTwoHeapsMerge(arr: List[int]) -> List[int]:
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
    vector<int> medianTwoHeapsMerge(vector<int>& arr) {
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

Transfer elements to balance counts; track medians.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Median of Two Heaps After Merge'?**

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

A) Heaps
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Heaps techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
