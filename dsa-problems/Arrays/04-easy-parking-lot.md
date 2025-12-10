# Parking Lot Availability

**Difficulty:** Easy
**Topic:** Arrays, Boolean Logic
**License:** Free to use for commercial purposes

## Problem Statement

A parking lot uses a sensor array where each element represents a parking spot. The value `0` indicates an empty spot and `1` indicates an occupied spot. A driver needs at least `k` consecutive empty spots to park their vehicle.

Given an array `spots` and an integer `k`, return `true` if there are at least `k` consecutive empty spots, otherwise return `false`.

## Constraints

- `1 <= spots.length <= 1000`
- `spots[i]` is either `0` or `1`
- `1 <= k <= spots.length`

## Examples

### Example 1
```
Input: spots = [1, 0, 0, 0, 1, 0], k = 3
Output: true
Explanation: There are 3 consecutive empty spots (positions 1, 2, 3).
```

### Example 2
```
Input: spots = [1, 0, 1, 0, 1], k = 2
Output: false
Explanation: No 2 consecutive empty spots available.
```

### Example 3
```
Input: spots = [0, 0, 0, 0], k = 2
Output: true
Explanation: There are 4 consecutive empty spots, which is more than required 2.
```

### Example 4
```
Input: spots = [1, 1, 1], k = 1
Output: false
Explanation: No empty spots at all.
```

## Function Signature

### Python
```python
def can_park(spots: list[int], k: int) -> bool:
    pass
```

### JavaScript
```javascript
function canPark(spots, k) {
    // Your code here
}
```

### Java
```java
public boolean canPark(int[] spots, int k) {
    // Your code here
}
```

## Hints

1. Track consecutive zeros while iterating
2. Reset counter when you encounter a 1
3. Return true if counter reaches k
4. Don't forget to check at the end of iteration

## Tags
`array` `consecutive-elements` `boolean` `easy`
