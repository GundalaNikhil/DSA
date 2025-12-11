---
unique_problem_id: graph_012
display_id: GRAPH-012
slug: exam-seating-rooms-vip
version: 1.0.0
difficulty: Easy-Medium
topic_tags:
  - Graphs
  - Problem Solving
---

# Exam Seating Rooms with VIP Isolation

## Problem Description

An undirected graph shows students who must sit together. VIP nodes (given) cannot be in the same component as any other VIP. Remove the minimum number of edges to ensure no component contains more than one VIP. Return the resulting maximum component size after removals.

## Examples

- Input: `n=5`, edges `[(0,1),(1,2),(3,4)]`, VIPs `{2,3}`
  - Output: `3` (edge (3,4) allowed; largest component size 3)

## Constraints

`1 <= n <= 10^5`, `0 <= edges <= 2*10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] examSeatingRoomsVip(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def examSeatingRoomsVip(arr: List[int]) -> List[int]:
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
    vector<int> examSeatingRoomsVip(vector<int>& arr) {
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

Run DSU; when an edge would merge two components each containing a VIP, skip that edge; track component sizes.

## Quiz

### Question 1
**What is the optimal time complexity for solving 'Exam Seating Rooms with VIP Isolation'?**

A) O(n)
B) O(n log n)
C) O(n^2)
D) O(1)

**Correct Answer:** A

**Explanation:** The optimal solution can be achieved in linear time by processing the array in a single pass.

### Question 2
**Which data structure would be most suitable for this problem?**

A) Array/List
B) Hash Map
C) Tree
D) Graph

**Correct Answer:** A

**Explanation:** An array or list is the primary data structure needed for this problem.

### Question 3
**Which algorithmic paradigm does this problem primarily belong to?**

A) Graphs
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Graphs techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
