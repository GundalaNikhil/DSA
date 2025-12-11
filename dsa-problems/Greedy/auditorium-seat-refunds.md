---
unique_problem_id: greedy_013
display_id: GREEDY-013
slug: auditorium-seat-refunds
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Greedy
  - Problem Solving
---

# Auditorium Seat Refunds

## Problem Description

Seats sold in rows; refund requests list seat IDs. Process refunds to minimize the highest occupied row index after all refunds (lower rows fill first). Return that highest occupied row.

## Examples

- Input: `rows=3`, requests remove seats in row order `[3,3,2]`
  - Output: `1`

## Constraints

`1 <= rows <= 10^5`, initial occupancy full, requests `<= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] auditoriumSeatRefunds(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def auditoriumSeatRefunds(arr: List[int]) -> List[int]:
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
    vector<int> auditoriumSeatRefunds(vector<int>& arr) {
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

Use a max-heap of currently occupied rows; pop when emptied.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Auditorium Seat Refunds'?**

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

A) Greedy
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Greedy techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
