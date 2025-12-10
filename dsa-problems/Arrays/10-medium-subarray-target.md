# Subarray Sum Target

**Difficulty:** Medium
**Topic:** Arrays, Hash Map, Prefix Sum
**License:** Free to use for commercial purposes

## Problem Statement

A fitness app tracks daily calorie burn for a user. Given an array `calories` representing daily calorie burn and a `target` value, find the total number of continuous day ranges (subarrays) where the total calories burned equals the target.

## Constraints

- `1 <= calories.length <= 1000`
- `-1000 <= calories[i] <= 1000` (negative values represent rest days with calorie deficit)
- `-10000 <= target <= 10000`

## Examples

### Example 1
```
Input: calories = [500, 300, 200, 400], target = 500
Output: 2
Explanation:
  Subarray [500] at index 0: sum = 500 ✓
  Subarray [300, 200] at indices 1-2: sum = 500 ✓
  Total: 2 subarrays
```

### Example 2
```
Input: calories = [100, 200, 100, 200, 100], target = 300
Output: 4
Explanation:
  Subarray [100, 200] at indices 0-1: sum = 300 ✓
  Subarray [200, 100] at indices 1-2: sum = 300 ✓
  Subarray [100, 200] at indices 2-3: sum = 300 ✓
  Subarray [200, 100] at indices 3-4: sum = 300 ✓
  Total: 4 subarrays
```

### Example 3
```
Input: calories = [10, 20, 30], target = 100
Output: 0
Explanation: No subarray sums to 100.
```

### Example 4
```
Input: calories = [5, -5, 5, -5, 10], target = 0
Output: 4
Explanation:
  Subarray [5, -5] at indices 0-1: sum = 0 ✓
  Subarray [-5, 5] at indices 1-2: sum = 0 ✓
  Subarray [5, -5] at indices 2-3: sum = 0 ✓
  Subarray [5, -5, 5, -5] at indices 0-3: sum = 0 ✓
  Total: 4 subarrays
```

## Function Signature

### Python
```python
def count_subarrays_with_sum(calories: list[int], target: int) -> int:
    pass
```

### JavaScript
```javascript
function countSubarraysWithSum(calories, target) {
    // Your code here
}
```

### Java
```java
public int countSubarraysWithSum(int[] calories, int target) {
    // Your code here
}
```

## Hints

1. Brute force: Check all possible subarrays O(n²) or O(n³) - works but slow
2. Optimal: Use prefix sum technique with a hash map
3. For each position, calculate the cumulative sum from the start
4. If (current_sum - target) exists in the hash map, we found subarray(s)
5. Store the frequency of each prefix sum in the hash map
6. Time complexity: O(n), Space complexity: O(n)

## Tags
`array` `hash-map` `prefix-sum` `medium`
