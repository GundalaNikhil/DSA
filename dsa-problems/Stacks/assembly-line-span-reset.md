---
unique_problem_id: stack_016
display_id: STACK-016
slug: assembly-line-span-reset
version: 1.0.0
difficulty: Medium
topic_tags:
  - Stacks
  - Problem Solving
---

# Assembly Line Span Reset

## Problem Description

Given daily production counts, for each day find the span of consecutive prior days with counts strictly less than today. When you pop strictly smaller counts, reset the span accordingly.

## Examples

No examples provided.

## Constraints

`1 <= n <= 10^5`, `0 <= count[i] <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] assemblyLineSpanReset(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def assemblyLineSpanReset(arr: List[int]) -> List[int]:
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
    vector<int> assemblyLineSpanReset(vector<int>& arr) {
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

Variation of span using a stack of (value, span) but with strict inequality.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Assembly Line Span Reset'?**

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

A) Stacks
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Stacks techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
