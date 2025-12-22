---
problem_id: ARR_DP_COST__1FA6
display_id: ARR-011
slug: leaky-roof-reinforcement
title: "Leaky Roof Reinforcement"
difficulty: Hard
difficulty_score: 70
topics:
  - Array
  - Dynamic Programming
  - Optimization
  - Peak Finding
tags:
  - arrays
  - dynamic-programming
  - hard
premium: true
subscription_tier: pro
---

# Leaky Roof Reinforcement

![Problem Header](../images/ARR-011/header.png)

---

## Problem Summary

Modify an array to have a single-peak (mountain) shape with minimum additions to elements.

## Real-World Scenario

Imagine you're reinforcing a roof structure. Each section has a current height. For water drainage, you need the roof to have a single peak: heights should increase up to one peak point, then decrease after it. You can only add material (increase heights), not remove it. What's the minimum amount of material needed?

---

## Detailed Explanation

### What is a Single-Peak Array?

A single-peak (or mountain) array has:

1. **Ascending part**: Elements increase (or stay same) up to peak
2. **Peak**: One highest point
3. **Descending part**: Elements decrease (or stay same) after peak

Examples:

- `[1, 2, 3, 2, 1]` ✓ (peak at index 2)
- `[1, 3, 5, 5, 3]` ✓ (peak at index 2 or 3)
- `[1, 3, 2, 4, 1]` ✗ (multiple peaks)
- `[1, 2, 3, 4, 5]` ✓ (peak at end - valid!)

### Challenge

Given an array, we need to:

- Choose one position as the peak
- Make left side non-decreasing (ascending)
- Make right side non-increasing (descending)
- Minimize total additions

---

## Approach 1: Naive Solution

### Idea

For each position as potential peak, calculate the cost independently by scanning the entire array.

### Why is this inefficient?

For each of n potential peaks:

- Scan entire left side: O(n)
- Scan entire right side: O(n)
  Total: O(n) per peak × n peaks = O(n²)

### Complexity Analysis

**Time Complexity**: O(n²)

- **Why?** For each of n peak candidates, we scan the entire array (O(n))
- **Detailed breakdown**: n peaks × (n/2 left + n/2 right) = O(n²)

**Space Complexity**: O(1)

- Only tracking costs, no extra arrays

---

## Approach 2: Optimal Solution ⭐

### Key Insight

We can precompute costs! Instead of recalculating for each peak:

1. **Precompute left costs**: Cost to make array non-decreasing up to each position
2. **Precompute right costs**: Cost to make array non-increasing from each position
3. **Combine**: For each peak position, answer = leftCost[peak] + rightCost[peak]

### Algorithm (O(n²) - Simple Version)

For each potential peak position `p`:

1. **Left side (indices 0 to p)**:
   - Scan left to right
   - Maintain `maxSoFar`
   - If `height[i] < maxSoFar`, add cost = `maxSoFar - height[i]`
2. **Right side (indices p to n-1)**:

   - Scan right to left
   - Maintain `maxSoFar`
   - If `height[i] < maxSoFar`, add cost = `maxSoFar - height[i]`

3. Track minimum total cost

### Advanced Optimization (Can reach O(n))

Use dynamic programming arrays:

- `leftCost[i]` = cost to make [0...i] non-decreasing
- `rightCost[i]` = cost to make [i...n-1] non-increasing

But for clarity, we'll use the O(n²) approach which is still efficient for moderate n.

### Complexity Analysis

**Time Complexity**: O(n²)

- **Why?** For each of n peaks, we scan the array once
- **Practical**: Much better constant factors than naive approach
- **Can be optimized**: To O(n) with clever DP precomputation

**Space Complexity**: O(1)

- Only tracking costs

---

## Visual Representation

### Example: `height = [1, 3, 2, 4, 2]`

