# Rainwater Harvesting System

**Difficulty:** Hard
**Topic:** Arrays, Stack, Two Pointers
**License:** Free to use for commercial purposes

## Problem Statement

A building has a series of rooftop sections at different heights. After rain, water gets trapped between the sections, forming pools. Given an array `heights` where each element represents the height of a roof section, calculate the total volume of rainwater that can be trapped.

Water can only be trapped if there are higher sections on both left and right sides.

## Constraints

- `1 <= heights.length <= 10000`
- `0 <= heights[i] <= 50000`

## Examples

### Example 1
```
Input: heights = [4, 2, 0, 3, 2, 5]
Output: 9
Explanation:
  Visualization (rotated 90° for clarity):
  Index:     0  1  2  3  4  5
  Heights:   4  2  0  3  2  5

  Water trapped above each position:
  - Position 0 (height 4): 0 (no left wall)
  - Position 1 (height 2): min(4, 5) - 2 = 2
  - Position 2 (height 0): min(4, 5) - 0 = 4
  - Position 3 (height 3): min(4, 5) - 3 = 1
  - Position 4 (height 2): min(4, 5) - 2 = 2
  - Position 5 (height 5): 0 (no right wall)

  Total: 0 + 2 + 4 + 1 + 2 + 0 = 9
```

### Example 2
```
Input: heights = [3, 0, 2, 0, 4]
Output: 7
Explanation:
  Water trapped:
  - Position 0: 0
  - Position 1 (height 0): min(3, 4) - 0 = 3
  - Position 2 (height 2): min(3, 4) - 2 = 1
  - Position 3 (height 0): min(3, 4) - 0 = 3
  - Position 4: 0

  Total: 0 + 3 + 1 + 3 + 0 = 7
```

### Example 3
```
Input: heights = [5, 4, 3, 2, 1]
Output: 0
Explanation: No water can be trapped (strictly decreasing).
```

### Example 4
```
Input: heights = [2, 1, 2, 1, 2]
Output: 2
Explanation:
  Water trapped:
  - Position 0: 0
  - Position 1: min(2, 2) - 1 = 1
  - Position 2: 0 (peak)
  - Position 3: min(2, 2) - 1 = 1
  - Position 4: 0

  Total: 1 + 1 = 2
```

## Function Signature

### Python
```python
def trapped_rainwater(heights: list[int]) -> int:
    pass
```

### JavaScript
```javascript
function trappedRainwater(heights) {
    // Your code here
}
```

### Java
```java
public int trappedRainwater(int[] heights) {
    // Your code here
}
```

## Hints

1. For each position, water level = min(max_left, max_right)
2. Water trapped at position i = max(0, water_level - heights[i])
3. Approach 1: Precompute max_left and max_right arrays - O(n) time, O(n) space
4. Approach 2: Two pointers from both ends - O(n) time, O(1) space
5. Approach 3: Use a stack to track potential water containers
6. The two-pointer approach is most optimal

## Tags
`array` `two-pointers` `stack` `dynamic-programming` `hard`
