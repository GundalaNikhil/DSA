---
unique_problem_id: tree_001
display_id: TREE-001
slug: campus-directory-traversal
version: 1.0.0
difficulty: Easy
topic_tags:
  - Trees
  - Problem Solving
---

# Campus Directory Traversal

## Problem Description

Given a binary tree, return its preorder, inorder, and postorder traversals as three separate lists.

## Examples

- Input: Tree with preorder `[4, 2, 1, 3, 6]`, inorder `[1, 2, 3, 4, 6]`
  - Output: Preorder `[4,2,1,3,6]`, Inorder `[1,2,3,4,6]`, Postorder `[1,3,2,6,4]`

## Constraints

`1 <= n <= 10^5`, node values fit in 32-bit int.

## Function Signatures

### Java
```java
public class Solution {
    public int[] campusDirectoryTraversal(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def campusDirectoryTraversal(arr: List[int]) -> List[int]:
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
    vector<int> campusDirectoryTraversal(vector<int>& arr) {
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

Use recursion or explicit stacks; beware stack depth for skewed trees.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Campus Directory Traversal'?**

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

A) Trees
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Trees techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
