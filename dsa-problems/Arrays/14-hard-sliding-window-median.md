# Real-time Sensor Calibration

**Difficulty:** Hard
**Topic:** Arrays, Sliding Window, Heap, Binary Search
**License:** Free to use for commercial purposes

## Problem Statement

A high-precision sensor produces a continuous stream of data readings. To filter out noise and calibrate the system in real-time, the software needs to calculate the median of the last `k` readings for every new reading that comes in.

Given an array `readings` and an integer `k`, return an array of median values where each median corresponds to a sliding window of size `k`.

For even-sized windows, the median is the average of the two middle elements. For odd-sized windows, it's the middle element.

## Constraints

- `1 <= k <= readings.length <= 1000`
- `1 <= readings[i] <= 10000`

## Examples

### Example 1
```
Input: readings = [100, 300, 200, 400, 500], k = 3
Output: [200.0, 300.0, 400.0]
Explanation:
  Window [100, 300, 200] → sorted [100, 200, 300] → median = 200.0
  Window [300, 200, 400] → sorted [200, 300, 400] → median = 300.0
  Window [200, 400, 500] → sorted [200, 400, 500] → median = 400.0
```

### Example 2
```
Input: readings = [50, 100, 150, 200], k = 2
Output: [75.0, 125.0, 175.0]
Explanation:
  Window [50, 100] → median = (50 + 100) / 2 = 75.0
  Window [100, 150] → median = (100 + 150) / 2 = 125.0
  Window [150, 200] → median = (150 + 200) / 2 = 175.0
```

### Example 3
```
Input: readings = [10, 20, 30, 40, 50], k = 1
Output: [10.0, 20.0, 30.0, 40.0, 50.0]
Explanation: Window size 1, each element is its own median.
```

### Example 4
```
Input: readings = [5, 5, 5, 5], k = 4
Output: [5.0]
Explanation:
  Window [5, 5, 5, 5] → median = (5 + 5) / 2 = 5.0
```

## Function Signature

### Python
```python
def calibrate_medians(readings: list[int], k: int) -> list[float]:
    pass
```

### JavaScript
```javascript
function calibrateMedians(readings, k) {
    // Your code here
}
```

### Java
```java
public double[] calibrateMedians(int[] readings, int k) {
    // Your code here
}
```

## Hints

1. Brute force: Sort each window to find median - O(n × k log k)
2. Optimal approach: Use two heaps (max heap for lower half, min heap for upper half)
3. Maintain heap balance: sizes differ by at most 1
4. When window slides, remove outgoing element and add incoming element
5. Use lazy deletion or track elements to remove
6. Alternative: Use a balanced binary search tree with deletion
7. Time complexity: O(n × log k), Space complexity: O(k)

## Tags
`array` `sliding-window` `heap` `median` `binary-search-tree` `hard`
