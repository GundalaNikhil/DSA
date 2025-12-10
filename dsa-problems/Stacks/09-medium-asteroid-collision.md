# Particle Collider Simulation

**Difficulty:** Medium
**Topic:** Stacks, Simulation
**License:** Free to use for commercial purposes

## Problem Statement

Physicists are simulating high-energy particle collisions. Particles move in a 1D tube. Each particle has a size (absolute value) and direction (sign: positive = right, negative = left).

When two particles collide:
- If they are moving in the same direction, they don't collide.
- If they move towards each other, they collide.
- The smaller particle is annihilated.
- If they are the same size, both are annihilated.

Given an array `particles` representing the initial state, return the state of particles after all collisions are resolved.

## Constraints

- `2 <= particles.length <= 10000`
- `-1000 <= particles[i] <= 1000`
- `particles[i] != 0`

## Examples

### Example 1
```
Input: particles = [3, 6, -3]
Output: [3, 6]
Explanation:
- 6 (right) and -3 (left) collide.
- 6 is larger than 3, so -3 is annihilated.
- Result: [3, 6]
```

### Example 2
```
Input: particles = [4, -4]
Output: []
Explanation: 4 and -4 collide. Equal size, both annihilated.
```

### Example 3
```
Input: particles = [10, 2, -5]
Output: [10]
Explanation:
- 2 and -5 collide: -5 wins (5 > 2). Array becomes [10, -5].
- 10 and -5 collide: 10 wins (10 > 5). Array becomes [10].
```

### Example 4
```
Input: particles = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: Left-moving particles are on the left, right-moving on the right. No collisions occur.
```

## Function Signature

### Python
```python
from typing import List

def simulate_collisions(particles: List[int]) -> List[int]:
    pass
```

### JavaScript
```javascript
function simulateCollisions(particles) {
    // Your code here
}
```

### Java
```java
public int[] simulateCollisions(int[] particles) {
    // Your code here
}
```

## Hints

1. Use stack to track surviving particles moving right
2. For each particle moving right, push to stack
3. For particle moving left, compare with stack top (moving right)
4. While left particle survives collisions, keep popping from stack
5. Time complexity: O(n), Space complexity: O(n)

## Tags
`stack` `array` `simulation` `collision` `medium`
