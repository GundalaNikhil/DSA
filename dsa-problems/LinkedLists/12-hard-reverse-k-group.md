# Reverse Nodes in K-Group

**Difficulty:** Hard
**Topic:** Linked Lists, Recursion, Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A data transformer reverses segments of data. Given the head of a linked list and an integer `k`, reverse the nodes in groups of `k`. If remaining nodes are less than `k`, keep them as is.

Return the head of the modified list.

## Constraints

- `1 <= number of nodes <= 5000`
- `0 <= node.val <= 1000`
- `1 <= k <= number of nodes`

## Examples

### Example 1
```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
```

### Example 2
```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
```

### Example 3
```
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
```

## Function Signature

### Python
```python
def reverse_k_group(head: ListNode, k: int) -> ListNode:
    pass
```

### JavaScript
```javascript
function reverseKGroup(head, k) {
    // Your code here
}
```

### Java
```java
public ListNode reverseKGroup(ListNode head, int k) {
    // Your code here
}
```

## Hints

1. Count if k nodes are available
2. Reverse k nodes if available
3. Recursively process rest
4. Time: O(n), Space: O(n/k) for recursion

## Tags
`linked-list` `recursion` `reverse` `pointers` `hard`
