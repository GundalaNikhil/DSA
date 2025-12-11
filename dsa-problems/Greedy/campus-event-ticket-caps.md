---
unique_problem_id: greedy_011
display_id: GREEDY-011
slug: campus-event-ticket-caps
version: 1.0.0
difficulty: Medium
topic_tags:
  - Greedy
  - Problem Solving
---

# Campus Event Ticket Caps

## Problem Description

Ticket requests have quantities `q[i]` and deadlines `d[i]`. You can process at most one request per day; partially fulfill is allowed but counts as a day. Maximize total tickets sold.

## Examples

- Input: `q=[3,5,2], d=[1,3,2]`
  - Output: `7`

## Constraints

`1 <= n <= 10^5`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] campusEventTicketCaps(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def campusEventTicketCaps(arr: List[int]) -> List[int]:
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
    vector<int> campusEventTicketCaps(vector<int>& arr) {
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

Sort by deadline; use a min-heap of quantities kept to current day; if heap size exceeds days, drop smallest quantity.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Campus Event Ticket Caps'?**

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

A) Greedy
B) Backtracking
C) Branch and Bound
D) Brute Force

**Correct Answer:** A

**Explanation:** This problem is a classic example of Greedy techniques.

### Question 4
**What is the key insight to solve this problem optimally?**

A) Preprocessing the data structure
B) Using brute force enumeration
C) Random sampling
D) Parallel processing

**Correct Answer:** A

**Explanation:** Preprocessing the data structure allows for efficient query processing.
