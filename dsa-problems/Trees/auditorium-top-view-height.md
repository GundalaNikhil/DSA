---
unique_problem_id: tree_010
display_id: TREE-010
slug: auditorium-top-view-height
version: 1.0.0
difficulty: Medium
topic_tags:
  - Trees
  - Problem Solving
---

# Auditorium Top View With Height Bonus

## Problem Description

For each column, choose the node with smallest depth; if multiple at same depth, choose the one with largest value. Return columns left to right.

## Examples

- Input: Root `1`, left `2`, right `3`, `2` has right `4`, `3` has left `5`
  - Output: `[4,1,5]`

## Constraints

`0 <= n <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] auditoriumTopViewHeight(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def auditoriumTopViewHeight(arr: List[int]) -> List[int]:
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
    vector<int> auditoriumTopViewHeight(vector<int>& arr) {
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

BFS with column and depth; update when depth smaller or equal but value larger.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Auditorium Top View With Height Bonus'?**

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
