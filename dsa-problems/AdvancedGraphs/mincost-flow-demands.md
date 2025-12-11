---
unique_problem_id: advgraph_012
display_id: ADVGRAPH-012
slug: mincost-flow-demands
version: 1.0.0
difficulty: Hard
topic_tags:
  - Advanced Graphs
  - Problem Solving
---

# Minimum-Cost Flow With Demands

## Problem Description

Some edges have lower/upper bounds and costs. Nodes have supply/demand. Determine feasible flow and minimum cost if feasible.

## Examples

- Input: demands: s supply 5, t demand 5; edge s->t lower 2 upper 5 cost 1
  - Output: feasible, cost 5

## Constraints

n<=500, m<=2000.

## Function Signatures

### Java
```java
public class Solution {
    public int[] mincostFlowDemands(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def mincostFlowDemands(arr: List[int]) -> List[int]:
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
    vector<int> mincostFlowDemands(vector<int>& arr) {
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

Convert to circulation with super source/sink; use potentials + SPFA/Dijkstra for min cost flow.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Minimum-Cost Flow With Demands'?**

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
