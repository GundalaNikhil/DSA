---
unique_problem_id: stringalgo_001
display_id: STRINGALGO-001
slug: kmp-prefix-function
version: 1.0.0
difficulty: Easy
topic_tags:
  - String Algorithms
  - Problem Solving
---

# Prefix Function (KMP) Construction

## Problem Description

Compute prefix function (pi array) for a string; return the array.

## Examples

- Input: `"ababa"`
  - Output: `[0,0,1,2,3]`

## Constraints

`1 <= |s| <= 2 * 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] kmpPrefixFunction(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def kmpPrefixFunction(arr: List[int]) -> List[int]:
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
    vector<int> kmpPrefixFunction(vector<int>& arr) {
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
**What is the optimal time complexity for solving 'Prefix Function (KMP) Construction'?**

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

A) String Algorithms
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of String Algorithms techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
