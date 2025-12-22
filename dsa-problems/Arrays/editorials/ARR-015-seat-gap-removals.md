---
problem_id: ARR_MIN_REMOVE__1DC9
display_id: ARR-015
slug: seat-gap-removals
title: "Seat Gap After Removals"
difficulty: Hard
difficulty_score: 70
topics:
  - Array
  - Hash Set
  - Filtering
  - Maximum Gap
tags:
  - arrays
  - hashset
  - hard
premium: true
subscription_tier: pro
---

# Seat Gap After Removals

![Problem Header](../images/ARR-015/header.png)

---

## Problem Summary

Find the maximum gap between consecutive remaining seats after removing seats at specified indices.

## Real-World Scenario

Imagine a theater with numbered seats [10, 15, 20, 25, 30, 35]. Due to social distancing, you need to remove certain seats (e.g., seats at indices 1 and 3). After removal, remaining seats are [10, 20, 30, 35]. What's the maximum distance between any two consecutive remaining seats? This helps determine if the gaps are safe/comfortable.

---

## Detailed Explanation

### Understanding "Gap"

**Gap** = difference in seat numbers (not array indices!)

Example:

```
Seats: [10, 15, 20, 25]
       positions (not indices!)

Gap between seat 10 and 15 = 15 - 10 = 5
Gap between seat 15 and 20 = 20 - 15 = 5
Gap between seat 20 and 25 = 25 - 20 = 5
```

### After Removals

```
Original:  [10, 15, 20, 25, 30]
Indices:    0   1   2   3   4
Remove indices: {1, 3}

Remaining: [10, 20, 30] (indices 0, 2, 4 kept)
Gaps: 20-10=10, 30-20=10
Max gap: 10
```

---

## Visual Representation

### Example: `seats = [5, 10, 15, 20, 25, 30]`, `remove = [1, 3, 4]`

```
Original Theater Layout:
Index:  0   1   2   3   4   5
Seat:   5  10  15  20  25  30
        ✓   ✗   ✓   ✗   ✗   ✓
      keep  X  keep  X   X  keep

Removal Visualization:
    [5]  [10]  [15]  [20]  [25]  [30]
     ↓    ✗     ↓    ✗     ✗     ↓
  Index 0     Index 2           Index 5

Remaining Seats: [5, 15, 30]

Computing Gaps:
  Gap 1: 15 - 5  = 10
  Gap 2: 30 - 15 = 15 ← Maximum!

Maximum Gap: 15
```

### Step-by-Step Process

```
Step 1: Create removal set
━━━━━━━━━━━━━━━━━━━━━━━━━━━
remove_set = {1, 3, 4}

Step 2: Filter seats
━━━━━━━━━━━━━━━━━━━━━━━━━━━
i=0: not in set → keep seats[0]=5
i=1: in set → skip
i=2: not in set → keep seats[2]=15
i=3: in set → skip
i=4: in set → skip
i=5: not in set → keep seats[5]=30

Remaining: [5, 15, 30]

Step 3: Find maximum gap
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pair (5, 15):  gap = 10
Pair (15, 30): gap = 15 ← max

Answer: 15
```

---

## Test Case Walkthrough

### Input: `seats = [100, 110, 115, 125, 140, 150]`, `remove = [2, 4]`

```
Detailed Execution:

Original seats:
Index: 0    1    2    3    4    5
Seat:  100  110  115  125  140  150

Remove indices {2, 4}:
Index 2 → seat 115 removed
Index 4 → seat 140 removed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Filtering Process:
i=0: 0 not in {2,4} → remaining.add(100)
i=1: 1 not in {2,4} → remaining.add(110)
i=2: 2 in {2,4} → skip
i=3: 3 not in {2,4} → remaining.add(125)
i=4: 4 in {2,4} → skip
i=5: 5 not in {2,4} → remaining.add(150)

Remaining: [100, 110, 125, 150]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Gap Calculation:
i=1: remaining[1] - remaining[0] = 110 - 100 = 10
i=2: remaining[2] - remaining[1] = 125 - 110 = 15 ← current max
i=3: remaining[3] - remaining[2] = 150 - 125 = 25 ← new max!

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Maximum Gap: 25

Visual:
100───10───110───15───125───25───150
   small     medium      LARGE!
```

---

### Common Mistakes & Pitfalls

### 1. Confusing Index vs Value ⚠️

- ❌ Removing seat numbers instead of indices
- ✅ `remove` contains array indices, not seat values
- Example: `remove=[1]` means remove index 1, not seat numbered "1"

### 2. Computing Gap Between Indices ⚠️

- ❌ Gap = index_j - index_i
- ✅ Gap = seats[index_j] - seats[index_i]
- The gap is between seat NUMBERS, not positions!

### 3. Not Handling Edge Cases ⚠️

- ❌ Assuming at least 2 seats remain
- ✅ Check: if remaining.size() < 2, return 0
- Example: Remove all but one seat → no gap exists

### 4. Inefficient Removal Check ⚠️

- ❌ Checking if index in remove list: O(r) per check
- ✅ Use hash set: O(1) per check

### 5. Forgetting to Sort (if needed) ⚠️

- ❌ Assuming input array is sorted
- ✅ Problem usually guarantees sorted, but verify!
- If not sorted, gaps between consecutive in unsorted array are meaningless

