---
unique_problem_id: graph_017
display_id: GRAPH-017
slug: festival-maze-shortest-path
version: 1.0.0
difficulty: Medium
topic_tags:
  - Graphs
  - Problem Solving
---

# Festival Maze Shortest Path

## Problem Description

Grid contains one start `S`, one exit `E`, at least one food stall `F`, walls `#`, and open cells `.`. You may move 4-directionally through non-wall cells. You must visit any food stall at least once before exiting. Find the minimum steps from `S` to `E` that satisfy the visit rule, or `-1` if impossible.

## Examples

- Input:
    ```
    S F .
    # # E
    . F .
    ```
  - Output: `4` (path S→F(0,1)→(0,2)→(1,2)→E)

## Constraints

`1 <= r,c <= 400`; at least one `F`; `S` and `E` exist; total cells `<= 1.6 * 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] festivalMazeShortestPath(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def festivalMazeShortestPath(arr: List[int]) -> List[int]:
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
    vector<int> festivalMazeShortestPath(vector<int>& arr) {
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

BFS on state `(r,c,seenFood)` where `seenFood` is 0/1; first time a stall is reached flip the flag.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Festival Maze Shortest Path'?**

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
