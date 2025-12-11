---
unique_problem_id: queue_002
display_id: QUEUE-002
slug: circular-shuttle-buffer-overwrite
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Queues
  - Problem Solving
---

# Circular Shuttle Buffer with Overwrite

## Problem Description

Design a circular queue with fixed capacity `k` supporting enqueue, dequeue, front, rear, isEmpty/isFull, and `ENQ_OVR x` that overwrites the oldest element when full (returns the overwritten value). Normal `ENQ` should fail when full.

## Examples

No examples provided.

## Constraints

`1 <= k <= 10^5`, operations `<= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] circularShuttleBufferOverwrite(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def circularShuttleBufferOverwrite(arr: List[int]) -> List[int]:
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
    vector<int> circularShuttleBufferOverwrite(vector<int>& arr) {
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

Maintain head/tail indices modulo `k` and size; `ENQ_OVR` advances head when overwriting.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Circular Shuttle Buffer with Overwrite'?**

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
