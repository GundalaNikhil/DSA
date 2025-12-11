---
unique_problem_id: segtree_015
display_id: SEGTREE-015
slug: range-min-after-toggles
version: 1.0.0
difficulty: Medium
topic_tags:
  - Segment Tree
  - Problem Solving
---

# Range Min After Additive Toggles

## Problem Description

Two update types: add x to [l,r] and multiply by -1 on [l,r]. Queries: min in [l,r].

## Examples

- Input: arr=[1,-2,3], flip(0,2), add(1,2,1), min(0,2)
  - Output: -4

## Constraints

`1 <= n,q <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] rangeMinAfterToggles(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def rangeMinAfterToggles(arr: List[int]) -> List[int]:
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
    vector<int> rangeMinAfterToggles(vector<int>& arr) {
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

Segment tree with lazy storing add and flip flags.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Range Min After Additive Toggles'?**

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

A) Segment Tree
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Segment Tree techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
