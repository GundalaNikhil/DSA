---
unique_problem_id: strings_003
display_id: STRINGS-003
slug: smallest-missing-substring
version: 1.0.0
difficulty: Medium
topic_tags:
  - Strings
  - Problem Solving
---

# Smallest Missing Substring

## Problem Description

Find the lexicographically smallest lowercase string of length `k` that does not appear as a substring of `s`. If all length-k strings exist, return empty.

## Examples

- Input: `s="ababa", k=2`
  - Output: `"aa"`

## Constraints

`1 <= |s| <= 10^5`, `1 <= k <= 5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] smallestMissingSubstring(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def smallestMissingSubstring(arr: List[int]) -> List[int]:
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
    vector<int> smallestMissingSubstring(vector<int>& arr) {
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

Use rolling hash or set of substrings; iterate candidates in lexicographic order via DFS until missing found.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Smallest Missing Substring'?**

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
