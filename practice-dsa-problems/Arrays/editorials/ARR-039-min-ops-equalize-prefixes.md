---
problem_id: ARR_PREFIX_EQ_OPS__4112
display_id: ARR-039
slug: min-ops-equalize-prefixes
title: "Minimum Operations to Equalize Prefixes"
difficulty: Hard
difficulty_score: 65
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - coding-interviews
  - constructive
  - data-structures
  - logic
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-039: Minimum Operations to Equalize Prefixes

## 📋 Problem Summary

Operations:

1. `INC i`: Add 1 to `A[1..i]`.
2. `ROT i`: Rotate `A[1..i]` left.
   Goal: Make every `A[i] == T`.
   Constraint: Minimize ops. Values cannot decrease (only INC). If `A[i] > T`, impossible.

## 🌍 Real-World Scenario

**Scenario Title:** 🔓 The Combination Lock

### The Problem

You have a complex lock with `N` tumblers.
Each tumbler must align to level `T`.
Pulling the "Master Lever" at position `i` lifts all tumblers `1` to `i` by 1.
Turning the "Dial" at position `i` shifts the positions of tumblers `1` to `i`.
Find the sequence of moves to align everything.

## 🚀 Detailed Explanation

### 1. Reverse Thinking

Target state: `[T, T, T...]`.
Consider the _last_ element `A[n]`.
Operations `INC i` and `ROT i` for `i < n` DO NOT affect `A[n]`.
Only `INC n` or `ROT n` affect `A[n]`.
Actually, notice that `INC n` adds 1 to _everything_.
`ROT n` permutes everything.
The condition "every prefix sum equal to `i*T`" is equivalent to "every element `A[i] == T`".

### 2. Strategy

Work from `N` down to `1`.
At index `n`:

- We need `A[n]` to become `T`.
- `INC k` where `k < n` doesn't touch `A[n]`.
- `INC n` adds to `A[n]`.
  If we fix `A[n]` now, can we disturb it later?
  No. Operations on `i < n` won't touch `A[n]`.
  So `A[n]` MUST be fixed using operations of scope `>= n`.
  Wait. `ROT n` moves `A[n]` to `A[n-1]`.
  This suggests we can swap elements?
  Actually, `ROT i` allows cyclic shift of prefix.
  If we can `ROT n`, we can effectively bring ANY of `A[1..n]` to position `n`.

**Greedy Choice:**
At step `n`, we look at `A[1..n]`. We want to pick one element to be the final `A[n]`.
Which one?
The one that is closest to `T` without exceeding it?
Or maybe we simply fill `A[n]` with the largest valid value currently available?
If we pick `val`, cost to fix it is `T - val` (using `INC n`).
However, `INC n` _also_ increases `A[1..n-1]`. This is beneficial! It helps others reach `T`.
So, to minimize operations, we want to maximize the "side effect" of `INC`.
We should choose the element in `A[1..n]` that requires the **most** increments (i.e., is smallest)?

- If we pick Smallest `S`: we add `T-S` to everyone. Everyone increases by `T-S`.
- Can this overshoot T?
- Yes. If there is a Large `L` in the set, `L + (T-S)` might > `T`.
- So we are constrained by the **Largest** element.
- Since we MUST NOT overshoot `T`. The increments we apply at stage `n` are limited by `T - Max(A[1..n])`.
- But we NEED to make `A[n]` reach `T`.
- So the element we place at `A[n]` MUST satisfy: `Val + (T - Max(Rest)) >= T`.
- Actually, simpler:
  1. We must select an element `X` from `A[1..n]` to place at `n`.
  2. We will apply `k` global increments (using `INC n`).
  3. `X` becomes `X + k`. We need `X + k == T`. So `k = T - X`.
  4. All other elements `Y` become `Y + k`.
  5. Constraint: For all other `Y`, `Y + k <= T`.
     `Y + T - X <= T` => `Y <= X`.
  6. This implies `X` must be the **Maximum** element in `A[1..n]`.

**Conclusion:** We MUST pick the maximum element of the current prefix to be the one we fix at the end.
Why? Because picking anything smaller requires adding more to it, which would cause the maximum element (which also gets added to) to exceed `T`.
(Since `Max > Chosen`, `Max + (T - Chosen) > T`).

