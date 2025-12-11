---
unique_problem_id: heaps_013
display_id: HEAPS-013
slug: project-selection-risk-budget
version: 1.0.0
difficulty: Medium
topic_tags:
  - Heaps
  - Problem Solving
---

# Project Selection with Risk Budget

## Problem Description

Each project i has cost[i], profit[i], and risk[i]. Start with capital C and risk budget R. You may pick at most k projects, only if cost <= capital and cumulative risk + risk[i] <= R. Maximize final capital.

## Examples

- Input: cost=[1,2,3], profit=[1,2,3], risk=[1,2,2], C=1, R=3, k=2
  - Output: 5

## Constraints

`1 <= n <= 10^5`, `1 <= k <= n`, values up to 1e9.

## Function Signatures

### Java
```java
public class Solution {
    public int[] projectSelectionRiskBudget(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def projectSelectionRiskBudget(arr: List[int]) -> List[int]:
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
    vector<int> projectSelectionRiskBudget(vector<int>& arr) {
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

Min-heap by cost for affordability; among affordable within risk budget, pick max profit; decrement risk budget per choice.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Project Selection with Risk Budget'?**

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
