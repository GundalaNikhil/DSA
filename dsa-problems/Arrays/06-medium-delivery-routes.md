# Delivery Route Optimizer

**Difficulty:** Medium
**Topic:** Arrays, Sliding Window
**License:** Free to use for commercial purposes

## Problem Statement

A delivery driver has a list of package weights to deliver in order. The driver's vehicle has a weight limit per trip. Find the minimum number of trips needed if the driver must deliver packages in the exact order given (cannot rearrange), and can combine consecutive packages into one trip as long as their total weight doesn't exceed the limit.

Given an array `packages` where each element is a package weight, and an integer `limit` representing the weight limit per trip, return the minimum number of trips needed.

## Constraints

- `1 <= packages.length <= 1000`
- `1 <= packages[i] <= limit`
- `1 <= limit <= 10000`
- Each individual package weight is guaranteed to be <= limit

## Examples

### Example 1
```
Input: packages = [5, 8, 3, 7, 4], limit = 12
Output: 3
Explanation:
  Trip 1: [5, 8] = 13 > 12, so only [5], remaining capacity wasted
  Trip 1 (corrected): [5] only = 5
  Trip 2: [8, 3] = 11 <= 12 ✓
  Trip 3: [7, 4] = 11 <= 12 ✓
  Actually, optimal is:
  Trip 1: [5] = 5 (can't add 8, would exceed)
  Trip 2: [8, 3] = 11 ✓
  Trip 3: [7, 4] = 11 ✓
  Wait, let me recalculate:
  Trip 1: [5, 8] would be 13 > 12, so [5] only
  Trip 2: [8, 3] = 11 ✓
  Trip 3: [7, 4] = 11 ✓
  Answer: 3 trips
```

### Example 2
```
Input: packages = [10, 2, 5, 8, 3], limit = 10
Output: 4
Explanation:
  Trip 1: [10] = 10 ✓ (can't add 2)
  Trip 2: [2, 5] = 7 ✓ (can't add 8)
  Trip 3: [8] = 8 ✓ (can't add 3)
  Trip 4: [3] = 3 ✓
  Answer: 4 trips
```

### Example 3
```
Input: packages = [3, 3, 3, 3, 3], limit = 9
Output: 2
Explanation:
  Trip 1: [3, 3, 3] = 9 ✓
  Trip 2: [3, 3] = 6 ✓
  Answer: 2 trips
```

## Function Signature

### Python
```python
def min_delivery_trips(packages: list[int], limit: int) -> int:
    pass
```

### JavaScript
```javascript
function minDeliveryTrips(packages, limit) {
    // Your code here
}
```

### Java
```java
public int minDeliveryTrips(int[] packages, int limit) {
    // Your code here
}
```

## Hints

1. Use a greedy approach - try to fit as many consecutive packages as possible in each trip
2. Keep a running sum for the current trip
3. When adding the next package would exceed the limit, start a new trip
4. Time complexity: O(n), Space complexity: O(1)

## Tags
`array` `greedy` `sliding-window` `medium`
