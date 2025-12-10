# Sort Linked List

**Difficulty:** Hard
**Topic:** Linked Lists, Merge Sort, Sorting
**License:** Free to use for commercial purposes

## Problem Statement

A priority queue needs efficient sorting. Given the head of a linked list, sort it in ascending order using O(n log n) time complexity and O(1) space (excluding recursion stack).

Return the head of the sorted list.

## Constraints

- `0 <= number of nodes <= 50000`
- `-100000 <= node.val <= 100000`

## Examples

### Example 1
```
Input: head = [4,2,1,3]
Output: [1,2,3,4]
```

### Example 2
```
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
```

### Example 3
```
Input: head = []
Output: []
```

## Function Signature

### Python
```python
def sort_list(head: ListNode) -> ListNode:
    pass
```

### JavaScript
```javascript
function sortList(head) {
    // Your code here
}
```

### Java
```java
public ListNode sortList(ListNode head) {
    // Your code here
}
```

## Hints

1. Use merge sort for linked lists
2. Find middle using slow/fast pointers
3. Recursively sort both halves
4. Merge sorted halves
5. Time: O(n log n), Space: O(log n) recursion

## Tags
`linked-list` `merge-sort` `sorting` `divide-conquer` `hard`
