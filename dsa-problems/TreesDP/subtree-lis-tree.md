---
unique_problem_id: treedp_015
display_id: TREEDP-015
slug: subtree-lis-tree
version: 1.0.0
difficulty: Hard
topic_tags:
  - Tree DP
  - Problem Solving
---

# DP for Subtree LIS on Tree

## Problem Description

For each node, compute length of LIS of values along path from root to that node.

## Examples

- Input: tree 1-2,1-3 with values [2,1,3]
  - Output: [1,1,2]? Actually LIS to node1=1, node2=1, node3=2

## Constraints

n<=2e5.

## Function Signatures

### Java
```java
public class Solution {
    public int[] subtreeLisTree(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def subtreeLisTree(arr: List[int]) -> List[int]:
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
    vector<int> subtreeLisTree(vector<int>& arr) {
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

Use multiset or Fenwick with coordinate compression during DFS.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'DP for Subtree LIS on Tree'?**

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

A) Tree DP
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Tree DP techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
