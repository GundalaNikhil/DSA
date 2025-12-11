---
unique_problem_id: arrays_009
display_id: ARRAYS-009
slug: best-streak-one-smoothing
version: 1.0.0
difficulty: Medium
topic_tags:
  - Arrays
  - Dynamic Programming
  - Kadane's Algorithm
---

# Best Streak With One Smoothing

## Problem Description

You may choose exactly one index `i` and replace `a[i]` with `floor((a[i-1]+a[i]+a[i+1])/3)` (use existing neighbors; for endpoints, smoothing not allowed). Then compute the maximum subarray sum. Find the maximum achievable sum.

## Examples

### Example 1
- Input: `[-2, 3, -4, 5]`
- Output: `9`
- Explanation: Smooth index 2 (value -4) with neighbors: floor((3 + (-4) + 5) / 3) = floor(4/3) = 1. The array becomes [-2, 3, 1, 5]. Maximum subarray sum is 3 + 1 + 5 = 9.

### Example 2
- Input: `[5, -10, 3, 8, -2]`
- Output: `13`
- Explanation: Smooth index 1 (value -10): floor((5 + (-10) + 3) / 3) = floor(-2/3) = -1. The array becomes [5, -1, 3, 8, -2]. Maximum subarray sum is 5 + (-1) + 3 + 8 = 15. Or smooth index 4 (value -2): floor((8 + (-2) + 0) / 3). Actually without smoothing subarray [3, 8] gives 11, with smoothing at position 1 we get [5, -1, 3, 8] = 15.

### Example 3
- Input: `[10, -5, -3, 7]`
- Output: `14`
- Explanation: Smooth index 2 (value -3): floor((-5 + (-3) + 7) / 3) = floor(-1/3) = -1. Array becomes [10, -5, -1, 7]. Maximum subarray sum could be just [10] = 10, or [10, -5, -1, 7] = 11, or just [7] = 7. Without smoothing: [10] or [7] gives max 10. With smoothing we can get better results.

## Constraints

- `3 <= n <= 2 * 10^5` (array length)
- `-10^9 <= a[i] <= 10^9` (array element values)
- Smoothing can only be applied to non-endpoint indices (1 to n-2)
- Time limit: 2 seconds per test case

## Function Signatures

### Java
```java
public class Solution {
    /**
     * Finds maximum subarray sum after applying one smoothing operation.
     * @param arr The input array
     * @return The maximum achievable sum
     */
    public int bestStreakOneSmoothing(int[] arr) {
        // Implementation here
        return 0;
    }
}
```

### Python
```python
from typing import List

def bestStreakOneSmoothing(arr: List[int]) -> int:
    """
    Finds maximum subarray sum after applying one smoothing operation.
    
    Args:
        arr: Input array
    
    Returns:
        The maximum achievable sum
    """
    pass
```

### C++
```cpp
#include <vector>
using namespace std;

class Solution {
public:
    /**
     * Finds maximum subarray sum after applying one smoothing operation.
     * @param arr The input array
     * @return The maximum achievable sum
     */
    int bestStreakOneSmoothing(vector<int>& arr) {
        // Implementation here
        return 0;
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

Precompute best prefix/suffix Kadane values; test smoothing effect as replacing `a[i]` with new value and combining left/right bests.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Best Streak With One Smoothing'?**

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
