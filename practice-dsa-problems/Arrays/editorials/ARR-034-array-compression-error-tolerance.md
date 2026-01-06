---
problem_id: ARR_COMPRESS_TOLERANCE__1029
display_id: ARR-034
slug: array-compression-error-tolerance
title: "Array Compression with Error Tolerance"
difficulty: Medium
difficulty_score: 45
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - compression
  - data-structures
  - optimization
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-034: Array Compression with Error Tolerance

## 📋 Problem Summary

You have a sequence of data points.
You want to assume they are "constant" segments to save space.
We replace a segment `[a_l...a_r]` with a single value `V = floor(average)`.
**Constraint:** Every original point `a_i` in the segment must be close to `V`: `|a_i - V| <= E`.
**Goal:** Minimize the total number of segments (make segments as long as possible).

## 🌍 Real-World Scenario

**Scenario Title:** 📉 The Sensor Data Logger

### The Problem

You are designing a black-box recorder for an aircraft or an IoT temperature sensor.

- The sensor reads data 100 times a second.
- Storing every float value is expensive (memory/bandwidth).
- Usually, the temperature stays roughly `25.0` for minutes.
- Instead of writing `25.1, 24.9, 25.0, 25.2...`, you want to write: "`Start: 10:00, Len: 500, Value: 25`".
- However, if the temperature spikes to `30`, you must break the segment.
- Your "Error Tolerance" `E` defines how much "noise" you ignore before you acknowledge a "change" has occurred.

## 🚀 Detailed Explanation

### 1. The Greedy Strategy

We want to minimize the number of segments. This is equivalent to **maximizing the length of each segment**.
Why?
Suppose we start a segment at index `i`.
If valid segments ending at `j` and `j+1` are both possible, is there any reason to stop at `j`?
No. Stopping early forces us to start the _next_ segment at `j+1`. Starting at `j+2` (by extending the current one) is strictly better (or at least equal) because it pushes the "problem" of the next segment further
down the array.
Thus, the optimal strategy is:
**"Start at `L`. Extend `R` as far as possible until the segment becomes invalid. Then start new segment at `R+1`."**

### 2. Validity Check

For a current segment `[L, R]`:

- Calculate `Sum`.
- Calculate `Count = R - L + 1`.
- `V = floor(Sum / Count)`.
- Check: `max(Segment) - V <= E` AND `V - min(Segment) <= E`.

### 3. Incremental Implementation

We iterate `R` from `0` to `N-1`.
Maintain `CurrentMin`, `CurrentMax`, `CurrentSum` for the active segment.
At each step `R`:

1. Update `CurrentSum += arr[R]`.
2. Update `CurrentMin = min(CurrentMin, arr[R])`.
3. Update `CurrentMax = max(CurrentMax, arr[R])`.
4. Calculate `V = floor(CurrentSum / Length)`.
5. Check if `CurrentMax - V <= E` and `V - CurrentMin <= E`.
   - If **Valid**: Continue extending.
   - If **Invalid**:
     - The segment _must_ end at `R-1`.
     - Record segment length `(R-1) - L + 1`.
     - Increment Segment Count.
     - Start new segment at `R`. (Reset Min, Max, Sum).

**Wait!**
Does adding an element _always_ preserve the monotonicity of validity?
Usually yes, variance increases.
However, `Average` can shift.
Example: `E=1`. Segment `[10]`. Avg 10. Valid.
Add `100`. Segment `[10, 100]`. Avg 55. `|10-55|=45`. Invalid.
Add `10` again? `[10, 100, 10]`. Avg 40. `|100-40|=60`.
Generally, once a "spike" enters, it breaks validity and adding more "normal" values won't fix the fact that the spike is too far from the average.
Also, `Max - Min` is non-decreasing.
Bounded Mean check is roughly monotonic.
So Greedy works.

### 🔄 Algorithm Flow Diagram

<!-- mermaid -->

```mermaid
flowchart TD
    A[Start] --> B[Init Segments=0, L=0]
    B --> C[Init Window: Min=INF, Max=-INF, Sum=0]
    C --> D[Loop R from L to N-1]
    D --> E[Update Min, Max, Sum with arr[R]]
    E --> F[V = Sum / (R-L+1)]
    F --> G{Max-V <= E AND V-Min <= E?}
    G -- Yes (Valid) --> H[Continue]
    G -- No (Invalid) --> I[Close Segment at R-1]
    I --> J[Store Length R-L]
    J --> K[L = R, Segments++, Reset Window]
    K --> E
    D -- End of Array --> L[Close Last Segment]
    L --> M[Return Count, Lengths]
```

## 🧪 Edge Cases to Test

1.  **Single Element:** Always valid. Avg = Value. Error 0.
2.  **Zero Tolerance (E=0):** Compression only works for identical values `[2, 2, 2]`. `[2, 3]` -> Avg 2. `3-2=1 > 0`. Invalid.
3.  **Large Tolerance:** Entire array becomes one segment? Yes, check if `Max-Min <= 2E` roughly.

## 🏃 Naive vs Optimal Approach

### Naive

Iterate all valid ends? Just simple iteration.

### Greedy Linear Scan O(N)

- **Time:** O(N). Single pass.
- **Space:** O(1) auxiliary (excluding output).
  Optimal.
