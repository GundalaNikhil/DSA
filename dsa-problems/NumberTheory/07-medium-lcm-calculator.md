# Least Common Multiple Finder

**Difficulty:** Medium
**Topic:** Number Theory, LCM, GCD
**License:** Free to use for commercial purposes

## Problem Statement

Find the Least Common Multiple (LCM) of two positive integers `a` and `b`. The LCM is the smallest positive integer that is divisible by both `a` and `b`.

## Constraints

- `1 <= a, b <= 100000`
- Result will fit in a 64-bit integer

## Examples

### Example 1
```
Input: a = 12, b = 8
Output: 24
Explanation:
  Multiples of 12: 12, 24, 36, 48...
  Multiples of 8: 8, 16, 24, 32...
  Smallest common: 24
```

### Example 2
```
Input: a = 5, b = 7
Output: 35
Explanation: Both are prime, LCM = 5 × 7 = 35
```

### Example 3
```
Input: a = 10, b = 15
Output: 30
Explanation: LCM(10, 15) = 30
```

### Example 4
```
Input: a = 1, b = 100
Output: 100
Explanation: LCM with 1 is always the other number.
```

### Example 5
```
Input: a = 21, b = 6
Output: 42
Explanation: LCM(21, 6) = 42
```

## Function Signature

### Python
```python
def calculate_lcm(a: int, b: int) -> int:
    pass
```

### JavaScript
```javascript
function calculateLcm(a, b) {
    // Your code here
}
```

### Java
```java
public long calculateLcm(int a, int b) {
    // Your code here
}
```

## Hints

1. **Key relationship**: LCM(a, b) × GCD(a, b) = a × b
2. Therefore: LCM(a, b) = (a × b) / GCD(a, b)
3. First calculate GCD using Euclidean algorithm
4. Then use the formula to find LCM
5. **Important**: Compute (a / GCD) × b instead of (a × b) / GCD to avoid integer overflow
6. Time complexity: O(log min(a, b))
7. Space complexity: O(1)

## Example Calculation:
For a = 12, b = 8:
- GCD(12, 8) = 4
- LCM(12, 8) = (12 × 8) / 4 = 96 / 4 = 24

## Tags
`number-theory` `lcm` `gcd` `mathematics` `medium`
