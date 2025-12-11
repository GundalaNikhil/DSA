---
unique_problem_id: heaps_010
display_id: HEAPS-010
slug: topk-products-index-gap
version: 1.0.0
difficulty: Medium
topic_tags:
  - Heaps
  - Problem Solving
---

# Top K Products with Index Gap

## Problem Description

Two sorted arrays (desc). Find top k largest products `A[i]*B[j]` subject to |i-j| >= d (given). If fewer than k pairs satisfy, return all possible.

## Examples

- Input: A=[9,7], B=[8,3], d=1, k=2
  - Output: [27,24]

## Constraints

`1 <= n,m <= 10^5`, `1 <= k <= min(10^5, n*m)`, `0 <= d < max(n,m)`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] topkProductsIndexGap(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def topkProductsIndexGap(arr: List[int]) -> List[int]:
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
    vector<int> topkProductsIndexGap(vector<int>& arr) {
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

Max-heap of candidate pairs respecting the gap; expand neighbors while maintaining gap constraint.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Top K Products with Index Gap'?**

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
