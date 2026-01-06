---
problem_id: ARR_CIRCULAR_PEAK__8392
display_id: ARR-018
slug: circular-peak-detection
title: "Circular Peak Detection"
difficulty: Easy
difficulty_score: 15
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - data-structures
  - iteration
  - logic
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-018: Circular Peak Detection

## 📋 Problem Summary

Given a circular array of integers, count the number of **local maxima** - elements that are strictly greater than both of their neighbors. In a circular array, the first and last elements are considered adjacent.

**Definition:**

- An element `arr[i]` is a peak if `arr[i] > arr[left]` AND `arr[i] > arr[right]`
- "Strictly greater" means equality doesn't count
- Circular: `arr[0]`'s neighbors are `arr[N-1]` and `arr[1]`

**Special Cases:**

- Single element (`N=1`): Considered a peak by definition
- Two elements (`N=2`): Check if either is greater than the other

## 🌍 Real-World Scenarios

**Scenario 1:** 🎡 **Ferris Wheel Heightmap Analysis**

You're analyzing sensor data from a Ferris wheel measuring cabin heights at different rotation angles. Since the wheel is circular, position 0 connects back to position N-1. Find "local highs" where a cabin is elevated above both neighbors - these might indicate mechanical issues or unusual weight distribution.

**Scenario 2:** ⏰ **Circular Clock Signal Detection**

A circular sensor array around a clock face records light intensity at different positions. Detect peaks (brightest spots) that are brighter than their neighbors on bothsides. Used in optical clock calibration.

**Scenario 3:** 🌊 **Circular Island Coastline Elevation**

Mapping the elevation of points around a circular island. Find peaks (promontories jutting into the sea) where the land is higher than both neighboring points. Critical for lighthouse placement.

**Scenario 4:** 🧬 **DNA Circular Chromosome Feature Detection**

Bacterial DNA is circular (plasmid). Analyzing gene expression levels around the circular chromosome, detect regions of peak activity surrounded by lower expression on both sides.

**Scenario 5:** 🎵 **Audio Waveform Loop Analysis**

In music production, seamless audio loops are circular (end connects to start). Detect peak amplitude points that might cause clicks if not properly handled.

### Real-World Relevance

- **Signal Processing:** Detecting periodic peaks in circular buffers
- **Geography:** Analyzing closed-loop terrain (islands, craters, depressions)
- **Computer Graphics:** Finding local maxima in spherical/toroidal mappings
- **Game Development:** Detecting collision points in circular game boundaries
- **Robotics:** Obstacle detection in 360° sensor arrays

## 🚀 Detailed Explanation

### 1. Understanding Circular Arrays

**Concept:** The array "wraps around" - after the last element comes the first.

```
Linear Array:  [A, B, C, D, E]
               ↓  ↓  ↓  ↓  ↓
Neighbors:    - A-B B-C C-D D-E E-
              (No left)         (No right)

Circular Array: [A, B, C, D, E]
                 ↓  ↓  ↓  ↓  ↓
Neighbors:      E-A-B B-C C-D D-E E-A
                ↑_______________↑
                   Wraps around
```

### 2. Neighbor Calculation with Modular Arithmetic

For any index `i` in range `[0, N-1]`:

**Left Neighbor:**

```
left = (i - 1 + N) % N
```

**Why `+ N`?**  
When `i = 0`, `i - 1 = -1`. In many languages, `-1 % N` gives negative results. Adding `N` ensures positive values:

```
i = 0: (0 - 1 + N) % N = (N - 1) % N = N - 1 ✓
i = 3: (3 - 1 + 5) % 5 = 7 % 5 = 2 ✓
```

**Right Neighbor:**

```
right = (i + 1) % N
```

**Examples:**

```
i = 0: (0 + 1) % N = 1
i = N-1: (N-1 + 1) % N = N % N = 0 ✓ (wraps to start)
```

### 3. Peak Detection Algorithm

**Step-by-Step Process:**

```
1. Handle edge case: N = 1 → return 1
2. Initialize count = 0
3. For each index i from 0 to N-1:
   a. Calculate left = (i - 1 + N) % N
   b. Calculate right = (i + 1) % N
   c. If arr[i] > arr[left] AND arr[i] > arr[right]:
      count++
4. Return count
```

**Detailed Example:**

