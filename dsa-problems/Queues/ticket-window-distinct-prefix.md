---
unique_problem_id: queue_006
display_id: QUEUE-006
slug: ticket-window-distinct-prefix
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Queues
  - Problem Solving
---

# Ticket Window Distinct Prefix

## Problem Description

Given a stream of lowercase letters, after each arrival output the shortest prefix of the stream that ends at the current character and contains all distinct letters seen so far. If no such prefix exists (a letter missing), output `"#"`.

## Examples

No examples provided.

## Constraints

`1 <= len(stream) <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] ticketWindowDistinctPrefix(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def ticketWindowDistinctPrefix(arr: List[int]) -> List[int]:
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
    vector<int> ticketWindowDistinctPrefix(vector<int>& arr) {
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

Track first occurrence index of each character and the maximum of those indices among seen letters; output prefix length = current index - minIndex + 1 when all seen letters accounted for.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Ticket Window Distinct Prefix'?**

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
