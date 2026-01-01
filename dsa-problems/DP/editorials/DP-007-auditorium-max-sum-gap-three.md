---
problem_id: DP_MAXSUM_GAP3__7706
display_id: DP-007
slug: auditorium-max-sum-gap-three
title: "Auditorium Max Sum With Gap Three"
difficulty: Medium
difficulty_score: 45
topics:
  - Dynamic Programming
  - Array
  - Optimization
tags:
  - dp
  - arrays
  - maximum-sum
  - medium
premium: true
subscription_tier: basic
---

# DP-007: Auditorium Max Sum With Gap Three

## 📋 Problem Summary

You are given an array `a[0..n-1]`. Pick some indices so that any two picked indices are at least 3 apart, and maximize the sum of the picked values.

Key constraint:

- If you pick `i`, you must skip `i-1`, `i-2`, `i+1`, `i+2`.

Return the maximum possible sum. You are allowed to pick nothing (sum 0), which matters when all numbers are negative.

## 🌍 Real-World Scenario

**Scenario Title:** Auditorium Seat Rewards With Buffer Rows

Imagine an auditorium where each seat row has a “reward score” for placing a volunteer there (maybe it improves supervision or distribution). But due to crowd management, if you place a volunteer in row `i`, you must keep rows `i±1` and `i±2` free of volunteers to avoid interference and maintain clear aisles.

So you want to pick a set of rows (indices) to maximize total reward while respecting a **gap of 3**.

This pattern is common in:

- scheduling tasks with a cooling period
- placing sensors with minimum distance constraints
- maximizing profit while enforcing “no nearby selections”

**Why This Problem Matters:**

- It’s a clean introduction to “max sum with skipping” DP (House Robber family)
- It teaches you to encode constraints into state transitions
- It reinforces O(n) DP with O(1) memory

![Real-World Application](../images/DP-007/real-world-scenario.png)

## ✅ Clarifications (Be brutally accurate)

- Indices are 0-based conceptually, but input is just a list.
- Gap rule: for any two chosen indices `i` and `j`, `|i-j| >= 3`.
- You may choose an empty set. That means the answer is at least `0`.
  - Example: `[-5, -2]` ⇒ answer `0`.
- Values can be negative and large in magnitude, so use 64-bit (`long long`/`long`).

## Detailed Explanation

### Seat Selection Visualization with Gap-3 Constraint

```
Seats:  [50, 30, 70, 20, 60, 40, 80]
Index:   0   1   2   3   4   5   6

Gap constraint: Cannot select adjacent or within 2 seats
(gap=3 means at least 2 empty between selected seats)

Visual representation of valid selections:
  ●   ○   ○   ●   ○   ○   ●
  [0] [_] [_] [3] [_] [_] [6]  → 50 + 20 + 80 = 150

  ○   ●   ○   ○   ●   ○   ○
  [_] [1] [_] [_] [4] [_] [_]  → 30 + 60 = 90

  ○   ○   ●   ○   ○   ●   ○
  [_] [_] [2] [_] [_] [5] [_]  → 70 + 40 = 110

Legend: ● = selected, ○ = skipped, _ = forced skip

State Transitions:
  dp[i] = max(dp[i-1], dp[i-3] + a[i])
           └─────┬─────┘
           Skip i    Rob i (must skip i-1, i-2)

For each seat i:
  Option 1: Skip seat i → carry forward dp[i-1]
  Option 2: Rob seat i  → add a[i] to dp[i-3] (last valid state)

Example transitions:
  dp[0] = max(0, 50 + 0) = 50
  dp[1] = max(50, 30 + 0) = 50
  dp[2] = max(50, 70 + 0) = 70
  dp[3] = max(70, 20 + 50) = 70
  dp[4] = max(70, 60 + 50) = 110
  dp[5] = max(110, 40 + 70) = 110
  dp[6] = max(110, 80 + 70) = 150
```

### Visual intuition (gap = 3)

For each index `i`, indices that conflict with `i` are:

- `i-2`, `i-1`, `i+1`, `i+2`

So if you pick `i`, the next pick to the right can start only from `i+3`.