```
Input: arr = [3, 1, 4, 5, 2], N = 5

Index 0 (value=3):
  left = (0-1+5) % 5 = 4, arr[4] = 2
  right = (0+1) % 5 = 1, arr[1] = 1
  Check: 3 > 2 AND 3 > 1 → TRUE ✓
  count = 1

Index 1 (value=1):
  left = (1-1+5) % 5 = 0, arr[0] = 3
  right = (1+1) % 5 = 2, arr[2] = 4
  Check: 1 > 3 AND 1 > 4 → FALSE
  count = 1

Index 2 (value=4):
  left = (2-1+5) % 5 = 1, arr[1] = 1
  right = (2+1) % 5 = 3, arr[3] = 5
  Check: 4 > 1 AND 4 > 5 → FALSE
  count = 1

Index 3 (value=5):
  left = (3-1+5) % 5 = 2, arr[2] = 4
  right = (3+1) % 5 = 4, arr[4] = 2
  Check: 5 > 4 AND 5 > 2 → TRUE ✓
  count = 2

Index 4 (value=2):
  left = (4-1+5) % 5 = 3, arr[3] = 5
  right = (4+1) % 5 = 0, arr[0] = 3
  Check: 2 > 5 AND 2 > 3 → FALSE
  count = 2

Result: 2 peaks (at indices 0 and 3)
```

**Visual Representation:**

```
Circular Array: [3, 1, 4, 5, 2]
                 ↑     ↑     ↑
                 └─────┘─────┘
                  wraps around

Position:  0   1   2   3   4
Value:     3   1   4   5   2
Peak?      ✓   ✗   ✗   ✓   ✗

3: neighbors are 2 and 1 → 3 > both ✓
5: neighbors are 4 and 2 → 5 > both ✓
```

### 🔄 Algorithm Flow Diagram

```mermaid
flowchart TD
    A[Start] --> B{N == 1?}
    B -- Yes --> C[Return 1]
    B -- No --> D[Initialize count = 0]
    D --> E[Loop i from 0 to N-1]
    E --> F[left = i-1+N % N]
    F --> G[right = i+1 % N]
    G --> H{arr[i] > arr[left]?}
    H -- No --> E
    H -- Yes --> I{arr[i] > arr[right]?}
    I -- No --> E
    I -- Yes --> J[count++]
    J --> E
    E -- End Loop --> K[Return count]
```

## 🔍 Complexity Analysis

### Time Complexity: O(N)

- Single pass through the array: O(N)
- For each element:
  - Modulo operations: O(1)
  - Array accesses: O(1)
  - Comparisons: O(1)
- **Total: O(N)**

### Space Complexity: O(1)

- Only using variables: `count`, `i`, `left`, `right`
- No additional data structures
- **Total: O(1)** auxiliary space

### Optimality

This algorithm is **optimal**:

- Cannot solve in less than O(N) since we must examine every element
- Space cannot be better than O(1)

## 🧪 Edge Cases & Testing

### Edge Case 1: Single Element

```
Input: arr = [42], N = 1
By definition, single element is a peak
Output: 1
```

### Edge Case 2: Two Elements - Both Different

```
Input: arr = [5, 3], N = 2
- arr[0]=5: neighbors are arr[1]=3, arr[1]=3 → 5 > 3 → peak
- arr[1]=3: neighbors are arr[0]=5, arr[0]=5 → 3 > 5 → not peak
Output: 1
```

### Edge Case 3: Two Elements - Equal

```
Input: arr = [5, 5], N = 2
- arr[0]=5: 5 > 5? NO (strictly greater required)
- arr[1]=5: 5 > 5? NO
Output: 0
```

### Edge Case 4: All Equal (Plateau)

```
Input: arr = [7, 7, 7, 7], N = 4
No element is strictly greater than its neighbors
Output: 0
```

### Edge Case 5: Strictly Increasing then Decreasing (Mountain)

```
Input: arr = [1, 2, 3, 2, 1], N = 5
- arr[0]=1: neighbors 1, 2 → not peak
- arr[1]=2: neighbors 1, 3 → not peak
- arr[2]=3: neighbors 2, 2 → 3 > 2 AND 3 > 2 → peak ✓
- arr[3]=2: neighbors 3, 1 → not peak
- arr[4]=1: neighbors 2, 1 → not peak
Output: 1 (only the top of the mountain)
```

### Edge Case 6: Strictly Monotonic

```
Input: arr = [1, 2, 3, 4, 5], N = 5
Circular: [1, 2, 3, 4, 5]
- arr[0]=1: neighbors 5, 2 → NO
- arr[1]=2: neighbors 1, 3 → NO
- arr[2]=3: neighbors 2, 4 → NO
- arr[3]=4: neighbors 3, 5 → NO
- arr[4]=5: neighbors 4, 1 → 5 > 4 AND 5 > 1 → YES ✓
Output: 1 (highest element is a peak)
```

### Edge Case 7: Alternating Pattern

