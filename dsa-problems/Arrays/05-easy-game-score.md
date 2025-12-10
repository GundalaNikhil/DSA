# Game Score Calculator

**Difficulty:** Easy
**Topic:** Arrays, Accumulation
**License:** Free to use for commercial purposes

## Problem Statement

In a mobile game, a player earns points in each level. However, the game has a special rule: if a player scores exactly `0` in any level, all previous points are forfeited (reset to 0), but the game continues.

Given an array `scores` representing points earned in each level in order, calculate the total points the player has at the end.

## Constraints

- `1 <= scores.length <= 500`
- `-100 <= scores[i] <= 100`

## Examples

### Example 1
```
Input: scores = [10, 20, 30]
Output: 60
Explanation: No zeros encountered, sum all scores: 10 + 20 + 30 = 60
```

### Example 2
```
Input: scores = [15, 25, 0, 10, 20]
Output: 30
Explanation: After level 3 (score 0), previous points are forfeited. Only 10 + 20 = 30 count.
```

### Example 3
```
Input: scores = [5, 0, 10, 0, 8]
Output: 8
Explanation: First 0 resets (5 lost), second 0 resets (10 lost), only 8 remains.
```

### Example 4
```
Input: scores = [0, 50, 25]
Output: 75
Explanation: Starting with 0 doesn't reset anything, then 50 + 25 = 75
```

## Function Signature

### Python
```python
def calculate_final_score(scores: list[int]) -> int:
    pass
```

### JavaScript
```javascript
function calculateFinalScore(scores) {
    // Your code here
}
```

### Java
```java
public int calculateFinalScore(int[] scores) {
    // Your code here
}
```

## Hints

1. Iterate through the array maintaining a running total
2. When you encounter 0, reset the total to 0
3. Continue adding subsequent scores
4. Time complexity: O(n), Space complexity: O(1)

## Tags
`array` `simulation` `accumulation` `easy`