You can think of it as: “pick an element, then force-skip the next two elements.”

### Why `dp[i-3]` is the only valid look-back for “take”

When you take index `i`, any other chosen index must satisfy distance ≥ 3.

So the previous chosen index `j` must be:

- `j <= i-3`

Among all solutions that end before or at `i-3`, the best sum is exactly `dp[i-3]`.

That is why the recurrence has `a[i] + dp[i-3]`.

If you mistakenly use `dp[i-2]`:

- you allow combining `i` with `i-2`, which is distance 2 (illegal)

So `i-3` is not “a random hack”; it comes directly from the constraint.

### Mini table for understanding (n small)

Let `a = [4, 1, 2]`:

- dp[-1]=0, dp[-2]=0, dp[-3]=0
- dp[0] = max(0, 4) = 4
- dp[1] = max(4, 1) = 4
- dp[2] = max(4, 2) = 4

Because with gap 3, you cannot take two elements within indices 0..2 anyway (all are too close). So the best is just the max single element.

Now extend: `a = [4, 1, 2, 9]`

- dp[3] = max(dp[2]=4, a[3]+dp[0]=9+4=13) = 13

Now you can combine index 0 and 3 because they are exactly 3 apart.

This is the first index where “take” can beat “skip”.

### What makes it DP?

At each position `i`, you face a binary choice:

- **Skip `i`**: then the best answer up to `i` is whatever was best up to `i-1`.
- **Take `i`**: then you must ensure no picked index is within distance 2 of `i`, so the previous picked index can be at most `i-3`.

So “take i” connects to `dp[i-3]`, not `dp[i-1]` or `dp[i-2]`.

### DP definition

Let:

`dp[i] = maximum sum you can obtain using indices in [0..i]`

Then:

- `dp[i] = max( dp[i-1], a[i] + dp[i-3] )`

Where:

- `dp[x] = 0` for any `x < 0` (meaning “take nothing before start”)
- also ensure we never return negative sums (empty set allowed). This is automatically handled by the recurrence if `dp` never goes below 0.

### Base behavior for small i

Using the `dp[x]=0 for x<0` trick, the formula works uniformly:

- i = 0:
  - dp[0] = max(dp[-1]=0, a[0] + dp[-3]=0) = max(0, a[0])
- i = 1:
  - dp[1] = max(dp[0], a[1] + dp[-2]=0)
- i = 2:
  - dp[2] = max(dp[1], a[2] + dp[-1]=0)

That already enforces the rule “cannot pick two indices within distance 2”, because taking i never adds dp[i-1] or dp[i-2].

### Another correct way to describe the state (prefix optimality)

`dp[i]` is optimal for a prefix. That means:

- It may or may not include index `i`.
- It does not care which indices were chosen, only the best achievable sum.

This “forgetting” of exact chosen indices is valid because the constraint is local and the decision at `i` only needs the best answer from far enough back (`i-3`).

This is exactly the DP principle: store only what you need for future transitions.

### Decision Tree for Gap-3 Constraint

```
For each seat i with value a[i]:
    │
    ├─ Option 1: Skip seat i
    │   │
    │   ├─ Carry forward best solution without i
    │   └─ dp[i] = dp[i-1]
    │
    └─ Option 2: Rob seat i (requires gap ≥ 3)
        │
        ├─ Cannot use seats i-1 or i-2 (conflict)
        │
        ├─ Can only come from seats 0..i-3
        │   └─ Best solution up to i-3 is dp[i-3]
        │
        └─ dp[i] = dp[i-3] + a[i]
            │
            └─ Final: dp[i] = max(Option 1, Option 2)
                            = max(dp[i-1], dp[i-3] + a[i])

Base cases:
  dp[-3] = dp[-2] = dp[-1] = 0 (no seats before start)
  dp[0] = max(0, a[0])
  dp[1] = max(dp[0], a[1])
  dp[2] = max(dp[1], a[2])
```

## Naive Approach

### Intuition

Try all subsets and check which ones satisfy the gap constraint, then take the max sum.

### Complexity

- Number of subsets = `2^n`
- Impossible for `n=100000`

Even if you prune, it’s still exponential.

