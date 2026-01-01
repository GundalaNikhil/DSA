---
problem_id: DP_COIN_CAP_PENALTY__1842
display_id: DP-002
slug: capped-coin-change-penalty
title: "Capped Coin Change With Penalty"
difficulty: Medium
difficulty_score: 58
topics:
  - Dynamic Programming
  - Knapsack
  - Optimization
tags:
  - dp
  - knapsack
  - bounded-knapsack
  - medium
premium: true
subscription_tier: basic
---

# DP-002: Capped Coin Change With Penalty

## 📋 Problem Summary

You must form an exact sum `target` using `k` coin types. Each type has a denomination `d[i]` and a maximum count `c[i]`. The base cost is the total number of coins used. But there is a twist: if you use **more than** `floor(c[i]/2)` coins of a type, you pay a one-time penalty `p[i]` for that type.

Return the minimum possible cost, or `-1` if the target cannot be formed.

## 🌍 Real-World Scenario

**Scenario Title:** Hostel Canteen Tokens With “Bulk Usage” Fee

Your hostel canteen issues meal tokens in different denominations (₹1, ₹5, ₹10, ...). Each denomination is limited because tokens are physically counted and distributed (that’s your `c[i]`).

To discourage students from exhausting a single denomination, the canteen adds a rule:

- If you use “too many” tokens of a certain type (more than half the available stock of that denomination), you pay an extra service fee (the penalty).

As a developer building the billing system:

- you must respect the limited stock
- you want to minimize the total “cost” (number of tokens + any fees)
- and you must return `-1` if a bill cannot be paid exactly with available tokens

This maps directly to a bounded knapsack with a threshold-based activation cost.

**Why This Problem Matters:**

- Forces you to model per-type constraints (bounded knapsack, not unbounded)
- Introduces “activation cost” patterns (pay once if you cross a threshold)
- Tests whether you can optimize DP beyond naive triple loops for `target <= 5000`

![Real-World Application](../images/DP-002/real-world-scenario.png)

## ✅ Input/Output Clarifications (Non-Negotiable)

- You must form **exactly** `target`. Not “at least”.
- For each type `i`, you may use `0..c[i]` coins.
- The penalty `p[i]` is charged:
  - **once per type** (not per coin)
  - only if `used_i > floor(c[i]/2)`
- If `c[i]` is huge (even 10^9), you still cannot use more than `target / d[i]` coins of that type because you cannot exceed `target`.
- Output can be large; use 64-bit integers (`long long` / `long`).

## Detailed Explanation

### ASCII Diagram: Coins with Caps and Penalties

```
Coins with caps and penalties:

┌──────┬──────┬──────────┬──────────────┐
│ Type │ Denom│   Cap    │   Penalty    │
├──────┼──────┼──────────┼──────────────┤
│  1   │   1  │     5    │  2 (if >2)   │
│  2   │   5  │    10    │  3 (if >5)   │
│  3   │  10  │    20    │  5 (if >10)  │
└──────┴──────┴──────────┴──────────────┘

Penalty Threshold = floor(Cap/2)

Example: Target = 26
Possible combinations (showing cost calculation):

Option A: 1×10 + 3×5 + 1×1
  - Type 3: 1 coin (≤10, no penalty) → cost: 1
  - Type 2: 3 coins (≤5, no penalty) → cost: 3
  - Type 1: 1 coin (≤2, no penalty) → cost: 1
  Total cost: 5 coins

Option B: 2×10 + 1×5 + 1×1
  - Type 3: 2 coins (≤10, no penalty) → cost: 2
  - Type 2: 1 coin (≤5, no penalty) → cost: 1
  - Type 1: 1 coin (≤2, no penalty) → cost: 1
  Total cost: 4 coins ✓ Better!
```

### Cost function per coin type

Suppose you decide to use `x` coins of type `i`.

- Denomination contribution: `x * d[i]`
- Base coin cost: `x`
- Penalty rule:
  - let `t = floor(c[i]/2)`
  - penalty is `0` if `x <= t`
  - penalty is `p[i]` if `x >= t+1`

So:

`cost_i(x) = x + (x > t ? p[i] : 0)`

This is a “linear cost” with a one-time jump at `t+1`.

