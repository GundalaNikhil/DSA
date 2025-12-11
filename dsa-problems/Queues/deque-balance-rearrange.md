---
unique_problem_id: queue_014
display_id: QUEUE-014
slug: deque-balance-rearrange
version: 1.0.0
difficulty: Medium
topic_tags:
  - Queues
  - Problem Solving
---

# Deque Balance Rearrange

## Problem Description

Given an array, rearrange it by alternately taking from the front and back into a new deque, then output the deque from front to back.

## Examples

No examples provided.

## Constraints

`1 <= n <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] dequeBalanceRearrange(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def dequeBalanceRearrange(arr: List[int]) -> List[int]:
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
    vector<int> dequeBalanceRearrange(vector<int>& arr) {
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

Use two indices (start/end) and push_front/push_back alternately.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Deque Balance Rearrange'?**

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

A) Queues
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Queues techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
