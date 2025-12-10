# Symmetric DNA Strand Check

**Difficulty:** Medium
**Topic:** Linked Lists, Two Pointers
**License:** Free to use for commercial purposes

## Problem Statement

Biologists are analyzing DNA strands represented as linked lists of nucleotide markers (integers). A symmetric strand is one that reads the same forwards and backwards.

Given the head of a singly linked list representing a DNA strand, determine if it is symmetric (a palindrome).

Return `true` if it is symmetric, `false` otherwise.

## Constraints

- `1 <= number of markers <= 100000`
- `0 <= marker.val <= 9`

## Examples

### Example 1
```
Input: head = [5, 9, 3, 9, 5]
Output: true
Explanation: The sequence reads 5-9-3-9-5 in both directions.
```

### Example 2
```
Input: head = [1, 2, 3]
Output: false
Explanation: Forward: 1-2-3, Backward: 3-2-1. Not symmetric.
```

### Example 3
```
Input: head = [8, 8]
Output: true
Explanation: Two identical markers form a symmetric strand.
```

### Example 4
```
Input: head = [1, 2, 2, 1]
Output: true
Explanation: Even length symmetric strand.
```

## Function Signature

### Python
```python
def is_symmetric_strand(head: ListNode) -> bool:
    pass
```

### JavaScript
```javascript
function isSymmetricStrand(head) {
    // Your code here
}
```

### Java
```java
public boolean isSymmetricStrand(ListNode head) {
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
