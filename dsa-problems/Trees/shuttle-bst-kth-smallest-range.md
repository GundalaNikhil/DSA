---
unique_problem_id: tree_015
display_id: TREE-015
slug: shuttle-bst-kth-smallest-range
version: 1.0.0
difficulty: Medium
topic_tags:
  - Trees
  - Problem Solving
---

# Shuttle BST Kth Smallest in Range

## Problem Description

Given a BST, an integer range `[L,R]`, and integer `k`, return the k-th smallest value that lies within `[L,R]` (1-indexed among the filtered set). If fewer than `k` values exist in the range, return -1.

## Examples

- Input: BST inorder `[2,4,5,7,9]`, range `[4,8]`, `k=2`
  - Output: `5`

## Constraints

`1 <= n <= 10^5`, values fit in 64-bit, `1 <= k <= n`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] shuttleBstKthSmallestRange(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def shuttleBstKthSmallestRange(arr: List[int]) -> List[int]:
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
    vector<int> shuttleBstKthSmallestRange(vector<int>& arr) {
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

Inorder traversal skipping nodes outside range; decrement k only on in-range nodes.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Shuttle BST Kth Smallest in Range'?**

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

A) Trees
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Trees techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
