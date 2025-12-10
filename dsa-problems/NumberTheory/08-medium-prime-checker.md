# Prime Number Validator

**Difficulty:** Medium
**Topic:** Number Theory, Prime Numbers
**License:** Free to use for commercial purposes

## Problem Statement

Determine whether a given positive integer `n` is a prime number. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Implement an efficient algorithm that works for large values of `n`.

## Constraints

- `1 <= n <= 10000000` (10⁷)

## Examples

### Example 1
```
Input: n = 17
Output: true
Explanation: 17 is only divisible by 1 and 17.
```

### Example 2
```
Input: n = 20
Output: false
Explanation: 20 is divisible by 1, 2, 4, 5, 10, 20.
```

### Example 3
```
Input: n = 1
Output: false
Explanation: 1 is not considered prime by definition.
```

### Example 4
```
Input: n = 2
Output: true
Explanation: 2 is the only even prime number.
```

### Example 5
```
Input: n = 9999991
Output: true
Explanation: 9999991 is prime (large prime number).
```

## Function Signature

### Python
```python
def is_prime(n: int) -> bool:
    pass
```

### JavaScript
```javascript
function isPrime(n) {
    // Your code here
}
```

### Java
```java
public boolean isPrime(int n) {
    // Your code here
}
```

## Hints

1. **Naive approach**: Check divisibility from 2 to n-1
   - Time: O(n) - too slow for large n

2. **Optimized approach**: Only check up to √n
   - If n has a divisor > √n, it must also have a divisor < √n
   - Time: O(√n)

3. **Further optimization**:
   - Handle special cases: n ≤ 1 (false), n = 2 (true), even numbers > 2 (false)
   - Only check odd divisors: 2, then 3, 5, 7, 9, 11... up to √n

4. **Algorithm outline**:
   ```
   if n <= 1: return false
   if n == 2: return true
   if n % 2 == 0: return false
   for i from 3 to √n (step by 2):
       if n % i == 0: return false
   return true
   ```

5. Time complexity: O(√n)
6. Space complexity: O(1)

## Tags
`number-theory` `prime-numbers` `divisibility` `optimization` `medium`
