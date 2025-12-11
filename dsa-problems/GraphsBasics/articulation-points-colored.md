---
unique_problem_id: graphbasic_010
display_id: GRAPHBASIC-010
slug: articulation-points-colored
version: 1.0.0
difficulty: Medium
topic_tags:
  - Graph Basics
  - Problem Solving
---

# Articulation Points Under Edge Colors

## Problem Description

Undirected graph edges are colored red or blue. A node is a critical point if removing it disconnects some red component from some blue component (i.e., separates colors). Find all such critical nodes.

## Examples

- Input: edges (0-1 red),(1-2 blue),(2-0 red),(1-3 blue)
  - Output: {1}

## Constraints

n<=1e5, m<=2e5.

## Function Signatures

### Java
```java
public class Solution {
    public int[] articulationPointsColored(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def articulationPointsColored(arr: List[int]) -> List[int]:
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
    vector<int> articulationPointsColored(vector<int>& arr) {
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

Use DFS lowlink; track reachable colors in subtrees and ancestors.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Articulation Points Under Edge Colors'?**

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
