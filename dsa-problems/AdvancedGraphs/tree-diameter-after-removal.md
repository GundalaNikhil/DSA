---
unique_problem_id: advgraph_014
display_id: ADVGRAPH-014
slug: tree-diameter-after-removal
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Problem Solving
---

# Tree Diameter With Edge Removal

## Problem Description

Given a tree, for each edge, compute the diameter of the graph if that edge is removed (two components). Return the maximum of these diameters.

## Examples

- Input: tree edges (0-1,1-2,1-3)
  - Output: 2

## Constraints

n<=2e5.

## Function Signatures

### Java
```java
public class Solution {
    public int[] treeDiameterAfterRemoval(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def treeDiameterAfterRemoval(arr: List[int]) -> List[int]:
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
    vector<int> treeDiameterAfterRemoval(vector<int>& arr) {
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

Precompute subtree heights and reroot; for each edge, diameter = max(diam(component1), diam(component2)).

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Tree Diameter With Edge Removal'?**

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

A) Advanced Graphs
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Advanced Graphs techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
