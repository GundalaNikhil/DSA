# Faulty Wagon Removal

**Difficulty:** Easy
**Topic:** Linked Lists
**License:** Free to use for commercial purposes

## Problem Statement

A train maintenance crew needs to remove a faulty wagon from the middle of a train. However, they only have direct access to the faulty wagon itself, not the engine (head) or the previous wagon.

Given a node `wagon` to be deleted (which is guaranteed not to be the last node), delete it from the linked list.

## Constraints

- The number of wagons is in the range `[2, 1000]`.
- `-1000 <= wagon.val <= 1000`
- The given node is not the tail.

## Examples

### Example 1
```
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
```

### Example 2
```
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9.
```

## Function Signature

### Python
```python
def remove_faulty_wagon(wagon: ListNode) -> None:
    pass
```

### JavaScript
```javascript
function removeFaultyWagon(wagon) {
    // Your code here
}
```

### Java
```java
public void removeFaultyWagon(ListNode wagon) {
    // Your code here
}
```

## Hints

1. You can't access the previous node
2. Copy the value of the next node to the current node
3. Delete the next node by skipping it
4. Time complexity: O(1), Space complexity: O(1)

## Tags
`linked-list` `deletion` `easy`
