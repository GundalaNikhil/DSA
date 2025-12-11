---
unique_problem_id: probabilistic_002
display_id: PROBABILISTIC-002
slug: expected-steps-random-walk-1d
version: 1.0.0
difficulty: Medium
topic_tags:
  - Probabilistic
  - Problem Solving
---

# Expected Steps Random Walk 1D

## Problem Description

On integer line starting at 0, each step move +1 with prob p else -1. Expected steps to hit +a or -b (absorbing). Compute in closed form or via DP.

## Examples

- Input: `a=2, b=1, p=0.5`
  - Output: `2`

## Constraints

`1 <= a,b <= 200`, `0 < p < 1`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] expectedStepsRandomWalk1d(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def expectedStepsRandomWalk1d(arr: List[int]) -> List[int]:
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
    vector<int> expectedStepsRandomWalk1d(vector<int>& arr) {
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
**What is the space complexity of an efficient solution to 'Expected Steps Random Walk 1D'?**

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
