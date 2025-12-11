---
unique_problem_id: sorting_016
display_id: SORTING-016
slug: locate-peak-limited-queries
version: 1.0.0
difficulty: Medium
topic_tags:
  - Sorting
  - Problem Solving
---

# Locate Peak with Limited Queries

## Problem Description

You can query array elements by index at most `q` times (black-box API). Array has at least one peak (greater than neighbors). Devise a strategy to find a peak index within `q` queries.

## Examples

- Input: implicit array `[1,3,2,4,1]`, q=5
  - Output: `1` or `3`

## Constraints

`1 <= n <= 10^5`, `1 <= q <= 20`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] locatePeakLimitedQueries(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def locatePeakLimitedQueries(arr: List[int]) -> List[int]:
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
    vector<int> locatePeakLimitedQueries(vector<int>& arr) {
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

Binary search with lazy evaluation; ensure you don't exceed query budget.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Locate Peak with Limited Queries'?**

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
