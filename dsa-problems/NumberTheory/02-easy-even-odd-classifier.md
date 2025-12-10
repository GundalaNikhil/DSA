# Number Parity Classifier

**Difficulty:** Easy
**Topic:** Number Theory, Parity
**License:** Free to use for commercial purposes

## Problem Statement

Given an array of integers, count how many numbers are even and how many are odd.

Return an array `[evenCount, oddCount]`.

## Constraints

- `1 <= numbers.length <= 10000`
- `-1000000 <= numbers[i] <= 1000000`
- Note: 0 is considered even
- Negative numbers follow standard parity rules (-2 is even, -3 is odd)

## Examples

### Example 1
```
Input: numbers = [1, 2, 3, 4, 5]
Output: [2, 3]
Explanation: Even: {2, 4}, Odd: {1, 3, 5}
```

### Example 2
```
Input: numbers = [10, 20, 30]
Output: [3, 0]
Explanation: All numbers are even.
```

### Example 3
```
Input: numbers = [0, -1, -2, 5, 8]
Output: [3, 2]
Explanation: Even: {0, -2, 8}, Odd: {-1, 5}
```

### Example 4
```
Input: numbers = [7]
Output: [0, 1]
Explanation: Single odd number.
```

### Example 5
```
Input: numbers = [-10, -20, -30, -40]
Output: [4, 0]
Explanation: All negative even numbers.
```

## Function Signature

### Python
```python
def count_parity(numbers: list[int]) -> list[int]:
    pass
```

### JavaScript
```javascript
function countParity(numbers) {
    // Your code here
}
```

### Java
```java
public int[] countParity(int[] numbers) {
    // Your code here
}
```

## Hints

1. Use modulo operator to check parity: `n % 2`
2. Even number: `n % 2 == 0`
3. Odd number: `n % 2 != 0` or `n % 2 == 1` (for positive) or `n % 2 == -1` (for negative in some languages)
4. Iterate through array and count
5. Handle negative numbers correctly
6. Time complexity: O(n), Space complexity: O(1)

## Tags
`number-theory` `parity` `even-odd` `iteration` `easy`
