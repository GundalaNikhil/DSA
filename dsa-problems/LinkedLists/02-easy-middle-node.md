# Caravan Center Supply

**Difficulty:** Easy
**Topic:** Linked Lists, Two Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A caravan of camels is trekking across the desert, linked together in a single line. The leader needs to distribute water supplies starting from the middle of the caravan.

Given the head of a linked list representing the caravan, return the middle node. If there are two middle nodes (even number of camels), return the second middle node.

## Constraints

- `1 <= number of camels <= 100`
- `1 <= camel.val <= 100`

## Examples

### Example 1
```
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle camel is node 3.
```

### Example 2
```
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
```

## Function Signature

### Python
```python
def find_middle_camel(head: ListNode) -> ListNode:
    pass
```

### JavaScript
```javascript
function findMiddleCamel(head) {
    // Your code here
}
```

### Java
```java
public ListNode findMiddleCamel(ListNode head) {
    // Your code here
}
```

## Hints

1. Use two pointers: slow and fast
2. Move slow one step, fast two steps
3. When fast reaches end, slow is at middle
4. Time complexity: O(n), Space complexity: O(1)

## Tags
`linked-list` `two-pointers` `middle` `easy`
