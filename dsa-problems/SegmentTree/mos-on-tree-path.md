---
unique_problem_id: advsegtree_012
display_id: ADVSEGTREE-012
slug: mos-on-tree-path
version: 1.0.0
difficulty: Hard
topic_tags:
  - Advanced Segment Tree
  - Problem Solving
---

# Mo’s on Tree for Path Queries

## Problem Description

Given a tree with colors, offline answer queries asking distinct colors on path (u,v). Use Euler + Mo on tree.

## Examples

- Input: path 1-2-3, colors [1,2,1], query (1,3)
  - Output: 2

## Constraints

`1 <= n,q <= 2 * 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] mosOnTreePath(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def mosOnTreePath(arr: List[int]) -> List[int]:
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
    vector<int> mosOnTreePath(vector<int>& arr) {
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
**What is the space complexity of an efficient solution to 'Mo’s on Tree for Path Queries'?**

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
