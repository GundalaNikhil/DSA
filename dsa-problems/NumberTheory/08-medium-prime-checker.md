# Secure Key Validation

**Difficulty:** Medium
**Topic:** Number Theory, Prime Numbers
**License:** Free to use for commercial purposes

## Problem Statement

A cryptographic system requires keys to be prime numbers for security. Given a proposed key `n`, validate if it is a prime number.

Return `true` if prime, `false` otherwise.

## Constraints

- `1 <= n <= 10^7`

## Examples

### Example 1
```
Input: n = 29
Output: true
```

### Example 2
```
Input: n = 15
Output: false
Explanation: 3 * 5 = 15.
```

### Example 3
```
Input: n = 1
Output: false
```

## Function Signature

### Python
```python
def is_valid_key(n: int) -> bool:
    pass
```

### JavaScript
```javascript
function isValidKey(n) {
    // Your code here
}
```

### Java
```java
public boolean isValidKey(int n) {
    // Your code here
}
```

## Hints
1. Check divisibility up to sqrt(n)
2. Handle 2 and even numbers separately

## Tags
`number-theory` `prime` `medium`
