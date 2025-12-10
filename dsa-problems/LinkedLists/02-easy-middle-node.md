# Find Middle Node

**Difficulty:** Easy
**Topic:** Linked Lists, Two Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A data structure needs to quickly access the middle element. Given the head of a singly linked list, return the middle node. If there are two middle nodes, return the second one.

## Constraints

- `1 <= number of nodes <= 100`
- `-100 <= node.val <= 100`

## Examples

### Example 1
```
Input: head = [1,2,3,4,5]
Output: Node with value 3
Explanation: Middle node is the 3rd node.
```

### Example 2
```
Input: head = [1,2,3,4,5,6]
Output: Node with value 4
Explanation: Two middle nodes (3,4), return second.
```

## Function Signature

### Python
```python
def find_middle(head: ListNode) -> ListNode:
    pass
```

### JavaScript
```javascript
function findMiddle(head) {
    // Your code here
}
```

### Java
```java
public ListNode findMiddle(ListNode head) {
    // Your code here
}
```

## Hints

1. Use slow and fast pointers
2. Fast moves 2 steps, slow moves 1 step
3. When fast reaches end, slow is at middle
4. Time: O(n), Space: O(1)

## Tags
`linked-list` `two-pointers` `slow-fast` `easy`
