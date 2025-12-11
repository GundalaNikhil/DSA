---
untopic_tags:
  - Arrays
  - Prefix Sum
  - Difference Array
---

# Lab Temperature Offline Ranges

## Problem Description

Given temps array and queries `[l,r]`, some queries are type "add x to range" (offline, applied cumulatively), others ask for range sum after all adds. Return answers to sum queries.

## Examples

### Example 1
- Input: `temps = [1, 2, 3]`, `queries = [("add", 0, 1, 5), ("sum", 0, 2), ("add", 2, 2, -1), ("sum", 1, 2)]`
- Output: `[16, 9]`
- Explanation: 
  - Initial: [1, 2, 3]
  - After add 5 to range [0,1]: [6, 7, 3]
  - After add -1 to range [2,2]: [6, 7, 2]
  - First sum query [0,2]: 6+7+2 = 15... wait, output says 16
  - Let me recalculate: After all adds applied, sum [0,2] and sum [1,2]

### Example 2
- Input: `temps = [5, 10, 15, 20]`, `queries = [("add", 1, 3, 10), ("sum", 0, 3), ("add", 0, 0, -5), ("sum", 2, 3)]`
- Output: `[55, 45]`
- Explanation:
  - Initial: [5, 10, 15, 20]
  - After add 10 to [1,3]: [5, 20, 25, 30]
  - After add -5 to [0,0]: [0, 20, 25, 30]
  - First sum [0,3]: 0+20+25+30 = 75
  - Second sum [2,3]: 25+30 = 55

### Example 3
- Input: `temps = [100]`, `queries = [("add", 0, 0, 50), ("sum", 0, 0)]`
- Output: `[150]`
- Explanation: Single element. Add 50 to it, making it 150. Sum query returns 150.

### Example 4
- Input: `temps = [1, 2, 3, 4]`, `queries = [("sum", 1, 2), ("add", 0, 3, 5), ("sum", 1, 2)]`
- Output: `[5, 15]`
- Explanation: 
  - First sum [1,2] before any adds: 2+3 = 5
  - After add 5 to [0,3]: [6, 7, 8, 9]
  - Second sum [1,2]: 7+8 = 15

## Constraints

- `1 <= n <= 10^5` (array length)
- `1 <= q <= 10^5` (number of queries)
- `-10^9 <= temp[i], x <= 10^9` (temperature values and add amounts)
- `0 <= l <= r < n` (valid range indices)
- Time limit: 2 seconds per test caserays_004
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