```
Input: arr = [1, 3, 2, 4, 2], N = 5
- arr[0]=1: neighbors 2, 3 → NO
- arr[1]=3: neighbors 1, 2 → 3 > 1 AND 3 > 2 → YES ✓
- arr[2]=2: neighbors 3, 4 → NO
- arr[3]=4: neighbors 2, 2 → 4 > 2 AND 4 > 2 → YES ✓
- arr[4]=2: neighbors 4, 1 → NO
Output: 2
```

### Edge Case 8: All Peaks (Maximum Possible)

```
For alternating high-low pattern: [5, 1, 5, 1, 5], N = 5
- arr[0]=5: neighbors 5, 1 → 5 > 5? NO (equality fails)
- Won't get all peaks if values repeat

True alternating: [5, 1, 6, 2, 7], N = 5
- arr[0]=5: neighbors 7, 1 → NO (5 < 7)
- Maximum peaks = floor(N/2) for optimal arrangements
```

> [!TIP]
> Maximum possible peaks in a circular array of size N is approximately N/2 (alternating high-low pattern).

## ⚠️ Common Pitfalls & Debugging

### Pitfall 1: Forgetting Circular Wrap-Around

```java
// ❌ Wrong: Doesn't handle i=0 and i=N-1
for (int i = 1; i < N - 1; i++) {
    if (arr[i] > arr[i-1] && arr[i] > arr[i+1]) {
        count++;
    }
}
// Misses potential peaks at positions 0 and N-1!

// ✓ Correct: Use modulo arithmetic for all positions
```

### Pitfall 2: Incorrect Negative Modulo Handling

```cpp
// ❌ Wrong in C++: -1 % 5 = -1 (negative!)
int left = (i - 1) % N;  // Crashes when i=0

// ✓ Correct: Add N before modulo
int left = (i - 1 + N) % N;
```

### Pitfall 3: Using >= Instead of >

```python
# ❌ Wrong: Problem requires STRICTLY greater
if arr[i] >= arr[left] and arr[i] >= arr[right]:
    count += 1
# This counts plateaus as peaks!

# ✓ Correct: Strictly greater
if arr[i] > arr[left] and arr[i] > arr[right]:
    count += 1
```

### Pitfall 4: Missing N=1 Special Case

```javascript
// ❌ Wrong: Doesn't handle single element
// For N=1, left=(0-1+1)%1=0, right=(0+1)%1=0
// Compares arr[0] with itself → always false

// ✓ Correct: Handle explicitly
if (N === 1) return 1;
```

## 🎯 Variations & Extensions

### Variation 1: Return Peak Indices

Instead of count, return list of peak positions:

```python
def getPeakIndices(arr):
    peaks = []
    for i in range(len(arr)):
        left, right = (i-1+N)%N, (i+1)%N
        if arr[i] > arr[left] and arr[i] > arr[right]:
            peaks.append(i)
    return peaks
```

### Variation 2: Find Peak Values

Return the actual peak values:

```java
List<Integer> peakValues = new ArrayList<>();
// ... in loop:
if (arr[i] > arr[left] && arr[i] > arr[right]) {
    peakValues.add(arr[i]);
}
```

### Variation 3: Minimum or Maximum Distance Between Peaks

```python
peak_indices = [list of peaks]
min_distance = min(peak_indices[i+1] - peak_indices[i]
                   for i in range(len(peak_indices)-1))
# Handle circular distance for last to first
```

### Variation 4: 2D Circular Peak Detection

Extend to 2D grid where both dimensions wrap:

```
arr[i][j] is peak if greater than all 8 neighbors (with wrap-around)
```

### Variation 5: K-Neighbor Peaks

Element must be greater than K neighbors on each side (with wrap):

```
for offset in range(1, K+1):
    left = (i - offset + N) % N
    right = (i + offset) % N
    if not (arr[i] > arr[left] and arr[i] > arr[right]):
        is_peak = False
```

## 🎓 Key Takeaways

1. **Circular arrays** require modular arithmetic: `(i ± offset + N) % N`
2. **Negative modulo** needs special handling: always add `N` before modulo in `(i-1+N)%N`
3. **Edge cases** are critical: N=1, N=2, all equal, strictly monotonic
4. This is an **optimal O(N)** algorithm - cannot do better
5. Pattern appears frequently in **signal processing**, **robotics**, and **geographic analysis**

## 📚 Related Problems

- **Linear Peak Detection:** Same problem without circular wrap
- **Peak Element in Matrix:** 2D version of peak finding
- **Valley Detection:** Find local minima instead of maxima
- **Circular Array Maximum:** Different property in circular arrays
- **Periodic Signal Analysis:** Finding peaks in periodic/circular data

## 🔗 Additional Resources

- **Modular Arithmetic:** Understanding circular indexing
- **Circular Buffers:** Data structures using circular arrays
- **Signal Processing:** Peak detection in periodic signals
- **Topological Analysis:** Finding local extrema in closed surfaces
