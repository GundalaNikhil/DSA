---
unique_problem_id: greedy_001
display_id: GREEDY-001
slug: campus-shuttle-driver-swaps
version: 1.0.0
difficulty: Easy
topic_tags:
  - Greedy
  - Problem Solving
---

# Campus Shuttle Driver Swaps

## Problem Description

You have `n` shuttle trips, each needing one driver. Two drivers A and B have availability intervals `[start, end]`. Assign trips to minimize the number of driver switches (A->B or B->A) while covering all trips. Return the minimum switches or -1 if impossible.

## Examples

- Input: trips `[1-3, 4-6, 7-9]`, A available `[1-8]`, B `[3-10]`
  - Output: `1`

## Constraints

`1 <= n <= 10^5`, times are integers, trips are non-overlapping.

## Function Signatures

### Java
```java
public class Solution {
    public int[] campusShuttleDriverSwaps(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def campusShuttleDriverSwaps(arr: List[int]) -> List[int]:
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
    vector<int> campusShuttleDriverSwaps(vector<int>& arr) {
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

Greedily extend the current driver as far as possible; switch only when a gap cannot be covered.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Campus Shuttle Driver Swaps'?**

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
