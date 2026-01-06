---
problem_id: ARR_DUP_DIST_MIN__8812
display_id: ARR-025
slug: duplicate-distance-minimization
title: "Duplicate Distance Minimization"
difficulty: Medium
difficulty_score: 45
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - case-analysis
  - coding-interviews
  - data-structures
  - optimization
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-025: Duplicate Distance Minimization

## 📋 Problem Summary

You have an array.
"Duplicate Distance" = Minimum distance (`|j-i|`) between any two equal values in the array.
You can remove **at most one** element.
Goal: Minimize this "Duplicate Distance".
Wait. **Minimize** the minimum distance? That sounds easy — try to create a close pair?
Read carefully: "Minimize this duplicate distance by removing at most one element."
Usually removing elements _increases_ gaps (increases distance).
So the problem likely implies: "The current Duplicate Distance is determined by some pair. Can you remove an element to _break_ that pair (or shift indices) such that the _new_ global minimum distance is smaller?"
Actually, removing an element makes indices shift. `index 5` becomes `index 4`.
Distances might _decrease_. `|5-2|=3` -> `|4-2|=2`.
So removing an element between a pair brings them closer!
Yes. We want to bring equal elements **closer** together to minimize the distance.

## 🌍 Real-World Scenario

**Scenario Title:** 🚂 The Train Carriage Gap

### The Problem

You have a train with carriages of different types (Colors).
You want two Red carriages to be as close as possible (small distance) so passengers can walk between them easily.
Currently, the closest pair of same-colored carriages is distance 5 apart.
You can remove ONE carriage from the train (uncouple it). The train reconnects.
Can you make a pair closer?

### Real-World Relevance

- **Memory Allocation:** Compacting memory by removing a block to bring related memory pages closer (cache locality).

## 🚀 Detailed Explanation

### 1. How Distance Changes

Gap between `i` and `j` is `j - i`.
If we remove `k`:

- If `k < i`: Both `i, j` shift left by 1. Gap `(j-1) - (i-1) = j - i`. Unchanged.
- If `k > j`: Indices unchanged. Gap unchanged.
- If `i < k < j`: `j` shifts to `j-1`. `i` stays. Gap becomes `j - i - 1`. **Reduced by 1!**

So, removing an element _between_ a pair decreases their distance by 1.
Removing one of the elements _itself_ destroys that specific pair.

### 2. Strategy

We want to minimize the GLOBAL minimum distance.
Let `GlobalMin` be the min distance in the original array.
We want to see if we can reach `GlobalMin - 1`.
Can we?
If we find the pair `(u, v)` that creates `GlobalMin`, and we remove any `k` such that `u < k < v`, the distance becomes `GlobalMin - 1`.
This is only possible if `GlobalMin - 1 >= 1` (distance cannot be 0).
Also, we need `u < k < v` to exist. (i.e., `v - u > 1`).
So if `GlobalMin >= 2`, we can reduce it to `GlobalMin - 1`.

What if there are multiple pairs defining `GlobalMin`?
We need to reduce _all_ of them?
Wait. The Metric is `Min(All Pairs)`.
If we have pairs with dist 5, 10, 20. `GlobalMin` = 5.
If we reduce the 5 -> 4. `GlobalMin` becomes 4.
If we reduce 10 -> 9. `GlobalMin` remains 5 (determined by the other pair).
To _decrease_ the result, we must reduce the specific pair(s) that are minimal.
However, we assume we simply want to finding the _best possible single move_.
We iterate all adjacent equal pairs (since min dist must be adjacent occurrences of a value).
For each pair `(u, v)`, if we remove something between, dist becomes `dist-1`.
We take the minimum over all pairs.

Wait! Could removing an element create a _new_ pair?
No. Duplicate means same value. Removing an element (unless it's the value itself) doesn't delete values. It just shifts indices.
Could removing `X` bring `A` and `B` closer? Yes.
So we essentially calculate `OriginalDist - 1` for every pair (that has a gap), and `OriginalDist` for pairs with no gap (adjacent).
The answer is `min(OriginalDist - 1)`?
Yes. Effectively `min(OriginalDist)` over the whole array, but if `pair_dist >= 2`, we can potentially count it as `pair_dist - 1`. This effectively means `GlobalMin` can be reduced by 1 if `GlobalMin >= 2`.
Exception: If the _only_ pairs with `GlobalMin` are adjacent (`dist=1`), we cannot put anything between them. We cannot reduce them.
So if `GlobalMin == 1`, answer is 1.
If `GlobalMin > 1`, answer is `GlobalMin - 1`.

Is that it?
What if removing an element `X` helps pair A (`dist 5->4`) but we ignore pair B (`dist 4`)?
We need the _Global_ min of the modified array.
The modified array's global min is `min(Pair_1_new, Pair_2_new, ... Pair_N_new)`.
Since we remove `k`, _every_ pair spanning `k` reduces by 1. Pairs not spanning `k` stay same.
We want to pick `k` to minimize the _result_.
Actually, since we want to _minimize_ the minimum, we just need to find ONE pair that becomes very small.
Wait.
`Result = min over valid removal k ( min over pairs (dist_pair) )`.
This logic is inverted.
We want the final state to have a small distance.
Does it involve reducing the _current_ minimum?
No.
Example: `1 ... 1` (dist 100), `2 ... 2` (dist 5).
If we remove between 2s, dist becomes 4. Result 4.
If we remove between 1s, dist 1s -> 99. Dist 2s -> 5. Result 5.
We pick the move that gives 4.
So we look at ALL pairs.
For each pair, `PotentialDist = OriginalDist - 1` (if gap exists) or `OriginalDist` (if adjacent).
The Answer is `min(PotentialDist)` across all pairs?
Yes! Because we can choose to target _that specific pair_ to reduce it.
And since `min` operator is monotonic, reducing one term never hurts the global minimum (unless we ignored an even smaller term).
But we iterate _all_ pairs. So we will definitely see the smallest term.

So Algorithm:

1. Find all duplicate pairs (adjacent occurrences of same value).
2. Calculate their distance.
3. `EffectiveDistance = (dist > 1) ? dist - 1 : dist`.
4. Ans = `min(EffectiveDistance)` over all pairs.

### 🔄 Algorithm Flow Diagram

<!-- mermaid -->

```mermaid
flowchart TD
    A[Start] --> B[Map: Value -> LastIndex]
    B --> C[GlobalMin = Infinity]
    B --> D[Loop i from 0 to N-1]
    D --> E{seen arr[i]?}
    E -- Yes --> F[Dist = i - Map[arr[i]]]
    F --> G[NewDist = (Dist > 1) ? Dist-1 : 1]
    G --> H[GlobalMin = min(GlobalMin, NewDist)]
    H --> I[Update Map[arr[i]] = i]
    E -- No --> I
    I --> D
    D -- End Loop --> J[Return GlobalMin]
```

## 🧪 Edge Cases to Test

1.  **No Duplicates:** Return -1.
2.  **Adjacent Pairs:** `1 1`. Dist 1. Cannot reduce. Ans 1.
3.  **Gap 1:** `1 2 1`. Dist 2. Remove '2'. Dist 1. Ans 1.

## 🏃 Naive vs Optimal Approach

### Linear Scan O(N)

- **Time:** O(N).
- **Space:** O(N) for Map.
  Optimal.