```
Original heights:
Index: 0  1  2  3  4
Height:1  3  2  4  2

Let's try each position as peak:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PEAK at Index 0 (height=1):
  Left: []
  Right: [1, 3, 2, 4, 2]
  Need non-increasing after peak

  Current:  1→3→2→4→2
  Required: 1→1→1→1→1 (all ≤ 1)
  Cost: (1-1)+(3-1)+(2-1)+(4-1)+(2-1) = 0+2+1+3+1 = 7

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PEAK at Index 1 (height=3):
  Left: [1]
  Right: [3, 2, 4, 2]

  Left side (non-decreasing up to 3):
    1→3: OK (1≤3) → cost = 0

  Right side (non-increasing from 3):
    3→2: OK (3≥2) → cost = 0
    2→4: BAD! Need 4→2, add (4-2)=2
    4→2: After fix, have 4→4→2: OK

  Total cost: 0 + 2 = 2 ✓

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PEAK at Index 2 (height=2):
  Left: [1, 3]
  Right: [2, 4, 2]

  Left side:
    1→3: OK
    3→2: BAD! Need 2→2, add (3-2)=1

  Right side:
    2→4: BAD! Need 4→2, add (4-2)=2
    4→2: After fix, OK

  Total cost: 1 + 2 = 3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PEAK at Index 3 (height=4):
  Left: [1, 3, 2]
  Right: [4, 2]

  Left side (make non-decreasing):
    1→3: OK
    3→2: BAD! Need 2→3, add 1
    Result: 1→3→3→4

  Right side:
    4→2: OK

  Total cost: 1 + 0 = 1 ✓✓ BEST!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PEAK at Index 4 (height=2):
  Left: [1, 3, 2, 4]
  Right: []

  Left side:
    Need: 1→3→3→4→4
    Cost: 0+0+1+0 = 1

Minimum Cost: 1 (peak at index 3)
```

### Visual Transformation

```
Original Array:
  4 |       ●
  3 |   ●
  2 |     ● ● ●
  1 | ●
    └─────────────
      0 1 2 3 4

After Optimization (peak at index 3):
  4 |       ● ●
  3 |   ● ●
  2 |         ●
  1 | ●
    └─────────────
      0 1 2 3 4

Changes: index 2 raised from 2→3 (cost=1)
```

---

## Test Case Walkthrough

### Input: `height = [5, 3, 4, 2, 6, 1]`

```
Trying each peak position:

Peak 0 (h=5):
  Left: []
  Right: [5,3,4,2,6,1] → make ≤5 each
  Cost: 0 + (0+0+0+0+1+0) = 1

Peak 1 (h=3):
  Left: [5] → make ≤3: (5-3)=2
  Right: [3,4,2,6,1] → max so far from right
    Scanning right: 3→4 (add 1), 4→2 (ok), 2→6 (add 4), 6→1 (ok)
  Cost: 2 + 5 = 7

Peak 2 (h=4):
  Left: [5,3] → make non-decreasing up to 4
    max_so_far: 5 (add 5-3=2 to index 1 → 5)
  Cost left: 2

  Right: [4,2,6,1] → make non-increasing from 4
    Scanning from right: 1→6 (add 5), 6→2 (ok), 2→4 (add 2)
  Cost right: 7
  Total: 9

Peak 3 (h=2):
  Left: [5,3,4] → make ≤2
    Cost: (5-2)+(3-2)+(4-2) = 3+1+2 = 6
  Right: [2,6,1]
    6→2: add 4
  Cost: 6+4 = 10

Peak 4 (h=6):
  Left: [5,3,4,2] → make non-decreasing
    5→3: add 2
    5→4: add 1
    5→2: add 3
    → Actually: maintain max
    Cost: 2
  Right: [6,1] → ok
    Cost: 0
  Total: 2

Peak 5 (h=1):
  Left: [5,3,4,2,6] → all ≥1, need ≤1
    Cost: 4+2+3+1+5 = 15
  Right: []
  Total: 15

Minimum: 1 (peak at index 0)
```

---

### C++ommon Mistakes & Pitfalls

### 1. Wrong Direction Scanning ⚠️

- ❌ Scanning left side from right to left
- ✅ Scan left side left-to-right for non-decreasing

### 2. Not Maintaining Maximum Properly ⚠️

- ❌ Comparing adjacent elements only
- ✅ Maintain global max so far and compare each element to it

### 3. Double Counting the Peak ⚠️

- ❌ Including peak in both left and right costs
- ✅ Peak can be included in either side, not both

### 4. Forgetting Edge Peaks ⚠️

- ❌ Skipping index 0 or n-1 as potential peaks
- ✅ Array can be fully ascending or descending (peak at end)