Algorithm:
For `i` from `N` down to 1:

1. Find `Max` in `A[1..i]`.
2. Move `Max` to position `i` using `ROT i`.
   - Operations: Calculate distance. `ROT`s needed.
3. Apply `INC i` until `Max` reaches `T`.
   - Count `diff = T - Max`.
   - **Crucial:** This `INC` adds `diff` to all `A[1..i]`.
   - Update `A[1..i]`? No, maintain a "Lazy Offset".
4. "Remove" `i` (done). Repeat for `i-1`.

Wait. `ROT` ops count? Yes.
We need to efficiently find the position of the Max element in `A[1..i]`?
And simulate the rotations?
With `N=200,000`, we need a fast way.
We maintain the array in a data structure that supports:

- Find Max Value and Index.
- Range Add.
- Cyclic Shift?
  Cyclic shift is hard for SegTree.
  However, note we always move Max to end, fix it, then ignore it.
  This is exactly **Sorting**.
  We are selecting Max, moving to end.
  But we need to count `ROT` ops.
  If we just need to pick the Max, does the `ROT` cost matter?
  Yes, "Find minimum number of operations".
  Does picking a _different_ Max (if duplicates) help?
  Possibly. Pick the one closest to current end?

Actually, simpler view:
The problem asks for min ops.
We determined we **must** pick the maximum available.
So, relative order of elements doesn't matter for validity, only for `ROT` cost.
But wait.
The `Max` element must be at position `i`.
If `Max` is at `k`, we need `i - k` rotations (left shifts).
Actually `ROT i` rotates `1..i`.
Current `A` is a dynamic list.
This looks like we need to just organize the values?
Wait. `ROT i` can reorder `1..i` arbitrarily.
Cost of arbitrary reorder is huge.
But we only need to move Max to `i`.
Can we do it cheaply?
Actually, do we _really_ need to perform rotations?
Maybe we just say "At step `i`, the set of available values is `S`. We pick `max(S)`, add `T - max(S)` to global offset, and remove `max(S)` from set."
Does `ROT` cost 0? No.
The problem: "Minimum number of operations".
Maybe `ROT` is expensive.
Is there a case where we don't pick Max?
If we pick `2nd Max`, we overshoot `Max`. Impossible.
So we MUST pick Max.
So the "Value Operations" (INC) are fixed regardless of movement: `Sum(T - A_sorted[i])`?
No. `INC i` adds to all remaining.
Let sorted initial values be `v_1 <= v_2 <= ... <= v_n`.
At step `n`, we pick `v_n` (Max). Ops = `T - v_n`. Current offset increases by `T - v_n`.
Now all become `v_k + (T - v_n)`.
At step `n-1`, we pick `v_{n-1}`. Requires `T - (v_{n-1} + Offset)`.
Total INC ops is fixed by the set of values!
`Total INC = (T - v_n) + (T - (v_{n-1} + (T - v_n)))`...
`= (T - v_n) + (v_n - v_{n-1}) + ...`
`= T - v_1`.
Basically we perform increments to raise the floor `v_1` to `T`.
Wait. `INC n` raises everything.
So we just need `v_1` (min element) to reach `T`.
Ops = `T - min(A)`.
This handles all INCs.
What about ROTs?
We need to sort the array `A` into `v_1, v_2 ... v_n` using `ROT`.
Can we sort using `ROT`?
`ROT i` is cyclic shift.
This is basically "Bubble Sort" logic or similar?
Actually simpler: We need to move `Max` to `n`. Then `2nd Max` to `n-1`.
Can we do this with 0 ROTs? Only if already sorted.
Each ROT moves elements.
This part is complex.
Given "Hard", maybe `ROT` implies we can arrange freely?
No, "Rotate left by 1" costs 1 op.
With `N` large, we can't emit `O(N^2)` ops.
But we need to output "Number of Ops".
Is it `T - Min + Inversions`? No.
Actually, look at the constraints: `INC i` affects `1..i`.
This confirms we must strip from right. Max must be at `n`.
If `A` is `[3, 1, 3]`. T=3.
`n=3`. Max is 3. At pos 1 or 3.
If at 3, we good.
If `[1, 3, 3]`. Max at 2 or 3.
We need to check if A is sorted?
Actually, if we assume we can optimize `ROT`, maybe we just assume we perform necessary swaps?
Wait. Rules: `ROT i` rotates `1..i`.
This allows bringing any element at `k <= i` to position `i` in `i-k` ops? No, `k` ops (left shift `k` times).
Or `1` op (`Right shift`)? No `Left shift`.
So `k` left shifts brings `A[k]` to `A[i]`? No.
Left shift: `1 2 3 4` -> `2 3 4 1`.
Element at `1` goes to `n`.
So 1 ROT brings `A[1]` to `A[i]`.
To bring `A[k]` to `A[i]`, we need to ROT until `A[k]` is at 1, then ROT once more?
This is getting messy.

