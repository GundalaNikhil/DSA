# Digital Root Calculator

**Difficulty:** Easy
**Topic:** Number Theory, Digit Manipulation
**License:** Free to use for commercial purposes

## Problem Statement

Calculate the sum of all digits of a positive integer `n`. If `n` is negative, treat it as positive.

For example:
- 123 → 1 + 2 + 3 = 6
- 4567 → 4 + 5 + 6 + 7 = 22

## Constraints

- `-1000000 <= n <= 1000000`

## Examples

### Example 1
```
Input: n = 123
Output: 6
Explanation: 1 + 2 + 3 = 6
```

### Example 2
```
Input: n = 9999
Output: 36
Explanation: 9 + 9 + 9 + 9 = 36
```

### Example 3
```
Input: n = 0
Output: 0
Explanation: Sum of digits of 0 is 0.
```

### Example 4
```
Input: n = -456
Output: 15
Explanation: Treat as positive: 4 + 5 + 6 = 15
```

### Example 5
```
Input: n = 1000000
Output: 1
Explanation: 1 + 0 + 0 + 0 + 0 + 0 + 0 = 1
```

## Function Signature

### Python
```python
def sum_of_digits(n: int) -> int:
    pass
```

### JavaScript
```javascript
function sumOfDigits(n) {
    // Your code here
}
```

### Java
```java
public int sumOfDigits(int n) {
    // Your code here
}
```

## Hints

1. Convert negative numbers to positive using abs()
2. **Method 1**: Convert to string, iterate through characters, convert back to int and sum
3. **Method 2**: Use modulo and division:
   - Extract last digit: `digit = n % 10`
   - Remove last digit: `n = n // 10`
   - Repeat until n becomes 0
4. Time complexity: O(log n) where n is the number (number of digits)
5. Space complexity: O(1)

## Tags
`number-theory` `digit-manipulation` `modulo` `easy`
