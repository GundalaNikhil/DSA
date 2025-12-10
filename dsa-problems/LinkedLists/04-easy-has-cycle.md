# Circular Race Track Detection

**Difficulty:** Easy
**Topic:** Linked Lists, Two Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A race track simulation needs to detect if a track layout contains a loop. The track is represented as a linked list where each node is a checkpoint. If a checkpoint points back to a previous checkpoint, a loop exists.

Given the head of a linked list, determine if the linked list has a cycle in it.

Return `true` if there is a cycle, `false` otherwise.

## Constraints

- `0 <= number of checkpoints <= 10000`
- `-100000 <= checkpoint.val <= 100000`

## Examples

### Example 1
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```

### Example 2
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```

### Example 3
```
Input: head = [1], pos = -1
Output: false
Explanation: No cycle.
```

## Function Signature

### Python
```python
def has_track_cycle(head: ListNode) -> bool:
    pass
```

### JavaScript
```javascript
function hasTrackCycle(head) {
    // Your code here
}
```

### Java
```java
public boolean hasTrackCycle(ListNode head) {
    // Your code here
}
```

## Hints

1. Use Floyd's Cycle-Finding Algorithm (Tortoise and Hare)
2. Use two pointers: slow and fast
3. If fast catches up to slow, there is a cycle
4. If fast reaches null, there is no cycle
5. Time complexity: O(n), Space complexity: O(1)

## Tags
`linked-list` `two-pointers` `cycle-detection` `easy`
