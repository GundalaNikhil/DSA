---
unique_problem_id: probabilistic_006
display_id: PROBABILISTIC-006
slug: min-cut-random-contraction
version: 1.0.0
difficulty: Medium
topic_tags:
  - Probabilistic
  - Problem Solving
---

# Min-Cut with Randomized Contraction

## Problem Description

Implement Karger’s randomized contraction to find global min-cut; run enough trials to get success probability >= 0.99. Return best cut size found.

## Examples

- Input: small graph; output min cut size 2

## Constraints

n<=200, m<=2000.

## Function Signatures

### Java
```java
public class Solution {
    public int[] minCutRandomContraction(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def minCutRandomContraction(arr: List[int]) -> List[int]:
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
    vector<int> minCutRandomContraction(vector<int>& arr) {
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
**What is the space complexity of an efficient solution to 'Min-Cut with Randomized Contraction'?**

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

A) Probabilistic
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Probabilistic techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
