# Summing Reversed Ledger Entries

**Difficulty:** Medium
**Topic:** Linked Lists, Math
**License:** Free to use for commercial purposes

## Problem Statement

An old accounting system stores large numbers as linked lists of digits, but in reverse order (least significant digit first). You need to sum two such ledger entries.

Given two linked lists `entry1` and `entry2` representing non-negative integers, add the two numbers and return the sum as a linked list in the same reverse order format.

## Constraints

- `1 <= number of nodes <= 100`
- `0 <= node.val <= 9`
- Numbers don't have leading zeros (except for the number 0 itself)

## Examples

### Example 1
```
Input: entry1 = [5, 2, 1], entry2 = [5, 9, 2]
Output: [0, 2, 4]
Explanation:
  entry1 represents 125
  entry2 represents 295
  Sum = 125 + 295 = 420
  Result list: [0, 2, 4] (reverse of 420)
```

### Example 2
```
Input: entry1 = [0], entry2 = [0]
Output: [0]
Explanation: 0 + 0 = 0
```

### Example 3
```
Input: entry1 = [9, 9], entry2 = [1]
Output: [0, 0, 1]
Explanation:
  entry1 represents 99
  entry2 represents 1
  Sum = 99 + 1 = 100
  Result list: [0, 0, 1]
```

## Function Signature

### Python
```python
def sum_ledger_entries(entry1: ListNode, entry2: ListNode) -> ListNode:
    pass
```

### JavaScript
```javascript
function sumLedgerEntries(entry1, entry2) {
    // Your code here
}
```

### Java
```java
public ListNode sumLedgerEntries(ListNode entry1, ListNode entry2) {
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
