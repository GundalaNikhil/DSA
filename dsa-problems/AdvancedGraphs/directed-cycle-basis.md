---
unique_problem_id: advgraph_015
display_id: ADVGRAPH-015
slug: directed-cycle-basis
version: 1.0.0
difficulty: Hard
topic_tags:
  - Advanced Graphs
  - Problem Solving
---

# Directed Cycle Basis

## Problem Description

Given a directed graph, find a basis of simple cycles (over GF(2) incidence) of minimal size (m - n + c). Output the cycles.

## Examples

- Input: edges (0->1,1->2,2->0,1->3,3->1)
  - Output: cycles [0-1-2-0,1-3-1]

## Constraints

n<=500, m<=2000.

## Function Signatures

### Java
```java
public class Solution {
    public int[] directedCycleBasis(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def directedCycleBasis(arr: List[int]) -> List[int]:
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
    vector<int> directedCycleBasis(vector<int>& arr) {
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

Build spanning forest; add back edges to recover cycles via parent pointers.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Directed Cycle Basis'?**

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
