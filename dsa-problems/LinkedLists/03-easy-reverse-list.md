# Train Reversal

**Difficulty:** Easy
**Topic:** Linked Lists, Recursion, Iteration
**License:** Free to use for commercial purposes

## Problem Statement

A train consists of multiple carriages linked together. The train needs to reverse its direction on the track, meaning the order of carriages must be completely flipped.

Given the head of a linked list representing the train carriages, reverse the list and return the new head.

## Constraints

- `0 <= number of carriages <= 5000`
- `-5000 <= carriage.val <= 5000`

## Examples

### Example 1
```
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
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
def reverse_train(head: ListNode) -> ListNode:
    pass
```

### JavaScript
```javascript
function reverseTrain(head) {
    // Your code here
}
```

### Java
```java
public ListNode reverseTrain(ListNode head) {
    // Your code here
}
```

## Hints

1. Iterative: Use three pointers (prev, curr, next)
2. Recursive: Reverse rest of list, then fix current node
3. Be careful with null checks
4. Time complexity: O(n), Space complexity: O(1) iterative

## Tags
`linked-list` `reverse` `recursion` `easy`
