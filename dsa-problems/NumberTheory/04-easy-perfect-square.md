# Square Room Verification

**Difficulty:** Easy
**Topic:** Number Theory, Perfect Squares
**License:** Free to use for commercial purposes

## Problem Statement

An architect is designing rooms. Some clients specifically request perfectly square rooms where the floor area `area` corresponds to an integer side length (e.g., 25 sq ft -> 5x5).

Given an integer `area`, determine if it represents a perfect square room.

Return `true` if it is a perfect square, `false` otherwise.

## Constraints

- `1 <= area <= 2^31 - 1`

## Examples

### Example 1
```
Input: area = 49
Output: true
Explanation: 7 * 7 = 49.
```

### Example 2
```
Input: area = 50
Output: false
Explanation: sqrt(50) is approx 7.07.
```

### Example 3
```
Input: area = 1
Output: true
```

## Function Signature

### Python
```python
def is_square_room(area: int) -> bool:
    pass
```

### JavaScript
```javascript
function isSquareRoom(area) {
    // Your code here
}
```

### Java
```java
public boolean isSquareRoom(int area) {
    // Your code here
}
```

## Hints
1. Calculate integer square root
2. Check if root * root == area

## Tags
`number-theory` `perfect-square` `easy`
