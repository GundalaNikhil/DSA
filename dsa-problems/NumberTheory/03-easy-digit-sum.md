# Serial Number Checksum

**Difficulty:** Easy
**Topic:** Number Theory, Digit Manipulation
**License:** Free to use for commercial purposes

## Problem Statement

A manufacturing plant verifies product serial numbers by calculating a simple checksum: the sum of all individual digits in the serial number.

Given a serial number `n` (which can be negative if it represents a return code), calculate its checksum. Treat negative numbers as positive for the sum.

## Constraints

- `-10^9 <= n <= 10^9`

## Examples

### Example 1
```
Input: n = 8421
Output: 15
Explanation: 8+4+2+1 = 15.
```

### Example 2
```
Input: n = -505
Output: 10
Explanation: 5+0+5 = 10.
```

### Example 3
```
Input: n = 0
Output: 0
```

## Function Signature

### Python
```python
def calculate_checksum(n: int) -> int:
    pass
```

### JavaScript
```javascript
function calculateChecksum(n) {
    // Your code here
}
```

### Java
```java
public int calculateChecksum(int n) {
    // Your code here
}
```

## Hints
1. Use abs()
2. Modulo 10 to get last digit
3. Integer division by 10 to remove last digit

## Tags
`number-theory` `digits` `easy`
