# Cinema Seat Arrangement

**Difficulty:** Easy
**Topic:** Math, Basic Operations
**License:** Free to use for commercial purposes

## Problem Statement

A cinema has `rows` of seats, and each row contains `seatsPerRow` seats. The cinema wants to host a group booking of `totalPeople` people. Determine if all the people can be seated in the cinema, and if so, how many empty seats will remain.

Return an array `[canSeat, emptySeats]` where:
- `canSeat` is `1` if all people can be seated, `0` otherwise
- `emptySeats` is the number of empty seats remaining (or `-1` if people cannot be seated)

## Constraints

- `1 <= rows <= 500`
- `1 <= seatsPerRow <= 100`
- `1 <= totalPeople <= 100000`

## Examples

### Example 1
```
Input: rows = 10, seatsPerRow = 15, totalPeople = 120
Output: [1, 30]
Explanation: Total seats = 10 × 15 = 150. After seating 120 people, 30 seats remain empty.
```

### Example 2
```
Input: rows = 5, seatsPerRow = 8, totalPeople = 50
Output: [0, -1]
Explanation: Total seats = 5 × 8 = 40. Cannot seat 50 people as there are only 40 seats.
```

### Example 3
```
Input: rows = 20, seatsPerRow = 25, totalPeople = 500
Output: [1, 0]
Explanation: Total seats = 20 × 25 = 500. Exactly enough seats, 0 empty seats remain.
```

### Example 4
```
Input: rows = 1, seatsPerRow = 1, totalPeople = 1
Output: [1, 0]
Explanation: Minimum case - exactly one seat for one person.
```

## Function Signature

### Python
```python
def check_cinema_capacity(rows: int, seatsPerRow: int, totalPeople: int) -> list[int]:
    pass
```

### JavaScript
```javascript
function checkCinemaCapacity(rows, seatsPerRow, totalPeople) {
    // Your code here
}
```

### Java
```java
public int[] checkCinemaCapacity(int rows, int seatsPerRow, int totalPeople) {
    // Your code here
}
```

## Hints

1. Calculate total capacity by multiplying rows by seatsPerRow
2. Compare total capacity with totalPeople
3. If capacity >= totalPeople, calculate remaining seats
4. Time complexity: O(1), Space complexity: O(1)

## Tags
`math` `basic-operations` `multiplication` `easy`