### 5. Integer Overflow ⚠️

- ❌ Using `int` when heights are large
- ✅ Use `long` for cost accumulation

---

## Implementations

### Java

```java
class Solution {
    public int minAdditionsForPeak(int[] height) {
        int n = height.length;
        if (n <= 1) return 0;

        int minCost = Integer.MAX_VALUE;

        for (int peak = 0; peak < n; peak++) {
            int cost = 0;

            // Make left side non-decreasing (up to peak)
            int maxSoFar = 0;
            for (int i = 0; i <= peak; i++) {
                if (height[i] < maxSoFar) {
                    cost += maxSoFar - height[i];
                } else {
                    maxSoFar = height[i];
                }
            }

            // Make right side non-increasing (from peak)
            maxSoFar = 0;
            for (int i = n - 1; i >= peak; i--) {
                if (height[i] < maxSoFar) {
                    cost += maxSoFar - height[i];
                } else {
                    maxSoFar = height[i];
                }
            }

            minCost = Math.min(minCost, cost);
        }

        return minCost;
    }
}
```

### Python

```python
def min_additions_for_peak(height):
    n = len(height)
    if n <= 1:
        return 0

    min_cost = float('inf')

    for peak in range(n):
        cost = 0

        # Make left side non-decreasing (up to peak)
        max_so_far = 0
        for i in range(peak + 1):
            if height[i] < max_so_far:
                cost += max_so_far - height[i]
            else:
                max_so_far = height[i]

        # Make right side non-increasing (from peak)
        max_so_far = 0
        for i in range(n - 1, peak - 1, -1):
            if height[i] < max_so_far:
                cost += max_so_far - height[i]
            else:
                max_so_far = height[i]

        min_cost = min(min_cost, cost)

    return min_cost
```

### C++

```cpp
class Solution {
public:
    int minAdditionsForPeak(vector<int>& height) {
        int n = height.size();
        if (n <= 1) return 0;

        int minCost = INT_MAX;

        for (int peak = 0; peak < n; peak++) {
            int cost = 0;

            // Make left side non-decreasing (up to peak)
            int maxSoFar = 0;
            for (int i = 0; i <= peak; i++) {
                if (height[i] < maxSoFar) {
                    cost += maxSoFar - height[i];
                } else {
                    maxSoFar = height[i];
                }
            }

            // Make right side non-increasing (from peak)
            maxSoFar = 0;
            for (int i = n - 1; i >= peak; i--) {
                if (height[i] < maxSoFar) {
                    cost += maxSoFar - height[i];
                } else {
                    maxSoFar = height[i];
                }
            }

            minCost = min(minCost, cost);
        }

        return minCost;
    }
};
```

### JavaScript

```javascript
/**
 * @param {number[]} height
 * @return {number}
 */
var minAdditionsForPeak = function(height) {
    const n = height.length;
    if (n <= 1) return 0;

    let minCost = Infinity;

    for (let peak = 0; peak < n; peak++) {
        let cost = 0;

        // Make left side non-decreasing
        let maxSoFar = 0;
        for (let i = 0; i <= peak; i++) {
            if (height[i] < maxSoFar) {
                cost += maxSoFar - height[i];
            } else {
                maxSoFar = height[i];
            }
        }

        // Make right side non-increasing
        maxSoFar = 0;
        for (let i = n - 1; i >= peak; i--) {
            if (height[i] < maxSoFar) {
                cost += maxSoFar - height[i];
            } else {
                maxSoFar = height[i];
            }
        }

        minCost = Math.min(minCost, cost);
    }

    return minCost;
};

// Time: O(n^2), Space: O(1)
```

---

## Quick Comparison Table

| Aspect                | Naive O(n²)            | Optimized O(n²)    | DP O(n)            |
| --------------------- | ---------------------- | ------------------ | ------------------ |
| For n=100             | ~10,000 ops            | ~10,000 ops        | ~100 ops           |
| For n=1000            | ~1,000,000 ops         | ~1,000,000 ops     | ~1,000 ops         |
| Space                 | O(1)                   | O(1)               | O(n)               |
| Implementation        | Simple                 | Simple             | Complex            |
| Peak Cost Calculation | Recalculated each time | Optimized scanning | Precomputed arrays |

---
