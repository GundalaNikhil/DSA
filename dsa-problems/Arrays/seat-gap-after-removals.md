---
unique_problem_id: arrays_015
display_id: ARRAYS-015
slug: seat-gap-after-removals
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Arrays
  - Simulation
  - Greedy
---

# Seat Gap After Removals

## Problem Description

Seats are sorted; remove seats at given indices (by position in array, not seat number). After removals, return max gap between remaining consecutive seats.

## Examples

### Example 1
- Input: seats = `[2, 5, 9, 10]`, remove indices = `[1]`
- Output: `7`
- Explanation: Remove seat at index 1 (seat number 5). Remaining seats: [2, 9, 10]. Gaps: 9-2=7, 10-9=1. Maximum gap is 7.

### Example 2
- Input: seats = `[1, 3, 7, 12, 20]`, remove indices = `[0, 3]`
- Output: `8`
- Explanation: Remove indices 0 (seat 1) and 3 (seat 12). Remaining: [3, 7, 20]. Gaps: 7-3=4, 20-7=13. Maximum gap is 13.

### Example 3
- Input: seats = `[5, 10, 15, 20, 25]`, remove indices = `[2]`
- Output: `10`
- Explanation: Remove index 2 (seat 15). Remaining: [5, 10, 20, 25]. Gaps: 5, 10, 5. Maximum gap is 10 (between 10 and 20).

### Example 4
- Input: seats = `[1, 2, 3, 4]`, remove indices = `[]`
- Output: `1`
- Explanation: No removals. All seats remain. All gaps are 1. Maximum is 1.

## Constraints

- `2 <= n <= 2 * 10^5` (number of seats)
- Seats array is sorted in ascending order
- Removal indices are valid (0 to n-1)
- `0 <= |removals| <= n-2` (must have at least 2 seats remaining)
- `1 <= seats[i] <= 10^9`
- Time limit: 2 seconds per test case

## Function Signatures

### Java
```java
public class Solution {
    public int[] seatGapAfterRemovals(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def seatGapAfterRemovals(arr: List[int]) -> List[int]:
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
    vector<int> seatGapAfterRemovals(vector<int>& arr) {
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

Use set of indices; iterate remaining to compute gaps.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Seat Gap After Removals'?**

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
