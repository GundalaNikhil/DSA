---
unique_problem_id: arrays_001
display_id: ARRAYS-001
slug: snack-restock-snapshot
version: 1.0.0
difficulty: Easy
topic_tags:
  - Arrays
  - Prefix Sum
  - Math
---

# Snack Restock Snapshot

## Problem Description

Given daily deliveries `arr[i]`, output prefix averages rounded down for each day.

## Examples

### Example 1
- Input: `[4, 6, 6, 0]`
- Output: `[4, 5, 5, 4]`
- Explanation: Day 0: avg(4) = 4. Day 1: avg(4,6) = 10/2 = 5. Day 2: avg(4,6,6) = 16/3 = 5. Day 3: avg(4,6,6,0) = 16/4 = 4.

### Example 2
- Input: `[10, 20, 30]`
- Output: `[10, 15, 20]`
- Explanation: Day 0: 10/1 = 10. Day 1: 30/2 = 15. Day 2: 60/3 = 20.

### Example 3
- Input: `[7, 7, 7, 7]`
- Output: `[7, 7, 7, 7]`
- Explanation: All values are 7, so average is always 7.

### Example 4
- Input: `[1]`
- Output: `[1]`
- Explanation: Single day with delivery of 1. Average is 1.

### Example 5
- Input: `[0, 0, 0, 10]`
- Output: `[0, 0, 0, 2]`
- Explanation: Day 0-2: avg is 0. Day 3: 10/4 = 2 (rounded down).

## Constraints

- `1 <= n <= 10^5` (number of days)
- `0 <= arr[i] <= 10^6` (daily deliveries)
- Averages are rounded down (floor division)
- Time limit: 2 seconds per test case

## Function Signatures

### Java
```java
public class Solution {
    public int[] snackRestockSnapshot(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def snackRestockSnapshot(arr: List[int]) -> List[int]:
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
    vector<int> snackRestockSnapshot(vector<int>& arr) {
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

Maintain running sum; avg = sum//(i+1).

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Snack Restock Snapshot'?**

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

A) Arrays
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Arrays techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
