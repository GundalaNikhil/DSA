---
unique_problem_id: arrays_007
display_id: ARRAYS-007
slug: hostel-roster-merge-gap
version: 1.0.0
difficulty: Medium
topic_tags:
  - Arrays
  - Two Pointers
  - Merge Algorithm
---

# Hostel Roster Merge With Gap

## Problem Description

Merge two sorted arrays `A` and `B` into sorted order, but if two equal elements come from different arrays, place the one from `A` before the one from `B`. Return merged array.

## Examples

### Example 1
- Input: `A = [1, 3, 3]`, `B = [3, 4]`
- Output: `[1, 3, 3, 3, 4]`
- Explanation: When merging, we encounter three 3s. Two 3s from array A come first (at indices 1 and 2), followed by the 3 from array B. Final order: 1, then all three 3s (A's first), then 4.

### Example 2
- Input: `A = [2, 5, 7]`, `B = [1, 2, 5, 8]`
- Output: `[1, 2, 2, 5, 5, 7, 8]`
- Explanation: 1 from B, then 2 from A before 2 from B (stable merge with A priority), then 5 from A before 5 from B, then 7 from A, finally 8 from B.

### Example 3
- Input: `A = [1, 1, 1]`, `B = [1, 1]`
- Output: `[1, 1, 1, 1, 1]`
- Explanation: All elements are equal. All 1s from A (3 elements) appear first, followed by all 1s from B (2 elements).

### Example 4
- Input: `A = []`, `B = [3, 5, 7]`
- Output: `[3, 5, 7]`
- Explanation: Edge case with empty array A. Result is simply array B.

## Constraints

- `0 <= n, m <= 10^5` (lengths of arrays A and B)
- Arrays A and B are sorted in non-decreasing order
- `-10^9 <= A[i], B[i] <= 10^9`
- When elements are equal, A's element must come before B's element
- Time limit: 2 seconds per test case

## Function Signatures

### Java
```java
public class Solution {
    /**
     * Merges two sorted arrays with stable ordering (A's elements before B's when equal).
     * @param A First sorted array
     * @param B Second sorted array
     * @return Merged sorted array
     */
    public int[] hostelRosterMergeGap(int[] A, int[] B) {
        // Implementation here
        return new int[A.length + B.length];
    }
}
```

### Python
```python
from typing import List

def hostelRosterMergeGap(A: List[int], B: List[int]) -> List[int]:
    """
    Merges two sorted arrays with stable ordering (A's elements before B's when equal).
    
    Args:
        A: First sorted array
        B: Second sorted array
    
    Returns:
        Merged sorted array
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
     * Merges two sorted arrays with stable ordering (A's elements before B's when equal).
     * @param A First sorted array
     * @param B Second sorted array
     * @return Merged sorted array
     */
    vector<int> hostelRosterMergeGap(vector<int>& A, vector<int>& B) {
        // Implementation here
        return vector<int>(A.size() + B.size());
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

Standard merge with tie-break on source.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Hostel Roster Merge With Gap'?**

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

**Explanation:** Using two pointers to merge arrays with stable ordering based on source is the key approach.

### Question 5
**What is the time complexity of the optimal solution?**

A) O(n + m)
B) O(n log m)
C) O(n * m)
D) O(max(n, m))

**Correct Answer:** A

**Explanation:** We traverse both arrays once using two pointers, resulting in O(n + m) time complexity where n and m are the lengths of the two arrays.

### Question 6
**What happens when all elements in both arrays are equal?**

A) The merge fails
B) Elements from A come before elements from B
C) Elements are randomly ordered
D) Elements from B come before elements from A

**Correct Answer:** B

**Explanation:** According to the problem's stable merge requirement, when elements are equal, all elements from array A must be placed before elements from array B.