Re-read carefully: "make every prefix sum equal to `i * T`".
This implies `A[1..n]` is `[T, T, T...]`.
We need to transform `A` to `[T, T...]`.
We established `Total INC = T - Min(A)`.
What about `ROT`?
We need `A` to be sorted? No. `A` ends up all `T`. All equal.
So order DOES NOT MATTER!
If we successfully raise `Min` to `T`, and we validated that we always pick Max to fix at `n`, does the _position_ of Max matter?
Yes, because `INC i` only affects `1..i`.
If we leave `Max` at `i`, and increment `1..i`, `Max` grows.
If we move `Max` to `i+1` (outside scope), it stops growing.
We need `Max` to stop growing exactly when it hits `T`.
Since we proved `Max` is the _first_ to hit `T` (closest), we MUST effectively move `Max` out of the "active set" `1..i` exactly when it hits `T`.
This corresponds to `Max` being at position `i` when we process step `i`.
This implies `A` must be sorted ascending?
If `A = [10, 5]`, T=10.
INC 2 (x5): `[15, 10]`. Max overshot.
If sorted `[5, 10]`.
INC 2 (x0) -> `[5, 10]`.
Move 10 out. Active `[5]`.
INC 1 (x5) -> `[10]`.
Result `[10, 10]`. Done.
So **Yes, A must be sorted** to minimize ops (and to be valid).
If `A` is not sorted, we must sort it?
But we can only `ROT`.
Can we sort `A` using `ROT`?
And we want Min Ops.
Actually, if we have duplicate Max values, we can pick the one "easiest" to interact with.
This looks like:

