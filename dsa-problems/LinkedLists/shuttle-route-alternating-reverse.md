---
unique_problem_id: linkedlist_005
display_id: LINKEDLIST-005
slug: shuttle-route-alternating-reverse
version: 1.0.0
difficulty: Medium
topic_tags:
  - Linked Lists
  - Problem Solving
---

# Shuttle Route Alternating Reverse

## Problem Description

Starting at position `l`, reverse every other contiguous segment of length `k` (reverse k, skip k, reverse k, ...). The last segment may be shorter; still reverse it if it’s a “reverse” turn. Return the head.

## Examples

- Input: `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7`, `l=2`, `k=2`
  - Output: `1 -> 3 -> 2 -> 4 -> 5 -> 7 -> 6`

## Constraints

`1 <= l <= n <= 10^5`, `1 <= k <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] shuttleRouteAlternatingReverse(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def shuttleRouteAlternatingReverse(arr: List[int]) -> List[int]:
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
    vector<int> shuttleRouteAlternatingReverse(vector<int>& arr) {
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

Traverse to position `l`, then alternately reverse and skip blocks of size `k`.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Shuttle Route Alternating Reverse'?**

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

A) Linked Lists
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Linked Lists techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
