# Palindrome Linked List

**Difficulty:** Medium
**Topic:** Linked Lists, Two Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A sequence validator checks if data is symmetric. Given the head of a singly linked list, determine if it's a palindrome (reads same forward and backward).

Return `true` if palindrome, `false` otherwise.

## Constraints

- `1 <= number of nodes <= 100000`
- `0 <= node.val <= 9`

## Examples

### Example 1
```
Input: head = [1,2,2,1]
Output: true
```

### Example 2
```
Input: head = [1,2]
Output: false
```

### Example 3
```
Input: head = [1]
Output: true
```

## Function Signature

### Python
```python
def is_palindrome(head: ListNode) -> bool:
    pass
```

### JavaScript
```javascript
function isPalindrome(head) {
    // Your code here
}
```

### Java
```java
public boolean isPalindrome(ListNode head) {
    // Your code here
}
```

## Hints

1. Find middle using slow/fast pointers
2. Reverse second half
3. Compare first and second half
4. Time: O(n), Space: O(1)

## Tags
`linked-list` `two-pointers` `palindrome` `medium`
