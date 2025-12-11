---
unique_problem_id: stringalgo_011
display_id: STRINGALGO-011
slug: lcs-two-strings-sa
version: 1.0.0
difficulty: Medium
topic_tags:
  - String Algorithms
  - Problem Solving
---

# Longest Common Substring of Two Strings (SA)

## Problem Description

Build SA of s1 + '#' + s2; find max LCP between suffixes from different strings.

## Examples

- Input: `"abcd", "bc"`
  - Output: `2`

## Constraints

`1 <= |s1|,|s2| <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] lcsTwoStringsSa(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def lcsTwoStringsSa(arr: List[int]) -> List[int]:
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
    vector<int> lcsTwoStringsSa(vector<int>& arr) {
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
**What is the space complexity of an efficient solution to 'Longest Common Substring of Two Strings (SA)'?**

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

A) String Algorithms
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of String Algorithms techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
