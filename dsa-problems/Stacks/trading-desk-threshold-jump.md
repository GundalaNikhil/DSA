---
unique_problem_id: stack_007
display_id: STACK-007
slug: trading-desk-threshold-jump
version: 1.0.0
difficulty: Medium
topic_tags:
  - Stacks
  - Problem Solving
---

# Trading Desk Threshold Jump

## Problem Description

Given intraday prices and a threshold `t`, for each price find how many steps forward until you see a price at least `t` units higher; output 0 if none exists.

## Examples

No examples provided.

## Constraints

`1 <= n <= 2 * 10^5`, `0 <= price[i], t <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] tradingDeskThresholdJump(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def tradingDeskThresholdJump(arr: List[int]) -> List[int]:
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
    vector<int> tradingDeskThresholdJump(vector<int>& arr) {
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

Monotonic stack but compare `price[next] - price[i] >= t`; pop while current price is too small to help prior items.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Trading Desk Threshold Jump'?**

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
