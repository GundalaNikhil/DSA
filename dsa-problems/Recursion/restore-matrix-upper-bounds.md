---
unique_problem_id: recursion_010
display_id: RECURSION-010
slug: restore-matrix-upper-bounds
version: 1.0.0
difficulty: Medium
topic_tags:
  - Recursion
  - Problem Solving
---

# Restore Matrix With Upper Bounds

## Problem Description

Given row sums, column sums, and a matrix of per-cell upper bounds `u[i][j]`, construct any non-negative integer matrix satisfying all sums and bounds, or return empty if impossible.

## Examples

- Input: rowSums `[3,4]`, colSums `[4,3]`, bounds `[[2,3],[3,4]]`
  - Output: `[[2,1],[2,2]]`

## Constraints

`1 <= r,c <= 6`, sums up to `20`, `0 <= u[i][j] <= 20`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] restoreMatrixUpperBounds(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def restoreMatrixUpperBounds(arr: List[int]) -> List[int]:
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
    vector<int> restoreMatrixUpperBounds(vector<int>& arr) {
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
**What is the space complexity of an efficient solution to 'Restore Matrix With Upper Bounds'?**

A) O(1)
B) O(n)
C) O(n log n)
D) O(n^2)

**Correct Answer:** B

**Explanation:** The solution requires additional space proportional to the input size for preprocessing or storage.

### Question 2
**What technique is most applicable to solve this problem efficiently?**

A) Two pointers
B) Divide and conquer
C) Dynamic programming
D) Greedy approach

**Correct Answer:** A

**Explanation:** The problem can be efficiently solved using the two-pointer technique.

### Question 3
**Which algorithmic paradigm does this problem primarily belong to?**

A) Recursion
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Recursion techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
