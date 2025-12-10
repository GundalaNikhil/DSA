# Meeting Room Scheduler

**Difficulty:** Medium
**Topic:** Arrays, Intervals, Sorting
**License:** Free to use for commercial purposes

## Problem Statement

A company has multiple meeting rooms and needs to schedule meetings. Each meeting is represented by a start and end time in hours (24-hour format). Given an array of meeting time intervals where `meetings[i] = [start_i, end_i]`, determine the minimum number of meeting rooms required to schedule all meetings without conflicts.

Note: If a meeting ends at time T, another meeting can start at time T (no gap needed).

## Constraints

- `1 <= meetings.length <= 1000`
- `0 <= start_i < end_i <= 24`
- Times are in 24-hour format (0-24)

## Examples

### Example 1
```
Input: meetings = [[9, 11], [10, 12], [13, 15]]
Output: 2
Explanation:
  Room 1: 9-11, then 13-15
  Room 2: 10-12
  At time 10, we need 2 rooms (meetings [9,11] and [10,12] overlap).
```

### Example 2
```
Input: meetings = [[8, 10], [10, 12], [12, 14]]
Output: 1
Explanation:
  All meetings can use the same room as they don't overlap.
  When one ends, the next can start immediately.
```

### Example 3
```
Input: meetings = [[9, 12], [10, 13], [11, 14], [12, 15]]
Output: 3
Explanation:
  At time 11, three meetings are ongoing: [9,12], [10,13], and [11,14].
  Room 1: 9-12, then 12-15
  Room 2: 10-13
  Room 3: 11-14
  Minimum rooms needed: 3
```

### Example 4
```
Input: meetings = [[14, 16]]
Output: 1
Explanation: Only one meeting, so only one room needed.
```

## Function Signature

### Python
```python
def min_meeting_rooms(meetings: list[list[int]]) -> int:
    pass
```

### JavaScript
```javascript
function minMeetingRooms(meetings) {
    // Your code here
}
```

### Java
```java
public int minMeetingRooms(int[][] meetings) {
    // Your code here
}
```

## Hints

1. Think about what happens at each time point - meetings start and end
2. Sort the start times and end times separately
3. Use two pointers to track starts and ends
4. The maximum number of overlapping meetings at any point is the answer
5. Alternatively, use a priority queue (min-heap) to track ongoing meetings
6. Time complexity: O(n log n), Space complexity: O(n)

## Tags
`array` `intervals` `sorting` `two-pointers` `heap` `medium`
