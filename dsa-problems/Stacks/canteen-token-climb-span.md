---
unique_problem_id: stack_008
display_id: STACK-008
slug: canteen-token-climb-span
version: 1.0.0
difficulty: Medium
topic_tags:
  - Stacks
  - Problem Solving
---

# Canteen Token Climb Span

## Problem Description

For each day's canteen demand, compute how many consecutive prior days (not including today) had demand strictly lower than today; if any of those prior days equals today’s demand, the span resets to zero. Return the span count (not including today).

## Examples

No examples provided.

## Constraints

`1 <= n <= 10^5`, `0 <= demand[i] <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] canteenTokenClimbSpan(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def canteenTokenClimbSpan(arr: List[int]) -> List[int]:
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
    vector<int> canteenTokenClimbSpan(vector<int>& arr) {
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

Use a strictly increasing monotonic stack of (value, index); pop while lower, reset to 0 if equal encountered.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Canteen Token Climb Span'?**

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
