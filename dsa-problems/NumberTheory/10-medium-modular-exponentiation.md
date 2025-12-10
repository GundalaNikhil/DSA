# Encrypted Message Power

**Difficulty:** Medium
**Topic:** Number Theory, Modular Arithmetic
**License:** Free to use for commercial purposes

## Problem Statement

In an encryption algorithm, a message `m` (base) is raised to a power `e` (exponent) modulo `n`. Calculate `(m^e) % n` efficiently.

## Constraints

- `1 <= m, n <= 10^9`
- `0 <= e <= 10^9`

## Examples

### Example 1
```
Input: m = 4, e = 13, n = 497
Output: 445
Explanation: 4^13 mod 497 = 67108864 mod 497 = 445.
```

### Example 2
```
Input: m = 3, e = 5, n = 7
Output: 5
Explanation: 243 % 7 = 5.
```

### Example 3
```
Input: m = 10, e = 0, n = 5
Output: 1
```

## Function Signature

### Python
```python
def encrypt_message(m: int, e: int, n: int) -> int:
    pass
```

### JavaScript
```javascript
function encryptMessage(m, e, n) {
    // Your code here
}
```

### Java
```java
public int encryptMessage(int m, int e, int n) {
    // Your code here
}
```

## Hints
1. Binary exponentiation (square and multiply)
2. Apply modulo at each step

## Tags
`number-theory` `modular-exponentiation` `medium`
