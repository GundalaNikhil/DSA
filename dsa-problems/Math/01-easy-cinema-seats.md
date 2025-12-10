# Conference Hall Seating

**Difficulty:** Easy
**Topic:** Math, Basic Operations
**License:** Free to use for commercial purposes

## Problem Statement

A conference center has a main hall with `rows` of chairs, and each row contains `chairsPerRow` chairs. An event organizer wants to book the hall for `attendees` people. Determine if all attendees can be seated, and if so, how many empty chairs will remain.

Return an array `[canSeat, emptyChairs]` where:
- `canSeat` is `1` if all attendees can be seated, `0` otherwise
- `emptyChairs` is the number of empty chairs remaining (or `-1` if capacity is insufficient)

## Constraints

- `1 <= rows <= 500`
- `1 <= chairsPerRow <= 100`
- `1 <= attendees <= 100000`

## Examples

### Example 1
```
Input: rows = 12, chairsPerRow = 20, attendees = 200
Output: [1, 40]
Explanation: Total capacity = 12 * 20 = 240. 240 - 200 = 40 empty chairs.
```

### Example 2
```
Input: rows = 8, chairsPerRow = 10, attendees = 85
Output: [0, -1]
Explanation: Capacity = 80. Attendees = 85. Not enough space.
```

### Example 3
```
Input: rows = 5, chairsPerRow = 5, attendees = 25
Output: [1, 0]
Explanation: Exact fit.
```

## Function Signature

### Python
```python
def check_hall_capacity(rows: int, chairsPerRow: int, attendees: int) -> list[int]:
    pass
```

### JavaScript
```javascript
function checkHallCapacity(rows, chairsPerRow, attendees) {
    // Your code here
}
```

### Java
```java
public int[] checkHallCapacity(int rows, int chairsPerRow, int attendees) {
    // Your code here
}
```

## Hints
1. Calculate total capacity
2. Compare with attendees count
3. Return appropriate status code and remainder

## Tags
`math` `basic-operations` `easy`
