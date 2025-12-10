# Reverse Linked List

**Difficulty:** Easy
**Topic:** Linked Lists, Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A browser's back button uses a reversed linked list. Given the head of a singly linked list, reverse the list and return the new head.

## Constraints

- `0 <= number of nodes <= 1000`
- `-100 <= node.val <= 100`

## Examples

### Example 1
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Explanation: List is reversed.
```

### Example 2
```
Input: head = [1,2]
Output: [2,1]
```

### Example 3
```
Input: head = []
Output: []
```

## Function Signature

### Python
```python
def reverse_list(head: ListNode) -> ListNode:
    pass
```

### JavaScript
```javascript
function reverseList(head) {
    // Your code here
}
```

### Java
```java
public ListNode reverseList(ListNode head) {
    // Your code here
}
```

## Hints

1. Use three pointers: prev, current, next
2. Iterate and reverse links
3. Can also solve recursively
4. Time: O(n), Space: O(1) iterative, O(n) recursive

## Tags
`linked-list` `pointers` `reverse` `easy`
