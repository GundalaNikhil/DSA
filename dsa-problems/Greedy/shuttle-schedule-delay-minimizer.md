---
unique_problem_id: greedy_016
display_id: GREEDY-016
slug: shuttle-schedule-delay-minimizer
version: 1.0.0
difficulty: Medium
topic_tags:
  - Greedy
  - Problem Solving
---

# Shuttle Schedule Delay Minimizer

## Problem Description

Trips have planned start times and durations. If a trip starts late, its delay adds to all subsequent trips. Choose an execution order to minimize total accumulated delay.

## Examples

- Input: start `[0,1]`, dur `[3,2]`
  - Output: Order `[1,0]` (total delay smaller)

## Constraints

`1 <= n <= 10^5`, durations and start times up to `10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] shuttleScheduleDelayMinimizer(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def shuttleScheduleDelayMinimizer(arr: List[int]) -> List[int]:
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
    vector<int> shuttleScheduleDelayMinimizer(vector<int>& arr) {
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

Sort by `(duration - start)` ascending (Smith-like rule for minimizing weighted completion with equal weights).

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Shuttle Schedule Delay Minimizer'?**

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
