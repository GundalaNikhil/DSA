---
unique_problem_id: numbertheory_002
display_id: NUMBERTHEORY-002
slug: coprime-pair-count
version: 1.0.0
difficulty: Medium
topic_tags:
  - Number Theory
  - Problem Solving
---

# Coprime Pair Count Up To N

## Problem Description

For given `N`, count ordered pairs `(i,j)` with `1 <= i < j <= N` and `gcd(i,j)=1`.

## Examples

- Input: `N=5`
  - Output: `7` (pairs: (1,2),(1,3),(1,4),(1,5),(2,3),(2,5),(3,4))

## Constraints

`1 <= N <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] coprimePairCount(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def coprimePairCount(arr: List[int]) -> List[int]:
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
    vector<int> coprimePairCount(vector<int>& arr) {
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

Use Euler’s totient: total pairs = sum_{k=2..N} phi(k); precompute phi via sieve.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Coprime Pair Count Up To N'?**

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

A) Number Theory
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Number Theory techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
