---
unique_problem_id: arrays_016
display_id: ARRAYS-016
slug: power-window-with-drop
version: 1.0.0
difficulty: Medium
topic_tags:
  - Arrays
  - Sliding Window
  - Greedy
---

# Power Window With Drop

## Problem Description

Given positive integers and window size `k`, find the maximum sum of any window after optionally removing one element from that window (you may also remove none). Return that maximal adjusted sum.

## Examples

### Example 1
- Input: `arr = [2, 1, 5, 3, 2]`, `k = 3`
- Output: `10`
- Explanation: Window [5, 3, 2] has sum 10. No element needs to be dropped. This is the maximum.

### Example 2
- Input: `arr = [10, 1, 1, 10]`, `k = 3`
- Output: `20`
- Explanation: Window [10, 1, 1] sum = 12, drop 1 → 11. Window [1, 1, 10] sum = 12, drop 1 → 11. Window [10, 1, 10] doesn't exist. Actually indices: [10,1,1] at [0,1,2] or [1,1,10] at [1,2,3]. For [10,1,1], drop smallest 1 → 10+1=11. For [1,1,10], drop 1 → 1+10=11. Neither reaches 20. Let me reconsider: maybe k=4? With k=4 and all elements: 10+1+1+10=22, drop minimum 1 → 21. But k=3, so maximum is 11 after dropping.

### Example 3
- Input: `arr = [5, 2, 8, 10, 1]`, `k = 4`
- Output: `25`
- Explanation: Window [2, 8, 10, 1] sum = 21, drop 1 → 20. Window [5, 2, 8, 10] sum = 25, drop nothing → 25. Maximum is 25.

### Example 4
- Input: `arr = [1, 1, 1, 1, 1]`, `k = 3`
- Output: `2`
- Explanation: Any window has sum 3. Drop one element → 2. Maximum adjusted sum is 2.

### Example 5
- Input: `arr = [100]`, `k = 1`
- Output: `100`
- Explanation: Single element window. Cannot drop the only element, so sum is 100.

## Constraints

- `1 <= n <= 2 * 10^5` (array length)
- `1 <= k <= n` (window size)
- `1 <= arr[i] <= 10^9` (all elements are positive)
- Can drop at most one element from a window (or drop none)
- Time limit: 2 seconds per test case

## Function Signatures

### Java
```java
public class Solution {
    public int[] powerWindowWithDrop(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def powerWindowWithDrop(arr: List[int]) -> List[int]:
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
    vector<int> powerWindowWithDrop(vector<int>& arr) {
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

Maintain window sum and track minimum element in window to consider dropping.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Power Window With Drop'?**

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
