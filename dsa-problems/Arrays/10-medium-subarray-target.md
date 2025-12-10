# Magic Spell Power

**Difficulty:** Medium
**Topic:** Arrays, Hash Map, Prefix Sum
**License:** Free to use for commercial purposes

## Problem Statement

A wizard casts a sequence of spells, each with a specific power level (positive or negative, as some spells drain energy). The wizard wants to find how many continuous sequences of spells combine to have a total power exactly equal to a `target` value.

Given an array `spell_powers` and an integer `target`, return the count of continuous subarrays where the sum of elements equals `target`.

## Constraints

- `1 <= spell_powers.length <= 1000`
- `-1000 <= spell_powers[i] <= 1000`
- `-10000 <= target <= 10000`

## Examples

### Example 1
```
Input: spell_powers = [500, 300, 200, 400], target = 500
Output: 2
Explanation:
  Sequence [500] at index 0: sum = 500 ✓
  Sequence [300, 200] at indices 1-2: sum = 500 ✓
  Total: 2 sequences
```

### Example 2
```
Input: spell_powers = [100, 200, 100, 200, 100], target = 300
Output: 4
Explanation:
  Sequence [100, 200] at indices 0-1: sum = 300 ✓
  Sequence [200, 100] at indices 1-2: sum = 300 ✓
  Sequence [100, 200] at indices 2-3: sum = 300 ✓
  Sequence [200, 100] at indices 3-4: sum = 300 ✓
  Total: 4 sequences
```

### Example 3
```
Input: spell_powers = [10, 20, 30], target = 100
Output: 0
Explanation: No sequence sums to 100.
```

### Example 4
```
Input: spell_powers = [5, -5, 5, -5, 10], target = 0
Output: 4
Explanation:
  Sequence [5, -5] at indices 0-1: sum = 0 ✓
  Sequence [-5, 5] at indices 1-2: sum = 0 ✓
  Sequence [5, -5] at indices 2-3: sum = 0 ✓
  Sequence [5, -5, 5, -5] at indices 0-3: sum = 0 ✓
  Total: 4 sequences
```

## Function Signature

### Python
```python
def count_spell_sequences(spell_powers: list[int], target: int) -> int:
    pass
```

### JavaScript
```javascript
function countSpellSequences(spellPowers, target) {
    // Your code here
}
```

### Java
```java
public int countSpellSequences(int[] spellPowers, int target) {
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
