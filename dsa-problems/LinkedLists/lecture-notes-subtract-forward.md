---
unique_problem_id: linkedlist_016
display_id: LINKEDLIST-016
slug: lecture-notes-subtract-forward
version: 1.0.0
difficulty: Medium
topic_tags:
  - Linked Lists
  - Problem Solving
---

# Lecture Notes Subtract Two Numbers (Forward Order)

## Problem Description

Two linked lists represent non-negative integers in forward order. Subtract the smaller number from the larger and return the result in forward order, along with a sign bit indicating if the result is zero (sign=0) or positive (sign=1). Do not use big integers.

## Examples

- Input: `7 -> 1 -> 6` (716) and `2 -> 9 -> 5` (295)
  - Output: `sign=1`, list `4 -> 2 -> 1` (421)
  - Input: `9 -> 0` (90) and `9 -> 0` (90)
  - Output: `sign=0`, list `0`

## Constraints

Length up to `10^5`, digits 0-9, no leading zeros except zero itself.

## Function Signatures

### Java
```java
public class Solution {
    public int[] lectureNotesSubtractForward(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def lectureNotesSubtractForward(arr: List[int]) -> List[int]:
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
    vector<int> lectureNotesSubtractForward(vector<int>& arr) {
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

Compare lengths and lexicographic order to pick minuend; use stacks to subtract with borrow; drop leading zeros in result.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Lecture Notes Subtract Two Numbers (Forward Order)'?**

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
