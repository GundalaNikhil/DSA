---
unique_problem_id: segtree_001
display_id: SEGTREE-001
slug: range-sum-point-updates
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Segment Tree
  - Problem Solving
---

# Range Sum with Point Updates

## Problem Description

Support an array with operations: `update(i, val)` replace a[i], and `query(l, r)` sum over [l, r]. Return answers to queries.

## Examples

- Input: n=5, arr=[1,2,3,4,5]; ops: query(1,3), update(2,10), query(0,4)
  - Output: [9, 22]

## Constraints

`1 <= n, q <= 2 * 10^5`, values fit 64-bit.

## Function Signatures

### Java
```java
public class Solution {
    public int[] rangeSumPointUpdates(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def rangeSumPointUpdates(arr: List[int]) -> List[int]:
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
    vector<int> rangeSumPointUpdates(vector<int>& arr) {
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

No hints available.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Range Sum with Point Updates'?**

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
