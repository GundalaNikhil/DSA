# Merge Two Sorted Lists

**Difficulty:** Medium
**Topic:** Linked Lists, Two Pointers, Merge
**License:** Free to use for commercial purposes

## Problem Statement

A file merger combines two sorted logs. Given the heads of two sorted linked lists `list1` and `list2`, merge them into one sorted list by splicing together the nodes.

Return the head of the merged linked list.

## Constraints

- `0 <= number of nodes <= 50` in each list
- `-100 <= node.val <= 100`
- Both lists are sorted in non-decreasing order

## Examples

### Example 1
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

### Example 2
```
Input: list1 = [], list2 = []
Output: []
```

### Example 3
```
Input: list1 = [], list2 = [0]
Output: [0]
```

## Function Signature

### Python
```python
def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    pass
```

### JavaScript
```javascript
function mergeTwoLists(list1, list2) {
    // Your code here
}
```

### Java
```java
public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
    // Your code here
}
```

## Hints

1. Use dummy node to simplify edge cases
2. Compare values and link smaller node
3. Handle remaining nodes
4. Time: O(n+m), Space: O(1)

## Tags
`linked-list` `two-pointers` `merge` `sorted` `medium`
