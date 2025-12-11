---
unique_problem_id: heaps_001
display_id: HEAPS-001
slug: running-median-with-delete-threshold
version: 1.0.0
difficulty: Medium
topic_tags:
  - Heaps
  - Problem Solving
---

# Running Median with Delete and Threshold

## Problem Description

Support a stream with insert x and delete x (if present). Also given a threshold `T`; when reporting median (lower middle on even count), if the multiset size is below `T`, output `"NA"` instead of the median. If empty, output `"EMPTY"`.

## Examples

- Input: ops [add 1, add 5, del 1, median], T=2
  - Output: "NA"

## Constraints

`1 <= ops <= 10^5`, `-10^9 <= x <= 10^9`, `0 <= T <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] runningMedianWithDeleteThreshold(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def runningMedianWithDeleteThreshold(arr: List[int]) -> List[int]:
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
    vector<int> runningMedianWithDeleteThreshold(vector<int>& arr) {
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

Two heaps with lazy deletion; track size vs T.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Running Median with Delete and Threshold'?**

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

A) Heaps
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Heaps techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
