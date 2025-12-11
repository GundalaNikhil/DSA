---
unique_problem_id: strings_013
display_id: STRINGS-013
slug: run-length-decode-cap
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Strings
  - Problem Solving
---

# Run-Length Decode with Cap

## Problem Description

Decode run-length string like "a3b12" but cap any run exceeding `cap` to exactly `cap`. Return decoded string.

## Examples

- Input: `s="a10b2", cap=3`
  - Output: `"aaabb"`

## Constraints

`1 <= |s| <= 10^5`, `1 <= cap <= 10^4`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] runLengthDecodeCap(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def runLengthDecodeCap(arr: List[int]) -> List[int]:
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
    vector<int> runLengthDecodeCap(vector<int>& arr) {
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

No hints available.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Run-Length Decode with Cap'?**

A) O(n)
B) O(n log n)
C) O(n^2)
D) O(1)

**Correct Answer:** A

**Explanation:** The optimal solution can be achieved in linear time by processing the array in a single pass.

### Question 2
**Which data structure would be most suitable for this problem?**

A) Array/List
B) Hash Map
C) Tree
D) Graph

**Correct Answer:** A

**Explanation:** An array or list is the primary data structure needed for this problem.

### Question 3
**Which algorithmic paradigm does this problem primarily belong to?**

A) Strings
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Strings techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
