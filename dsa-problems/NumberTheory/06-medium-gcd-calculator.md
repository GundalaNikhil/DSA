# Greatest Common Divisor Finder

**Difficulty:** Medium
**Topic:** Number Theory, GCD, Euclidean Algorithm
**License:** Free to use for commercial purposes

## Problem Statement

Find the Greatest Common Divisor (GCD) of two positive integers `a` and `b`. The GCD is the largest positive integer that divides both numbers without a remainder.

Implement an efficient algorithm to calculate GCD.

## Constraints

- `1 <= a, b <= 1000000000` (10⁹)
- Both numbers are positive integers

## Examples

### Example 1
```
Input: a = 12, b = 8
Output: 4
Explanation: Divisors of 12: {1, 2, 3, 4, 6, 12}
Divisors of 8: {1, 2, 4, 8}
Common divisors: {1, 2, 4}
Greatest: 4
```

### Example 2
```
Input: a = 17, b = 19
Output: 1
Explanation: Both are prime numbers, GCD = 1 (coprime).
```

### Example 3
```
Input: a = 100, b = 50
Output: 50
Explanation: 50 divides 100 exactly.
```

### Example 4
```
Input: a = 54, b = 24
Output: 6
Explanation: GCD(54, 24) = 6
```

### Example 5
```
Input: a = 1000000000, b = 500000000
Output: 500000000
Explanation: 500000000 divides 1000000000 exactly.
```

## Function Signature

### Python
```python
def calculate_gcd(a: int, b: int) -> int:
    pass
```

### JavaScript
```javascript
function calculateGcd(a, b) {
    // Your code here
}
```

### Java
```java
public int calculateGcd(int a, int b) {
    // Your code here
}
```

## Hints

1. **Euclidean Algorithm** (most efficient):
   - GCD(a, b) = GCD(b, a % b)
   - Base case: GCD(a, 0) = a
   - Recursive or iterative approach

2. **Example trace** for GCD(54, 24):
   - GCD(54, 24) = GCD(24, 54%24) = GCD(24, 6)
   - GCD(24, 6) = GCD(6, 24%6) = GCD(6, 0)
   - GCD(6, 0) = 6

3. Avoid brute force (checking all divisors) for large numbers
4. Time complexity: O(log min(a, b))
5. Space complexity: O(1) for iterative, O(log min(a, b)) for recursive

## Tags
`number-theory` `gcd` `euclidean-algorithm` `recursion` `medium`
