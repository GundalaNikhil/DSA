---
unique_problem_id: linkedlist_013
display_id: LINKEDLIST-013
slug: shuttle-ticket-rotate-blocks
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Linked Lists
  - Problem Solving
---

# Shuttle Ticket Rotate by Blocks

## Problem Description

Rotate the list to the right by `k` places but only within blocks of size `b` (last block may be smaller). Concatenate rotated blocks.

## Examples

- Input: `1 -> 2 -> 3 -> 4 -> 5 -> 6`, `b=3`, `k=1`
  - Output: `3 -> 1 -> 2 -> 6 -> 4 -> 5`

## Constraints

`0 <= n <= 10^5`, `1 <= b <= n`, `0 <= k <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] shuttleTicketRotateBlocks(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def shuttleTicketRotateBlocks(arr: List[int]) -> List[int]:
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
    vector<int> shuttleTicketRotateBlocks(vector<int>& arr) {
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

For each block, compute `k % blockSize` and rotate that block.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Shuttle Ticket Rotate by Blocks'?**

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
