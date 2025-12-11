---
unique_problem_id: probabilistic_005
display_id: PROBABILISTIC-005
slug: bloom-filter-fpr
version: 1.0.0
difficulty: Medium
topic_tags:
  - Probabilistic
  - Problem Solving
---

# Bloom Filter False Positive Rate

## Problem Description

Given m bits, k hash functions, and n inserted items, compute false positive probability of a Bloom filter.

## Examples

- Input: m=1000, k=3, n=100
  - Output: ~0.082

## Constraints

`1 <= m,n <= 10^6`, `1 <= k <= 20`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] bloomFilterFpr(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def bloomFilterFpr(arr: List[int]) -> List[int]:
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
    vector<int> bloomFilterFpr(vector<int>& arr) {
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
**What is the space complexity of an efficient solution to 'Bloom Filter False Positive Rate'?**

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