### DP state (standard knapsack style)

Let:

`dp[s] = minimum cost to form sum s using the first few coin types`

Initialize:

- `dp[0] = 0` (use no coins to make sum 0)
- `dp[s] = INF` for `s > 0`

We process coin types one by one and update dp.

## Naive Approach (and why it’s risky)

### Intuition

For each type, try all possible counts `x` and update dp.

### Algorithm

For each coin type `i`:

1. Create `newDp` filled with `INF`.
2. For every sum `s`:
   - if `dp[s]` is reachable:
     - try taking `x = 0..cap` coins of this type
     - update `newDp[s + x*d[i]] = min(newDp[...], dp[s] + cost_i(x))`
3. Replace `dp = newDp`.

Where `cap = min(c[i], target / d[i])`.

### Time Complexity

Worst case:

- `k = 50`
- `target = 5000`
- `d[i] = 1` and `cap = 5000`

Then the triple loop is around:

`O(k * target * cap) = 50 * 5000 * 5000 = 1.25e9` updates

That is not “maybe slow”. That is dead on arrival in most languages.

### Space Complexity

- `O(target)`

### Why This Works (Correctness)

It considers all valid choices for each type and takes the minimum.

### Limitations

- Time is too high in worst-case constraints.

## Optimal Approach (O(k · target)) Using Monotonic Queue Optimization

### Key Insight

For a fixed denomination `d`, sums can be grouped by the same remainder modulo `d`.

Example with `d=3`:

- remainder 0: 0, 3, 6, 9, ...
- remainder 1: 1, 4, 7, 10, ...
- remainder 2: 2, 5, 8, 11, ...

Within one remainder group, the DP transition becomes a 1D problem where every step moves by `d`.

### Rewrite DP transition within a remainder class

Fix a coin type with:

- denomination `d`
- effective cap `cap = min(c, target/d)` (in coins)
- threshold `t = min(floor(c/2), cap)`
- penalty `p`

For a fixed remainder `r` (0..d-1), define:

- `sum = r + q*d` where `q` is the “index” in that remainder class
- `prev[q] = dp[r + q*d]`
- `next[q] = newDp[r + q*d]`

Now if you use `x` coins of this type:

`next[q] = min(prev[q-x] + x + penalty(x))` over all `x` allowed.

Where:

- `0 <= x <= cap`
- penalty(x) = 0 if x <= t else p

Let `y = q - x` ⇒ `x = q - y`:

`next[q] = min(prev[y] + (q - y) + penalty(q - y))`

Rearrange:

`next[q] = q + min( prev[y] - y + penalty(q - y) )`

Now the only hard part is penalty(q-y), but it has only two cases:

### Case A: No penalty (x <= t)

x = q - y <= t  ⇒  y >= q - t

Also x <= cap ⇒ y >= q - cap.

So:

`y` is in `[q - min(cap, t), q]`.

Let `L1 = min(cap, t)`.

Then:

`bestNoPen[q] = min_{y in [q-L1, q]} (prev[y] - y)`

and candidate:

`candNoPen = q + bestNoPen[q]`

### Case B: Penalty active (x >= t+1)

x = q - y >= t+1  ⇒  y <= q - (t+1)

Also x <= cap ⇒ y >= q - cap.

So:

`y` is in `[q - cap, q - (t+1)]` (only if `cap > t`).

This interval length is constant (`cap - t`) as q slides.

`bestPen[q] = min_{y in [q-cap, q-(t+1)]} (prev[y] - y)`

and candidate:

`candPen = q + p + bestPen[q]`

### Sliding minimum = Monotonic deque

Both `bestNoPen[q]` and `bestPen[q]` are “min over a sliding window” of the sequence:

`value[y] = prev[y] - y`

We can maintain the minimum of a sliding window in O(1) amortized per step using a deque (monotonic queue).

So for each remainder class, we compute all `next[q]` in O(number of q values).

Across all remainders, total states are `target+1`, so per coin type we do O(target) work.

### Final complexity

- Time: `O(k * target)` which is at most `50 * 5000 = 250000` (plus small constants)
- Space: `O(target)`

This is the level of optimization that matches the constraints without hand-waving.

### Decision Tree for Coin Selection

