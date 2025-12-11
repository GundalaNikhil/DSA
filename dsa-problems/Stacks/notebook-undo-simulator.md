---
unique_problem_id: stack_001
display_id: STACK-001
slug: notebook-undo-simulator
version: 1.0.0
difficulty: Easy
topic_tags:
  - Stacks
  - Problem Solving
---

# Notebook Undo Simulator

## Problem Description

Implement a simple stack that supports `PUSH x`, `POP`, and `TOP` commands for a text editor undo buffer. Return the top element after each command that is not `PUSH`.

## Examples

No examples provided.

## Constraints

`1 <= m <= 10^5` commands, `-10^9 <= x <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] notebookUndoSimulator(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def notebookUndoSimulator(arr: List[int]) -> List[int]:
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
    vector<int> notebookUndoSimulator(vector<int>& arr) {
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

Use an array-backed stack; check for empty before `POP`/`TOP`.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Notebook Undo Simulator'?**

A) O(n)
B) O(n log n)
C) O(n^2)
D) O(1)

**Correct Answer:** A

**Explanation:** The optimal solution can be achieved in linear time by processing the array in a single pass.

### Question 2
**Which data structure would be most suitable for this problem?**

A) Array/List
B) Hash Map
C) Tree
D) Graph

**Correct Answer:** A

**Explanation:** An array or list is the primary data structure needed for this problem.

### Question 3
**Which algorithmic paradigm does this problem primarily belong to?**

A) Stacks
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Stacks techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
