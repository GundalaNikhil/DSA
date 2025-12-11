---
unique_problem_id: advsegtree_010
display_id: ADVSEGTREE-010
slug: rmq-dynamic-array
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Segment Tree
  - Problem Solving
---

# Range Minimum Query on Dynamic Array

## Problem Description

Support insert at end, delete from end, and RMQ on current array.

## Examples

- Input: push 3, push 1, min(0,1), pop, min(0,0)
  - Output: [1,3]

## Constraints

`1 <= ops <= 2 * 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] rmqDynamicArray(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def rmqDynamicArray(arr: List[int]) -> List[int]:
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
    vector<int> rmqDynamicArray(vector<int>& arr) {
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

Segment tree over max size; maintain size pointer.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Range Minimum Query on Dynamic Array'?**

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

A) Advanced Segment Tree
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Advanced Segment Tree techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
