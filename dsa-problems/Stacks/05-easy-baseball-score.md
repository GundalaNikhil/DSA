# Arcade Game Scorekeeper

**Difficulty:** Easy
**Topic:** Stacks, Simulation
**License:** Free to use for commercial purposes

## Problem Statement

You are building a scorekeeper for a retro arcade game. The game records scores based on a sequence of operations:
- Integer `x`: Record a new score of `x`.
- `+`: Record a new score that is the sum of the previous two scores.
- `D`: Record a new score that is double the previous score.
- `C`: Invalidate (remove) the previous score.

Given an array of strings `ops`, return the sum of all the scores on the record after applying all operations.

## Constraints

- `1 <= ops.length <= 1000`
- Operations are valid (e.g., `+` will only appear if there are at least 2 previous scores)

## Examples

### Example 1
```
Input: ops = ["5", "2", "C", "D", "+"]
Output: 30
Explanation:
- "5": [5]
- "2": [5, 2]
- "C": [5] (2 is removed)
- "D": [5, 10] (double of 5)
- "+": [5, 10, 15] (5 + 10)
Total sum: 5 + 10 + 15 = 30
```

### Example 2
```
Input: ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
Output: 27
Explanation:
- "5": [5]
- "-2": [5, -2]
- "4": [5, -2, 4]
- "C": [5, -2]
- "D": [5, -2, -4]
- "9": [5, -2, -4, 9]
- "+": [5, -2, -4, 9, 5] (-4 + 9)
- "+": [5, -2, -4, 9, 5, 14] (9 + 5)
Total sum: 5 - 2 - 4 + 9 + 5 + 14 = 27
```

### Example 3
```
Input: ops = ["1"]
Output: 1
```

## Function Signature

### Python
```python
from typing import List

def calculate_arcade_score(ops: List[str]) -> int:
    pass
```

### JavaScript
```javascript
function calculateArcadeScore(ops) {
    // Your code here
}
```

### Java
```java
public int calculateArcadeScore(String[] ops) {
    // Your code here
}
```

## Hints

1. Use stack to maintain score record
2. Process each operation sequentially
3. For "D", double the last score (peek and multiply by 2)
4. For "C", remove last score (pop)
5. For "+", add sum of last two scores
6. Return sum of all elements in stack
7. Time complexity: O(n), Space complexity: O(n)

## Tags
`stack` `simulation` `array` `easy`
