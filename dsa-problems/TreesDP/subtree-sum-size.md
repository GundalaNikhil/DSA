---
unique_problem_id: treedp_003
display_id: TREEDP-003
slug: subtree-sum-size
version: 1.0.0
difficulty: Easy
topic_tags:
  - Tree DP
  - Problem Solving
---

# Subtree Sum and Size

## Problem Description

For each node, compute sum and size of its subtree.

## Examples

- Input: tree 1-2,1-3, values [1,2,3]
  - Output: subtree sums [6,2,3]

## Constraints

n<=2e5, values |a[i]|<=1e9.

## Function Signatures

### Java
```java
public class Solution {
    public int[] subtreeSumSize(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def subtreeSumSize(arr: List[int]) -> List[int]:
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
    vector<int> subtreeSumSize(vector<int>& arr) {
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
**What is the optimal time complexity for solving 'Subtree Sum and Size'?**

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

A) Tree DP
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Tree DP techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
