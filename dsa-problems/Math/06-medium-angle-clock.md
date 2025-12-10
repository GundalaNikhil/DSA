# Clock Hand Angle Calculator

**Difficulty:** Medium
**Topic:** Math, Angles, Time Calculation
**License:** Free to use for commercial purposes

## Problem Statement

Given a time in hours and minutes (12-hour format), calculate the smaller angle between the hour hand and minute hand of an analog clock. The angle should be in degrees and represent the acute or right angle (≤ 180°).

## Constraints

- `1 <= hours <= 12`
- `0 <= minutes <= 59`
- Return angle as a floating-point number (can have decimal places)

## Examples

### Example 1
```
Input: hours = 3, minutes = 0
Output: 90.0
Explanation: At 3:00, the minute hand points to 12 and the hour hand points to 3.
Angle = 90 degrees.
```

### Example 2
```
Input: hours = 12, minutes = 30
Output: 165.0
Explanation: At 12:30, the minute hand points to 6 and the hour hand is halfway between 12 and 1.
Minute hand angle: 180° (pointing at 6)
Hour hand angle: 15° (12 + 30min movement = 0° + 15°)
Angle difference: |180 - 15| = 165 degrees.
```

### Example 3
```
Input: hours = 3, minutes = 15
Output: 7.5
Explanation: At 3:15, the minute hand points to 3 and the hour hand has moved past 3.
Minute hand: 90°
Hour hand: 90° + 7.5° = 97.5°
Angle: 97.5 - 90 = 7.5 degrees.
```

### Example 4
```
Input: hours = 6, minutes = 0
Output: 180.0
Explanation: At 6:00, hands are opposite each other, forming a straight line.
```

### Example 5
```
Input: hours = 9, minutes = 0
Output: 90.0
Explanation: At 9:00, hands form a right angle.
```

## Function Signature

### Python
```python
def calculate_clock_angle(hours: int, minutes: int) -> float:
    pass
```

### JavaScript
```javascript
function calculateClockAngle(hours, minutes) {
    // Your code here
}
```

### Java
```java
public double calculateClockAngle(int hours, int minutes) {
    // Your code here
}
```

## Hints

1. Minute hand moves 360° in 60 minutes = 6° per minute
2. Hour hand moves 360° in 12 hours (720 minutes) = 0.5° per minute
3. Hour hand angle = (hours % 12) × 30 + minutes × 0.5
4. Minute hand angle = minutes × 6
5. Find absolute difference, then return min(angle, 360 - angle) for smaller angle
6. Time complexity: O(1), Space complexity: O(1)

## Tags
`math` `angles` `time-calculation` `geometry` `medium`
