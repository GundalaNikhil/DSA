# Remove Nth Node From End

**Difficulty:** Medium
**Topic:** Linked Lists, Two Pointers
**License:** Free to use for commercial purposes

## Problem Statement

An undo system removes recent actions. Given the head of a linked list and an integer `n`, remove the `n`th node from the end of the list.

Return the head of the modified list.

## Constraints

- `1 <= number of nodes <= 30`
- `0 <= node.val <= 100`
- `1 <= n <= number of nodes`

## Examples

### Example 1
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Explanation: Remove 4 (2nd from end).
```

### Example 2
```
Input: head = [1], n = 1
Output: []
```

### Example 3
```
Input: head = [1,2], n = 1
Output: [1]
```

## Function Signature

### Python
```python
def remove_nth_from_end(head: ListNode, n: int) -> ListNode:
    pass
```

### JavaScript
```javascript
function removeNthFromEnd(head, n) {
    // Your code here
}
```

### Java
```java
public ListNode removeNthFromEnd(ListNode head, int n) {
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
