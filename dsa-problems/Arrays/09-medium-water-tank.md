# Space Telescope Alignment

**Difficulty:** Medium
**Topic:** Arrays, Two Pointers, Greedy
**License:** Free to use for commercial purposes

## Problem Statement

A series of signal towers are positioned in a line on a distant planet, each with a specific signal strength (represented by height). To establish a stable communication link, you must choose exactly two towers. The data throughput of the link is limited by the weaker tower's signal strength multiplied by the physical distance between them.

Given an array `signal_strengths` where `signal_strengths[i]` represents the strength of tower `i`, find the maximum amount of data throughput that can be achieved by optimally choosing two towers.

The distance between tower `i` and tower `j` is `|i - j|`.

## Constraints

- `2 <= signal_strengths.length <= 1000`
- `1 <= signal_strengths[i] <= 1000`

## Examples

### Example 1
```
Input: signal_strengths = [3, 7, 5, 9, 2, 8]
Output: 28
Explanation:
  Choose towers at index 1 (strength=7) and index 5 (strength=8).
  Throughput = min(7, 8) × |5 - 1| = 7 × 4 = 28
```

### Example 2
```
Input: signal_strengths = [2, 4, 3, 5]
Output: 8
Explanation:
  Choose towers at index 1 (strength=4) and index 3 (strength=5).
  Throughput = min(4, 5) × |3 - 1| = 4 × 2 = 8
```

### Example 3
```
Input: signal_strengths = [10, 5]
Output: 5
Explanation:
  Only two towers available.
  Throughput = min(10, 5) × |1 - 0| = 5 × 1 = 5
```

### Example 4
```
Input: signal_strengths = [6, 6, 6, 6]
Output: 18
Explanation:
  Choose towers at index 0 and index 3 (maximum distance).
  Throughput = min(6, 6) × |3 - 0| = 6 × 3 = 18
```

## Function Signature

### Python
```python
def max_data_throughput(signal_strengths: list[int]) -> int:
    pass
```

### JavaScript
```javascript
function maxDataThroughput(signalStrengths) {
    // Your code here
}
```

### Java
```java
public int maxDataThroughput(int[] signalStrengths) {
    // Your code here
}
```

## Hints

1. Brute force: Try all pairs O(n²) - this works but is not optimal
2. Optimal approach: Use two pointers starting from both ends
3. The throughput depends on both the minimum strength and the distance
4. Move the pointer with the smaller strength inward (greedy choice)
5. Time complexity: O(n), Space complexity: O(1)

## Tags
`array` `two-pointers` `greedy` `medium`
