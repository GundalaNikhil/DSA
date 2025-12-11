---
unique_problem_id: graphbasic_013
display_id: GRAPHBASIC-013
slug: two-sat-amo
version: 1.0.0
difficulty: Medium
topic_tags:
  - Graph Basics
  - Problem Solving
---

# 2-SAT with At-Most-One Constraints

## Problem Description

Variables with clauses (xi or yj) plus at-most-one constraints on given subsets (at most one variable in a subset can be true). Determine satisfiability and output assignment if exists using implication graph + pairwise encoding of at-most-one.

## Examples

- Input: (x1 or x2), subset {x1,x2} at-most-one
  - Output: assignment x1=true,x2=false or vice versa

## Constraints

variables<=1e5, clauses<=2e5, subsets total size<=2e5.

## Function Signatures

### Java
```java
public class Solution {
    public int[] twoSatAmo(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def twoSatAmo(arr: List[int]) -> List[int]:
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
    vector<int> twoSatAmo(vector<int>& arr) {
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
**What is the space complexity of an efficient solution to '2-SAT with At-Most-One Constraints'?**

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

A) Graph Basics
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Graph Basics techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
