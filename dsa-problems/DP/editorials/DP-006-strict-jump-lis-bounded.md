---
problem_id: DP_LIS_DIFF_RANGE__5881
display_id: DP-006
slug: strict-jump-lis-bounded
title: "Strict Jump LIS With Max Gap"
difficulty: Medium
difficulty_score: 64
topics:
  - Dynamic Programming
  - Segment Tree
  - Coordinate Compression
tags:
  - dp
  - lis
  - segment-tree
  - fenwick
  - medium
premium: true
subscription_tier: basic
---

# DP-006: Strict Jump LIS With Max Gap

## 📋 Problem Summary

Find the longest subsequence (preserving original order) where consecutive chosen values differ by a bounded range:

`d <= next - prev <= g`

This resembles LIS, but instead of “increasing” you need “difference in [d, g]”.

Constraints (`n` up to 100,000) force an `O(n log n)` approach.

## 🌍 Real-World Scenario

**Scenario Title:** Controlled Temperature Sampling

Suppose you’re processing sensor readings from a campus server room. You want to pick a sequence of readings (in time order) such that each new reading increases by:

- at least `d` (meaning a meaningful rise), but
- at most `g` (meaning it’s not a sudden spike)

This resembles trend detection in monitoring systems, finance (bounded jump prices), and anomaly analysis.

**Why This Problem Matters:**

- Trains “LIS with constraints” thinking (common interview pattern)
- Teaches coordinate compression + range maximum query
- Reinforces that `n=1e5` kills quadratic DP

![Real-World Application](../images/DP-006/real-world-scenario.png)

## ✅ Input/Output Clarifications

- Subsequence must preserve indices (`i1 < i2 < ...`).
- If `d = 0`, equal consecutive values are allowed.
- Negative numbers are allowed in the array.
- Answer is at least 1 (pick any single element).

## Detailed Explanation

### Value Range and Gap Visualization

```
Array: [10, 5, 20, 12, 8, 25]
d=3, g=15 (valid jump range)

For each element, valid previous values must be in [current - g, current - d]:

Step 0 (value 10):
  Can extend from values in [10-15, 10-3] = [-5, 7]
  No elements qualify → dp[0] = 1

Step 1 (value 5):
  Can extend from values in [5-15, 5-3] = [-10, 2]
  No elements qualify → dp[1] = 1

Step 2 (value 20):
  Can extend from values in [20-15, 20-3] = [5, 17]
  Values {10, 5, 12, 8} qualify
  Best dp among {10, 5, 12, 8} = 1
  dp[2] = 1 + 1 = 2

Step 3 (value 12):
  Can extend from values in [12-15, 12-3] = [-3, 9]
  Values {10, 5, 8} have dp = 1
  dp[3] = 1 + 1 = 2

Step 4 (value 8):
  Can extend from values in [8-15, 8-3] = [-7, 5]
  Value {5} qualifies with dp = 1
  dp[4] = 1 + 1 = 2

Step 5 (value 25):
  Can extend from values in [25-15, 25-3] = [10, 22]
  Values {20, 12} qualify
  Best dp among {20, 12} = 2
  dp[5] = 1 + 2 = 3

Answer: max(dp) = 3
```

### Naive DP (why it fails)

Classic DP idea:

`dp[i] = 1 + max(dp[j])` over all `j < i` such that `d <= a[i] - a[j] <= g`

This is correct but checking all `j` for each `i` costs `O(n^2)` in the worst case.

With `n=1e5`, that’s impossible.

### Key Insight: Query by value range, not by scanning indices

For each current value `x = a[i]`, we need the best previous dp among values in:

`[x - g, x - d]`

So the problem becomes:

- maintain a data structure over values that supports:
  - update at value `v`: store the best dp ending at `v`
  - query over a value interval: maximum dp in that interval

This is exactly a segment tree / Fenwick tree for range maximum.

### Coordinate Compression

Values are up to 1e9 and can be negative. We compress them:

1) Collect all values `a[i]` and sort unique to `vals`.
2) Map each `a[i]` to an index in `vals`.
3) To query `[x-g, x-d]`, find:
   - `L = lower_bound(vals, x-g)`
   - `R = upper_bound(vals, x-d) - 1`

Then query the segment tree on indices `[L, R]`.

### DP recurrence with segment tree

For each `x = a[i]`:

- `best = query(L, R)` (0 if empty range)
- `dp_i = best + 1`
- update at index of `x`: `tree[idx(x)] = max(tree[idx(x)], dp_i)`

This is safe because:

- we process elements in index order
- updates represent subsequences ending at already-processed positions

### Decision Tree for LIS with Bounded Jumps

