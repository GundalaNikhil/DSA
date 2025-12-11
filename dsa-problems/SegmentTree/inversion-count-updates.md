---
unique_problem_id: segtree_004
display_id: SEGTREE-004
slug: inversion-count-updates
version: 1.0.0
difficulty: Medium
topic_tags:
  - Segment Tree
  - Problem Solving
---

# Inversion Count Updates

## Problem Description

Array of size n <= 2e5 with point updates. After each update, output current inversion count.

## Examples

- Input: arr=[3,1,2]; update pos1->4
  - Output: initial 2, after update 2

## Constraints

Values within 32-bit; coordinate compress.

## Function Signatures

### Java
```java
public class Solution {
    public int[] inversionCountUpdates(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def inversionCountUpdates(arr: List[int]) -> List[int]:
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
    vector<int> inversionCountUpdates(vector<int>& arr) {
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

Fenwick for counts; segment tree over value domain.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Inversion Count Updates'?**

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

A) Segment Tree
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Segment Tree techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
