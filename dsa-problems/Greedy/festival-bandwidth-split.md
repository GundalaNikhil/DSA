---
unique_problem_id: greedy_014
display_id: GREEDY-014
slug: festival-bandwidth-split
version: 1.0.0
difficulty: Medium
topic_tags:
  - Greedy
  - Problem Solving
---

# Festival Bandwidth Split

## Problem Description

`n` stages share a bandwidth pipe of size `B`. Each stage `i` needs at least `b[i]` to run; unused bandwidth is wasted. Allocate bandwidth to maximize the number of running stages; ties broken by minimizing unused bandwidth.

## Examples

- Input: `b=[5,2,4]`, `B=7`
  - Output: `2`

## Constraints

`1 <= n <= 10^5`, `1 <= B <= 10^12`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] festivalBandwidthSplit(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def festivalBandwidthSplit(arr: List[int]) -> List[int]:
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
    vector<int> festivalBandwidthSplit(vector<int>& arr) {
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

Sort `b` ascending; greedily take smallest until cannot; track waste.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Festival Bandwidth Split'?**

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

A) Greedy
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Greedy techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
