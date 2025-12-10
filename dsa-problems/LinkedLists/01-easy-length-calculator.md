# Linked List Length Calculator

**Difficulty:** Easy
**Topic:** Linked Lists, Traversal
**License:** Free to use for commercial purposes

## Problem Statement

A playlist manager uses a linked list to store songs. Given the head of a singly linked list, count and return the total number of nodes in the list.

## Constraints

- `0 <= number of nodes <= 1000`
- `-100 <= node.val <= 100`

## Examples

### Example 1
```
Input: head = [1,2,3,4,5]
Output: 5
Explanation: List has 5 nodes.
```

### Example 2
```
Input: head = []
Output: 0
Explanation: Empty list has 0 nodes.
```

### Example 3
```
Input: head = [42]
Output: 1
Explanation: Single node list.
```

## Function Signature

### Python
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def count_nodes(head: ListNode) -> int:
    pass
```

### JavaScript
```javascript
function countNodes(head) {
    // Your code here
}
```

### Java
```java
public int countNodes(ListNode head) {
    // Your code here
}
```

## Hints

1. Traverse the list using a pointer
2. Count each node as you visit it
3. Stop when you reach null
4. Time complexity: O(n), Space complexity: O(1)

## Tags
`linked-list` `traversal` `counting` `easy`
