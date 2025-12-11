---
unique_problem_id: graph_007
display_id: GRAPH-007
slug: course-plan-mandatory-pairs
version: 1.0.0
difficulty: Medium
topic_tags:
  - Graphs
  - Problem Solving
---

# Course Plan with Mandatory Pairs

## Problem Description

You are given prerequisites as a DAG and also pairs of courses that must appear adjacent (in any order) in the schedule. Produce a topological ordering that respects adjacency pairs if possible; otherwise return empty.

## Examples

- Input: `n=4`, edges `[(0,2),(1,2)]`, pairs `[(2,3)]`
  - Output: A valid order `[0,1,2,3]` (2 and 3 adjacent)

## Constraints

`1 <= n <= 10^5`, `0 <= edges <= 2*10^5`, `0 <= pairs <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] coursePlanMandatoryPairs(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def coursePlanMandatoryPairs(arr: List[int]) -> List[int]:
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
    vector<int> coursePlanMandatoryPairs(vector<int>& arr) {
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

First contract each adjacency pair into a super-node if it doesn’t violate prerequisites; then run Kahn’s on the contracted graph while expanding pairs appropriately.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Course Plan with Mandatory Pairs'?**

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
