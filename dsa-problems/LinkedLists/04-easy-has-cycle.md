# Cycle Detector

**Difficulty:** Easy
**Topic:** Linked Lists, Two Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A memory leak detector needs to find circular references. Given the head of a linked list, determine if the list has a cycle. A cycle exists if a node can be reached again by following next pointers.

Return `true` if cycle exists, `false` otherwise.

## Constraints

- `0 <= number of nodes <= 10000`
- `-100000 <= node.val <= 100000`

## Examples

### Example 1
```
Input: head = [3,2,0,-4], cycle at node index 1
Output: true
Explanation: Tail connects to node at index 1.
```

### Example 2
```
Input: head = [1,2], cycle at node index 0
Output: true
```

### Example 3
```
Input: head = [1]
Output: false
```

## Function Signature

### Python
```python
def has_cycle(head: ListNode) -> bool:
    pass
```

### JavaScript
```javascript
function hasCycle(head) {
    // Your code here
}
```

### Java
```java
public boolean hasCycle(ListNode head) {
    // Your code here
}
```

## Hints

1. Floyd's cycle detection (tortoise and hare)
2. Use slow and fast pointers
3. If they meet, cycle exists
4. Time: O(n), Space: O(1)

## Tags
`linked-list` `two-pointers` `cycle-detection` `easy`
