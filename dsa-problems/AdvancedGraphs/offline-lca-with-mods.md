---
unique_problem_id: advgraph_016
display_id: ADVGRAPH-016
slug: offline-lca-with-mods
version: 1.0.0
difficulty: Hard
topic_tags:
  - Advanced Graphs
  - Problem Solving
---

# Offline Lowest Common Ancestor with Modifications

## Problem Description

Given a rooted tree, process operations: add edge (temporarily connecting two nodes), remove that added edge, and LCA queries between nodes considering currently active extra edges. Answer queries offline.

## Examples

- Input: base tree edges (0-1,1-2,1-3); add extra edge (2-3) active during certain queries; query LCA(2,3) during active phase.
  - Output: LCA becomes 2 or 3 when edge makes them directly connected? Actually with extra edge, treat as connectivity query; answer 1 when only tree edges active.

## Constraints

n<=2e5, events<=2e5.

## Function Signatures

### Java
```java
public class Solution {
    public int[] offlineLcaWithMods(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def offlineLcaWithMods(arr: List[int]) -> List[int]:
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
    vector<int> offlineLcaWithMods(vector<int>& arr) {
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

Use DSU rollback on Euler tour intervals; segment tree over time for edge activations; LCA via binary lifting on base tree plus DSU connectivity.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Offline Lowest Common Ancestor with Modifications'?**

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

A) Advanced Graphs
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Advanced Graphs techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
