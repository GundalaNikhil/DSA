---
unique_problem_id: linkedlist_006
display_id: LINKEDLIST-006
slug: lab-loop-detector-entry
version: 1.0.0
difficulty: Medium
topic_tags:
  - Linked Lists
  - Problem Solving
---

# Lab Loop Detector with Entry Index

## Problem Description

Detect if a singly linked list has a cycle; if yes, return the 0-based index of the entry node into the cycle, else return -1.

## Examples

- Input: `1 -> 2 -> 3 -> 4 -> (back to 2)`
  - Output: `1`

## Constraints

`0 <= n <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] labLoopDetectorEntry(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def labLoopDetectorEntry(arr: List[int]) -> List[int]:
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
    vector<int> labLoopDetectorEntry(vector<int>& arr) {
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

Floyd to detect, then move pointers to find entry; count distance from head.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Lab Loop Detector with Entry Index'?**

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

A) Linked Lists
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Linked Lists techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