## Optimal Approach (O(n) DP)

### Key Insight

The constraint only looks back a constant distance (3), so we only need to know dp values a few steps behind.

### Algorithm

1. Initialize three rolling dp values representing dp[i-3], dp[i-2], dp[i-1].
2. For each i from 0..n-1:
   - take = a[i] + dp[i-3]
   - skip = dp[i-1]
   - dp[i] = max(skip, take)
   - rotate the rolling variables
3. Return dp[n-1].

Because dp values are monotonic non-decreasing and start at 0, the result never drops below 0 (empty set option).

### Complexity

- Time: O(n)
- Space: O(1) extra space

![Algorithm Visualization](../images/DP-007/algorithm-visualization.png)
![Algorithm Steps](../images/DP-007/algorithm-steps.png)

## 🔁 Standard DP Table Form (Before Rolling Optimization)

Some students understand the “rolling variables” version only after seeing the full DP table version.

Let `dp[i]` be the best answer for prefix `[0..i]`.

Then:

- `dp[i] = max(dp[i-1], a[i] + dp[i-3])`
- treat `dp[x] = 0` when `x < 0`

Pseudo:

1. `dp = [0]*n`
2. for i in 0..n-1:
   - `take = a[i] + (dp[i-3] if i >= 3 else 0)`
   - `skip = dp[i-1] if i >= 1 else 0`
   - `dp[i] = max(skip, take)`
3. answer = dp[n-1]

This is already O(n) time and O(n) memory. Rolling variables compress the memory down to O(1).

## 🚫 Why “empty set allowed” changes answers

If you forget that you can pick nothing, you might incorrectly return a negative number.

Example:

`a = [-5, -2, -10]`

Any pick gives a negative sum, so the best choice is “pick nothing” ⇒ answer 0.

Our recurrence naturally supports this as long as `dp[-1]=0` and we always take `max(skip, take)` where skip is never negative.

## 🧪 Extra Example (All Negative)

Input:

```
4
-5 -1 -10 -3
```

Best answer is:

- pick nothing ⇒ 0

So output is `0`.

This case appears in hidden tests because many submissions incorrectly return `-1` or `-5`.

## 📊 Complexity Comparison (Interview-ready)

| Approach | Time | Space | Works for n=100000? |
|---------|------|-------|---------------------|
| Brute force subsets | `O(2^n)` | `O(n)` | ❌ |
| DP with array `dp[]` | `O(n)` | `O(n)` | ✅ |
| Rolling DP (this) | `O(n)` | `O(1)` | ✅ best |

The rolling DP is not “faster” in time; it is simply memory-optimized and cleaner.

## 🧩 Edge Cases Checklist (Quick sanity before submitting)

- `n = 1`: answer is `max(0, a[0])`.
- `n = 2`: answer is `max(0, a[0], a[1])` (cannot take both).
- `n = 3`: still cannot take two indices (any pair has distance ≤ 2), so answer is max single (or 0).
- Large negative values: answer can still be `0` because empty set is allowed.
- Large positive values: ensure you use 64-bit and avoid overflow in intermediate sums.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
Example:

`a = [4, 1, 2, 9, 3]`

We compute dp:

- i=0: dp[0] = max(0, 4) = 4
- i=1: dp[1] = max(4, 1) = 4
- i=2: dp[2] = max(4, 2) = 4
- i=3: dp[3] = max(4, 9 + dp[0]=4) = 13
- i=4: dp[4] = max(13, 3 + dp[1]=4) = 13

Answer = 13.

### State Evolution Table

| Index i | Value a[i] | dp[i-3] | dp[i-1] | Skip (dp[i-1]) | Rob (a[i] + dp[i-3]) | dp[i] | Decision |
|---------|------------|---------|---------|----------------|----------------------|-------|----------|
| 0       | 4          | 0       | 0       | 0              | 4 + 0 = 4            | 4     | Rob      |
| 1       | 1          | 0       | 4       | 4              | 1 + 0 = 1            | 4     | Skip     |
| 2       | 2          | 0       | 4       | 4              | 2 + 0 = 2            | 4     | Skip     |
| 3       | 9          | 4       | 4       | 4              | 9 + 4 = 13           | 13    | Rob      |
| 4       | 3          | 4       | 13      | 13             | 3 + 4 = 7            | 13    | Skip     |