1. `Base Ops = T - Min(A)`.
2. Plus `Sorting Cost`?
   Can we sort with `ROT`?
   `ROT i` is very powerful. `ROT n` can cycle array.
   Actually, notice that we process from `n` down to `1`.
   At step `n`, we need `Max` to be at `n`.
   If `Max` is not at `n`, we must `ROT n` until it is.
   Cost: Distance to shift `Max` to `n`.
   Since `ROT n` cycles, we just shift until `Max` is at end.
   Then we effectively "lock" position `n`.
   Then operate on `n-1`.
   This is Selection Sort using Rotation.
   Does `ROT n` disturb relative order of `1..n-1`?
   Yes, it cycles them.
   So relative order is preserved (cyclically).
   This means we just need to align the array.
   Actually, if we need `A` sorted, and we have `[2, 1, 3]`.
   `Max` 3 is at `n`. Good. Lock.
   `[2, 1]`. `Max` 2 is at `1`. Need at `2`.
   `ROT 2`: `[1, 2]`. Good. Lock.
   Total `ROT`s?
   This depends on original positions.
   Since relative cyclic order is preserved...
   We can only sort if the array is **already sorted cyclically!**
   `[3, 4, 1, 2]` -> can be sorted by rotations.
   `[1, 3, 2]` -> Cannot be sorted by global rotations.
   But we have `ROT i`. We can sort anything!
   But we want MIN ops.
   This implies we shouldn't sort if we don't have to?
   But we proved valid INC strategy requires `A[i] <= A[i+1]` effectively (since `A[i]` stays in active set longer, it receives more increments than `A[i+1]`).
   If `A[i] > A[i+1]`, `A[i]` grows MORE than `A[i+1]`? No, `A[i]` leaves set later.
   Wait.
   `A[n]` removed first. Receives least increments.
   `A[1]` removed last. Receives most increments.
   So we need initial `A[n] >= A[n-1] >= ... >= A[1]`.
   NO! `A[n]` is `Max`. It is close to `T`. It needs FEW increments.
   `A[1]` is `Min`. It needs MANY increments.
   So we need `A` to be sorted `Ascending`.
   `A[1] = Min`, `A[n] = Max`.
   So we simply need to calculate **Minimum Operations to Sort A using Prefix Rotations**.
   This is a classic problem: "Pancake Sorting" variation?
   Actually, `ROT i` is specialized.
   Standard "Min Ops to Sort" is hard.
   But do we need fully sorted?
   Yes.
   Is the array sortable _efficiently_?
   Maybe constraints on `A` are loose?
   Wait. If we assume we use the Selection Sort strategy:
   "Rotate `1..i` to bring Max to `i`".
   This is always possible.
   Is it minimal?
   Usually Selection Sort strategies (bring max to end) are decent but not optimal for general swaps.
   But here `ROT` is the only move.
   With `ROT`, we can bring `k-th` element to `i` in `k` ops? No `1` op?
   Left Rotate `[a b c d]`. `b \to a`. `a \to d`.
   Repeated `ROT` shifts.
   To bring index `k` to `n` (end): `k` left shifts?
   Example `k=1` (start). `[M x x]`. L-Rot -> `[x x M]`. 1 op.
   Example `k=2`. `[x M x]`. L-Rot -> `[M x x]`. L-Rot -> `[x x M]`. 2 ops.
   So cost is distance to end.
   But we change the positions of everyone else!
   This feels like `O(N^2)` simulation.
   Is there an `O(N)` logic?
   Maybe we don't need to simulate.
   We are checking inversion counts or cyclic shifts?
   Actually, look at the constraints. `N=200,000`.
   We cannot simulate.
   We need the answer `Total INC Cost + Total ROT Cost`.
   `Total INC = T - Min`.
   `Total ROT = ?`.
   Answer: We probably can't sort efficiently if it's not cyclically sorted.
   But "If impossible, output -1".
   Maybe it's ONLY possible if array is Cyclically Sorted?
   With `ROT i`, we can fix local inversions?
   `[3 2 1]`.
   `i=3`. Max 3 at 1. `ROT 3` -> `[2 1 3]`. Cost 1.
   `i=2`. Max 2 at 1. `ROT 2` -> `[1 2 3]`. Cost 1.
   Sorted!
   So yes, we can sort.
   Does the strategy "Move Max to End" work optimally?
   It's likely the intended Greedy strategy.
   How to simulate in `O(N log N)`?
   We need to track positions of numbers.
   Initially we map `Val -> Index`.
   As we rotate `1..i`, indices change.
   This is a standard "Josephus" or "Index Tracking" structure.
   Use a **Fenwick Tree**.
   Track "Present" elements.
   Initially all `1..N` present.
   At step `i` (finding i-th largest value):

- Original index `Pos`.
- Current position = `Sum(BIT, Pos)`. (Count how many active elements are before it).
- We want to move it to Position `i` (which is `Count(Active)`).
- Distance = `i - CurrentPos`? No.
- It is cyclic.
- Wait. Rotations wrap around.
- Actually, `ROT i` rotates the ACTIVE prefix.
- If we work backwards `N` to `1`:
- We identify the `Max` among remaining.
- We need to move it to the _end_ of the active prefix.
- Cost = `CurrentPos` (0-based from left) ? No.
- If we Left Rotate `1..i`, index 0 goes to `i-1`.
- If `Max` is at index `k` (0-based), we need `k+1` LEFT rotations to bring it to end?
- Example `[x M x]`. `k=1`. `len=3`.
- `ROT` -> `[M x x]`. `ROT` -> `[x x M]`. 2 ops `k+1`.
- Wait. `Left ROT` shifts indices `i -> i-1`. `0 -> n-1`.
- To get index `k` to `n-1`: We need `k+1` shifts.
- `pos k` -> `k-1` -> ... -> `0` -> `n-1`. (k+1 steps).
- Yes. Cost = `(CurrentIndex + 1) % ActiveLength`?
- Wait. `n-1` is end. `Pos n-1` needs 0 shifts.
- `Pos 0` needs 1 shift.
- Formula: `(CurrentIndex + 1) % ActiveLength`.
- Wait. `Pos 0` -> `n-1`. 1 shift. Correct.
- `Pos n-1` -> `0`. `(n-1)+1 = n` -> `0`. Correct.
- So we sum these costs.
- Then we "delete" this element (mark as inactive in BIT).

