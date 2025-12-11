---
unique_problem_id: hashing_008
display_id: HASHING-008
slug: max-repeated-block-length
version: 1.0.0
difficulty: Medium
topic_tags:
  - Hashing
  - Problem Solving
---

# Maximum Repeated Block Length

## Problem Description

Find the longest length `L` such that there exist two non-overlapping substrings of length `L` that are equal.

## Examples

- Input: `"banana"`
  - Output: `3` ("ana" repeats non-overlapping as positions 1-3 and 3-5 overlap; longest non-overlap is "ban"/"ana" length 3? better example "abcabc" -> 3)

## Constraints

`1 <= |s| <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] maxRepeatedBlockLength(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def maxRepeatedBlockLength(arr: List[int]) -> List[int]:
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
    vector<int> maxRepeatedBlockLength(vector<int>& arr) {
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

Binary search length, check equality via hashes with gap constraint.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Maximum Repeated Block Length'?**

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
