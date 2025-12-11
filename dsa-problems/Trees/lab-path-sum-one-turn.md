---
unique_problem_id: tree_006
display_id: TREE-006
slug: lab-path-sum-one-turn
version: 1.0.0
difficulty: Medium
topic_tags:
  - Trees
  - Problem Solving
---

# Lab Path Sum with Exactly One Turn

## Problem Description

Given a target sum, determine if there exists a path from some node downwards that first moves only left, then only right (exactly one direction change allowed), ending at any node (not necessarily leaf), whose node values sum to target.

## Examples

- Input: Tree with root `5` left `3` (left `2`, right `1`), right `8`; target `9`
  - Output: `true` (path 3 -> 2 -> 1 with a turn)

## Constraints

`0 <= n <= 10^5`, `-10^9 <= val <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] labPathSumOneTurn(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def labPathSumOneTurn(arr: List[int]) -> List[int]:
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
    vector<int> labPathSumOneTurn(vector<int>& arr) {
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

Precompute prefix sums along left and right chains; DFS keeping hash maps of downward sums; check combinations at each pivot node.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Lab Path Sum with Exactly One Turn'?**

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
