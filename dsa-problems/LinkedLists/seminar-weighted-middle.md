---
unique_problem_id: linkedlist_007
display_id: LINKEDLIST-007
slug: seminar-weighted-middle
version: 1.0.0
difficulty: Easy
topic_tags:
  - Linked Lists
  - Problem Solving
---

# Seminar Weighted Middle Seat

## Problem Description

Each node has an integer weight. Return the node where cumulative weight from head to that node is at least half of total weight but minimal index (weighted median node).

## Examples

- Input: `weights 2 -> 1 -> 3 -> 4`
  - Output: node with weight 3 (cumulative 6 of total 10)

## Constraints

`1 <= n <= 10^5`, weights positive.

## Function Signatures

### Java
```java
public class Solution {
    public int[] seminarWeightedMiddle(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def seminarWeightedMiddle(arr: List[int]) -> List[int]:
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
    vector<int> seminarWeightedMiddle(vector<int>& arr) {
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
**What is the optimal time complexity for solving 'Seminar Weighted Middle Seat'?**

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

A) Linked Lists
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Linked Lists techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
