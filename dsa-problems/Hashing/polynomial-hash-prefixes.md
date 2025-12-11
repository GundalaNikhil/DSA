---
unique_problem_id: hashing_001
display_id: HASHING-001
slug: polynomial-hash-prefixes
version: 1.0.0
difficulty: Easy
topic_tags:
  - Hashing
  - Problem Solving
---

# Polynomial Hash of Prefixes

## Problem Description

Compute polynomial rolling hash for all prefixes of a lowercase string with base `B` and mod `M`. Output the hash array.

## Examples

- Input: `s="abc", B=911382323, M=1_000_000_007`
  - Output: `[97, 97*B+98 mod M, (prev*B+99) mod M]`

## Constraints

`1 <= |s| <= 2 * 10^5`, `1 <= B <= 1e9+6`, `1 <= M <= 1e9+7`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] polynomialHashPrefixes(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def polynomialHashPrefixes(arr: List[int]) -> List[int]:
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
    vector<int> polynomialHashPrefixes(vector<int>& arr) {
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
**What is the optimal time complexity for solving 'Polynomial Hash of Prefixes'?**

A) O(n)
B) O(n log n)
C) O(n^2)
D) O(1)

**Correct Answer:** A

**Explanation:** The optimal solution can be achieved in linear time by processing the array in a single pass.

### Question 2
**Which data structure would be most suitable for this problem?**

A) Array/List
B) Hash Map
C) Tree
D) Graph

**Correct Answer:** A

**Explanation:** An array or list is the primary data structure needed for this problem.

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
