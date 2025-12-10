# Solar Flare Intensity

**Difficulty:** Hard
**Topic:** Arrays, Two Pointers, Greedy
**License:** Free to use for commercial purposes

## Problem Statement

Astronomers are analyzing data from a solar observatory. The intensity of a solar flare is recorded over time as an array of integers. A "flare event" is defined as a continuous period where the intensity strictly increases to a peak and then strictly decreases.

A valid flare event must:
1. Have a duration of at least 3 time units.
2. Consist of strictly increasing intensities followed by strictly decreasing intensities.
3. Have at least one increasing step and at least one decreasing step.

Given an array `intensities`, find the duration (length of the subarray) of the longest flare event.

## Constraints

- `1 <= intensities.length <= 10000`
- `0 <= intensities[i] <= 10000`

## Examples

### Example 1
```
Input: intensities = [5, 10, 15, 12, 8, 6, 9, 11]
Output: 5
Explanation:
  Flare event from index 0 to 4: [5, 10, 15, 12, 8]
  - Rising phase: 5→10→15
  - Falling phase: 15→12→8
  Duration: 5

  Another potential: [6, 9, 11] but this is only rising (not a complete event).
```

### Example 2
```
Input: intensities = [2, 5, 5, 7, 3, 1]
Output: 0
Explanation:
  No valid flare event exists.
  [2, 5, 5, 7] - has plateau (5, 5), not strictly increasing
  [5, 7, 3, 1] - would work but [5, 5] makes it invalid
  [7, 3, 1] - only falling, needs rising phase too
  Answer: 0
```

### Example 3
```
Input: intensities = [1, 3, 5, 4, 3, 6, 8, 7, 5, 2]
Output: 6
Explanation:
  Longest flare event: [3, 6, 8, 7, 5, 2] at indices 4-9
  - Rising: 3→6→8
  - Falling: 8→7→5→2
  Duration: 6
```

### Example 4
```
Input: intensities = [10, 9, 8, 7]
Output: 0
Explanation: Only falling, no rising phase, so no event.
```

## Function Signature

### Python
```python
def longest_flare_duration(intensities: list[int]) -> int:
    pass
```

### JavaScript
```javascript
function longestFlareDuration(intensities) {
    // Your code here
}
```

### Java
```java
public int longestFlareDuration(int[] intensities) {
    // Your code here
}
```

## Hints

1. Find all peaks (where intensities[i-1] < intensities[i] > intensities[i+1])
2. For each peak, expand left while strictly increasing and right while strictly decreasing
3. Calculate the event duration for each peak
4. Track the maximum duration found
5. Alternatively, use two-pass approach: track consecutive ups and downs
6. Time complexity: O(n), Space complexity: O(1)

## Tags
`array` `two-pointers` `greedy` `peaks` `hard`
