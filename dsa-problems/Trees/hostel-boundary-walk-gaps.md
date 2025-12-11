---
unique_problem_id: tree_008
display_id: TREE-008
slug: hostel-boundary-walk-gaps
version: 1.0.0
difficulty: Medium
topic_tags:
  - Trees
  - Problem Solving
---

# Hostel Boundary Walk with Gaps

## Problem Description

Same boundary walk but skip any boundary node whose value is negative; keep traversal order otherwise. Return the boundary list after skipping those nodes.

## Examples

- Input: Tree `10` with left `-5` (child `2`) and right `15` (child `-20`)
  - Output: `[10,2,15]`

## Constraints

`1 <= n <= 10^5`, node values 32-bit int.

## Function Signatures

### Java
```java
public class Solution {
    public int[] hostelBoundaryWalkGaps(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def hostelBoundaryWalkGaps(arr: List[int]) -> List[int]:
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
    vector<int> hostelBoundaryWalkGaps(vector<int>& arr) {
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

Standard boundary collection; filter out negatives at each stage; avoid duplicates.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Hostel Boundary Walk with Gaps'?**

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

A) Trees
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Trees techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
