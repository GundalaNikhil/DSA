---
problem_id: ARR_PARTITION_3WAY__308B
display_id: ARR-014
slug: boarding-order-fixed-ones
title: "Boarding Order With Fixed Ones"
difficulty: Medium
difficulty_score: 55
topics:
  - Array
  - Sorting
  - Two Pointers
  - Partitioning
tags:
  - arrays
  - sorting
  - two-pointers
  - medium
premium: true
subscription_tier: basic
---

# Boarding Order With Fixed Ones

![Problem Header](../images/ARR-014/header.png)

---

## Problem Summary

Sort an array containing only 0s, 1s, and 2s, but keep all 1s at their original positions (they're "anchored").

## Real-World Scenario

Imagine an airline boarding system with three priority groups:

- **0**: First class (boards first)
- **1**: Reserved seats (must stay in their assigned positions - wheelchair access, families, etc.)
- **2**: Economy (boards last)

You need to sort the boarding order so first class boards first, economy last, but reserved passengers stay exactly where they were assigned.

---

## Detailed Explanation

### The Anchoring Constraint

This is similar to the Dutch National Flag problem, but with a twist:

- **Normal sorting**: [2,1,0,2,1,0] → [0,0,1,1,2,2]
- **With anchored 1s**: [2,1,0,2,1,0] → [0,1,0,2,1,2]
  - The 1s at indices 1 and 4 don't move!

### Challenge

We can't use standard sorting or simple partitioning because:

1. 1s must remain at their exact positions
2. Only 0s and 2s are "movable"
3. Movable elements must be sorted relative to each other

---

## Approach 1: Naive Solution

### Idea

1. Extract all movable elements (0s and 2s) into a separate array
2. Sort this extracted array
3. Place sorted values back, skipping positions with 1s

### Why is this inefficient?

Sorting is O(n log n), but we're only sorting 0s and 2s which are already partially organized!

### Complexity Analysis

**Time Complexity**: O(n log n)

- **Why?** Sorting the extracted elements
- **Wasteful**: We know the output - just counting 0s and 2s is enough!

**Space Complexity**: O(n)

- Separate array for movable elements

---

## Approach 2: Optimal Solution ⭐

### Key Insight

We don't need to "sort" at all! We just need to:

1. **Count** how many 0s and 2s exist
2. **Place** all 0s first (in non-anchor positions)
3. **Place** all 2s next (in remaining non-anchor positions)
4. **Skip** positions with 1s

This is like **counting sort** but respecting anchor positions!

### Algorithm

1. Count occurrences: `count0`, `count2`
2. Create sorted movable array: [0, 0, ..., 2, 2, ...]
3. Iterate through original array:
   - If position has a 1: keep it
   - Otherwise: place next element from sorted movable array
4. Return result

**Alternative (even simpler)**:

1. Count 0s
2. First pass: fill non-anchor positions with 0s (up to count)
3. Second pass: fill remaining non-anchor positions with 2s

### Complexity Analysis

**Time Complexity**: O(n)

- **Why?** Count pass O(n) + placement pass O(n) = O(n)
- **No sorting needed!**

**Space Complexity**: O(n)

- Result array (could be O(1) if modifying in-place, but need to track anchors)

---

## Visual Representation

### Example: `arr = [2, 1, 0, 1, 2, 0, 1]`

```
Original Array:
Index: 0  1  2  3  4  5  6
Value: 2  1  0  1  2  0  1
       ↑  ✓  ↑  ✓  ↑  ↑  ✓
     move  |  move  |  move move  |
          anchor   anchor      anchor

Step 1: Identify anchors (1s at indices 1, 3, 6)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Positions with 1: {1, 3, 6}
Movable positions: {0, 2, 4, 5}

Step 2: Extract and sort movable elements
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Movable values: [2, 0, 2, 0]
Count: 2 zeros, 2 twos
Sorted movable: [0, 0, 2, 2]

Step 3: Place sorted values back
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Index 0: movable → take 0
Index 1: anchor (keep 1)
Index 2: movable → take 0
Index 3: anchor (keep 1)
Index 4: movable → take 2
Index 5: movable → take 2
Index 6: anchor (keep 1)

Result: [0, 1, 0, 1, 2, 2, 1]
```

### Visual Transformation

```
Before:  [2, 1, 0, 1, 2, 0, 1]
          ↓     ↓     ↓  ↓
Movable: [2, ., 0, ., 2, 0, .]
Sorted:  [0, ., 0, ., 2, 2, .]
          ↓     ↓     ↓  ↓
After:   [0, 1, 0, 1, 2, 2, 1]
             ✓     ✓        ✓
           (anchors stay!)
```

---

## Test Case Walkthrough

### Input: `arr = [0, 2, 1, 2, 0, 1, 0, 2]`

```
Detailed Trace:

Original: [0, 2, 1, 2, 0, 1, 0, 2]
Indices:   0  1  2  3  4  5  6  7

Step 1: Identify what we have
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Count 0s: 3 (at indices 0, 4, 6)
Count 1s: 2 (at indices 2, 5) ← ANCHORS
Count 2s: 3 (at indices 1, 3, 7)

Step 2: Build sorted movable list
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Movable: 3 zeros + 3 twos
Sorted: [0, 0, 0, 2, 2, 2]

Step 3: Place values (skipping anchors)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
movable_idx = 0

i=0: arr[0]=0, not anchor
  → result[0] = sorted_movable[0] = 0
  → movable_idx = 1

i=1: arr[1]=2, not anchor
  → result[1] = sorted_movable[1] = 0
  → movable_idx = 2

i=2: arr[2]=1, ANCHOR!
  → result[2] = 1 (keep original)
  → movable_idx unchanged

i=3: arr[3]=2, not anchor
  → result[3] = sorted_movable[2] = 0
  → movable_idx = 3

i=4: arr[4]=0, not anchor
  → result[4] = sorted_movable[3] = 2
  → movable_idx = 4

i=5: arr[5]=1, ANCHOR!
  → result[5] = 1 (keep original)
  → movable_idx unchanged

i=6: arr[6]=0, not anchor
  → result[6] = sorted_movable[4] = 2
  → movable_idx = 5

i=7: arr[7]=2, not anchor
  → result[7] = sorted_movable[5] = 2
  → movable_idx = 6

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Result: [0, 0, 1, 0, 2, 1, 2, 2]
```

---

### C++ommon Mistakes & Pitfalls

### 1. Modifying Anchor Positions ⚠️

- ❌ Sorting entire array including 1s
- ✅ Check if position contains 1 before modifying

### 2. Not Counting Correctly ⚠️

- ❌ Counting all elements instead of just movable ones
- ✅ Count only 0s and 2s, ignore 1s for the sorted list

### 3. Off-by-One in Placement ⚠️

- ❌ Using same index for both arrays
- ✅ Use separate index for movable array

### 4. Creating Sorted List Incorrectly ⚠️

- ❌ `[0] * count + [2] * count` (wrong counts)
- ✅ `[0] * count0 + [2] * count2` (correct counts)

### 5. In-Place Modification Issues ⚠️

- ❌ Modifying array while reading it
- ✅ Use result array or careful two-pass approach

---

## Implementations

### Java

```java
class Solution {
    public int[] sortWithAnchors(int[] arr) {
        int n = arr.length;
        int[] result = arr.clone();

        // Count movable elements
        List<Integer> movable = new ArrayList<>();
        for (int val : arr) {
            if (val == 0 || val == 2) {
                movable.add(val);
            }
        }

        // Sort movable elements (just 0s then 2s)
        Collections.sort(movable);

        // Place back, skipping anchors
        int movableIdx = 0;
        for (int i = 0; i < n; i++) {
            if (result[i] != 1) {
                result[i] = movable.get(movableIdx++);
            }
        }

        return result;
    }
}
```

### Python

```python
def sort_with_anchors(arr):
    n = len(arr)
    result = arr[:]

    # Build sorted movable list
    zeros = [0] * arr.count(0)
    twos = [2] * arr.count(2)
    movable = zeros + twos

    # Place back, skipping anchors
    movable_idx = 0
    for i in range(n):
        if result[i] != 1:
            result[i] = movable[movable_idx]
            movable_idx += 1

    return result
```

### C++

```cpp
class Solution {
public:
    vector<int> sortWithAnchors(vector<int>& arr) {
        int n = arr.size();
        vector<int> result = arr;

        // Extract and sort movable elements
        vector<int> movable;
        for (int val : arr) {
            if (val == 0 || val == 2) {
                movable.push_back(val);
            }
        }
        sort(movable.begin(), movable.end());

        // Place back, skipping anchors
        int movableIdx = 0;
        for (int i = 0; i < n; i++) {
            if (result[i] != 1) {
                result[i] = movable[movableIdx++];
            }
        }

        return result;
    }
};
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var sortWithAnchors = function(arr) {
    const n = arr.length;
    const result = [...arr];

    // Count movable elements
    const movable = [];
    for (const val of arr) {
        if (val === 0 || val === 2) {
            movable.push(val);
        }
    }

    // Sort movable elements
    movable.sort((a, b) => a - b);

    // Place back, skipping anchors
    let movableIdx = 0;
    for (let i = 0; i < n; i++) {
        if (result[i] !== 1) {
            result[i] = movable[movableIdx++];
        }
    }

    return result;
};

// Time: O(n), Space: O(n)
```

---

## Quick Comparison Table

| Aspect          | Naive O(n log n) | Optimal O(n)       |
| --------------- | ---------------- | ------------------ |
| For n=1000      | ~10,000 ops      | ~1,000 ops         |
| For n=10000     | ~130,000 ops     | ~10,000 ops        |
| Space           | O(n)             | O(n)               |
| Sorting needed? | Yes              | No (just counting) |
| Anchor check    | Yes              | Yes                |
| Simpler?        | No               | Yes                |

---