```
For each coin type i (denom=d, cap=c, penalty=p):
    │
    ├─ Process all sums in remainder classes (r = 0..d-1)
    │   │
    │   └─ For each sum s = r + q*d:
    │       │
    │       ├─ Can we use x coins of this type to reach s?
    │       │   │
    │       │   ├─ YES: Calculate cost based on x
    │       │   │   │
    │       │   │   ├─ Is x <= threshold (floor(c/2))?
    │       │   │   │   │
    │       │   │   │   ├─ YES: cost = prev_cost + x
    │       │   │   │   │        (no penalty applied)
    │       │   │   │   │
    │       │   │   │   └─ NO:  cost = prev_cost + x + p
    │       │   │   │            (penalty applies)
    │       │   │   │
    │       │   │   └─ Update dp[s] = min(dp[s], cost)
    │       │   │
    │       │   └─ NO: Skip this combination
    │       │
    │       └─ Use monotonic deque to optimize:
    │           - Track minimum (prev[y] - y) in sliding window
    │           - Maintain two deques: one for no-penalty, one for penalty
    │           - Each deque handles a different range of coin counts
```

![Algorithm Visualization](../images/DP-002/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
Sample:

```
k=2, target=7
(d,c,p):
1 4 2
5 2 1
```

Thresholds:

- For denom 1: `t=floor(4/2)=2`, penalty `2` triggers if we use 3 or 4 ones.
- For denom 5: `t=floor(2/2)=1`, penalty `1` triggers only if we use 2 fives.

### State Evolution Table

| Amount | Min Cost | Coin Selection | Breakdown |
|--------|----------|----------------|-----------|
| 0 | 0 | none | base case |
| 1 | 1 | 1×(denom=1) | 1 coin, no penalty |
| 2 | 2 | 2×(denom=1) | 2 coins, no penalty |
| 3 | 3 | 3×(denom=1) | 3 coins + penalty(2) = 5 OR just 3 |
| 4 | 4 | 4×(denom=1) | 4 coins + penalty(2) = 6 OR just 4 |
| 5 | 1 | 1×(denom=5) | 1 coin, no penalty (better than 5×denom1) |
| 6 | 2 | 1×(denom=5) + 1×(denom=1) | 2 coins, no penalty |
| 7 | 3 | 1×(denom=5) + 2×(denom=1) | 3 coins, no penalty ✓ |

To make 7, the sensible candidates are:

- `5 + 1 + 1`:
  - ones used=2 (no penalty)
  - fives used=1 (no penalty)
  - total cost = 3 ✅
- `1+1+1+1+1+1+1`:
  - ones used=7, but cap is 4 so invalid

So minimum cost is 3.

![Example Visualization](../images/DP-002/example-1.png)

## ✅ Proof Sketch (Why the deque optimization is correct)

For each remainder class, the transition reduces to taking a minimum of the form:

`next[q] = q + min(value[y])` over a sliding window of valid `y` indices, where `value[y] = prev[y] - y`.

Since the window moves by 1 each step and `value[y]` depends only on `y`, a monotonic deque maintains the window minimum correctly in O(1) amortized time. We compute two such minima (no-penalty window and penalty window) and take the smaller candidate.

### Common Mistakes to Avoid

1. **Misunderstanding the penalty condition**

   - Penalty triggers on `used_i > floor(c[i]/2)`, not `>=`.
   - Example: if `c=4`, then `floor(c/2)=2`:
     - using 2 coins: no penalty
     - using 3 coins: penalty applies

2. **Ignoring “effective cap”**

   - If `c[i]` is huge, you still can’t use more than `target / d[i]`.
   - ✅ Always set `cap = min(c[i], target/d[i])`.

3. **Triple-loop DP that times out**

   - `k=50`, `target=5000`, `d=1` is the stress case.
   - ✅ Use the modulo-class + deque optimization to get O(k·target).

4. **Using 32-bit integers for cost**

   - Costs can exceed 2^31.
   - ✅ Use `long` / `long long`.


## Related Concepts

- Bounded knapsack optimization (monotonic queue by remainder classes)
- DP with activation costs / step costs
- Min-plus convolution intuition
- Sliding window minimum (monotonic deque)
