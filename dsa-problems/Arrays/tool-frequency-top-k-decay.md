---
unique_problem_id: arrays_013
display_id: ARRAYS-013
slug: tool-frequency-top-k-decay
version: 1.0.0
difficulty: Medium
topic_tags:
  - Arrays
  - Problem Solving
---

# Tool Frequency Top K with Recency Decay

## Problem Description

Each element appears with a timestamp. Score of value v is `sum(exp(-(now - t_i)/D))` over its occurrences (D given). Return the k values with highest decayed score; ties broken by smaller value.

## Examples

- Input: values `[3@0,1@0,3@5,2@6,1@9]`, now=10, D=5, k=2
  - Output: `[3,1]`

## Constraints

`1 <= n <= 2 * 10^5`, timestamps non-decreasing up to 1e9, `1 <= k <= n`, `1 <= D <= 10^6`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] toolFrequencyTopKDecay(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def toolFrequencyTopKDecay(arr: List[int]) -> List[int]:
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
    vector<int> toolFrequencyTopKDecay(vector<int>& arr) {
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

Aggregate scores per value using decay formula; maintain top-k via min-heap.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Tool Frequency Top K with Recency Decay'?**

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

A) Arrays
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Arrays techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
