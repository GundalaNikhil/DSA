---
unique_problem_id: queue_007
display_id: QUEUE-007
slug: lab-window-instability
version: 1.0.0
difficulty: Medium
topic_tags:
  - Queues
  - Problem Solving
---

# Lab Window Instability

## Problem Description

For each window of size `k`, output `(max - min) / median` rounded down (median is lower median for even k). If median is 0, output 0.

## Examples

No examples provided.

## Constraints

`1 <= n <= 2 * 10^5`, `1 <= k <= n`, readings are 32-bit ints.

## Function Signatures

### Java
```java
public class Solution {
    public int[] labWindowInstability(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def labWindowInstability(arr: List[int]) -> List[int]:
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
    vector<int> labWindowInstability(vector<int>& arr) {
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

Deques for max/min plus two-heaps for median with lazy deletions.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Lab Window Instability'?**

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
