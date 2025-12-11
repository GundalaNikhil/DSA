---
unique_problem_id: bitwise_002
display_id: BITWISE-002
slug: two-unique-with-triples-mask
version: 1.0.0
difficulty: Medium
topic_tags:
  - Bitwise
  - Problem Solving
---

# Two Unique With Triple Others Under Mask

## Problem Description

Every number appears exactly three times except two distinct numbers that appear once each. Also given a mask `M`; the two uniques are guaranteed to differ in at least one bit set in `M`. Find the two uniques.

## Examples

- Input: `[5,5,5,9,9,9,3,6], M=2`
  - Output: `3 6`

## Constraints

`2 <= n <= 2 * 10^5`, `0 <= M <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] twoUniqueWithTriplesMask(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def twoUniqueWithTriplesMask(arr: List[int]) -> List[int]:
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
    vector<int> twoUniqueWithTriplesMask(vector<int>& arr) {
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

Count bits mod 3 to get XOR of uniques; choose a differing bit that is also set in M to split.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Two Unique With Triple Others Under Mask'?**

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

A) Bitwise
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Bitwise techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
