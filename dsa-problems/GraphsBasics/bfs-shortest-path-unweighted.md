---
unique_problem_id: graphbasic_001
display_id: GRAPHBASIC-001
slug: bfs-shortest-path-unweighted
version: 1.0.0
difficulty: Easy
topic_tags:
  - Graph Basics
  - Problem Solving
---

# BFS Shortest Path Unweighted

## Problem Description

Given unweighted undirected graph, compute shortest path length from s to all nodes.

## Examples

- Input: n=4, edges [(0,1),(1,2),(0,3)]
  - Output: dist from 0 = [0,1,2,1]

## Constraints

n<=1e5, m<=2e5.

## Function Signatures

### Java
```java
public class Solution {
    public int[] bfsShortestPathUnweighted(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def bfsShortestPathUnweighted(arr: List[int]) -> List[int]:
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
    vector<int> bfsShortestPathUnweighted(vector<int>& arr) {
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
**What is the optimal time complexity for solving 'BFS Shortest Path Unweighted'?**

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

A) Graph Basics
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Graph Basics techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
