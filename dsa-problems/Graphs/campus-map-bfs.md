---
unique_problem_id: graph_001
display_id: GRAPH-001
slug: campus-map-bfs
version: 1.0.0
difficulty: Easy
topic_tags:
  - Graphs
  - Problem Solving
---

# Campus Map BFS

## Problem Description

Given an undirected unweighted graph (n nodes, adjacency list), perform BFS starting from node 0 and return visit order.

## Examples

- Input: `n=4`, edges `[(0,1),(0,2),(1,3)]`
  - Output: `[0,1,2,3]`

## Constraints

`1 <= n <= 10^5`, `0 <= edges <= 2*10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] campusMapBfs(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def campusMapBfs(arr: List[int]) -> List[int]:
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
    vector<int> campusMapBfs(vector<int>& arr) {
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

Use a queue and visited array.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Campus Map BFS'?**

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

A) Graphs
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Graphs techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
