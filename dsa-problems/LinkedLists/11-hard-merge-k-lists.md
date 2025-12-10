# Multi-lane Highway Merge

**Difficulty:** Hard
**Topic:** Linked Lists, Heap, Divide and Conquer
**License:** Free to use for commercial purposes

## Problem Statement

A traffic control system needs to merge traffic from multiple lanes into a single main highway. Each lane has cars arriving at different times (represented by timestamps), and the cars in each lane are already sorted by arrival time.

Given an array of `k` linked lists where each list represents a lane of sorted timestamps, merge all lanes into one sorted sequence of cars.

Return the head of the merged linked list.

## Constraints

- `k == lanes.length`
- `0 <= k <= 10000`
- `0 <= lanes[i].length <= 500`
- `0 <= lanes[i].val <= 10000` (timestamps)
- Each lane is sorted in ascending order

## Examples

### Example 1
```
Input: lanes = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: Merging timestamps from 3 lanes.
```

### Example 2
```
Input: lanes = []
Output: []
```

### Example 3
```
Input: lanes = [[]]
Output: []
```

## Function Signature

### Python
```python
def merge_traffic_lanes(lanes: list[ListNode]) -> ListNode:
    pass
```

### JavaScript
```javascript
function mergeTrafficLanes(lanes) {
    // Your code here
}
```

### Java
```java
public ListNode mergeTrafficLanes(ListNode[] lanes) {
    // Your code here
}
```

## Hints

1. Use min heap to track smallest timestamp among all lane heads
2. Or use divide and conquer (merge pairs of lanes)
3. Heap: Time O(N log k), Space O(k)
4. Divide: Time O(N log k), Space O(1)

## Tags
`linked-list` `heap` `divide-conquer` `merge` `hard`
