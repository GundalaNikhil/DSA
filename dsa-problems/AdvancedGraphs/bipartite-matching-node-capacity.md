---
unique_problem_id: advgraph_009
display_id: ADVGRAPH-009
slug: bipartite-matching-node-capacity
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Problem Solving
---

# Maximum Matching with Node Capacities

## Problem Description

Bipartite graph (U,V,E), each node u in U has capacity capU[u] (max edges it can match), each v in V has capV[v]. Find a maximum feasible matching respecting capacities.

## Examples

- Input: U={0,1}, V={2,3}, capsU=[1,2], capsV=[1,1], edges (0,2),(1,2),(1,3)
  - Output: size 3 possible? caps limit -> matching size 2

## Constraints

|U|+|V| <= 1e5, m<=2e5.

## Function Signatures

### Java
```java
public class Solution {
    public int[] bipartiteMatchingNodeCapacity(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def bipartiteMatchingNodeCapacity(arr: List[int]) -> List[int]:
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
    vector<int> bipartiteMatchingNodeCapacity(vector<int>& arr) {
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

Convert to flow network with node splitting and run Dinic.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Maximum Matching with Node Capacities'?**

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