Selected seats: indices 0 and 3 → values [4, 9] → sum = 13

Rolling variables during execution:
```
Initial: dp_i_3=0, dp_i_2=0, dp_i_1=0

i=0, a[0]=4:
  cur = max(0, 4+0) = 4
  shift: dp_i_3=0, dp_i_2=0, dp_i_1=4

i=1, a[1]=1:
  cur = max(4, 1+0) = 4
  shift: dp_i_3=0, dp_i_2=4, dp_i_1=4

i=2, a[2]=2:
  cur = max(4, 2+0) = 4
  shift: dp_i_3=4, dp_i_2=4, dp_i_1=4

i=3, a[3]=9:
  cur = max(4, 9+4) = 13
  shift: dp_i_3=4, dp_i_2=4, dp_i_1=13

i=4, a[4]=3:
  cur = max(13, 3+4) = 13
  shift: dp_i_3=4, dp_i_2=13, dp_i_1=13
```

![Example Visualization](../images/DP-007/example-1.png)

## 🧪 Another Quick Walkthrough (Shows skip wins)

`a = [10, 100, 10, 10]`

- You might want to take 100 at index 1, but then you cannot take index 3 (distance 2).
- Best choices:
  - take index 1 only ⇒ 100
  - take indices 0 and 3 ⇒ 20

So answer is 100 (skipping a large-looking combination is correct).

This example is great for interviews because it proves you understand “local maximum” is not enough.

## ✅ Proof of Correctness

Consider the optimal solution for prefix `[0..i]`:

- If it does not take index `i`, then it is an optimal solution for `[0..i-1]`, with value `dp[i-1]`.
- If it takes index `i`, then it cannot take `i-1` or `i-2`. So all other chosen indices must be from `[0..i-3]`, and the best such value is `dp[i-3]`. Total is `a[i] + dp[i-3]`.

The optimal must be one of these two cases, so:

`dp[i] = max(dp[i-1], a[i] + dp[i-3])`

This recurrence computes the optimal answer for every prefix. The final answer is `dp[n-1]`.

## 💡 Interview Extensions (High-Value Add-ons)

1. **Generalize the gap**

If the required gap is `K` instead of 3 (meaning `|i-j| >= K`), the recurrence becomes:

`dp[i] = max(dp[i-1], a[i] + dp[i-K])`

with the same `dp[x]=0 for x<0` trick.

2. **If empty set is NOT allowed**

Sometimes a variant says “choose at least one element”.

Then for all-negative arrays, you must return the maximum element instead of 0. The DP changes slightly:

- initialize dp with very negative values
- handle base separately

In this problem, empty set is allowed, so returning 0 is correct.

3. **Recover the chosen indices**

If asked to output which indices were picked:

- store a `take[i]` boolean or parent pointer
- after dp is built, backtrack from `n-1`:
  - if dp[i] == dp[i-1], i--
  - else pick i and jump i -= 3

This costs O(n) extra space.

### Common Mistakes to Avoid

1. **Using the wrong skip distance**
   - If you write `dp[i-2]` instead of `dp[i-3]`, you allow illegal picks (distance 2).
2. **Forgetting the empty set**
   - If all values are negative, the correct answer is 0 (pick nothing).
3. **Overflow in sums**
   - Use 64-bit types; values can be up to 1e9 and n up to 1e5.
4. **Off-by-one on base cases**
   - The `dp[x]=0 for x<0` trick avoids messy conditionals.
5. **Accidentally mixing subsequence vs subarray**
   - You are selecting indices (a subset), not a contiguous subarray.
   - ✅ You can pick `0` and `3` even though indices in between are not taken.
6. **Assuming you must pick at least one element**
   - Not in this problem. Empty selection is explicitly allowed.
   - If you force-pick one, you’ll fail hidden tests with all-negative arrays.


## Related Concepts

- Maximum sum under distance constraints
- House-robber DP patterns
- Rolling DP optimization
