---
unique_problem_id: heaps_005
display_id: HEAPS-005
slug: meeting-rooms-min-idle-setup
version: 1.0.0
difficulty: Medium
topic_tags:
  - Heaps
  - Problem Solving
---

# Meeting Rooms Min Idle with Setup Time

## Problem Description

Meetings have (start,end) and require setup time `s` before each meeting in a room (cannot overlap). With `k` rooms, schedule to minimize total idle + setup slack (time between end+setup and next start). Return minimum slack.

## Examples

- Input: intervals [(0,30),(5,10),(15,20)], k=2, s=2
  - Output: 2 (slack between meetings in same room)

## Constraints

`1 <= n <= 10^5`, `1 <= k <= n`, `0 <= s <= 10^6`.

## Function Signatures

### Java
```java
public class Solution {
    public int[] meetingRoomsMinIdleSetup(int[] arr) {
        // Implementation here
        return new int[0];
    }
}
```

### Python
```python
def meetingRoomsMinIdleSetup(arr: List[int]) -> List[int]:
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
    vector<int> meetingRoomsMinIdleSetup(vector<int>& arr) {
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

Sort by start; min-heap by room available time (end + setup); assign greedily.

## Quiz

### Question 1
**What is the space complexity of an efficient solution to 'Meeting Rooms Min Idle with Setup Time'?**

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
