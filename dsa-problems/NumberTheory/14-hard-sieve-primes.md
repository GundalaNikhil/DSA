# Efficient Prime Mining

**Difficulty:** Hard
**Topic:** Number Theory, Sieve of Eratosthenes
**License:** Free to use for commercial purposes

## Problem Statement

In a cryptocurrency mining operation, "prime blocks" are highly valuable. You need to identify all prime numbers up to a maximum block height `limit`.

Return a list of all prime numbers less than or equal to `limit`.

## Constraints

- `2 <= limit <= 10^7`

## Examples

### Example 1
```
Input: limit = 10
Output: [2, 3, 5, 7]
```

### Example 2
```
Input: limit = 20
Output: [2, 3, 5, 7, 11, 13, 17, 19]
```

### Example 3
```
Input: limit = 2
Output: [2]
```

## Function Signature

### Python
```python
def mine_primes(limit: int) -> list[int]:
    pass
```

### JavaScript
```javascript
function minePrimes(limit) {
    // Your code here
}
```

### Java
```java
public List<Integer> minePrimes(int limit) {
    // Your code here
}
```

## Hints
1. Sieve of Eratosthenes
2. Mark multiples of each prime starting from p*p

## Tags
`number-theory` `sieve` `hard`
