---
unique_problem_id: greedy_005
display_id: GREEDY-005
slug: shuttle-overtime-minimizer
version: 1.0.0
difficulty: Medium
topic_tags:
  - Greedy
  - Problem Solving
---

# Shuttle Overtime Minimizer

## Problem Description

Each driver shift `i` has length `l[i]` and overtime cost per extra hour `p[i]`. You must cover `H` total hours; shifts can be partially used but overtime cost applies beyond `l[i]`. Minimize cost.

## Examples

- Input: `l=[4,2], p=[3,1]`, `H=8`
  - Output: `14`

## Constraints

`1 <= n <= 10^5`, `0 <= l[i], p[i] <= 10^9`, `1 <= H <= 10^12`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] shuttleOvertimeMinimizer(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def shuttleOvertimeMinimizer(arr: List[int]) -> List[int]:
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
    vector<int> shuttleOvertimeMinimizer(vector<int>& arr) {
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

Use a max-heap on `p[i]`; fill cheaper overtime last.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Shuttle Overtime Minimizer'?**

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
