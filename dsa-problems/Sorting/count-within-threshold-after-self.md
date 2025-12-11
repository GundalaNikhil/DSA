---
unique_problem_id: sorting_012
display_id: SORTING-012
slug: count-within-threshold-after-self
version: 1.0.0
difficulty: Medium
topic_tags:
  - Sorting
  - Problem Solving
---

# Count Within Threshold After Self

## Problem Description

For each element `a[i]`, count how many elements to its right satisfy `a[i] - a[j] <= T` (threshold given). Return the counts.

## Examples

- Input: `a=[5,2,6,1], T=3`
  - Output: `[2,1,1,0]` (for 5: 2 and 1 within 3; for 2: only 1 within 3; for 6: none within 3 except 1; for 1: none)

## Constraints

`1 <= n <= 2 * 10^5`, `-10^9 <= a[i] <= 10^9`, `0 <= T <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] countWithinThresholdAfterSelf(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def countWithinThresholdAfterSelf(arr: List[int]) -> List[int]:
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
    vector<int> countWithinThresholdAfterSelf(vector<int>& arr) {
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

Use merge-sort based counting on sorted halves comparing differences.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Count Within Threshold After Self'?**

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

A) Sorting
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Sorting techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
