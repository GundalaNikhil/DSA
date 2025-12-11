---
unique_problem_id: tree_005
display_id: TREE-005
slug: robotics-mirror-check-colors
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Trees
  - Problem Solving
---

# Robotics Mirror Check with Colors

## Problem Description

Each node has a value and a color bit (0/1). Determine if the tree is symmetric in structure and values, and also the multiset of colors on each mirrored level must match (but colors need not match node-for-node).

## Examples

- Input: Root `4`(0), children `2`(1) and `2`(1), grandchildren `1`(0),`3`(1) mirrored with swapped colors
  - Output: `true`

## Constraints

`0 <= n <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] roboticsMirrorCheckColors(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def roboticsMirrorCheckColors(arr: List[int]) -> List[int]:
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
    vector<int> roboticsMirrorCheckColors(vector<int>& arr) {
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

Compare mirrored nodes for value equality and collect colors per level; both structural mirror and level-color multisets must align.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Robotics Mirror Check with Colors'?**

A) O(n)
B) O(n log n)
C) O(n^2)
D) O(1)

**Correct Answer:** A

**Explanation:** The optimal solution can be achieved in linear time by processing the array in a single pass.

### Question 2
**Which data structure would be most suitable for this problem?**

A) Array/List
B) Hash Map
C) Tree
D) Graph

**Correct Answer:** A

**Explanation:** An array or list is the primary data structure needed for this problem.

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
