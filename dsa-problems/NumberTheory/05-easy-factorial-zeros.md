# Trailing Zeros in Factorial

**Difficulty:** Easy
**Topic:** Number Theory, Factorials
**License:** Free to use for commercial purposes

## Problem Statement

Calculate how many trailing zeros are in the factorial of a given number `n` (n!).

Trailing zeros are the zeros at the end of a number. For example:
- 10! = 3628800 has 2 trailing zeros
- 5! = 120 has 1 trailing zero

**Important**: Do NOT actually calculate the factorial (it would be too large). Use a mathematical approach.

## Constraints

- `0 <= n <= 10000`

## Examples

### Example 1
```
Input: n = 5
Output: 1
Explanation: 5! = 120, which has 1 trailing zero.
```

### Example 2
```
Input: n = 10
Output: 2
Explanation: 10! = 3628800, which has 2 trailing zeros.
```

### Example 3
```
Input: n = 25
Output: 6
Explanation: 25! has 6 trailing zeros.
```

### Example 4
```
Input: n = 0
Output: 0
Explanation: 0! = 1, no trailing zeros.
```

### Example 5
```
Input: n = 100
Output: 24
Explanation: 100! has 24 trailing zeros.
```

## Function Signature

### Python
```python
def count_trailing_zeros(n: int) -> int:
    pass
```

### JavaScript
```javascript
function countTrailingZeros(n) {
    // Your code here
}
```

### Java
```java
public int countTrailingZeros(int n) {
    // Your code here
}
```

## Hints

1. Trailing zeros come from factors of 10
2. 10 = 2 × 5
3. In n!, there are always more factors of 2 than factors of 5
4. So count the number of times 5 appears as a factor in n!
5. Formula: floor(n/5) + floor(n/25) + floor(n/125) + floor(n/625) + ...
6. Keep dividing n by 5 and sum the quotients
7. Time complexity: O(log₅ n), Space complexity: O(1)

## Example Calculation:
For n = 25:
- 25/5 = 5 (numbers divisible by 5: 5, 10, 15, 20, 25)
- 25/25 = 1 (numbers divisible by 25: 25, which contributes an extra 5)
- Total = 5 + 1 = 6

## Tags
`number-theory` `factorial` `trailing-zeros` `divisibility` `easy`
