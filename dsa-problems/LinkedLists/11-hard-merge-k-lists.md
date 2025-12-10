# Merge K Sorted Lists

**Difficulty:** Hard
**Topic:** Linked Lists, Heap, Divide and Conquer
**License:** Free to use for commercial purposes

## Problem Statement

A log aggregator merges multiple sorted log streams. Given an array of `k` sorted linked lists, merge all lists into one sorted list.

Return the head of the merged linked list.

## Constraints

- `k == lists.length`
- `0 <= k <= 10000`
- `0 <= lists[i].length <= 500`
- `-10000 <= lists[i][j] <= 10000`
- Lists are sorted in ascending order

## Examples

### Example 1
```
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

### Example 2
```
Input: lists = []
Output: []
```

### Example 3
```
Input: lists = [[]]
Output: []
```

## Function Signature

### Python
```python
def merge_k_lists(lists: list[ListNode]) -> ListNode:
    pass
```

### JavaScript
```javascript
function mergeKLists(lists) {
    // Your code here
}
```

### Java
```java
public ListNode mergeKLists(ListNode[] lists) {
    // Your code here
}
```

## Hints

1. Use min heap to track smallest elements
2. Or use divide and conquer (merge pairs)
3. Heap: Time O(N log k), Space O(k)
4. Divide: Time O(N log k), Space O(1)

## Tags
`linked-list` `heap` `divide-conquer` `merge` `hard`
