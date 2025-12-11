---
unique_problem_id: graph_010
display_id: GRAPH-010
slug: battery-archipelago-analyzer
version: 1.0.0
difficulty: Medium
topic_tags:
  - Graphs
  - Problem Solving
---

# Battery Archipelago Analyzer

## Problem Description

A grid stores elevation integers. Cells with elevation `> 0` are land, `0` is shallow water, `-1` is a bridge tile that does not count as land but connects land components 4-directionally. Count how many distinct land masses remain if bridges are removed, and also report the size of the largest land mass after bridges are removed.

## Examples

- Input: `[[2,-1,3],[0,-1,0],[1,0,4]]`
  - Output: `Components = 2, Largest = 3`

## Constraints

`1 <= r,c <= 400`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] batteryArchipelagoAnalyzer(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def batteryArchipelagoAnalyzer(arr: List[int]) -> List[int]:
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
    vector<int> batteryArchipelagoAnalyzer(vector<int>& arr) {
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

First treat only `>0` as land to label components; bridges connect components but are not counted in size. Use BFS/DFS and a set union step over bridges.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Battery Archipelago Analyzer'?**

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
