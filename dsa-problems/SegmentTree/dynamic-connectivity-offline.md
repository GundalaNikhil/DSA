---
unique_problem_id: segtree_016
display_id: SEGTREE-016
slug: dynamic-connectivity-offline
version: 1.0.0
difficulty: Hard
topic_tags:
  - Segment Tree
  - Problem Solving
---

# Dynamic Connectivity Over Time (Offline)

## Problem Description

Given edges added/removed over time and connectivity queries, answer if nodes u,v are connected at query times.

## Examples

- Input: n=3; events: add(1-2) at t1..t3, query(1,2,t2), remove(1-2), query(1,2,t4)
  - Output: [true,false]

## Constraints

`1 <= n <= 10^5`, `1 <= events <= 2 * 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] dynamicConnectivityOffline(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def dynamicConnectivityOffline(arr: List[int]) -> List[int]:
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
    vector<int> dynamicConnectivityOffline(vector<int>& arr) {
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

Use segment tree over time with union-find rollback.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Dynamic Connectivity Over Time (Offline)'?**

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

A) Segment Tree
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Segment Tree techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
