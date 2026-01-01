---
problem_id: ARR_SEAT_GAP_REMOVALS__6037
display_id: ARR-015
slug: seat-gap-after-removals
title: "Seat Gap After Removals"
difficulty: Easy-Medium
difficulty_score: 33
topics:
  - Arrays
  - Simulation
  - Greedy
tags:
  - arrays
  - simulation
  - greedy
  - easy-medium
premium: true
subscription_tier: basic
---

# ARR-015: Seat Gap After Removals

## 📋 Problem Summary

Given a sorted list of seat positions, remove specific seats based on their indices. Calculate the maximum distance between any two adjacent seats remaining in the list.

## 🌍 Real-World Scenario

**Scenario Title:** The Social Distancing Protocol

You manage a row of theater seats. Due to maintenance or social distancing rules, specific seats (identified by their ticket index) are blocked off and emptied.
Customers are sitting in the remaining chairs. You want to know the *largest physical gap* between any two neighbors to check if your spacing requirements are met or if there's a huge empty space that looks awkward.

**Why This Problem Matters:**

- **Filtering**: Processing a dataset by excluding specific items.
- **Gap Analysis**: Finding the largest interval in a sequence is common in scheduling (finding free time) and memory allocation (largest free block).
- **Index vs Value**: Distinguishing between the *position* of a seat (value) and its *ID* (index).

![Real-World Application](../images/ARR-015/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Removing Seats
```
Indices:   0    1    2    3
Seats:    [2]  [5]  [9]  [10]

Command: Remove Index 1.

Action: Mark Index 1 as invalid.
Valid:     0         2    3
Values:   [2]       [9]  [10]

Gaps:
  9 - 2 = 7
  10 - 9 = 1

Max Gap: 7
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input Indices**: The removal list refers to the 0-based index in the original `seats` array, NOT the seat position value.
- **Sorted Input**: `seats` array is sorted.
- **Guarantee**: At least 2 seats remain, so a gap always exists.

Common interpretation mistake:

- ❌ Removing the value `5` instead of the element at `index 5`.
- ✅ Using a boolean mask or Hash Set to track removed indices for O(1) lookups.

### Core Concept: Simulation with Filtering

Ideally, we'd just iterate through the seats and ignore the removed ones. The gap is simply `current_valid_seat - previous_valid_seat`. We update the maximum gap found.

### Why Naive Approach is too slow

If we delete elements from an array list (`List.remove(index)`), strictly shifting elements takes O(N). Doing this `r` times implies O(N*R) ~ O(N²).
With N=200,000, we need O(N).

## Naive Approach (List Removal)

### Intuition

Convert array to list. Call `remove` for each index. Compute gaps.
*Note: Indices shift after removal! This requires handling removals in descending order of index.*

### Algorithm

1. Convert array to ArrayList.
2. Sort `removeIndices` descending.
3. For each `idx` in `removeIndices`: `list.remove(idx)`.
4. Iterate list `i` from 0 to `size-2`: `max = max(max, list[i+1] - list[i])`.

### Time Complexity

- **O(R * N)**: List removals shift elements.

### Space Complexity

- **O(N)**.

## Optimal Approach (Boolean Mask)

### Key Insight

Don't physically remove elements. Just mark them as "dead".
Iterate through the original array and process only the "live" elements.

### Algorithm

1. Create a boolean array `removed` of size `n`.
2. For each `idx` in `removeIndices`, set `removed[idx] = true`.
3. Initialize `last_pos = -1` (or undefined).
4. `max_gap = 0`.
5. Loop `i` from 0 to `n-1`:
   - If `!removed[i]`:
     - If `last_pos` is valid:
       - `gap = seats[i] - last_pos`
       - `max_gap = max(max_gap, gap)`
     - `last_pos = seats[i]`
6. Return `max_gap`.

### Time Complexity

- **O(N)**: One pass to mark, one pass to scan.

### Space Complexity

- **O(N)**: For the boolean array.

### Why This Is Optimal

We touch every element constant times.

![Algorithm Visualization](../images/ARR-015/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-015/algorithm-steps.png)

## Implementations

### Java


### Python

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxGapAfterRemovals(vector<int>& seats, vector<int>& removeIndices) {
        int n = seats.size();
        vector<bool> removed(n, false);
        
        for (int idx : removeIndices) {
            removed[idx] = true;
        }
        
        int maxGap = 0;
        int lastPos = -1;
        bool first = true;
        
        for (int i = 0; i < n; i++) {
            if (!removed[i]) {
                if (!first) {
                    maxGap = max(maxGap, seats[i] - lastPos);
                }
                lastPos = seats[i];
                first = false;
            }
        }
        
        return maxGap;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    
    vector<int> seats(n);
    for (int i = 0; i < n; i++) cin >> seats[i];
    
    int r;
    cin >> r;
    vector<int> removeIndices(r);
    for (int i = 0; i < r; i++) cin >> removeIndices[i];

    Solution solution;
    cout << solution.maxGapAfterRemovals(seats, removeIndices) << "\n";
    return 0;
}
```

### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: Seats `[2, 5, 9, 10]`, Removes `[1]`.

1. `removed` array: `[F, T, F, F]`.
2. `i=0`, Valid. `lastPos = 2`.
3. `i=1` (5), Removed. Skip.
4. `i=2`, Valid. `Gap = 9 - 2 = 7`. `MaxGap = 7`. `lastPos = 9`.
5. `i=3`, Valid. `Gap = 10 - 9 = 1`. `MaxGap = 7`. `lastPos = 10`.

**Result**: 7. Matches Example.

![Example Visualization](../images/ARR-015/example-1.png)

## ✅ Proof of Correctness

### Invariant

`lastPos` always holds the position of the most recently processed non-removed seat. The calculation simply measures the distance to the next non-removed seat. By induction, checking all adjacent `valid` pairs covers all possible gaps.

### Why the approach is correct

Simple linear scan of valid elements.

## 💡 Interview Extensions (High-Value Add-ons)

- **Unsorted Input**: Sort first (O(N log N)).
- **Stream**: If removals come in online? (A: Use Linked List or inverse Union-Find).

## Common Mistakes to Avoid

1. **Incorrect Indexing**:
   - ❌ Treating input indices as values.
   - ✅ Indices map to array slots.

2. **Edge Cases**:
   - ❌ `removeIndices` is empty? (Loop works).
   - ✅ Constraint says at least 2 items remain.

## Related Concepts

- **Linked List Deletion**: Logical equivalent.
- **Sparse Arrays**: Handling active/inactive states.
