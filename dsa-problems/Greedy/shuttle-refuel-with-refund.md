---
unique_problem_id: greedy_009
display_id: GREEDY-009
slug: shuttle-refuel-with-refund
version: 1.0.0
difficulty: Medium
topic_tags:
  - Greedy
  - Problem Solving
---

# Shuttle Refuel with Refund

## Problem Description

A circular route with fuel at stops `gain[i]`, cost to next `cost[i]`, and a coupon that refunds the fuel you spend at exactly one segment. Find a start index to complete the loop using the refund optimally, or -1 if impossible.

## Examples

- Input: `gain=[1,4,2], cost=[3,2,3]`
  - Output: `1`

## Constraints

`1 <= n <= 10^5`, `0 <= gain[i], cost[i] <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] shuttleRefuelWithRefund(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def shuttleRefuelWithRefund(arr: List[int]) -> List[int]:
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
    vector<int> shuttleRefuelWithRefund(vector<int>& arr) {
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

Track surplus and best refund opportunity; similar to gas-station but consider max `(cost - gain)` segment to refund.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Shuttle Refuel with Refund'?**

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

A) Greedy
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Greedy techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
