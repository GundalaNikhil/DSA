---
unique_problem_id: tree_009
display_id: TREE-009
slug: campus-vertical-order-cutoff
version: 1.0.0
difficulty: Medium
topic_tags:
  - Trees
  - Problem Solving
---

# Campus Vertical Order With Distance Cutoff

## Problem Description

Return vertical order groups but only include nodes whose absolute horizontal distance from root is <= `D`. Order within columns is top-to-bottom, left-to-right.

## Examples

- Input: Root `3`, left `9`, right `8`, `8` has children `4` and `7`, D=1
  - Output: `[[9],[3],[8]]`

## Constraints

`0 <= n <= 10^5`, `0 <= D <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] campusVerticalOrderCutoff(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def campusVerticalOrderCutoff(arr: List[int]) -> List[int]:
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
    vector<int> campusVerticalOrderCutoff(vector<int>& arr) {
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

BFS storing column; skip columns outside [-D,D]; track min/max within cutoff.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Campus Vertical Order With Distance Cutoff'?**

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
