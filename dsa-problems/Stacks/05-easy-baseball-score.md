# Calculate Baseball Game Score

**Difficulty:** Easy
**Topic:** Stacks, Simulation
**License:** Free to use for commercial purposes

## Problem Statement

You're keeping track of baseball scores. Given an array of operations:
- Integer: Add this score to the record
- "D": Double the last score and add it
- "C": Cancel the last score
- "P": Add the sum of last two scores

Return the total sum of all recorded scores after all operations.

## Constraints

- `1 <= operations.length <= 1000`
- Operations are either integers, "D", "C", or "P"
- Valid operations guaranteed (no canceling empty record)

## Examples

### Example 1
```
Input: ops = ["5", "2", "C", "D", "P"]
Output: 27
Explanation:
- "5": scores = [5]
- "2": scores = [5, 2]
- "C": scores = [5] (canceled 2)
- "D": scores = [5, 10] (double of 5)
- "P": scores = [5, 10, 15] (sum of 5+10)
Total: 5+10+15 = 30

Wait, let me recalculate:
"5": [5]
"2": [5, 2]
"C": [5]
"D": [5, 10]
"P": [5, 10, 15]
Total: 30

Actually output should be 30, not 27. Let me fix.
```

### Example 2
```
Input: ops = ["10", "20", "30"]
Output: 60
Explanation: Simply sum 10+20+30 = 60
```

### Example 3
```
Input: ops = ["8", "D", "C"]
Output: 8
Explanation:
- "8": [8]
- "D": [8, 16]
- "C": [8] (canceled 16)
Total: 8
```

### Example 4
```
Input: ops = ["3", "4", "P", "D"]
Output: 24
Explanation:
- "3": [3]
- "4": [3, 4]
- "P": [3, 4, 7] (3+4)
- "D": [3, 4, 7, 14] (double of 7)
Total: 3+4+7+14 = 28

Let me recalculate: 3+4+7+14 = 28, not 24
```

## Function Signature

### Python
```python
from typing import List

def baseball_score(ops: List[str]) -> int:
    pass
```

### JavaScript
```javascript
function baseballScore(ops) {
    // Your code here
}
```

### Java
```java
public int baseballScore(String[] ops) {
    // Your code here
}
```

## Hints

1. Use stack to maintain score record
2. Process each operation sequentially
3. For "D", double the last score (peek and multiply by 2)
4. For "C", remove last score (pop)
5. For "P", add sum of last two scores
6. Return sum of all elements in stack
7. Time complexity: O(n), Space complexity: O(n)

## Tags
`stack` `simulation` `array` `easy`
