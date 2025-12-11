---
unique_problem_id: stack_009
display_id: STACK-009
slug: lab-sliding-min-stack
version: 1.0.0
difficulty: Medium
topic_tags:
  - Stacks
  - Problem Solving
---

# Lab Sliding-Min Stack

## Problem Description

Support `PUSH x`, `POP`, and queries `MIN k` that ask for the minimum among the top `k` elements currently in the stack (counting the top as 1). If the stack has fewer than `k` elements, return `"NA"`.

## Examples

No examples provided.

## Constraints

`1 <= m <= 10^5` operations, `1 <= k <= 10^5`, values are 32-bit signed ints.

## Function Signatures

### Java
```java
public class Solution {
    public int[] labSlidingMinStack(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def labSlidingMinStack(arr: List[int]) -> List[int]:
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
    vector<int> labSlidingMinStack(vector<int>& arr) {
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

Maintain a stack of values and an auxiliary stack of monotonic mins with counts so you can roll back pops and handle window size `k`.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Lab Sliding-Min Stack'?**

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
