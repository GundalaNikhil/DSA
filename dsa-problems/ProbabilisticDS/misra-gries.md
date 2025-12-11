---
unique_problem_id: probds_005
display_id: PROBDS-005
slug: misra-gries
version: 1.0.0
difficulty: Medium
topic_tags:
  - Probabilistic Data Structures
  - Problem Solving
---

# Frequent Items with Misra-Gries

## Problem Description

Using k-1 counters, guarantee finding all items with frequency > n/k. Implement and return candidates.

## Examples

- Input: stream [1,2,1,3,1,2,4], k=3
  - Output: candidates [1,2]

## Constraints

`1 <= n <= 10^6`, `2 <= k <= 1000`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] misraGries(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def misraGries(arr: List[int]) -> List[int]:
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
    vector<int> misraGries(vector<int>& arr) {
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
**What is the space complexity of an efficient solution to 'Frequent Items with Misra-Gries'?**

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

A) Probabilistic Data Structures
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Probabilistic Data Structures techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
