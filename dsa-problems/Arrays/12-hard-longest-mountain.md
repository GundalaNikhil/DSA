# Longest Mountain Subarray

**Difficulty:** Hard
**Topic:** Arrays, Two Pointers, Greedy
**License:** Free to use for commercial purposes

## Problem Statement

A hiking trail's elevation profile is represented as an array. A "mountain" in this array is defined as a subarray that:
1. Has a length of at least 3
2. Consists of strictly increasing elements followed by strictly decreasing elements
3. Has at least one increasing element and at least one decreasing element

Given an array `elevation`, find the length of the longest mountain subarray.

## Constraints

- `1 <= elevation.length <= 10000`
- `0 <= elevation[i] <= 10000`

## Examples

### Example 1
```
Input: elevation = [5, 10, 15, 12, 8, 6, 9, 11]
Output: 5
Explanation:
  Mountain from index 0 to 4: [5, 10, 15, 12, 8]
  - Increasing: 5→10→15
  - Decreasing: 15→12→8
  Length: 5

  Another potential: [6, 9, 11] but this is only increasing (not a mountain).
```

### Example 2
```
Input: elevation = [2, 5, 5, 7, 3, 1]
Output: 0
Explanation:
  No valid mountain exists.
  [2, 5, 5, 7] - has plateau (5, 5), not strictly increasing
  [5, 7, 3, 1] - would work but [5, 5] makes it invalid
  [7, 3, 1] - only decreasing, needs increasing part too
  Answer: 0
```

### Example 3
```
Input: elevation = [1, 3, 5, 4, 3, 6, 8, 7, 5, 2]
Output: 6
Explanation:
  Longest mountain: [3, 6, 8, 7, 5, 2] at indices 4-9
  - Increasing: 3→6→8
  - Decreasing: 8→7→5→2
  Length: 6
```

### Example 4
```
Input: elevation = [10, 9, 8, 7]
Output: 0
Explanation: Only decreasing, no increasing part, so no mountain.
```

## Function Signature

### Python
```python
def longest_mountain(elevation: list[int]) -> int:
    pass
```

### JavaScript
```javascript
function longestMountain(elevation) {
    // Your code here
}
```

### Java
```java
public int longestMountain(int[] elevation) {
    // Your code here
}
```

## Hints

1. Find all peaks (where elevation[i-1] < elevation[i] > elevation[i+1])
2. For each peak, expand left while strictly increasing and right while strictly decreasing
3. Calculate the mountain length for each peak
4. Track the maximum length found
5. Alternatively, use two-pass approach: track consecutive ups and downs
6. Time complexity: O(n), Space complexity: O(1)

## Tags
`array` `two-pointers` `greedy` `peaks` `hard`
