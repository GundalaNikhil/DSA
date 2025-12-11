---
unique_problem_id: arrays_003
display_id: ARRAYS-003
slug: shuttle-shift-blackout
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Arrays
  - Cyclic Rotation
  - Simulation
---

# Shuttle Shift With Blackout

## Problem Description

Rotate the array left by `k` but positions listed in `blackout` stay in place; only other positions rotate cyclically among themselves.

## Examples

### Example 1
- Input: `arr = [1, 2, 3, 4, 5]`, `k = 2`, `blackout = {1, 3}`
- Output: `[3, 2, 5, 4, 1]`
- Explanation: Positions 1 and 3 are locked (values 2 and 4 stay). Movable values [1, 3, 5] at positions [0, 2, 4] rotate left by 2: [5, 1, 3] becomes [3, 1, 5] at same positions. But we need left rotation by 2, so [1,3,5] → [5,1,3]. Final: [3, 2, 5, 4, 1].

### Example 2
- Input: `arr = [10, 20, 30, 40]`, `k = 1`, `blackout = {0, 3}`
- Output: `[10, 30, 20, 40]`
- Explanation: Positions 0 and 3 locked (values 10 and 40 stay). Movable: [20, 30] at positions [1, 2]. Rotate left by 1: [30, 20]. Result: [10, 30, 20, 40].

### Example 3
- Input: `arr = [5, 6, 7, 8, 9]`, `k = 0`, `blackout = {2}`
- Output: `[5, 6, 7, 8, 9]`
- Explanation: k=0 means no rotation. Array remains unchanged.

### Example 4
- Input: `arr = [1, 2, 3]`, `k = 5`, `blackout = {}`
- Output: `[3, 1, 2]`
- Explanation: No blackout positions. Rotate left by 5. Since 5 % 3 = 2, rotate left by 2: [1,2,3] → [3,1,2].

## Constraints

- `1 <= n <= 2 * 10^5` (array length)
- `0 <= k <= 10^9` (rotation amount)
- `0 <= |blackout| <= n` (number of locked positions)
- Blackout positions are valid indices (0 to n-1)
- `-10^9 <= arr[i] <= 10^9`
- Time limit: 2 seconds per test case

## Function Signatures

### Java
```java
public class Solution {
    public int[] shuttleShiftBlackout(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def shuttleShiftBlackout(arr: List[int]) -> List[int]:
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
    vector<int> shuttleShiftBlackout(vector<int>& arr) {
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

Extract movable elements, rotate them, then reinsert.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Shuttle Shift With Blackout'?**

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
