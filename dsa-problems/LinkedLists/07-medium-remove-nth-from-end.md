# Removing Outdated Log Entry

**Difficulty:** Medium
**Topic:** Linked Lists, Two Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A server log system stores entries in a linked list. To save space, the system periodically removes specific old entries. You need to remove the `n`-th log entry from the end of the list.

Given the head of a linked list and an integer `n`, remove the `n`-th node from the end of the list and return the head of the modified list.

## Constraints

- `1 <= number of logs <= 30`
- `0 <= log.id <= 100`
- `1 <= n <= number of logs`

## Examples

### Example 1
```
Input: logs = [101, 202, 303, 404, 505], n = 2
Output: [101, 202, 303, 505]
Explanation: The 2nd node from the end is 404. Removing it leaves [101, 202, 303, 505].
```

### Example 2
```
Input: logs = [10], n = 1
Output: []
Explanation: Removing the only node (1st from end) leaves an empty list.
```

### Example 3
```
Input: logs = [50, 60], n = 1
Output: [50]
Explanation: Removing the last node (60).
```

### Example 4
```
Input: logs = [50, 60], n = 2
Output: [60]
Explanation: Removing the first node (2nd from end).
```

## Function Signature

### Python
```python
def remove_nth_log(head: ListNode, n: int) -> ListNode:
    pass
```

### JavaScript
```javascript
function removeNthLog(head, n) {
    // Your code here
}
```

### Java
```java
public ListNode removeNthLog(ListNode head, int n) {
    // Your code here
}
```

## Hints

1. Use two pointers with n gap between them
2. Move both until first reaches end
3. Second pointer is at node before target
4. Time: O(n), Space: O(1)

## Tags
`linked-list` `two-pointers` `deletion` `medium`
