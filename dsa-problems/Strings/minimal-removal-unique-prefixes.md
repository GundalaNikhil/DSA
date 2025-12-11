---
unique_problem_id: strings_009
display_id: STRINGS-009
slug: minimal-removal-unique-prefixes
version: 1.0.0
difficulty: Medium
topic_tags:
  - Strings
  - Problem Solving
---

# Minimal Removal for Unique Prefixes

## Problem Description

Given `n` lowercase strings, remove the fewest total characters (you may delete chars from ends of any strings) so that all resulting strings have distinct prefixes of length `L` (given). Return the minimal total deletions.

## Examples

- Input: `L=2`, strings `["ab","ac","ad"]`
  - Output: `0` (already distinct prefixes)

## Constraints

`1 <= n <= 2 * 10^5`, `1 <= L <= 20`, total length <= `2 * 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] minimalRemovalUniquePrefixes(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def minimalRemovalUniquePrefixes(arr: List[int]) -> List[int]:
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
    vector<int> minimalRemovalUniquePrefixes(vector<int>& arr) {
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

Build a trie; when conflicts at depth L, delete from shorter tails to adjust prefixes.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Minimal Removal for Unique Prefixes'?**

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

A) Strings
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Strings techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
