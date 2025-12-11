---
unique_problem_id: heaps_014
display_id: HEAPS-014
slug: scheduler-cooling-priority
version: 1.0.0
difficulty: Medium
topic_tags:
  - Heaps
  - Problem Solving
---

# Scheduler With Cooling and Priority

## Problem Description

Tasks A..Z with counts and priority weights. Cooling time k between identical tasks. Schedule to maximize total priority executed in given time T.

## Examples

- Input: tasks {A:2 (p=3), B:1 (p=5)}, k=1, T=3
  - Output: total priority 11

## Constraints

`1 <= T <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] schedulerCoolingPriority(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def schedulerCoolingPriority(arr: List[int]) -> List[int]:
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
    vector<int> schedulerCoolingPriority(vector<int>& arr) {
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

Max-heap by priority; cooldown queue with ready time.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Scheduler With Cooling and Priority'?**

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

A) Heaps
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Heaps techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
