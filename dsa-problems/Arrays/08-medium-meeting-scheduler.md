# Festival Stage Management

**Difficulty:** Medium
**Topic:** Arrays, Intervals, Sorting
**License:** Free to use for commercial purposes

## Problem Statement

A music festival organizer has a lineup of bands that need to perform. Each band has a specific start and end time for their set. The festival wants to know the minimum number of stages required to host all the bands so that no two bands overlap on the same stage.

Given an array of performance intervals where `performances[i] = [start_i, end_i]`, determine the minimum number of stages required.

Note: If a band finishes at time T, another band can start at time T on the same stage (setup time is negligible).

## Constraints

- `1 <= performances.length <= 1000`
- `0 <= start_i < end_i <= 24`
- Times are in 24-hour format (0-24)

## Examples

### Example 1
```
Input: performances = [[9, 11], [10, 12], [13, 15]]
Output: 2
Explanation:
  Stage 1: 9-11, then 13-15
  Stage 2: 10-12
  At time 10, we need 2 stages (performances [9,11] and [10,12] overlap).
```

### Example 2
```
Input: performances = [[8, 10], [10, 12], [12, 14]]
Output: 1
Explanation:
  All performances can use the same stage as they don't overlap.
  When one ends, the next can start immediately.
```

### Example 3
```
Input: performances = [[9, 12], [10, 13], [11, 14], [12, 15]]
Output: 3
Explanation:
  At time 11, three performances are ongoing: [9,12], [10,13], and [11,14].
  Stage 1: 9-12, then 12-15
  Stage 2: 10-13
  Stage 3: 11-14
  Minimum stages needed: 3
```

### Example 4
```
Input: performances = [[14, 16]]
Output: 1
Explanation: Only one band, so only one stage needed.
```

## Function Signature

### Python
```python
def min_stages_required(performances: list[list[int]]) -> int:
    pass
```

### JavaScript
```javascript
function minStagesRequired(performances) {
    // Your code here
}
```

### Java
```java
public int minStagesRequired(int[][] performances) {
    // Your code here
}
```

## Hints

1. Think about what happens at each time point - performances start and end
2. Sort the start times and end times separately
3. Use two pointers to track starts and ends
4. The maximum number of overlapping performances at any point is the answer
5. Alternatively, use a priority queue (min-heap) to track ongoing performances
6. Time complexity: O(n log n), Space complexity: O(n)

## Tags
`array` `intervals` `sorting` `two-pointers` `heap` `medium`
