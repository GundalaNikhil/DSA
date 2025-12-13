# Problem 3: Shuttle Shift With Blackout (ARR-003)

**Topic Tags**: `Array`, `Rotation`, `Conditional Operations`  
**Difficulty**: Medium  
**Problem ID**: ARRAY-003

---

## Problem Summary

Rotate array elements left by k positions, but keep elements at blackout indices fixed in place.

---

## Approach 1: Naive Solution

### Idea

Create a copy of the array, perform rotations on non-blackout elements only.

### Complexity Analysis

**Time Complexity**: O(n × k)

- For each of k rotations, shift all movable elements

**Space Complexity**: O(n)

- Copy of the array

---

## Approach 2: Optimal Solution ⭐

### Key Insight

Extract non-blackout elements, rotate them efficiently, then place back. This is actually optimal for this problem.

### Algorithm

1. Create a set of blackout indices for O(1) lookup
2. Extract all movable values and their original positions
3. Rotate movable values by `k % movableCount` positions
4. Place rotated values back in movable positions
5. Keep blackout positions unchanged

### Complexity Analysis

**Time Complexity**: O(n)

- Extract movable elements: O(n)
- Rotate by calculating new positions: O(m) where m = movable count
- Place back: O(m)
- Total: O(n)

**Space Complexity**: O(n)

- Set for blackout indices: O(b) where b = blackout count
- Arrays for movable values and positions: O(m)
- Result array: O(n)

---

## Visual Representation

### Example: `arr = [1, 2, 3, 4, 5]`, `k = 2`, `blackout = [1, 3]`

```
Initial:         [1, 2, 3, 4, 5]
Blackout:           ↑     ↑
Movable indices:  0     2     4
Movable values:   1     3     5

After rotating movable by k=2:
Movable: [1, 3, 5] → rotate left by 2 → [5, 1, 3]

Placement:
Position 0: gets 5
Position 1: stays 2 (blackout)
Position 2: gets 1
Position 3: stays 4 (blackout)
Position 4: gets 3

Result: [5, 2, 1, 4, 3]
```

---

## Step-by-Step Algorithm Breakdown

### Phase 1: Identify Movable Elements

```
arr = [10, 20, 30, 40, 50]
blackout = [1, 3]

Movable positions: [0, 2, 4]
Movable values: [10, 30, 50]
```

### Phase 2: Rotate Movable Values

```
Original movable: [10, 30, 50]
k = 1, rotate left by 1
After rotation: [30, 50, 10]
```

### Phase 3: Place Back

```
Position 0 ← 30
Position 1 ← 20 (unchanged, blackout)
Position 2 ← 50
Position 3 ← 40 (unchanged, blackout)
Position 4 ← 10

Result: [30, 20, 50, 40, 10]
```

---

## Implementations

### Java

```java
class Solution {
    public int[] rotateWithBlackout(int[] arr, int k, int[] blackout) {
        int n = arr.length;
        Set<Integer> blackoutSet = new HashSet<>();
        for (int idx : blackout) {
            blackoutSet.add(idx);
        }

        List<Integer> movableValues = new ArrayList<>();
        List<Integer> movablePositions = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            if (!blackoutSet.contains(i)) {
                movableValues.add(arr[i]);
                movablePositions.add(i);
            }
        }

        int m = movableValues.size();
        if (m == 0) return arr;

        k = k % m;
        int[] result = arr.clone();

        for (int i = 0; i < m; i++) {
            int newPos = movablePositions.get(i);
            int oldValueIdx = (i + k) % m;
            result[newPos] = movableValues.get(oldValueIdx);
        }

        return result;
    }
}
```

### Python

```python
def rotate_with_blackout(arr, k, blackout):
    n = len(arr)
    blackout_set = set(blackout)

    movable_values = []
    movable_positions = []

    for i in range(n):
        if i not in blackout_set:
            movable_values.append(arr[i])
            movable_positions.append(i)

    m = len(movable_values)
    if m == 0:
        return arr[:]

    k = k % m
    result = arr[:]

    for i in range(m):
        new_pos = movable_positions[i]
        old_value_idx = (i + k) % m
        result[new_pos] = movable_values[old_value_idx]

    return result
```

### C++

```cpp
class Solution {
public:
    vector<int> rotateWithBlackout(vector<int>& arr, int k, vector<int>& blackout) {
        int n = arr.size();
        unordered_set<int> blackoutSet(blackout.begin(), blackout.end());

        vector<int> movableValues;
        vector<int> movablePositions;

        for (int i = 0; i < n; i++) {
            if (blackoutSet.find(i) == blackoutSet.end()) {
                movableValues.push_back(arr[i]);
                movablePositions.push_back(i);
            }
        }

        int m = movableValues.size();
        if (m == 0) return arr;

        k = k % m;
        vector<int> result = arr;

        for (int i = 0; i < m; i++) {
            int newPos = movablePositions[i];
            int oldValueIdx = (i + k) % m;
            result[newPos] = movableValues[oldValueIdx];
        }

        return result;
    }
};
```

---

## Common Mistakes & Pitfalls

### 1. Not Handling k > m ⚠️

- ❌ Directly using k for rotation
- ✅ Use `k % m` to handle cases where k exceeds movable count

### 2. Modifying Blackout Elements ⚠️

- ❌ Accidentally including blackout indices in rotation
- ✅ Always check if index is in blackout set before operations

### 3. Inefficient Blackout Lookup ⚠️

- ❌ Using array/list for blackout indices (O(n) lookup)
- ✅ Use set/hash set for O(1) lookup

### 4. Empty Movable Array ⚠️

- ❌ Not handling case where all indices are blackout
- ✅ Check if movable count is 0 and return original array

---

## Edge Cases

### Case 1: All indices blackout

```
arr = [1, 2, 3], blackout = [0, 1, 2]
Result: [1, 2, 3] (no change)
```

### Case 2: No blackout indices

```
arr = [1, 2, 3], k = 1, blackout = []
Result: [2, 3, 1] (normal rotation)
```

### Case 3: k = 0

```
arr = [1, 2, 3], k = 0, blackout = [1]
Result: [1, 2, 3] (no rotation)
```

---

## Quiz Questions

### Q1: What is the purpose of using modulo (k % m) in the rotation?

- A) To make the code faster
- B) To handle cases where k is larger than the number of movable elements
- C) To reverse the rotation direction
- D) It's not necessary

<details>
<summary>Answer</summary>

**B) To handle cases where k is larger than the number of movable elements**

Explanation: Rotating by k positions where k >= m is equivalent to rotating by k % m positions, as rotations repeat after m steps.

</details>

### Q2: Why use a Set for blackout indices?

- A) Sets are always faster
- B) For O(1) lookup instead of O(n)
- C) To automatically sort indices
- D) To remove duplicates

<details>
<summary>Answer</summary>

**B) For O(1) lookup instead of O(n)**

Explanation: Using a set allows constant-time checking if an index is blackout, versus linear search in an array.

</details>

---

## Related Problems

- Array Rotation
- Selective Element Operations
- Conditional Array Manipulation

## Tags

`#arrays` `#rotation` `#hashset` `#medium`
