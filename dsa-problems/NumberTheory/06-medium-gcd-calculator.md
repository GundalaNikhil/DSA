# Resource Allocation GCD

**Difficulty:** Medium
**Topic:** Number Theory, GCD, Euclidean Algorithm
**License:** Free to use for commercial purposes

## Problem Statement

A logistics manager has two shipments of goods with quantities `a` and `b`. They want to package these goods into identical containers such that each container holds the same amount, and no goods are left over. Find the maximum number of items that can be placed in each container (Greatest Common Divisor).

## Constraints

- `1 <= a, b <= 10^9`

## Examples

### Example 1
```
Input: a = 48, b = 18
Output: 6
Explanation:
Divisors of 48: 1, 2, 3, 4, 6, 8, 12, 16, 24, 48.
Divisors of 18: 1, 2, 3, 6, 9, 18.
Common: 1, 2, 3, 6.
Max: 6.
```

### Example 2
```
Input: a = 101, b = 103
Output: 1
Explanation: Both are prime.
```

### Example 3
```
Input: a = 20, b = 100
Output: 20
```

## Function Signature

### Python
```python
def calculate_max_container_size(a: int, b: int) -> int:
    pass
```

### JavaScript
```javascript
function calculateMaxContainerSize(a, b) {
    // Your code here
}
```

### Java
```java
public int calculateMaxContainerSize(int a, int b) {
    // Your code here
}
```

## Hints
1. Euclidean algorithm: gcd(a, b) = gcd(b, a % b)

## Tags
`number-theory` `gcd` `medium`
