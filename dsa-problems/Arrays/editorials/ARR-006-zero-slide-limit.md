---
problem_id: ARR_ZERO_SLIDE__7E16
display_id: ARR-006
slug: zero-slide-limit
title: "Zero Slide With Limit"
difficulty: Easy
difficulty_score: 35
topics:
  - Array
  - Two Pointers
  - In-Place
  - Conditional Movement
tags:
  - arrays
  - two-pointers
  - easy
premium: true
subscription_tier: basic
---

# Zero Slide With Limit

![Problem Header](../images/ARR-006/header.png)

### 📋 Problem Summary

Move all zeros to the end of the array using at most `m` swap operations. If the swap limit is reached before all zeros are moved, stop and return the partially rearranged array.

### 🌍 Real-World Scenario

**Manufacturing Quality Control**

Imagine a conveyor belt with defective items (zeros) mixed with good items (non-zeros):

- Defective items (zeros) need to be moved to the end for removal
- Moving items costs resources (swap = operation cost)
- Budget limit: at most `m` moves allowed
- Non-zero items must stay in relative order

Example:

```
Original: [0, 4, 0, 5, 7]  m=1 (one swap allowed)
After 1 swap: Move 4 forward → [4, 0, 0, 5, 7]
Budget exhausted, stop here

Original: [0, 0, 3, 0, 5]  m=3
After 2 swaps: Move 3 and 5 → [3, 5, 0, 0, 0]
All zeros moved, done!
```

**Applications**:

- Limited-resource optimization (budget-constrained operations)
- Incremental processing (swaps added gradually over time)
- Load-balanced systems (spread operations across iterations)

### 📚 Detailed Explanation

**What Makes This Tricky?**

- Must track swap count carefully
- Each swap when writing over a zero costs one operation
- Must respect the hard limit `m`
- Stop immediately when budget runs out
- Non-zeros maintain relative order naturally

**Key Insight**:
Use write pointer approach:

1. Scan through array with read pointer
2. When finding a non-zero, swap with write pointer position
3. Count each swap
4. Stop when swap count reaches `m`
5. Return partially rearranged array

### ✅ Optimal Approach: Write Pointer with Swap Counting

**Algorithm**:

```
1. Initialize write pointer at start (0)
2. Scan through array with read pointer
3. For each non-zero element:
   - If position has a zero, increment swap counter
   - Swap non-zero with position at write pointer
   - Move write pointer forward
   - Check if swap limit reached
4. Stop if swaps == m
5. Return modified array
```

**⏱️ Time Complexity: O(n)**

- Single pass through array (worst case all swaps performed)

**📦 Space Complexity: O(1)**

- Only using pointers (constant space)
- In-place modification! ✓

**Key Insight**:
A swap only costs when we're moving a non-zero over a zero. If write pointer points to a non-zero already, no swap cost.

### 🎨 Visual Representation

**Example**: `arr = [0, 4, 0, 5, 7]`, `m = 1` (one swap allowed)

```
Initial state:
[0, 4, 0, 5, 7]
 ↑
writePos=0, swaps=0

Step 1: Read 0 at index 0
[0, 4, 0, 5, 7]
 ↑
writePos points to 0 (no swap needed, same position)
Move to next

Step 2: Read 4 at index 1
[0, 4, 0, 5, 7]
   ↑
Found non-zero! Position has 0 → SWAP COSTS 1
[4, 0, 0, 5, 7]
 ↑
writePos=1, swaps=1 (LIMIT REACHED!)

Stop here. Budget exhausted.
```

**Walkthrough with more swaps allowed**:

```
Initial: [0, 0, 3, 0, 5]  m=3

Step 1: Read 0 at index 0
Position 0 has 0, no swap needed
writePos=0

Step 2: Read 0 at index 1
Position 0 has 0, no swap needed
writePos=0

Step 3: Read 3 at index 2
Position 0 has 0 → SWAP (swap count: 1)
[3, 0, 0, 0, 5]
writePos=1

Step 4: Read 0 at index 3
Position 1 has 0, no swap needed
writePos=1

Step 5: Read 5 at index 4
Position 1 has 0 → SWAP (swap count: 2)
[3, 5, 0, 0, 0]
writePos=2

All zeros at end! Swaps used: 2 (< limit of 3)
```

### ⚠️ Common Mistakes

#### 1. **Forgetting to Check Swap Limit**

```java
// ❌ WRONG - ignores swap limit
int writePos = 0;
for (int i = 0; i < n; i++) {
    if (arr[i] != 0) {
        swap(arr, writePos, i);
        writePos++;
    }
}

// ✅ CORRECT - check limit before swap
int writePos = 0;
int swaps = 0;
for (int i = 0; i < n && swaps < m; i++) {
    if (arr[i] != 0 && arr[writePos] == 0) {
        swap(arr, writePos, i);
        swaps++;
    }
    if (arr[writePos] != 0) writePos++;
}
```

#### 2. **Not Advancing Write Pointer Correctly**

```java
// ❌ WRONG - advances even when no swap
for (int i = 0; i < n; i++) {
    if (arr[i] != 0) {
        if (arr[writePos] == 0) {
            swap(arr, writePos, i);
            swaps++;
        }
        writePos++;  // ALWAYS increments!
    }
}

// ✅ CORRECT - only advance when position is occupied
for (int i = 0; i < n && swaps < m; i++) {
    if (arr[i] != 0) {
        if (arr[writePos] == 0) {
            swap(arr, writePos, i);
            swaps++;
        }
        if (arr[writePos] != 0) {  // Only if now has non-zero
            writePos++;
        }
    }
}
```

#### 3. **Counting Swaps Incorrectly**

