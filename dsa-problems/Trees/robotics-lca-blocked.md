---
unique_problem_id: tree_012
display_id: TREE-012
slug: robotics-lca-blocked
version: 1.0.0
difficulty: Medium
topic_tags:
  - Trees
  - Problem Solving
---

# Robotics LCA with Blocked Nodes

## Problem Description

Some nodes are blocked and cannot be used as part of the path. Given two target nodes that are not blocked, find their lowest common ancestor that is also not blocked; if all common ancestors are blocked, return `null`.

## Examples

- Input: Tree `6` with children `2` and `8`; `2` has children `1` and `4`; blocked node `6`; targets `1` and `4`
  - Output: `2`

## Constraints

`1 <= n <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] roboticsLcaBlocked(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def roboticsLcaBlocked(arr: List[int]) -> List[int]:
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
    vector<int> roboticsLcaBlocked(vector<int>& arr) {
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

Postorder DFS returning presence of targets and ignoring blocked subtrees; only count an ancestor if unblocked.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Robotics LCA with Blocked Nodes'?**

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
