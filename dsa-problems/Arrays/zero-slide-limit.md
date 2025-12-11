---
unique_problem_id: arrays_006
display_id: ARRAYS-006
slug: zero-slide-limit
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Arrays
  - Two Pointers
  - In-Place Algorithm
---

# Zero Slide With Limit

## Problem Description

Move all zeros to the end but allow at most `m` swaps total; stop once swaps exceed `m`. Return resulting array.

## Examples

### Example 1
- Input: `[0, 4, 0, 5, 7]`, `m = 1`
- Output: `[4, 0, 0, 5, 7]`
- Explanation: Swap 0 and 4 (1 swap used). Cannot continue as we've used all m=1 swaps. Result: [4, 0, 0, 5, 7].

### Example 2
- Input: `[0, 0, 1, 2, 3]`, `m = 2`
- Output: `[1, 2, 0, 0, 3]`
- Explanation: Move 1 over first 0 (swap 1), move 2 over second 0 (swap 2). Used 2 swaps. Result: [1, 2, 0, 0, 3].

### Example 3
- Input: `[3, 0, 0, 0, 5]`, `m = 10`
- Output: `[3, 5, 0, 0, 0]`
- Explanation: Only need 1 swap to move 5 left. Even with m=10 available, we only need 1. Result: [3, 5, 0, 0, 0].

### Example 4
- Input: `[1, 2, 3, 4]`, `m = 5`
- Output: `[1, 2, 3, 4]`
- Explanation: No zeros to move. Array remains unchanged.

### Example 5
- Input: `[0, 0, 0]`, `m = 0`
- Output: `[0, 0, 0]`
- Explanation: No swaps allowed (m=0). Array remains unchanged.

## Constraints

- `1 <= n <= 2 * 10^5` (array length)
- `0 <= m <= 10^9` (maximum swaps allowed)
- Array contains integers (including zeros)
- `-10^9 <= arr[i] <= 10^9`
- Stop moving zeros once m swaps are used
- Time limit: 2 seconds per test case

## Function Signatures

### Java
```java
public class Solution {
    public int[] zeroSlideLimit(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def zeroSlideLimit(arr: List[int]) -> List[int]:
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
    vector<int> zeroSlideLimit(vector<int>& arr) {
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

Use write pointer; count swaps when writing non-zero over zero.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Zero Slide With Limit'?**

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
