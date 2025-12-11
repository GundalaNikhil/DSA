---
unique_problem_id: heaps_016
display_id: HEAPS-016
slug: priority-queue-decrease-key
version: 1.0.0
difficulty: Medium
topic_tags:
  - Heaps
  - Problem Solving
---

# Priority Queue with Decrease-Key

## Problem Description

Implement a priority queue supporting insert, extract-min, and decrease-key by handle/id.

## Examples

- Input: insert(5,id1), insert(3,id2), dec(id1,1), extract -> ?
  - Output: 1 (id1), then next extract 3 (id2)

## Constraints

`1 <= ops <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] priorityQueueDecreaseKey(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def priorityQueueDecreaseKey(arr: List[int]) -> List[int]:
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
    vector<int> priorityQueueDecreaseKey(vector<int>& arr) {
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

Binary heap with position map or pairing heap.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Priority Queue with Decrease-Key'?**

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
