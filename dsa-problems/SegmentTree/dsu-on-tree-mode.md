---
unique_problem_id: advsegtree_004
display_id: ADVSEGTREE-004
slug: dsu-on-tree-mode
version: 1.0.0
difficulty: Medium
topic_tags:
  - Advanced Segment Tree
  - Problem Solving
---

# DSU on Tree Subtree Mode Query

## Problem Description

For a rooted tree with node colors, for every node output the color with highest frequency in its subtree (smallest color on tie). Use DSU on tree (small-to-large).

## Examples

- Input: tree 1-2,1-3, colors [1,2,2]
  - Output: node1->2, node2->2, node3->2

## Constraints

`1 <= n <= 2 * 10^5`, colors <= 10^9.

## Function Signatures

### Java
```java
public class Solution {
    public int[] dsuOnTreeMode(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def dsuOnTreeMode(arr: List[int]) -> List[int]:
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
    vector<int> dsuOnTreeMode(vector<int>& arr) {
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
**What is the space complexity of an efficient solution to 'DSU on Tree Subtree Mode Query'?**

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