```
For each element a[i] at index i:
    │
    ├─ Compute valid value range: [a[i] - g, a[i] - d]
    │
    ├─ Coordinate compress range to indices [L, R]
    │   │
    │   ├─ L = lower_bound(vals, a[i] - g)
    │   └─ R = upper_bound(vals, a[i] - d) - 1
    │
    ├─ Query segment tree for max dp in range [L, R]
    │   │
    │   └─ best = tree.query(L, R)
    │
    ├─ Compute dp[i] = best + 1
    │
    ├─ Update segment tree at compressed index of a[i]
    │   │
    │   └─ tree.update(index(a[i]), dp[i])
    │
    └─ Update global answer: ans = max(ans, dp[i])

Final answer: ans
```

## Naive Approach

### Algorithm

For each i:

1. Compute dp[i] by scanning all j < i and checking diff range.
2. Return max dp[i].

### Complexity

- Time: `O(n^2)` (TLE)
- Space: `O(n)`

## Optimal Approach (Compression + Segment Tree)

### Algorithm

1. Coordinate compress values of `a`.
2. Initialize a segment tree storing max dp per value index (initial 0).
3. For i = 0..n-1:
   - x = a[i]
   - compute value range `[x-g, x-d]`
   - query tree for maximum in that compressed index range
   - dp_i = best + 1
   - update tree at index of x with dp_i
4. Return global maximum dp_i.

### Complexity

- Time: `O(n log n)`
- Space: `O(n)` for compressed list and segment tree

![Algorithm Visualization](../images/DP-006/algorithm-visualization.png)
![Algorithm Steps](../images/DP-006/algorithm-steps.png)

## Implementations

### Java (Segment Tree)


### Python (Fenwick Tree for max)


### C++ (Segment Tree)


### JavaScript (Segment Tree)


## 🧪 Test Case Walkthrough (Dry Run)
`a = [1, 3, 4, 9, 10]`, `d=2`, `g=6`

When processing `9`:

- valid previous values are in `[9-6, 9-2] = [3, 7]`
- the best dp among values {3,4} is 2 (from `1 -> 3` or `1 -> 4`)
- so dp at 9 becomes 3

Answer is 3.

### State Evolution Table

| Index | Value | Valid Range [val-g, val-d] | Compressed [L, R] | Query Result | dp[i] | Updated Answer |
|-------|-------|----------------------------|-------------------|--------------|-------|----------------|
| 0     | 1     | [-5, -1]                   | empty             | 0            | 1     | 1              |
| 1     | 3     | [-3, 1]                    | [0, 0] (value 1)  | 1            | 2     | 2              |
| 2     | 4     | [-2, 2]                    | [0, 1] (1,3)      | max(1,2)=2   | 3     | 3              |
| 3     | 9     | [3, 7]                     | [1, 2] (3,4)      | max(2,3)=3   | 4     | 4              |
| 4     | 10    | [4, 8]                     | [2, 3] (4,9)      | max(3,4)=4   | 5     | 5              |

Final answer: 5 (subsequence: 1 → 3 → 4 → 9 → 10)

Note: The differences are: 3-1=2, 4-3=1 (invalid if d=2).
Recalculating correctly for d=2, g=6:
- From 1: can go to values in [1+2, 1+6] = [3, 7] → {3, 4}
- From 3: can go to [5, 9] → {9}
- From 4: can go to [6, 10] → {9, 10}
- From 9: can go to [11, 15] → {10} (NO, 10-9=1 < d=2)

Corrected walkthrough with forward checking:
| Index | Value | dp[i] | Can extend to |
|-------|-------|-------|---------------|
| 0     | 1     | 1     | values [3,7] → indices 1,2 |
| 1     | 3     | 2     | values [5,9] → index 3 |
| 2     | 4     | 2     | values [6,10] → indices 3,4 |
| 3     | 9     | 3     | values [11,15] → none |
| 4     | 10    | 3     | values [12,16] → none |

Final: max = 3 (path: 1→3→9 or 1→4→10)

![Example Visualization](../images/DP-006/example-1.png)

## ✅ Proof of Correctness (Sketch)

We store, for each value `v`, the maximum subsequence length ending at value `v` among processed indices.

For a new value `x`, any valid predecessor must have value in `[x-g, x-d]`. Querying the data structure over this interval gives the best achievable predecessor length. Adding 1 gives the best length for a subsequence ending at `x`.

Processing in index order ensures we only build subsequences with increasing indices. Taking max updates at `x` handles duplicates correctly.

### Common Mistakes to Avoid

1. **Using O(n^2) DP (will time out)**
2. **Forgetting coordinate compression (values are up to 1e9)**
3. **Using wrong bounds: must query `[x-g, x-d]`**
4. **Off-by-one in binary search for R (use upper_bound - 1)**


## Related Concepts

- Coordinate compression
- Range maximum query (segment tree)
- LIS-style DP

