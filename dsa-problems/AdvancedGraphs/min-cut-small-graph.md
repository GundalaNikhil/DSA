---
unique_problem_id: advgraph_001
display_id: ADVGRAPH-001
slug: min-cut-small-graph
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Problem Solving
---

# Minimum Cut on Small Graph

## Problem Description

Given an undirected weighted graph with n<=200 and m<=2000, compute the global minimum cut value.

## Examples

- Input: n=4, edges [(0,1,1),(1,2,2),(2,3,1),(0,3,2)]
  - Output: 3

## Constraints

No constraints specified.

## Function Signatures

### Java
```java
public class Solution {
    public int[] minCutSmallGraph(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def minCutSmallGraph(arr: List[int]) -> List[int]:
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
    vector<int> minCutSmallGraph(vector<int>& arr) {
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

Use Stoer-Wagner algorithm.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Minimum Cut on Small Graph'?**

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
