---
unique_problem_id: arrays_002
display_id: ARRAYS-002
slug: bench-flip-locked-ends
version: 1.0.0
difficulty: Easy
topic_tags:
  - Arrays
  - Two Pointers
  - In-Place Algorithm
---

# Bench Flip With Locked Ends

## Problem Description

Reverse the array in place but keep the first and last elements fixed; only the middle segment reverses.

## Examples

### Example 1
- Input: `[9, 3, 8, 1, 5]`
- Output: `[9, 5, 1, 8, 3]`
- Explanation: The first element (9) and last element (5) stay in place. The middle elements [3, 8, 1] are reversed to [1, 8, 3].

### Example 2
- Input: `[10, 20, 30, 40]`
- Output: `[10, 30, 20, 40]`
- Explanation: The first element (10) and last element (40) remain fixed. The middle elements [20, 30] are reversed to [30, 20].

### Example 3
- Input: `[7, 2]`
- Output: `[7, 2]`
- Explanation: With only 2 elements, there are no middle elements to reverse. The array remains unchanged.

## Constraints

- `2 <= n <= 2 * 10^5` (array length)
- `-10^9 <= arr[i] <= 10^9` (array element values)
- The array must be modified in-place

## Function Signatures

### Java
```java
public class Solution {
    /**
     * Reverses the middle elements of the array while keeping first and last elements fixed.
     * @param arr The input array
     * @return The modified array with middle elements reversed
     */
    public int[] benchFlipLockedEnds(int[] arr) {
        // Implementation here
        return arr;
    }
}
```

### Python
```python
from typing import List

def benchFlipLockedEnds(arr: List[int]) -> List[int]:
    """
    TODO: Add description
    
    Args:
        arr: Input array/parameter
    
    Returns:
        The result
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
     * Reverses the middle elements of the array while keeping first and last elements fixed.
     * @param arr The input array
     * @return The modified array with middle elements reversed
     */
    vector<int> benchFlipLockedEnds(vector<int>& arr) {
        // Implementation here
        return arr;
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

Two-pointer from positions 1 and n-2.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Bench Flip With Locked Ends'?**

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

**Explanation:** Using two pointers starting from index 1 and n-2 and swapping elements while moving towards center is the key insight.

### Question 5
**What is the space complexity of the optimal solution?**

A) O(n)
B) O(log n)
C) O(1)
D) O(n^2)

**Correct Answer:** C

**Explanation:** The problem can be solved in-place with constant extra space by using two pointers to swap elements.

### Question 6
**How many swaps are required in the worst case for an array of size n?**

A) n
B) n - 1
C) (n - 2) / 2
D) n / 2

**Correct Answer:** C

**Explanation:** We need to reverse n-2 elements (excluding first and last), which requires at most (n-2)/2 swaps using the two-pointer approach.
