---
unique_problem_id: gametheory_008
display_id: GAMETHEORY-008
slug: kayles-on-graph
version: 1.0.0
difficulty: Hard
topic_tags:
  - Game Theory
  - Problem Solving
---

# Kayles on Graph

## Problem Description

Undirected graph. Move: choose a vertex, remove it and its neighbors. Player unable to move loses. Determine winner using Sprague-Grundy (connected components).

## Examples

- Input: path of 3 nodes
  - Output: `First`

## Constraints

n <= 100, m <= 300.

## Function Signatures

### Java
```java
public class Solution {
    public int[] kaylesOnGraph(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def kaylesOnGraph(arr: List[int]) -> List[int]:
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
    vector<int> kaylesOnGraph(vector<int>& arr) {
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

No hints available.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Kayles on Graph'?**

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

A) Game Theory
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Game Theory techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
