---
unique_problem_id: queue_004
display_id: QUEUE-004
slug: hallway-interleave
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Queues
  - Problem Solving
---

# Hallway Interleave

## Problem Description

Given a queue with even length, interleave its first half with the second half (preserve relative order within each half).

## Examples

No examples provided.

## Constraints

`2 <= n <= 10^5`, `n` is even.

## Function Signatures

### Java
```java
public class Solution {
    public int[] hallwayInterleave(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def hallwayInterleave(arr: List[int]) -> List[int]:
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
    vector<int> hallwayInterleave(vector<int>& arr) {
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

Move first half into a stack or auxiliary queue, then alternately merge back.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Hallway Interleave'?**

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

A) Queues
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Queues techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
