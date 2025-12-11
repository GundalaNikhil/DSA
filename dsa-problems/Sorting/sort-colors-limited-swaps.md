---
unique_problem_id: sorting_010
display_id: SORTING-010
slug: sort-colors-limited-swaps
version: 1.0.0
difficulty: Medium
topic_tags:
  - Sorting
  - Problem Solving
---

# Sort Colors With Limited Swaps

## Problem Description

Array contains 0,1,2. You may swap only adjacent elements and at most `S` total swaps. Produce the lexicographically smallest array reachable within `S` swaps while moving toward 0s before 1s before 2s.

## Examples

- Input: `arr=[2,1,0], S=1`
  - Output: `[2,0,1]`

## Constraints

`1 <= n <= 2 * 10^5`, `0 <= S <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] sortColorsLimitedSwaps(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def sortColorsLimitedSwaps(arr: List[int]) -> List[int]:
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
    vector<int> sortColorsLimitedSwaps(vector<int>& arr) {
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

Greedy bubble 0s left then 1s left, bounded by remaining swaps.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Sort Colors With Limited Swaps'?**

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
