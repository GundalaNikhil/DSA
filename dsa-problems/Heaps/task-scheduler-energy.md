---
unique_problem_id: heaps_006
display_id: HEAPS-006
slug: task-scheduler-energy
version: 1.0.0
difficulty: Medium
topic_tags:
  - Heaps
  - Problem Solving
---

# Task Scheduler with Energy

## Problem Description

Tasks have duration and energy gain. You have initial energy E; executing a task consumes 1 energy unit per time unit of its duration but gives a one-time gain. Pick order to maximize completed tasks.

## Examples

- Input: tasks [(dur=2,gain=3),(dur=3,gain=1)], E=3
  - Output: 2

## Constraints

`1 <= n <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] taskSchedulerEnergy(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def taskSchedulerEnergy(arr: List[int]) -> List[int]:
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
    vector<int> taskSchedulerEnergy(vector<int>& arr) {
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

Sort by start energy requirement; min-heap for durations when energy limited.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Task Scheduler with Energy'?**

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
