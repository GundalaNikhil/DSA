---
unique_problem_id: graph_018
display_id: GRAPH-018
slug: robotics-weighted-reachability
version: 1.0.0
difficulty: Medium
topic_tags:
  - Graphs
  - Problem Solving
---

# Robotics Weighted Reachability

## Problem Description

Given a weighted undirected graph and threshold `T`, count how many nodes are reachable from node 0 using only edges with weight <= T.

## Examples

- Input: `n=5`, edges `[(0,1,3),(1,2,7),(0,3,2),(3,4,5)]`, `T=4`
  - Output: `3` (nodes 0,1,3)

## Constraints

`1 <= n <= 10^5`, `1 <= edges <= 2*10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] roboticsWeightedReachability(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def roboticsWeightedReachability(arr: List[int]) -> List[int]:
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
    vector<int> roboticsWeightedReachability(vector<int>& arr) {
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

BFS/DFS on filtered edges; or sort edges and union-find all with weight<=T then count component size of node 0.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Robotics Weighted Reachability'?**

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
