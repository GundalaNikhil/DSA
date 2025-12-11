---
unique_problem_id: numbertheory_005
display_id: NUMBERTHEORY-005
slug: factorials-missing-primes
version: 1.0.0
difficulty: Medium
topic_tags:
  - Number Theory
  - Problem Solving
---

# Factorials With Missing Primes

## Problem Description

Given `n` and a forbidden prime `p`, compute `n!` modulo `p` but with all factors divisible by `p` removed before multiplying. Return result mod p.

## Examples

- Input: `n=6, p=5`
  - Output: `4` (6! without multiples of 5 is 6*4*3*2*1 = 144 mod5 = 4)

## Constraints

`1 <= n <= 10^12`, `p` prime, `2 <= p <= 10^6`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] factorialsMissingPrimes(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def factorialsMissingPrimes(arr: List[int]) -> List[int]:
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
    vector<int> factorialsMissingPrimes(vector<int>& arr) {
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

Use multiplicative pattern over blocks of size p; exclude multiples of p.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Factorials With Missing Primes'?**

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
