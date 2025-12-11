---
unique_problem_id: graph_004
display_id: GRAPH-004
slug: seminar-bipartite-check-locked
version: 1.0.0
difficulty: Medium
topic_tags:
  - Graphs
  - Problem Solving
---

# Seminar Bipartite Check with Locked Nodes

## Problem Description

Some nodes are pre-colored either group A or group B and cannot change. Determine if the undirected graph can be colored to satisfy bipartite constraints while respecting locked nodes.

## Examples

- Input: `n=4`, edges `[(0,1),(1,2),(2,3),(3,0)]`, locked `[1,0,2,0]`
  - Output: `true`

## Constraints

`1 <= n <= 10^5`, locked array length n with values {0=unlocked,1=force A,2=force B}.

## Function Signatures

### Java
```java
public class Solution {
    public int[] seminarBipartiteCheckLocked(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def seminarBipartiteCheckLocked(arr: List[int]) -> List[int]:
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
    vector<int> seminarBipartiteCheckLocked(vector<int>& arr) {
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

BFS/DFS coloring; if a locked node conflicts with its forced color, fail early.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Seminar Bipartite Check with Locked Nodes'?**

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