```java
// ❌ WRONG - counts every movement as swap
int swaps = 0;
for (int i = 0; i < n; i++) {
    if (arr[i] != 0) swaps++;  // Counts non-zeros, not swaps!
}

// ✅ CORRECT - only count when moving non-zero over zero
if (arr[writePos] == 0) {
    swap(arr, writePos, i);
    swaps++;  // Only increment on actual swap
}
```

#### 4. **Edge Case: m = 0**

```java
// ❌ WRONG - doesn't handle no swaps allowed
// Will fail if m = 0

// ✅ CORRECT - handle zero swaps
if (m == 0) {
    return arr;  // Array unchanged
}
```

#### 5. **Edge Case: All Zeros or No Zeros**

```java
// ❌ WRONG - crashes on edge cases
// Assumes both zeros and non-zeros exist

// ✅ CORRECT - handle special cases
// All zeros: writePos stays at 0, no swaps performed
// No zeros: writePos moves through all non-zeros, no swaps
// Both cases handled naturally by the algorithm
```

### 🔑 Key Algorithm Points

1. **Two-pass approach**: Separate collection and placement
2. **Write pointer**: Track where to place next element
3. **Relative order**: Process non-zeros in original order
4. **Fill strategy**: Zeros before k, non-zeros after k, then remaining zeros

### 💻 Implementations

### Java

```java
class Solution {
    public void zeroSlideWithLimit(int[] arr, int k) {
        int n = arr.length;
        if (n == 0 || k >= n) return;

        // Count zeros
        int zeroCount = 0;
        for (int num : arr) {
            if (num == 0) zeroCount++;
        }

        // Collect non-zeros in a list
        List<Integer> nonZeros = new ArrayList<>();
        for (int num : arr) {
            if (num != 0) {
                nonZeros.add(num);
            }
        }

        // Fill array:
        // 1. First k positions with zeros (or all zeros if zeroCount < k)
        int zerosToPlaceFirst = Math.min(k, zeroCount);
        for (int i = 0; i < zerosToPlaceFirst; i++) {
            arr[i] = 0;
        }

        // 2. Then non-zero elements
        int writePos = zerosToPlaceFirst;
        for (int num : nonZeros) {
            arr[writePos++] = num;
        }

        // 3. Remaining zeros (if any)
        while (writePos < n) {
            arr[writePos++] = 0;
        }
    }
}

// Time: O(n), Space: O(n) for list - can optimize to O(1) with in-place
```

### Python

```python
def zero_slide_with_limit(arr, k):
    """
    Move all zeros to positions before index k, maintaining order of non-zeros.

    Args:
        arr: List of integers (modified in-place)
        k: Limit index for zero placement
    """
    n = len(arr)
    if n == 0 or k >= n:
        return

    # Count zeros
    zero_count = sum(1 for x in arr if x == 0)

    # Collect non-zeros
    non_zeros = [x for x in arr if x != 0]

    # Fill array
    zeros_to_place_first = min(k, zero_count)

    # First k positions with zeros
    for i in range(zeros_to_place_first):
        arr[i] = 0

    # Then non-zeros
    write_pos = zeros_to_place_first
    for num in non_zeros:
        arr[write_pos] = num
        write_pos += 1

    # Remaining zeros
    while write_pos < n:
        arr[write_pos] = 0
        write_pos += 1

# Time: O(n), Space: O(n)
```

### C++++

```cpp
class Solution {
public:
    void zeroSlideWithLimit(vector<int>& arr, int k) {
        int n = arr.size();
        if (n == 0 || k >= n) return;

        // Count zeros
        int zeroCount = 0;
        for (int num : arr) {
            if (num == 0) zeroCount++;
        }

        // Collect non-zeros
        vector<int> nonZeros;
        for (int num : arr) {
            if (num != 0) {
                nonZeros.push_back(num);
            }
        }

        // Fill array
        int zerosToPlaceFirst = min(k, zeroCount);

        // First k positions with zeros
        for (int i = 0; i < zerosToPlaceFirst; i++) {
            arr[i] = 0;
        }

        // Then non-zeros
        int writePos = zerosToPlaceFirst;
        for (int num : nonZeros) {
            arr[writePos++] = num;
        }

        // Remaining zeros
        while (writePos < n) {
            arr[writePos++] = 0;
        }
    }
};

// Time: O(n), Space: O(n)
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {void} Do not return anything, modify arr in-place.
 */
var zeroSlideWithLimit = function(arr, k) {
    const n = arr.length;
    if (n === 0 || k >= n) return;

    let zeroCount = 0;
    for (const num of arr) {
        if (num === 0) zeroCount++;
    }

    const nonZeros = [];
    for (const num of arr) {
        if (num !== 0) nonZeros.push(num);
    }

    const zerosToPlaceFirst = Math.min(k, zeroCount);

    for (let i = 0; i < zerosToPlaceFirst; i++) {
        arr[i] = 0;
    }

    let writePos = zerosToPlaceFirst;
    for (const num of nonZeros) {
        arr[writePos++] = num;
    }

    while (writePos < n) {
        arr[writePos++] = 0;
    }
};

// Time: O(n), Space: O(n)
```

### 📊 Comparison Table

| **Aspect**           | **Naive (Extra Array)**            | **Optimal (In-Place)**       |
| -------------------- | ---------------------------------- | ---------------------------- |
| **Algorithm**        | Copy to temp, rearrange, copy back | Two-pass with pointers       |
| **Time Complexity**  | O(n)                               | O(n)                         |
| **Space Complexity** | O(n)                               | O(n) for list, O(1) possible |
| **Passes**           | 2-3                                | 2                            |
| **Best for**         | Clarity                            | Space efficiency             |

