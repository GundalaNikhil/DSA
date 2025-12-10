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
Output: 7
Explanation:
  Mountain from index 3 to 9: [4, 3, 6, 8, 7, 5, 2]
  Wait, that's not right. [4, 3] is decreasing.

  Let me recalculate:
  - [1, 3, 5, 4, 3]: increasing [1,3,5], decreasing [5,4,3], length = 5
  - [3, 6, 8, 7, 5, 2]: increasing [3,6,8], decreasing [8,7,5,2], length = 6

  Wait, these mountains share the element 3. Let me be more careful:
  - Mountain 1: indices 0-4 → [1, 3, 5, 4, 3], length = 5
    - Up: 1→3→5
    - Down: 5→4→3
  - Mountain 2: indices 5-9 → [6, 8, 7, 5, 2]
    - Up: 6→8
    - Down: 8→7→5→2
    - Length = 5

  Maximum length = 5, not 7.

  Hmm, but maybe there's overlap? Let me check if we can form a longer mountain:
  - Can we have [3, 6, 8, 7, 5, 2]? Let's check:
    - Is 3→6→8 strictly increasing? Yes
    - Is 8→7→5→2 strictly decreasing? Yes
    - But wait, we need to check the full array context.

  At index 4, we have 3. At index 5, we have 6.
  So [3, 6, 8, 7, 5, 2] at indices 4-9 would be:
  - Up: 3→6→8
  - Down: 8→7→5→2
  - Length = 6

  But before index 4, we have elevation[3] = 4, which is > 3.
  So actually, the subarray starting at index 4 doesn't have 3 at the base of the mountain.

  Let me re-examine the array: [1, 3, 5, 4, 3, 6, 8, 7, 5, 2]
  Indices:                      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  Possible mountains:
  1. Start at 0: [1, 3, 5] up, [5, 4, 3] down → [1,3,5,4,3] length 5 ✓
  2. Start at 4: [3, 6, 8] up, [8, 7, 5, 2] down → [3,6,8,7,5,2] length 6 ✓

  Wait, for mountain starting at index 4:
  Before index 4 is index 3 with value 4.
  At index 4, value is 3.
  Since 4 > 3, the mountain cannot start before index 4.
  So mountain starting at 4: [3, 6, 8, 7, 5, 2] is valid, length 6.

  Actually, I realize we need to be more precise about what "mountain starting at index i" means.
  A mountain includes all elements from the start of the ascent to the end of the descent.

  Let me re-analyze:
  - For a mountain to exist, we need: up phase, peak, down phase
  - The up phase starts where elements begin strictly increasing
  - The down phase ends where elements stop strictly decreasing

  Scanning for peaks (local maxima where left < peak > right):
  - Index 2: 3 < 5 > 4 ✓ (peak)
  - Index 6: 6 < 8 > 7 ✓ (peak)

  For peak at index 2 (value 5):
  - Expand left: 5←3←1 (all the way to index 0)
  - Expand right: 5→4→3 (stops at index 4)
  - Mountain: [1, 3, 5, 4, 3], length 5

  For peak at index 6 (value 8):
  - Expand left: 8←6←3 (stops at index 4, since 4 > 3)
    Wait, at index 4 is value 3, at index 5 is value 6.
    3 < 6 < 8, so we can expand to index 4.
    But what about index 3? Value is 4.
    4 > 3, so we can't include index 3. Stop at index 4.
  - Expand right: 8→7→5→2 (all the way to index 9)
  - Mountain: [3, 6, 8, 7, 5, 2], length 6 ✓

  Maximum length = 6.

  But the expected output in the example is 7. Let me reconsider.

  Oh wait, maybe I miscounted the array. Let me recount:
  [1, 3, 5, 4, 3, 6, 8, 7, 5, 2]
   0  1  2  3  4  5  6  7  8  9  (10 elements)

  Mountain [3, 6, 8, 7, 5, 2] has 6 elements, not 7.

  Is there a 7-element mountain? Let me check all possibilities:
  - [1, 3, 5, 4, 3, 6, 8]: not a mountain (ends with increasing)
  - No 7-element mountain seems possible.

  I think the answer should be 6, not 7. Let me change the output.
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
