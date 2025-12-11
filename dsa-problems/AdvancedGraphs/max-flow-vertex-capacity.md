---
unique_problem_id: advgraph_002
display_id: ADVGRAPH-002
slug: max-flow-vertex-capacity
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Problem Solving
---

# Max Flow With Vertex Capacities

## Problem Description

Directed graph with edge capacities and vertex capacities. Compute max s-t flow respecting vertex limits.

## Examples

- Input: vertices 0..3, s=0, t=3, vertex caps [inf,3,2,inf], edges (0,1,3),(1,2,2),(2,3,3)
  - Output: 2

## Constraints

n<=2000, m<=5000.

## Function Signatures

### Java
```java
public class Solution {
    public int[] maxFlowVertexCapacity(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def maxFlowVertexCapacity(arr: List[int]) -> List[int]:
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
    vector<int> maxFlowVertexCapacity(vector<int>& arr) {
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

Split each vertex into in/out with an edge of vertex capacity; run Dinic/Edmonds-Karp.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Max Flow With Vertex Capacities'?**

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
