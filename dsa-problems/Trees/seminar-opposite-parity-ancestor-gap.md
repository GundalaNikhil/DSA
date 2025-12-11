---
unique_problem_id: tree_018
display_id: TREE-018
slug: seminar-opposite-parity-ancestor-gap
version: 1.0.0
difficulty: Medium
topic_tags:
  - Trees
  - Problem Solving
---

# Seminar Opposite-Parity Ancestor Gap

## Problem Description

For each node, consider only ancestors at a depth parity different from the node (one even, one odd). Find the maximum absolute difference between a node value and any such opposite-parity ancestor.

## Examples

- Input: Root `8`, left `3` (child `1`), right `10` (child `14`)
  - Output: `11` (node 14 vs ancestor 3 of opposite parity)

## Constraints

`0 <= n <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] seminarOppositeParityAncestorGap(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def seminarOppositeParityAncestorGap(arr: List[int]) -> List[int]:
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
    vector<int> seminarOppositeParityAncestorGap(vector<int>& arr) {
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

DFS carrying two pairs of min/max by parity; update answer using the opposite parity bucket.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Seminar Opposite-Parity Ancestor Gap'?**

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
