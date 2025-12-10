# Stadium Seat Row Expansion

**Difficulty:** Medium
**Topic:** Math, Pattern Recognition, Sequences
**License:** Free to use for commercial purposes

## Problem Statement

A stadium section is designed such that the first row has `base_seats`. Each subsequent row has `increment` more seats than the previous one.

Given `rows`, `base_seats`, and `increment`, calculate the total number of seats in the section.

## Constraints

- `1 <= rows <= 100000`
- `1 <= base_seats <= 100`
- `1 <= increment <= 10`

## Examples

### Example 1
```
Input: rows = 4, base_seats = 10, increment = 2
Output: 52
Explanation:
Row 1: 10
Row 2: 12
Row 3: 14
Row 4: 16
Total: 10+12+14+16 = 52.
```

### Example 2
```
Input: rows = 3, base_seats = 5, increment = 5
Output: 30
Explanation: 5 + 10 + 15 = 30.
```

### Example 3
```
Input: rows = 1, base_seats = 100, increment = 10
Output: 100
```

## Function Signature

### Python
```python
def count_stadium_seats(rows: int, base_seats: int, increment: int) -> int:
    pass
```

### JavaScript
```javascript
function countStadiumSeats(rows, baseSeats, increment) {
    // Your code here
}
```

### Java
```java
public int countStadiumSeats(int rows, int baseSeats, int increment) {
    // Your code here
}
```

## Hints
1. Arithmetic series sum formula: n/2 * (2a + (n-1)d)

## Tags
`math` `arithmetic-sequence` `medium`
