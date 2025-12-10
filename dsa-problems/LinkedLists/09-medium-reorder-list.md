# Reorder List

**Difficulty:** Medium
**Topic:** Linked Lists, Two Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A shuffle algorithm reorders playlist songs. Given a linked list `L0 → L1 → ... → Ln-1 → Ln`, reorder it to: `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...`

Modify the list in-place without changing node values.

## Constraints

- `1 <= number of nodes <= 50000`
- `1 <= node.val <= 1000`

## Examples

### Example 1
```
Input: head = [1,2,3,4]
Output: [1,4,2,3]
```

### Example 2
```
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
```

## Function Signature

### Python
```python
def reorder_list(head: ListNode) -> None:
    pass
```

### JavaScript
```javascript
function reorderList(head) {
    // Your code here
}
```

### Java
```java
public void reorderList(ListNode head) {
    // Your code here
}
```

## Hints

1. Find middle using slow/fast pointers
2. Reverse second half
3. Merge two halves alternately
4. Time: O(n), Space: O(1)

## Tags
`linked-list` `two-pointers` `reverse` `reorder` `medium`
