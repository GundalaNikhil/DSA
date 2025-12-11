---
unique_problem_id: linkedlist_011
display_id: LINKEDLIST-011
slug: exam-seating-intersection-sum
version: 1.0.0
difficulty: Medium
topic_tags:
  - Linked Lists
  - Problem Solving
---

# Exam Seating Intersection Sum

## Problem Description

Given two singly linked lists that may intersect (sharing nodes), return the sum of values of the shared suffix; return 0 if no intersection.

## Examples

- Input: A `1->2->3->4`, B `9->3->4` (nodes 3,4 shared)
  - Output: `7`

## Constraints

`0 <= n <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] examSeatingIntersectionSum(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def examSeatingIntersectionSum(arr: List[int]) -> List[int]:
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
    vector<int> examSeatingIntersectionSum(vector<int>& arr) {
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

Find intersection node via length or hash; then traverse shared suffix summing values.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Exam Seating Intersection Sum'?**

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
