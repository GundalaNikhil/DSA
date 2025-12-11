---
unique_problem_id: advgraph_004
display_id: ADVGRAPH-004
slug: apsp-with-negatives
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Graphs
  - Problem Solving
---

# All-Pairs Shortest Path With Negative Edges

## Problem Description

Given weighted directed graph (no negative cycles), compute all-pairs shortest paths.

## Examples

- Input: n=3, edges (0,1,2),(1,2,-1),(0,2,4)
  - Output: dist[0][2]=1

## Constraints

n<=2000, m<=5000.

## Function Signatures

### Java
```java
public class Solution {
    public int[] apspWithNegatives(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def apspWithNegatives(arr: List[int]) -> List[int]:
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
    vector<int> apspWithNegatives(vector<int>& arr) {
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

Johnson’s algorithm (Bellman-Ford + Dijkstra).

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'All-Pairs Shortest Path With Negative Edges'?**

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
