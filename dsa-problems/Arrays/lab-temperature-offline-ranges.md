---
unique_problem_id: arrays_004
display_id: ARRAYS-004
slug: lab-temperature-offline-ranges
version: 1.0.0
difficulty: Medium
topic_tags:
  - Arrays
  - Problem Solving
---

# Lab Temperature Offline Ranges

## Problem Description

Given temps array and queries `[l,r]`, some queries are type “add x to range” (offline, applied cumulatively), others ask for range sum after all adds. Return answers to sum queries.

## Examples

- Input: `temps=[1,2,3], queries=[("add",0,1,5),("sum",0,2),("add",2,2,-1),("sum",1,2)]`
  - Output: `[16,9]`

## Constraints

`1 <= n,q <= 10^5`, `-10^9 <= temp[i], x <= 10^9`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] labTemperatureOfflineRanges(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def labTemperatureOfflineRanges(arr: List[int]) -> List[int]:
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
    vector<int> labTemperatureOfflineRanges(vector<int>& arr) {
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

Use difference array to accumulate adds, then prefix for final temps before answering sums with prefix sums.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Lab Temperature Offline Ranges'?**

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

A) Arrays
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Arrays techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
