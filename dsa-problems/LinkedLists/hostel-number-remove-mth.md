---
unique_problem_id: linkedlist_012
display_id: LINKEDLIST-012
slug: hostel-number-remove-mth
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Linked Lists
  - Problem Solving
---

# Hostel Number Remove Mth from Start

## Problem Description

Remove the M-th node from the start (1-indexed) and return head; if M > length, return original list.

## Examples

- Input: `9 -> 8 -> 7 -> 6`, `M = 2`
  - Output: `9 -> 7 -> 6`

## Constraints

`1 <= n <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] hostelNumberRemoveMth(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def hostelNumberRemoveMth(arr: List[int]) -> List[int]:
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
    vector<int> hostelNumberRemoveMth(vector<int>& arr) {
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

Handle head removal carefully; single pass with counter.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Hostel Number Remove Mth from Start'?**

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
