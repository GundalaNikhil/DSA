# Delete Given Node

**Difficulty:** Easy
**Topic:** Linked Lists, Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A task list allows deleting items. Given a reference to a node in a singly linked list (not the head), delete that node from the list. The node to be deleted is not the tail.

## Constraints

- Number of nodes: `[2, 1000]`
- `-1000 <= node.val <= 1000`
- Node to delete is not tail
- All node values are unique

## Examples

### Example 1
```
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: Node with value 5 is deleted.
```

### Example 2
```
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
```

## Function Signature

### Python
```python
def delete_node(node: ListNode) -> None:
    pass
```

### JavaScript
```javascript
function deleteNode(node) {
    // Your code here
}
```

### Java
```java
public void deleteNode(ListNode node) {
    // Your code here
}
```

## Hints

1. Can't access previous node
2. Copy next node's data to current
3. Delete the next node instead
4. Time: O(1), Space: O(1)

## Tags
`linked-list` `pointers` `deletion` `easy`
