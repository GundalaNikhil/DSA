---
unique_problem_id: advgraph_003
display_id: ADVGRAPH-003
slug: k-shortest-loopless-paths
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Problem Solving
---

# K Shortest Paths (Loopless)

## Problem Description

Find the k shortest simple paths from s to t (length by edge weight) without cycles.

## Examples

- Input: graph 0-1 (1), 1-2 (1), 0-2 (3); k=2
  - Output: paths [0-1-2 length2, 0-2 length3]

## Constraints

n<=500, k<=50.

## Function Signatures

### Java
```java
public class Solution {
    public int[] kShortestLooplessPaths(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def kShortestLooplessPaths(arr: List[int]) -> List[int]:
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
    vector<int> kShortestLooplessPaths(vector<int>& arr) {
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

Yen’s algorithm over Dijkstra for spur paths.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'K Shortest Paths (Loopless)'?**

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
