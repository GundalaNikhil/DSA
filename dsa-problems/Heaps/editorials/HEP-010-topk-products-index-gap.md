---
problem_id: HEP_TOPK_PRODUCTS_INDEX_GAP__8206
display_id: HEP-010
slug: topk-products-index-gap
title: "Top K Products with Index Gap"
difficulty: Medium
difficulty_score: 59
topics:
  - Heaps
  - K Largest Pairs
  - Search
tags:
  - heaps
  - k-largest
  - two-arrays
  - medium
premium: true
subscription_tier: basic
---

# HEP-010: Top K Products with Index Gap

## 📋 Problem Summary

You have two sorted arrays `A` and `B` (non-increasing).
Find the top `k` products `A[i] * B[j]` such that `|i - j| >= d`.
Return the products in descending order.

## 🌍 Real-World Scenario

**Scenario Title:** Cross-Department Collaboration

Imagine pairing senior engineers from Dept A with junior engineers from Dept B.
- `A` and `B` are sorted by skill level.
- You want to form high-impact pairs (maximize skill product).
- However, to ensure diversity or avoid conflicts, the "rank difference" must be at least `d`.
- You want to find the top `k` best valid pairings.

![Real-World Application](../images/HEP-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Search Space

A: `[9, 7, 5]`
B: `[8, 3, 1]`
d: `1`

Grid of Products (A[i] * B[j]):
```
      B[0]=8  B[1]=3  B[2]=1
A[0]=9  72      27      9
A[1]=7  56      21      7
A[2]=5  40      15      5
```

Valid pairs (`|i-j| >= 1`):
- (0,0): |0-0|=0 < 1 (Invalid)
- (0,1): |0-1|=1 >= 1 (Valid, 27)
- (0,2): |0-2|=2 >= 1 (Valid, 9)
- (1,0): |1-0|=1 >= 1 (Valid, 56)
- (1,1): |1-1|=0 < 1 (Invalid)
- (1,2): |1-2|=1 >= 1 (Valid, 7)
- (2,0): |2-0|=2 >= 1 (Valid, 40)
- (2,1): |2-1|=1 >= 1 (Valid, 15)
- (2,2): |2-2|=0 < 1 (Invalid)

Valid values: `{27, 9, 56, 7, 40, 15}`.
Top 3: `56, 40, 27`.

### Key Concept: Priority Search on Grid

Since `A` and `B` are sorted descending, the products `A[i] * B[j]` generally decrease as `i` and `j` increase.
However, the constraint `|i - j| >= d` makes the valid region non-contiguous (it excludes a diagonal band).
We can still use a **Max-Heap** to explore candidates.
- Start with the "best possible" candidates.
  - Usually (0,0), but that can be invalid.
  - The valid region boundaries are `j <= i - d` and `j >= i + d`.
  - For row `i`, the best valid `j` is `0` (if valid) or `i+d`?
  - So for fixed `i`, we want smallest `j` such that `|i-j| >= d`.
  - Two regions for `j`: `[0, i-d]` and `[i+d, m-1]`.
  - Best candidates in these regions are `j=0` (if `0 <= i-d`) and `j=i+d` (if `i+d < m`).
- So, we can initialize the heap with the best valid pair for each row `i`.
  - For each `i`, check `j=0` (if valid) and `j=i+d` (if valid).
  - Better: Just push the "corners" of the valid regions.
  - The valid region is roughly two triangles.
  - Region 1: `j <= i - d`. Top-left corner is `(d, 0)`.
    - From `(d, 0)`, we can move to `(d+1, 0)` or `(d, 1)`.
  - Region 2: `j >= i + d`. Top-left corner is `(0, d)`.
    - From `(0, d)`, we can move to `(1, d)` or `(0, d+1)`.
  - This is like searching two separate sorted matrices!
  - Matrix 1: Rows `d..n-1`, Cols `0..m-1`. Constraint `j <= i-d`.
  - Matrix 2: Rows `0..n-1`, Cols `d..m-1`. Constraint `j >= i+d`.

Standard technique for "Kth Smallest/Largest in Sorted Matrix":
- Push `(0, 0)` to heap.
- Pop `(i, j)`. Push `(i+1, j)` and `(i, j+1)`.
- Check validity before pushing?
- No, because if `(0,0)` is invalid, we can't start there.
- We should start with the "roots" of the valid regions.
- **Root 1:** `(d, 0)`. This is the largest product in the lower-left valid triangle.
  - Neighbors: `(d+1, 0)` (down) and `(d, 1)` (right).
  - Constraint `j <= i - d` must hold.
  - If we are at `(i, j)`, `(i+1, j)` satisfies `j <= (i+1) - d` (since `j <= i-d < i+1-d`). Valid.
  - `(i, j+1)` satisfies `j+1 <= i - d`? Only if `j < i - d`.
- **Root 2:** `(0, d)`. This is the largest product in the upper-right valid triangle.
  - Neighbors: `(1, d)` (down) and `(0, d+1)` (right).
  - Constraint `j >= i + d`.
  - If we are at `(i, j)`, `(i, j+1)` satisfies `j+1 >= i + d` (since `j >= i+d`). Valid.
  - `(i+1, j)` satisfies `j >= i+1 + d`? Only if `j > i + d`.

So, we run two independent searches (or one combined heap):
1. Start `(d, 0)`. Expand `(i+1, j)` always. Expand `(i, j+1)` only if `j+1 <= i-d`.
2. Start `(0, d)`. Expand `(i, j+1)` always. Expand `(i+1, j)` only if `j >= i+1+d`.

- `(d+1, 1)` can be reached from `(d, 1)` (down) or `(d+1, 0)` (right).
- Use a `visited` set to avoid cycles/duplicates.

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Input:** `n, m, k, d`, Arrays `A`, `B`.
- **Output:** List of products.
- **Constraints:** `N, M <= 10^5`. `K` up to `10^5`.
- **Values:** Can be negative? Yes.
- **Negative Values:**
  - If values are negative, "largest product" logic changes.
  - `(-10) * (-10) = 100`.
  - The problem says "A and B sorted in non-increasing order".
  - If A = `[10, -5, -20]`, B = `[5, -2, -10]`.
  - `10*5=50`. `-20*-10=200`.
  - The "largest products" can come from the *end* of the arrays (large negative * large negative).
  - This breaks the monotonic property of the grid if we only look at the top-left.
  - **However**, with sorted arrays and negatives, you should check the 4 corners.
  - Or split into positive/negative parts.
  - Given "Medium" difficulty and standard "K Largest Pairs" template, usually inputs are non-negative or we just handle the complexity.
  - Assume general case.
  - Sorted non-increasing: `Positive ... Negative`.
  - Largest products come from `Pos * Pos` (start of A, start of B) OR `Neg * Neg` (end of A, end of B).
  - `Pos * Neg` is always negative (small).
  - So we have potentially **two** sources of large values:
    1. Top-Left of valid regions (Start A, Start B).
    2. Bottom-Right of valid regions (End A, End B).
  - We should initialize our heap with roots from BOTH perspectives?
  - Valid regions are the same.
  - Region 1 (`j <= i-d`):
    - Max `Pos*Pos` at `(d, 0)`.
    - Max `Neg*Neg` at `(n-1, m-1)`? No, `(n-1, m-1)` is not necessarily in Region 1.
    - We need the "largest indices" valid point in Region 1.
    - `i` max is `n-1`. `j` max is `n-1-d`.
    - So `(n-1, min(m-1, n-1-d))` is the corner for `Neg*Neg`.
  - Region 2 (`j >= i+d`):
    - Max `Pos*Pos` at `(0, d)`.
    - Max `Neg*Neg` at `(min(n-1, m-1-d), m-1)`.
  - So we have up to 4 starting points.
  - And we need to expand in the correct directions.
  - For `Pos*Pos` (indices 0,0), we expand `i++` and `j++` (decreasing values).
  - For `Neg*Neg` (indices n,m), we expand `i--` and `j--` (increasing values, i.e., larger negatives -> larger product).
  - We can put all 4 start points in the Max-Heap.
  - Use a global `visited` set.

## Naive Approach

### Intuition

Generate all valid pairs, sort them.

### Time Complexity

- **O(N*M log (NM))**: TLE.

## Optimal Approach

### Key Insight

Use a Max-Heap to explore the valid regions from the "corners" where products are maximized.
Since `A` and `B` are sorted descending:
- `A[0]*B[0]` is max positive (if positive).
- `A[n-1]*B[m-1]` is max positive (if negative * negative).
- We explore from `(d, 0)` and `(0, d)` moving `+i, +j`.
- We explore from `(n-1, min_j)` and `(min_i, m-1)` moving `-i, -j`.

### Algorithm

1. Identify Start Points:
   - **TL1:** `(d, 0)` if valid. Direction `(+1, +1)`.
   - **TL2:** `(0, d)` if valid. Direction `(+1, +1)`.
   - **BR1:** `(n-1, min(m-1, n-1-d))` if valid. Direction `(-1, -1)`.
   - **BR2:** `(min(n-1, m-1-d), m-1)` if valid. Direction `(-1, -1)`.
2. Max-Heap stores `(product, i, j, type)`.
   - `type` indicates expansion direction?
   - But we need to know which way to expand.
   - `Pos*Pos` candidates decrease as indices increase.
   - `Neg*Neg` candidates decrease as indices decrease.
   - So we can't mix them blindly without knowing direction.
   - Better: Just have 2 heaps? Or push `(product, i, j)` and try ALL neighbors?
   - No, `(d, 0)` neighbors are `(d+1, 0)` and `(d, 1)`.
   - `(n-1, k)` neighbors are `(n-2, k)` and `(n-1, k-1)`.
   - If we mix, we can expand `(d,0)` to `(d-1, 0)` which is wrong (larger value).
   - So, keep them separate or encode direction.
   - Use 4 start nodes in heap, each with a strategy.
   - `Strategy 1 (TL)`: Expand `(i+1, j)` and `(i, j+1)`. Check bounds and `|i-j|>=d`.
   - `Strategy 2 (BR)`: Expand `(i-1, j)` and `(i, j-1)`. Check bounds and `|i-j|>=d`.
   - Note: `TL` handles `Pos*Pos`. `BR` handles `Neg*Neg`.
   - What if `Pos*Neg`? Those are small, will be popped last.
   - Do we need to cover them? Yes, if k is large.
   - `TL` expansion eventually covers everything reachable by `+1`.
   - `BR` expansion covers everything reachable by `-1`.
   - Do they meet? Yes.
   - Is it sufficient?
   - `TL` starts at high positive, goes down.
   - `BR` starts at high positive (neg*neg), goes down.
   - This covers all local maxima.
3. **Visited Set:** `Set<String>` "i,j".

### Time Complexity

- **O(K log K)**.

### Space Complexity

- **O(K)**.

![Algorithm Visualization](../images/HEP-010/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input:** `3 3 3 1`. A: `9 7 5`. B: `8 3 1`.
d=1.
TL Starts: `(1,0)` -> 7*8=56. `(0,1)` -> 9*3=27.
BR Starts: `(2, 1)` -> 5*3=15. `(1, 2)` -> 7*1=7.
Heap: `[56, 27, 15, 7]`.

1. Pop 56 `(1,0)`. Res: `[56]`.
   - Expand `(2,0)` (40), `(1,1)` (Invalid).
   - Heap: `[40, 27, 15, 7]`.
2. Pop 40 `(2,0)`. Res: `[56, 40]`.
   - Expand `(3,0)` (Out), `(2,1)` (Visited).
   - Heap: `[27, 15, 7]`.
3. Pop 27 `(0,1)`. Res: `[56, 40, 27]`.
   - Expand `(1,1)` (Invalid), `(0,2)` (9).
   - Heap: `[15, 9, 7]`.

Result: `56, 40, 27`. Correct.

## ✅ Proof of Correctness

### Invariant
- The Max-Heap always contains the largest unexplored valid products reachable from the corners.
- Since valid regions are monotonic (mostly), expanding neighbors covers all candidates.
- Handling both TL (Pos*Pos) and BR (Neg*Neg) ensures we don't miss large products from negative numbers.

## 💡 Interview Extensions

- **Extension 1:** What if arrays are not sorted?
  - *Answer:* Sort them first (`O(N log N)`).
- **Extension 2:** K-th smallest?
  - *Answer:* Use Min-Heap and start from other corners.

### Common Mistakes to Avoid

1. **Missing Negative Products**
   - ❌ Wrong: Only checking top-left corners.
   - ✅ Correct: Check bottom-right corners too for large negative products.
2. **Infinite Loops**
   - ❌ Wrong: Not using visited set.
   - ✅ Correct: Track `(r, c)` to avoid re-processing.

## Related Concepts

- **K-Way Merge:** Generalization.
- **Dijkstra/BFS on Grid:** Similar traversal logic.
