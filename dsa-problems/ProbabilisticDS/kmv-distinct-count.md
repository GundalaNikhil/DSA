---
unique_problem_id: probds_009
display_id: PROBDS-009
slug: kmv-distinct-count
version: 1.0.0
difficulty: Medium
topic_tags:
  - Probabilistic Data Structures
  - Problem Solving
---

# k-Minimum Values (KMV) Distinct Count

## Problem Description

Keep k smallest hash values; estimate distinct count as (k-1)/h_k where h_k is kth smallest hash.

## Examples

- Input: k=3, hashes [0.1,0.2,0.4] => h3=0.4
  - Output: estimate ~5

## Constraints

k<=10^5.

## Function Signatures

### Java
```java
public class Solution {
    public int[] kmvDistinctCount(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def kmvDistinctCount(arr: List[int]) -> List[int]:
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
    vector<int> kmvDistinctCount(vector<int>& arr) {
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
**What is the space complexity of an efficient solution to 'k-Minimum Values (KMV) Distinct Count'?**

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