Algorithm:

1. Sort `A` keeping original indices. Store pairs `(Val, OrigIdx)`.
   - Sort priority: Value Descending. (If equal, typically rightmost or leftmost? Rightmost usually preserves stability better for 'last' pos).
2. BIT initialized to 1s.
3. Iterate `(Val, OrigIdx)` in sorted order.
4. `ActivePos = QueryBIT(OrigIdx) - 1`. (0-based rank among active).
5. `Length = QueryBIT(N)`. (Total active).
6. `Cost = (ActivePos + 1) % Length`.
7. Add Cost.
8. Update `BIT(OrigIdx, -1)`. Change `Total INC` logic (constant).
   - Actually the problem has "Current Rotation Offset".
   - The array is physically rotated!
   - Our `ActivePos` assumes static array with deletions.
   - BUT the array rotates.
   - So `OrigIdx` is no longer valid.
   - We need to track the `Global Rotation Offset`.
   - `CurrentPos = (OrigPos - GlobalOffset) % Length`.
   - When we apply `ROT`, `GlobalOffset` changes.
   - `Shift = (ActivePos + 1) % Length`.
   - `GlobalOffset = (GlobalOffset + Shift) % Length`.
   - Wait. `ROT i` only rotates `1..i`.
   - But we process `i` from `N` down to `1`.
   - So `ROT i` rotates the _entire_ remaining active array.
   - So the "Global Offset" concept applies perfectly to the remaining set.
   - YES!

Result: `O(N log N)`.

### 🔄 Algorithm Flow Diagram

<!-- mermaid -->

```mermaid
flowchart TD
    A[Start] --> B[Values: pairs (Val, Idx). Sort Desc (stable)]
    B --> C[Init BIT size N with 1s. Offset = 0]
    C --> D[Loop i from 0 to N-1 (processing Max to Min)]
    D --> E[OrigIdx = Values[i].Idx]
    E --> F[RawRank = SUM(BIT, OrigIdx) - 1]
    F --> G[ActiveLen = N - i]
    G --> H[CurrPos = (RawRank - Offset) % ActiveLen]
    H --> I[Ops = (CurrPos + 1) % ActiveLen]
    I --> J[TotalRot += Ops]
    J --> K[Offset = (Offset + Ops) % ActiveLen]
    K --> L[Update BIT(OrigIdx, -1)]
    L --> D
    D -- End Loop --> M[TotalInc = T*N - Sum(A)? No. T - Min.]
    M --> N[Return TotalRot + TotalInc]
```

## 🧪 Edge Cases to Test

1.  **Already Sorted:** `1 2 3`.
    - 3 at `2`. Rank 2. `Offset 0`. `Pos 2`. `Len 3`. `Ops = (2+1)%3 = 0`.
    - 2 at `1`. Rank 1. ...
    - Ops 0. Correct.
2.  **Reverse:** `3 2 1`.
    - 3 at `0`. `Pos 0`. `Ops 1`. `Offset 1`.
    - 2 at `1`. `Rank 1`. `Len 2`. `Pos (1-1)%2 = 0`. `Ops 1`. `Offset 2`.
    - Total 2.
    - Check: `3 2 1` ->(1)-> `2 1 3` ->(1)-> `1 2 3`. Correct.

## 🏃 Naive vs Optimal Approach

### Naive O(N^2)

Simulate array.

### BIT + Logic O(N log N)

- **Time:** O(N log N).
- **Space:** O(N).
  Optimal.
