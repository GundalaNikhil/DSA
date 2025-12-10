# Water Tank Collector

**Difficulty:** Medium
**Topic:** Arrays, Two Pointers, Greedy
**License:** Free to use for commercial purposes

## Problem Statement

A series of vertical water tanks are positioned in a line, each with a different height. You need to connect exactly two tanks with a horizontal pipe at their base to create a water collection system. The amount of water that can be collected is determined by the shorter tank's height multiplied by the distance between them.

Given an array `heights` where `heights[i]` represents the height of tank `i`, find the maximum amount of water that can be collected by optimally choosing two tanks.

The distance between tank `i` and tank `j` is `|i - j|`.

## Constraints

- `2 <= heights.length <= 1000`
- `1 <= heights[i] <= 1000`

## Examples

### Example 1
```
Input: heights = [3, 7, 5, 9, 2, 8]
Output: 28
Explanation:
  Choose tanks at index 1 (height=7) and index 5 (height=8).
  Water collected = min(7, 8) × |5 - 1| = 7 × 4 = 28
```

### Example 2
```
Input: heights = [2, 4, 3, 5]
Output: 6
Explanation:
  Choose tanks at index 0 (height=2) and index 3 (height=5).
  Water collected = min(2, 5) × |3 - 0| = 2 × 3 = 6

  Other options:
  Tanks 1 and 3: min(4, 5) × 2 = 8 (This is actually better!)

  Let me recalculate:
  - Tanks 0,1: min(2,4) × 1 = 2
  - Tanks 0,2: min(2,3) × 2 = 4
  - Tanks 0,3: min(2,5) × 3 = 6
  - Tanks 1,2: min(4,3) × 1 = 3
  - Tanks 1,3: min(4,5) × 2 = 8 ✓
  - Tanks 2,3: min(3,5) × 1 = 3

  Maximum is 8, not 6.
```

Let me correct Example 2:

### Example 2
```
Input: heights = [2, 4, 3, 5]
Output: 8
Explanation:
  Choose tanks at index 1 (height=4) and index 3 (height=5).
  Water collected = min(4, 5) × |3 - 1| = 4 × 2 = 8
```

### Example 3
```
Input: heights = [10, 5]
Output: 5
Explanation:
  Only two tanks available.
  Water collected = min(10, 5) × |1 - 0| = 5 × 1 = 5
```

### Example 4
```
Input: heights = [6, 6, 6, 6]
Output: 18
Explanation:
  Choose tanks at index 0 and index 3 (maximum distance).
  Water collected = min(6, 6) × |3 - 0| = 6 × 3 = 18
```

## Function Signature

### Python
```python
def max_water_collection(heights: list[int]) -> int:
    pass
```

### JavaScript
```javascript
function maxWaterCollection(heights) {
    // Your code here
}
```

### Java
```java
public int maxWaterCollection(int[] heights) {
    // Your code here
}
```

## Hints

1. Brute force: Try all pairs O(n²) - this works but is not optimal
2. Optimal approach: Use two pointers starting from both ends
3. The water collected depends on both the minimum height and the distance
4. Move the pointer with the smaller height inward (greedy choice)
5. Time complexity: O(n), Space complexity: O(1)

## Tags
`array` `two-pointers` `greedy` `medium`
