---
unique_problem_id: numbertheory_013
display_id: NUMBERTHEORY-013
slug: count-strings-exact-vowels
version: 1.0.0
difficulty: Medium
topic_tags:
  - Number Theory
  - Problem Solving
---

# Count Strings With Exact Vowels

## Problem Description

Count strings of length `n` over lowercase letters containing exactly `k` vowels. Return count modulo `MOD`.

## Examples

- Input: `n=3, k=1`
  - Output: `3 * 5 * 21^2 mod = 3*5*441=6615 mod... large; choose smaller n: n=2,k=1 => 2*5*21=210`

## Constraints

`1 <= n <= 10^6`, `0 <= k <= n`, `MOD=10^9+7`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] countStringsExactVowels(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def countStringsExactVowels(arr: List[int]) -> List[int]:
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
    vector<int> countStringsExactVowels(vector<int>& arr) {
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

Combinatorics: C(n,k)*5^k*21^{n-k} mod MOD; precompute factorials.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Count Strings With Exact Vowels'?**

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
