---
unique_problem_id: treedp_001
display_id: TREEDP-001
slug: lca-binary-lifting
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Tree DP
  - Problem Solving
---

# Lowest Common Ancestor (Binary Lifting)

## Problem Description

Preprocess rooted tree for O(log n) LCA queries.

## Examples

- Input: tree 1-2,1-3; query LCA(2,3)
  - Output: 1

## Constraints

n<=2e5, q<=2e5.

## Function Signatures

### Java
```java
public class Solution {
    public int[] lcaBinaryLifting(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def lcaBinaryLifting(arr: List[int]) -> List[int]:
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
    vector<int> lcaBinaryLifting(vector<int>& arr) {
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
**What is the optimal time complexity for solving 'Lowest Common Ancestor (Binary Lifting)'?**

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
