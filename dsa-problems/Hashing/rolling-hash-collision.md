---
unique_problem_id: hashing_011
display_id: HASHING-011
slug: rolling-hash-collision
version: 1.0.0
difficulty: Medium
topic_tags:
  - Hashing
  - Problem Solving
---

# Rolling Hash Collision Finder

## Problem Description

Given base B, modulus M, and length L, find two different strings of length L that collide under the polynomial hash. Return any pair.

## Examples

- Input: `B=3, M=7, L=3`
  - Output: e.g., "aaa" and "aba" (if collide; compute to ensure collision)

## Constraints

`1 <= L <= 8`, `1 <= M <= 1e9+7`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] rollingHashCollision(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def rollingHashCollision(arr: List[int]) -> List[int]:
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
    vector<int> rollingHashCollision(vector<int>& arr) {
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

Birthday search/backtracking.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Rolling Hash Collision Finder'?**

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

A) Hashing
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Hashing techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
