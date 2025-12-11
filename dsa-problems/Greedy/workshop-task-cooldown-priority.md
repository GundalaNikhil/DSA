---
unique_problem_id: greedy_012
display_id: GREEDY-012
slug: workshop-task-cooldown-priority
version: 1.0.0
difficulty: Medium
topic_tags:
  - Greedy
  - Problem Solving
---

# Workshop Task Cooldown with Priority Interrupts

## Problem Description

Tasks A..Z have counts `c[i]` and priority `p[i]` in {1..3}. Between identical tasks, at least `k` different tasks must occur. A higher-priority task can preempt the cooldown queue: when scheduled, it resets the cooldown of any lower-priority tasks currently cooling down (they must wait an extra `k` slots). Idle slots cost 1. Minimize total slots.

## Examples

- Input: tasks `A:3,p=2`, `B:2,p=1`, `k=1`
  - Output: `7`

## Constraints

`1 <= total tasks <= 10^5`, `0 <= k <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] workshopTaskCooldownPriority(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def workshopTaskCooldownPriority(arr: List[int]) -> List[int]:
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
    vector<int> workshopTaskCooldownPriority(vector<int>& arr) {
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

Max-heap by (priority, remaining count); cooldown queue carries readyTime and priority; when a high-priority task runs, push back lower-priority cooling tasks by k.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Workshop Task Cooldown with Priority Interrupts'?**

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
