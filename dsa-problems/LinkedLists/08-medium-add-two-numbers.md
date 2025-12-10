# Add Two Numbers

**Difficulty:** Medium
**Topic:** Linked Lists, Math
**License:** Free to use for commercial purposes

## Problem Statement

A calculator stores numbers as linked lists. Given two linked lists representing non-negative integers where digits are stored in reverse order, add the two numbers and return the sum as a linked list.

## Constraints

- `1 <= number of nodes <= 100`
- `0 <= node.val <= 9`
- Numbers don't have leading zeros

## Examples

### Example 1
```
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
```

### Example 2
```
Input: l1 = [0], l2 = [0]
Output: [0]
```

### Example 3
```
Input: l1 = [9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,0,1]
Explanation: 999 + 9999 = 10998
```

## Function Signature

### Python
```python
def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    pass
```

### JavaScript
```javascript
function addTwoNumbers(l1, l2) {
    // Your code here
}
```

### Java
```java
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    // Your code here
}
```

## Hints

1. Simulate addition with carry
2. Process both lists simultaneously
3. Don't forget final carry
4. Time: O(max(m,n)), Space: O(max(m,n))

## Tags
`linked-list` `math` `carry` `medium`
