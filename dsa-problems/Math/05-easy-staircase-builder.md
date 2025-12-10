# Staircase Block Counter

**Difficulty:** Easy
**Topic:** Math, Arithmetic Sequence
**License:** Free to use for commercial purposes

## Problem Statement

A child is building a staircase using toy blocks. The staircase has `steps` levels, where:
- Level 1 (ground level) has 1 block
- Level 2 has 2 blocks
- Level 3 has 3 blocks
- And so on...

Calculate the total number of blocks needed to build a staircase with `steps` levels.

## Constraints

- `1 <= steps <= 10000`

## Examples

### Example 1
```
Input: steps = 3
Output: 6
Explanation: Level 1: 1 block, Level 2: 2 blocks, Level 3: 3 blocks. Total = 1 + 2 + 3 = 6.
```

### Example 2
```
Input: steps = 5
Output: 15
Explanation: 1 + 2 + 3 + 4 + 5 = 15 blocks.
```

### Example 3
```
Input: steps = 1
Output: 1
Explanation: Only one level with 1 block.
```

### Example 4
```
Input: steps = 10
Output: 55
Explanation: 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55 blocks.
```

### Example 5
```
Input: steps = 100
Output: 5050
Explanation: Sum of first 100 natural numbers = 5050.
```

## Function Signature

### Python
```python
def count_staircase_blocks(steps: int) -> int:
    pass
```

### JavaScript
```javascript
function countStaircaseBlocks(steps) {
    // Your code here
}
```

### Java
```java
public int countStaircaseBlocks(int steps) {
    // Your code here
}
```

## Hints

1. This is the sum of first n natural numbers
2. Formula: sum = n × (n + 1) / 2
3. Avoid using loops for large values of steps
4. Use the mathematical formula for O(1) time complexity
5. Be careful with integer overflow for very large steps

## Tags
`math` `arithmetic-sequence` `sum-formula` `easy`
