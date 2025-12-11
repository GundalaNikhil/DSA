---
unique_problem_id: tree_007
display_id: TREE-007
slug: sports-dome-weighted-diameter
version: 1.0.0
difficulty: Medium
topic_tags:
  - Trees
  - Problem Solving
---

# Sports Dome Weighted Diameter

## Problem Description

Edges of the binary tree have non-negative weights. Find the maximum total edge weight on any path between two nodes.

## Examples

- Input: Root `1` with left child `2` (edge 4) and right child `3` (edge 1); `2` has left `4` (edge 2)
  - Output: `6` (path 4-2-1-3)

## Constraints

`0 <= n <= 10^5`, edge weights `0..10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] sportsDomeWeightedDiameter(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def sportsDomeWeightedDiameter(arr: List[int]) -> List[int]:
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
    vector<int> sportsDomeWeightedDiameter(vector<int>& arr) {
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

DFS returning best downward path weight; update answer with sum of two child paths plus their edge weights.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Sports Dome Weighted Diameter'?**

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
