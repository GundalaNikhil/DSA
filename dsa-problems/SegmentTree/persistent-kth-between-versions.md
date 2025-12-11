---
unique_problem_id: advsegtree_002
display_id: ADVSEGTREE-002
slug: persistent-kth-between-versions
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Segment Tree
  - Problem Solving
---

# Persistent Kth in Range Between Versions

## Problem Description

Given versions v1, v2 (v2 newer), find k-th smallest in subarray [l,r] when applying differences between v2 and v1 (i.e., multiset of elements added minus removed). Return value or -1 if k out of bounds.

## Examples

- Input: arr=[5,1,3], v1=base, v2 after update pos0->2; query l=0 r=2 k=1
  - Output: 2

## Constraints

`1 <= n,q <= 2 * 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] persistentKthBetweenVersions(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def persistentKthBetweenVersions(arr: List[int]) -> List[int]:
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
    vector<int> persistentKthBetweenVersions(vector<int>& arr) {
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

No hints available.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Persistent Kth in Range Between Versions'?**

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

A) Advanced Segment Tree
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Advanced Segment Tree techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
