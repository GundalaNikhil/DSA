---
unique_problem_id: graph_011
display_id: GRAPH-011
slug: library-fire-with-exhaustion
version: 1.0.0
difficulty: Medium
topic_tags:
  - Graphs
  - Problem Solving
---

# Library Fire With Exhaustion

## Problem Description

Grid cells are `0` empty, `1` wall, `2` fire source with stamina `s` (given in a parallel grid). Each minute, active fire cells spread to their 4 neighbors and their stamina decreases by 1; when a cell’s stamina reaches 0 it stops spreading further but stays burning. Compute minutes until no new cells ignite; if any empty cell never burns, return -1.

## Examples

- Input grid: `[[2,0],[0,0]]`, stamina grid: `[[2,0],[0,0]]`
  - Output: `2`

## Constraints

`1 <= r,c <= 200`, stamina values `1..10`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] libraryFireWithExhaustion(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def libraryFireWithExhaustion(arr: List[int]) -> List[int]:
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
    vector<int> libraryFireWithExhaustion(vector<int>& arr) {
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

Multi-source BFS carrying remaining stamina; only enqueue neighbors while stamina > 0 and neighbor not wall/burning.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Library Fire With Exhaustion'?**

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
