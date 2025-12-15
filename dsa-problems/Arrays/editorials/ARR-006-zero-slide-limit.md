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

Move all zeros in the array to positions before index `k`, while maintaining relative order of non-zero elements. Do this in-place.

### 🌍 Real-World Scenario

**Parking Lot Reorganization**

Imagine a parking lot with occupied spaces (non-zero) and empty spaces (zeros):

- First `k` spots are "buffer zone" for short-term parking
- Need to move all empty spaces to buffer zone
- Keep occupied cars in their relative order

Example:

```
Original: [1, 0, 2, 0, 3]  k=2
Goal: Move zeros to first 2 positions

Result: [0, 0, 1, 2, 3]
         └─┘  └─────┘
       zeros  non-zeros
    (before k) (maintain order)
```

**Applications**:

- Memory defragmentation (move unused blocks)
- Task queue reorganization (prioritize non-empty tasks)
- File system optimization (consolidate free space)

### 📚 Detailed Explanation

**What Makes This Tricky?**

- Not just "move zeros to end" (standard problem)
- Must move zeros to **specific position range** (before index k)
- Must maintain **relative order** of non-zeros
- Must do **in-place** (O(1) extra space)

**Key Insight**:
Think of it as partitioning:

1. Collect all non-zeros first
2. Fill zeros in the space before k
3. If more zeros than k slots, handle overflow

### ❌ Naive Approach

**Algorithm**:

```
1. Create temporary array
2. Separate zeros and non-zeros
3. Place zeros first (up to k positions)
4. Place non-zeros after
5. Copy back to original
```

**⏱️ Time Complexity: O(n)**

- Single pass: O(n)

**📦 Space Complexity: O(n)**

- Temporary array: O(n)
- Not in-place! ✗

### ✅ Optimal Approach

**Algorithm**:

```
1. Two-pointer technique:
   - Write pointer: where to place next element
   - Read pointer: scan through array
2. First pass: collect all non-zeros, place after index k
3. Second pass: fill zeros before index k
```

**⏱️ Time Complexity: O(n)**

```
Two passes through array: 2n = O(n)
```

**📦 Space Complexity: O(1)**

- Only using pointers (constant space)
- True in-place solution! ✓

### 🎨 Visual Representation

**Example**: `arr = [1, 0, 2, 0, 3, 0], k = 2`

```
Step 1: Count zeros and non-zeros
[1, 0, 2, 0, 3, 0]
 ✓  ✗  ✓  ✗  ✓  ✗

Zeros: 3, Non-zeros: 3

Step 2: Place non-zeros starting from index k
[?, ?, 1, 2, 3, ?]
 └─┘  └───────┘
  k    non-zeros

Step 3: Fill first k positions with zeros
[0, 0, 1, 2, 3, ?]

Step 4: Fill remaining with zeros
[0, 0, 1, 2, 3, 0]
```

**Walkthrough**:

```
Initial: [1, 0, 2, 0, 3, 0]  k=2

Phase 1: Collect non-zeros starting at index k
┌───┬───┬───┬───┬───┬───┐
│ 1 │ 0 │ 2 │ 0 │ 3 │ 0 │
└───┴───┴───┴───┴───┴───┘
  ↓
┌───┬───┬───┬───┬───┬───┐
│ ? │ ? │ 1 │ ? │ ? │ ? │  Write 1 at index 2
└───┴───┴───┴───┴───┴───┘
          ↑
      writePos=2

┌───┬───┬───┬───┬───┬───┐
│ ? │ ? │ 1 │ 2 │ ? │ ? │  Write 2 at index 3
└───┴───┴───┴───┴───┴───┘
              ↑
          writePos=3

┌───┬───┬───┬───┬───┬───┐
│ ? │ ? │ 1 │ 2 │ 3 │ ? │  Write 3 at index 4
└───┴───┴───┴───┴───┴───┘
                  ↑
              writePos=4

Phase 2: Fill zeros before k
┌───┬───┬───┬───┬───┬───┐
│ 0 │ 0 │ 1 │ 2 │ 3 │ ? │  Fill indices 0, 1
└───┴───┴───┴───┴───┴───┘

Phase 3: Fill remaining zeros
┌───┬───┬───┬───┬───┬───┐
│ 0 │ 0 │ 1 │ 2 │ 3 │ 0 │  Fill remaining
└───┴───┴───┴───┴───┴───┘
```

### 🧪 Test Case Walkthrough

**Input**: `arr = [3, 0, 1, 0, 2], k = 2`

| Phase   | Action              | Array State       | Explanation                           |
| ------- | ------------------- | ----------------- | ------------------------------------- |
| Initial | -                   | `[3, 0, 1, 0, 2]` | k=2 means first 2 positions for zeros |
| Pass 1  | Collect non-zeros   | `[?, ?, 3, 1, 2]` | Place 3,1,2 starting at index 2       |
| Pass 2  | Fill zeros before k | `[0, 0, 3, 1, 2]` | Fill indices 0,1 with zeros           |

**Output**: `[0, 0, 3, 1, 2]`

### ⚠️ Common Mistakes

#### 1. **Wrong Starting Position**

```java
// ❌ WRONG - starts from 0
int writePos = 0;
for (int num : arr) {
    if (num != 0) arr[writePos++] = num;
}

// ✅ CORRECT - starts from k
int writePos = k;
for (int num : arr) {
    if (num != 0) arr[writePos++] = num;
}
```

#### 2. **Not Preserving Relative Order**

```java
// ❌ WRONG - might swap incorrectly
// Using simple swapping destroys order

// ✅ CORRECT - collect then place
List<Integer> nonZeros = new ArrayList<>();
for (int num : arr) {
    if (num != 0) nonZeros.add(num);
}
```

#### 3. **Forgetting to Fill Remaining Zeros**

```java
// ❌ WRONG - missing remaining zeros
for (int i = 0; i < k; i++) {
    arr[i] = 0;
}
// Forgot to fill after writePos!

// ✅ CORRECT - fill both sections
for (int i = 0; i < k; i++) arr[i] = 0;
for (int i = writePos; i < n; i++) arr[i] = 0;  // Remaining
```

#### 4. **Edge Case: k = 0**

```java
// ❌ WRONG - doesn't handle k=0
// No special case

// ✅ CORRECT - check k=0
if (k == 0) {
    // All elements stay as-is, no zeros to move before index 0
}
```

#### 5. **Edge Case: More Zeros than k**

```java
// ❌ WRONG - assumes zeros fit in first k positions
// Doesn't handle overflow

// ✅ CORRECT - handle remaining zeros at end
int zeroCount = count zeros in array
if (zeroCount > k) {
    // Fill remaining zeros after non-zeros
}
```

### 🔑 Key Algorithm Points

1. **Two-pass approach**: Separate collection and placement
2. **Write pointer**: Track where to place next element
3. **Relative order**: Process non-zeros in original order
4. **Fill strategy**: Zeros before k, non-zeros after k, then remaining zeros

### 💻 Implementations

#### Java

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

#### Python

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

#### C++

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

### 📊 Comparison Table

| **Aspect**           | **Naive (Extra Array)**            | **Optimal (In-Place)**       |
| -------------------- | ---------------------------------- | ---------------------------- |
| **Algorithm**        | Copy to temp, rearrange, copy back | Two-pass with pointers       |
| **Time Complexity**  | O(n)                               | O(n)                         |
| **Space Complexity** | O(n)                               | O(n) for list, O(1) possible |
| **Passes**           | 2-3                                | 2                            |
| **Best for**         | Clarity                            | Space efficiency             |

