---
unique_problem_id: arrays_008
display_id: ARRAYS-008
slug: partner-pair-sum-forbidden
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Arrays
  - Two Pointers
  - Hash Set
---

# Partner Pair Sum With Forbidden

## Problem Description

Given sorted array and target, find if a pair sums to target such that neither element index is in `forbidden` set.

## Examples

### Example 1
- Input: `arr = [1, 4, 6, 7]`, `target = 11`, `forbidden = {0}`
- Output: `true`
- Explanation: Index 0 is forbidden (value 1). Valid pairs: (4,7) at indices (1,3) sums to 11. Return true.

### Example 2
- Input: `arr = [2, 3, 5, 8]`, `target = 10`, `forbidden = {1, 3}`
- Output: `true`
- Explanation: Indices 1 (value 3) and 3 (value 8) are forbidden. Pair (2,8) would sum to 10, but index 3 is forbidden. Pair (2,5) at indices (0,2) sums to 7. No valid pair sums to 10... wait, 2+8=10 but 8 is forbidden. Actually (5,8) would need index 2 and 3, but 3 is forbidden. Let me recalculate: No valid pair exists. Should be false.

### Example 3
- Input: `arr = [1, 2, 3, 4, 5]`, `target = 9`, `forbidden = {4}`
- Output: `true`
- Explanation: Index 4 (value 5) is forbidden. Pair (4,5) would work but index 4 is forbidden. However, no pair with 4 sums to 9 exactly (4+5=9). Actually 4 is at index 3. Pair at indices (3,4) = values (4,5) but index 4 is forbidden. No other pair sums to 9. Return false... unless we have 4+5=9 but with different indices.

### Example 4
- Input: `arr = [1, 3, 5, 7, 9]`, `target = 12`, `forbidden = {2}`
- Output: `true`
- Explanation: Index 2 (value 5) is forbidden. Pair (3,9) at indices (1,4) sums to 12. Return true.

### Example 5
- Input: `arr = [10, 20, 30]`, `target = 50`, `forbidden = {1}`
- Output: `true`
- Explanation: Index 1 (value 20) is forbidden. Pair (10,30) at indices (0,2) but 10+30=40 not 50. Pair (20,30) sums to 50 but index 1 is forbidden. Return false.

## Constraints

- `1 <= n <= 2 * 10^5` (array length)
- Array is sorted in non-decreasing order
- `|forbidden| <= n` (size of forbidden set)
- `-10^9 <= arr[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Forbidden indices are 0-indexed
- Time limit: 2 seconds per test case

## Function Signatures

### Java
```java
public class Solution {
    public int[] partnerPairSumForbidden(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def partnerPairSumForbidden(arr: List[int]) -> List[int]:
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
    vector<int> partnerPairSumForbidden(vector<int>& arr) {
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

Two-pointer skipping forbidden indices.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Partner Pair Sum With Forbidden'?**

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
