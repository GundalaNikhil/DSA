---
unique_problem_id: recursion_009
display_id: RECURSION-009
slug: expression-target-one-flip
version: 1.0.0
difficulty: Medium
topic_tags:
  - Recursion
  - Problem Solving
---

# Expression Target With One Negation Flip

## Problem Description

Given digits string `s` and target `T`, insert `+` or `-` or concatenate to form expressions evaluating to `T`, but you may also choose exactly one operand chunk to negate without using an operator (a unary flip applied to a chosen concatenated number). Use at most `c` binary operators total. Multiplication is NOT allowed. Return all valid expressions.

## Examples

- Input: `s="1203", T=0, c=2`
  - Output: `["1+-203", "12-12+0"]` (first uses the unary flip on chunk 203)

## Constraints

`1 <= |s| <= 10`, `0 <= c <= 9`, `-10^9 <= T <= 10^9`; no leading zeros in any chunk unless the chunk is exactly "0".

## Function Signatures

### Java
```java
public class Solution {
    public int[] expressionTargetOneFlip(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def expressionTargetOneFlip(arr: List[int]) -> List[int]:
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
    vector<int> expressionTargetOneFlip(vector<int>& arr) {
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
**What is the space complexity of an efficient solution to 'Expression Target With One Negation Flip'?**

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

A) Recursion
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Recursion techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