### 6. Off-by-One in Loop ⚠️

- ❌ Starting from index 0 when computing gaps
- ✅ Start from index 1 (comparing with previous)

---

## Approach 1: Naive Solution

### Idea

1. Create new array with removed elements
2. Check all consecutive pairs for maximum gap

```
result = []
for i in 0..n-1:
    if i not in remove_set:
        result.append(seats[i])

max_gap = 0
for i in 1..len(result)-1:
    max_gap = max(max_gap, result[i] - result[i-1])
```

### Complexity Analysis

**Time Complexity**: O(n + r)

- Filter array: O(n) where n = array length
- Mark removals: O(r) where r = number of removals
- Find max gap: O(n - r)

**Space Complexity**: O(n - r)

- Remaining seats array

---

## Approach 2: Optimal Solution ⭐

### Key Insight

We don't need to build a full remaining array! We can:

1. Mark removal indices in a set (O(r))
2. Scan once, tracking previous non-removed seat
3. Update max gap as we go

This still requires O(r) space for the set, but avoids building the remaining array.

**Even better**: If we must filter anyway, the "naive" approach is actually optimal!

### Algorithm

1. Create hash set of removal indices: O(r)
2. Filter seats to keep only non-removed ones: O(n)
3. Find maximum difference between consecutive remaining seats: O(remaining)
4. Handle edge case: fewer than 2 remaining seats → return 0

### Complexity Analysis

**Time Complexity**: O(n + r)

- **Why?** Create removal set (O(r)), filter array (O(n)), find max gap (O(n))
- This is optimal - we must at least look at each seat once!

**Space Complexity**: O(r) for removal set, O(n-r) for remaining seats

- Could optimize to O(r) if we don't store remaining array

---

## Implementations

### Java

```java
class Solution {
    public int maxGapAfterRemovals(int[] seats, int[] remove_indices) {
        // Create set for O(1) lookup
        Set<Integer> removeSet = new HashSet<>();
        for (int idx : remove_indices) {
            removeSet.add(idx);
        }

        // Filter to keep only non-removed seats
        List<Integer> remaining = new ArrayList<>();
        for (int i = 0; i < seats.length; i++) {
            if (!removeSet.contains(i)) {
                remaining.add(seats[i]);
            }
        }

        // Edge case: need at least 2 seats for a gap
        if (remaining.size() < 2) return 0;

        // Find maximum gap
        int maxGap = 0;
        for (int i = 1; i < remaining.size(); i++) {
            int gap = remaining.get(i) - remaining.get(i - 1);
            maxGap = Math.max(maxGap, gap);
        }

        return maxGap;
    }
}
```

### Python

```python
def max_gap_after_removals(seats, remove_indices):
    # Create set for O(1) lookup
    remove_set = set(remove_indices)

    # Filter to keep only non-removed seats
    remaining = [seats[i] for i in range(len(seats)) if i not in remove_set]

    # Edge case: need at least 2 seats
    if len(remaining) < 2:
        return 0

    # Find maximum gap
    max_gap = 0
    for i in range(1, len(remaining)):
        gap = remaining[i] - remaining[i - 1]
        max_gap = max(max_gap, gap)

    return max_gap
```

### C++

```cpp
class Solution {
public:
    int maxGapAfterRemovals(vector<int>& seats, vector<int>& remove_indices) {
        // Create set for O(1) lookup
        unordered_set<int> removeSet(remove_indices.begin(), remove_indices.end());

        // Filter to keep only non-removed seats
        vector<int> remaining;
        for (int i = 0; i < seats.size(); i++) {
            if (removeSet.find(i) == removeSet.end()) {
                remaining.push_back(seats[i]);
            }
        }

        // Edge case: need at least 2 seats
        if (remaining.size() < 2) return 0;

        // Find maximum gap
        int maxGap = 0;
        for (int i = 1; i < remaining.size(); i++) {
            int gap = remaining[i] - remaining[i - 1];
            maxGap = max(maxGap, gap);
        }

        return maxGap;
    }
};
```

### JavaScript

```javascript
/**
 * @param {number[]} seats
 * @param {number[]} remove_indices
 * @return {number}
 */
var maxGapAfterRemovals = function(seats, remove_indices) {
    // Create set for O(1) lookup
    const removeSet = new Set(remove_indices);

    // Filter to keep only non-removed seats
    const remaining = [];
    for (let i = 0; i < seats.length; i++) {
        if (!removeSet.has(i)) {
            remaining.push(seats[i]);
        }
    }

    // Edge case: need at least 2 seats
    if (remaining.length < 2) return 0;

    // Find maximum gap
    let maxGap = 0;
    for (let i = 1; i < remaining.length; i++) {
        const gap = remaining[i] - remaining[i - 1];
        maxGap = Math.max(maxGap, gap);
    }

    return maxGap;
};

// Time: O(n + r), Space: O(n + r)
```

---

## Quick Comparison Table

| Aspect            | Without Set O(n×r) | With Set O(n+r) |
| ----------------- | ------------------ | --------------- |
| For n=1000, r=100 | ~100,000 ops       | ~1,100 ops      |
| For n=10000, r=10 | ~100,000 ops       | ~10,010 ops     |
| Space             | O(n)               | O(r + n)        |
| Lookup time       | O(r) per check     | O(1) per check  |
| Optimal?          | No                 | Yes             |

---
