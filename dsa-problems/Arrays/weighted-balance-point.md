---
unique_problem_id: arrays_005
display_id: ARRAYS-005
slug: weighted-balance-point
version: 1.0.0
difficulty: Medium
topic_tags:
  - Arrays
  - Problem Solving
---

# Weighted Balance Point

## Problem Description

Find smallest index `i` where `sum(left)*L == sum(right)*R` for given weights `L` and `R`; left excludes `i`, right excludes `i`. If none, return -1.

## Examples

- Input: `a=[2,3,-1,3,2], L=2, R=1`
  - Output: `1` (left*2=4*2=8, right*1=8)

## Constraints

`1 <= n <= 2 * 10^5`, `-10^9 <= a[i] <= 10^9`, `1 <= L,R <= 10^6`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] weightedBalancePoint(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def weightedBalancePoint(arr: List[int]) -> List[int]:
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
    vector<int> weightedBalancePoint(vector<int>& arr) {
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

Precompute total; iterate maintaining left sum.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Weighted Balance Point'?**

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
