---
unique_problem_id: stack_005
display_id: STACK-005
slug: workshop-next-taller-width
version: 1.0.0
difficulty: Medium
topic_tags:
  - Stacks
  - Problem Solving
---

# Workshop Next Taller with Width

## Problem Description

For each machine height, find the next taller height to its right within distance at most `w`; if none within `w`, output -1.

## Examples

No examples provided.

## Constraints

`1 <= n <= 2 * 10^5`, `0 <= h[i] <= 10^9`, `1 <= w <= n`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] workshopNextTallerWidth(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def workshopNextTallerWidth(arr: List[int]) -> List[int]:
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
    vector<int> workshopNextTallerWidth(vector<int>& arr) {
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

Monotonic stack storing indices; pop outdated (>w away).

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Workshop Next Taller with Width'?**

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
