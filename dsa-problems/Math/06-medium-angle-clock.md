# Analog Clock Angle

**Difficulty:** Medium
**Topic:** Math, Angles, Time Calculation
**License:** Free to use for commercial purposes

## Problem Statement

Calculate the smaller angle (in degrees) between the hour and minute hands of an analog clock at a given time.

## Constraints

- `1 <= hours <= 12`
- `0 <= minutes <= 59`
- Return float

## Examples

### Example 1
```
Input: hours = 4, minutes = 20
Output: 10.0
Explanation:
Minute hand at 4 (120 deg).
Hour hand at 4 + 20/60 = 4.33 (130 deg).
Diff = 10.
```

### Example 2
```
Input: hours = 11, minutes = 11
Output: 109.5
Explanation:
Minute hand: 11 * 6 = 66 deg.
Hour hand: 11 * 30 + 11 * 0.5 = 330 + 5.5 = 335.5 deg.
Diff = 335.5 - 66 = 269.5.
Smaller angle = 360 - 269.5 = 90.5.
Wait, let's re-calc:
335.5 - 66 = 269.5.
360 - 269.5 = 90.5.
Correct.
```

### Example 3
```
Input: hours = 12, minutes = 0
Output: 0.0
```

## Function Signature

### Python
```python
def clock_angle(hours: int, minutes: int) -> float:
    pass
```

### JavaScript
```javascript
function clockAngle(hours, minutes) {
    // Your code here
}
```

### Java
```java
public double clockAngle(int hours, int minutes) {
    // Your code here
}
```

## Hints
1. Minute hand: 6 deg per min
2. Hour hand: 30 deg per hour + 0.5 deg per min
3. Abs diff, then min(diff, 360-diff)

## Tags
`math` `geometry` `medium`
