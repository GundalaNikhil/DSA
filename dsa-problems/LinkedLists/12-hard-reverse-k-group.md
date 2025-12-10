# Packet Batch Reversal

**Difficulty:** Hard
**Topic:** Linked Lists, Recursion, Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A network router processes data packets in batches. For security encoding, the router needs to reverse the order of packets in every group of `k` packets. If the number of remaining packets at the end is less than `k`, they should remain in their original order.

Given the head of a linked list representing the stream of packets and an integer `k`, reverse the nodes in groups of `k`.

Return the head of the modified packet stream.

## Constraints

- `1 <= number of packets <= 5000`
- `0 <= packet.val <= 1000`
- `1 <= k <= number of packets`

## Examples

### Example 1
```
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Explanation: Packets reversed in groups of 2. Last packet (5) remains as is.
```

### Example 2
```
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Explanation: First 3 packets reversed. Remaining 2 packets (4,5) are less than k, so unchanged.
```

### Example 3
```
Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Explanation: Reversing groups of 1 does nothing.
```

## Function Signature

### Python
```python
def reverse_packet_batches(head: ListNode, k: int) -> ListNode:
    pass
```

### JavaScript
```javascript
function reversePacketBatches(head, k) {
    // Your code here
}
```

### Java
```java
public ListNode reversePacketBatches(ListNode head, int k) {
    // Your code here
}
```

## Hints

1. Count if k packets are available
2. Reverse k packets if available
3. Recursively process rest of the stream
4. Time: O(n), Space: O(n/k) for recursion

## Tags
`linked-list` `recursion` `reverse` `pointers` `hard`
