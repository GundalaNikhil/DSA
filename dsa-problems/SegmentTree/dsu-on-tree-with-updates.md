---
unique_problem_id: advsegtree_005
display_id: ADVSEGTREE-005
slug: dsu-on-tree-with-updates
version: 1.0.0
difficulty: Hard
topic_tags:
  - Advanced Segment Tree
  - Problem Solving
---

# DSU on Tree With Updates

## Problem Description

Tree with color updates on nodes and queries asking distinct color count in subtree at that time. Offline process with Mo’s on tree + updates or Euler + sqrt-decomp.

## Examples

- Input: colors [1,2], edge(1,2); update node2 to 1; query subtree of 1
  - Output: before update 2, after update 1

## Constraints

`1 <= n,q <= 2 * 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] dsuOnTreeWithUpdates(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def dsuOnTreeWithUpdates(arr: List[int]) -> List[int]:
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
    vector<int> dsuOnTreeWithUpdates(vector<int>& arr) {
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
**What is the space complexity of an efficient solution to 'DSU on Tree With Updates'?**

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
