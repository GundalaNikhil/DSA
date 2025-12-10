# Interleaving Data Packets

**Difficulty:** Medium
**Topic:** Linked Lists, Two Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A data transmission protocol requires reordering packets for error correction. Given a stream of packets as a linked list `P0 → P1 → ... → Pn-1 → Pn`, reorder it to the pattern: `P0 → Pn → P1 → Pn-1 → P2 → Pn-2 → ...`

Modify the list in-place without changing the packet values.

## Constraints

- `1 <= number of packets <= 50000`
- `1 <= packet.id <= 1000`

## Examples

### Example 1
```
Input: head = [10, 20, 30, 40]
Output: [10, 40, 20, 30]
Explanation:
  Original: 10 -> 20 -> 30 -> 40
  Reordered: First(10) -> Last(40) -> Second(20) -> SecondLast(30)
```

### Example 2
```
Input: head = [1, 2, 3, 4, 5]
Output: [1, 5, 2, 4, 3]
Explanation:
  Original: 1 -> 2 -> 3 -> 4 -> 5
  Reordered: 1 -> 5 -> 2 -> 4 -> 3
```

### Example 3
```
Input: head = [100, 200]
Output: [100, 200]
Explanation: With only two nodes, the order remains the same.
```

## Function Signature

### Python
```python
def interleave_packets(head: ListNode) -> None:
    pass
```

### JavaScript
```javascript
function interleavePackets(head) {
    // Your code here
}
```

### Java
```java
public void interleavePackets(ListNode head) {
    // Your code here
}
```

## Hints

1. Find middle using slow/fast pointers
2. Reverse second half
3. Merge two halves alternately
4. Time: O(n), Space: O(1)

## Tags
`linked-list` `two-pointers` `reverse` `reorder` `medium`
