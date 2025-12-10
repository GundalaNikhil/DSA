# Asteroid Collision Simulation

**Difficulty:** Medium
**Topic:** Stacks, Simulation
**License:** Free to use for commercial purposes

## Problem Statement

Given an array of asteroids where absolute value is size and sign is direction (positive = right, negative = left), simulate collisions.

When two asteroids meet:
- Same direction: no collision
- Different direction: smaller explodes, or both if equal

Return the state after all collisions.

## Constraints

- `2 <= asteroids.length <= 10000`
- `-1000 <= asteroids[i] <= 1000`
- `asteroids[i] != 0`

## Examples

### Example 1
```
Input: asteroids = [5, 10, -5]
Output: [5, 10]
Explanation:
- 10 and -5 collide: 10 wins (10 > 5)
- Result: [5, 10]
```

### Example 2
```
Input: asteroids = [8, -8]
Output: []
Explanation: 8 and -8 collide with equal size, both explode
```

### Example 3
```
Input: asteroids = [10, 2, -5]
Output: [10]
Explanation:
- 2 and -5 collide: -5 wins (5 > 2)
- 10 and -5 collide: 10 wins (10 > 5)
- Result: [10]
```

### Example 4
```
Input: asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: [-2, -1] go left, [1, 2] go right, no collision
```

## Function Signature

### Python
```python
from typing import List

def asteroid_collision(asteroids: List[int]) -> List[int]:
    pass
```

### JavaScript
```javascript
function asteroidCollision(asteroids) {
    // Your code here
}
```

### Java
```java
public int[] asteroidCollision(int[] asteroids) {
    // Your code here
}
```

## Hints

1. Use stack to track surviving asteroids going right
2. For each asteroid going right, push to stack
3. For asteroid going left, compare with stack top (going right)
4. While left asteroid survives collisions, keep popping from stack
5. Time complexity: O(n), Space complexity: O(n)

## Tags
`stack` `array` `simulation` `collision` `medium`
