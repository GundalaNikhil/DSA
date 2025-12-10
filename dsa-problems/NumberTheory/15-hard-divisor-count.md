# Locker Toggle Puzzle

**Difficulty:** Hard
**Topic:** Number Theory, Divisors
**License:** Free to use for commercial purposes

## Problem Statement

A school has `n` lockers. Students perform a toggle game. The final state of a locker depends on the number of times it was toggled. Specifically, we are interested in the number of divisors of `n` to determine some property (e.g., if it ends up open or closed, though here we just want the count).

Given `n`, calculate the total number of its divisors.

## Constraints

- `1 <= n <= 10^9`

## Examples

### Example 1
```
Input: n = 12
Output: 6
Explanation: 1, 2, 3, 4, 6, 12.
```

### Example 2
```
Input: n = 36
Output: 9
Explanation: 1, 2, 3, 4, 6, 9, 12, 18, 36.
```

### Example 3
```
Input: n = 13
Output: 2
Explanation: 1, 13.
```

## Function Signature

### Python
```python
def count_divisors(n: int) -> int:
    pass
```

### JavaScript
```javascript
function countDivisors(n) {
    // Your code here
}
```

### Java
```java
public int countDivisors(int n) {
    // Your code here
}
```

## Hints
1. Prime factorization: n = p1^a1 * p2^a2...
2. Count = (a1+1) * (a2+1)...

## Tags
`number-theory` `divisors` `hard`
