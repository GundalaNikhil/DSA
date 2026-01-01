---
problem_id: DP_REQ_WEIGHT_KNAP__6427
display_id: DP-003
slug: required-weight-knapsack
title: "Required Weight Knapsack"
difficulty: Medium
difficulty_score: 54
topics:
  - Dynamic Programming
  - Knapsack
  - Optimization
tags:
  - dp
  - knapsack
  - 0-1-knapsack
  - medium
premium: true
subscription_tier: basic
---

# DP-003: Required Weight Knapsack

## 📋 Problem Summary

You have `n` items, each with a weight and a value. You want the **maximum value**, but you are only allowed to choose a subset whose total weight is:

- **at least** `R` (required minimum), and
- **at most** `W` (capacity).

This is a 0/1 knapsack variant where the final answer is not necessarily `dp[W]`; it is the best `dp[weight]` among weights in `[R..W]`.

## 🌍 Real-World Scenario

**Scenario Title:** Lab Kit Packing With Minimum Safety Weight

In a BTech chemistry lab, students must carry a lab kit in a safety box. The box has:

- a **maximum safe load** (if you exceed it, the box can break): `W`
- a **minimum required load** (the kit must include enough equipment to be useful; too light means missing essentials): `R`

Each piece of equipment has:

- weight (grams)
- usefulness value (how important it is for experiments)

You must pack a subset such that:

- total weight is between `R` and `W`, and
- total value is maximum.

This matches real constraints in packaging, shipping, and resource allocation problems where “at least some minimum” is required.

**Why This Problem Matters:**

- Trains you to adapt classic knapsack to extra constraints (minimum weight)
- Reinforces 0/1 DP iteration order (descending weight)
- Builds interview-ready clarity: define states, transitions, and how to extract the answer

![Real-World Application](../images/DP-003/real-world-scenario.png)

## ✅ Input/Output Clarifications (Don’t Lose Marks Here)

- It is **0/1 knapsack**: each item can be taken **at most once**.
- You must satisfy **both** constraints:
  - `totalWeight <= W` (hard cap)
  - `totalWeight >= R` (required minimum)
- If no subset can reach weight ≥ `R` within capacity `W`, output `-1`.
- Values can sum large, so use 64-bit integers.

## Detailed Explanation

### ASCII Diagram: Items and Constraints

```
Items with weights and values:

┌──────┬────────┬───────┐
│ Item │ Weight │ Value │
├──────┼────────┼───────┤
│  1   │   2    │   3   │
│  2   │   3    │   4   │
│  3   │   4    │   5   │
└──────┴────────┴───────┘

Constraints:
  Capacity (W):        6
  Required weight (R): 5

Valid selections must satisfy:
  5 ≤ total_weight ≤ 6

Knapsack visualization:
┌─────────────────┐
│   Capacity: 6   │  ← Maximum allowed
├─────────────────┤
│                 │
│    VALID ZONE   │  ← Weight between 5-6
│   (R=5 to W=6)  │
│                 │
├─────────────────┤
│   Required: 5   │  ← Minimum required
└─────────────────┘

Goal: Maximize value while staying in VALID ZONE
```

### Why greedy fails

Many students first think:

- “Take the best value/weight ratio items” (fractional knapsack mindset)

But this is 0/1 knapsack with a hard weight range; greedy is not reliable.

Example counter:

- W=6, R=5
- items: (w=3,v=100), (w=2,v=60), (w=2,v=60)

Greedy might pick 3+2=5 value 160 (good), but variants can be constructed where a different combination wins. So we use DP.

### DP state

Let:

`dp[wt] = maximum value achievable with exact total weight = wt`

This is the classic 1D 0/1 knapsack DP.

Initialization:

- `dp[0] = 0` (weight 0, value 0)
- `dp[wt] = -INF` for `wt > 0` (unreachable)

Transition for item `i` with weight `wi` and value `vi`:

For `wt` from `W` down to `wi`:

- if `dp[wt - wi]` is reachable, then:
  - `dp[wt] = max(dp[wt], dp[wt - wi] + vi)`

Descending loop is mandatory for 0/1 knapsack to prevent using the same item multiple times.

### How to enforce “required minimum weight”

After processing all items, the valid solutions are exactly weights `R..W`.

So:

`ans = max(dp[wt]) for wt in [R..W]`

If all dp[wt] in that range are unreachable, answer is -1.

## Naive Approach

### Intuition

Try all subsets of items and pick the best valid one.

### Algorithm

1. Enumerate all subsets (take / not take each item)
2. Compute total weight and total value for each subset
3. Keep the maximum value among subsets with `R <= weight <= W`

### Time Complexity

- `O(2^n)` subsets
- Impossible for `n=200`

### Space Complexity

- `O(n)` recursion depth

### Limitations

- Completely infeasible for constraints.

## Optimal Approach (0/1 Knapsack DP)

### Key Insight

Even though there are exponentially many subsets, the only thing that matters for future decisions is:

- current total weight
- best value achievable for that weight

So we compute best value for each weight 0..W iteratively.

### Algorithm

1. Initialize dp array:
   - `dp[0] = 0`
   - other dp entries = `-INF`
2. For each item `(wi, vi)`:
   - for `wt` from `W` down to `wi`:
     - `dp[wt] = max(dp[wt], dp[wt-wi] + vi)` (if `dp[wt-wi]` reachable)
3. Answer:
   - `max(dp[R..W])` if reachable, else `-1`

### Time Complexity

- `O(n * W)` ≤ `200 * 5000 = 1,000,000` updates (fast)

### Space Complexity

- `O(W)`

### Why This Is Optimal

You must process each item and each possible weight up to `W` to guarantee the correct maximum value. This DP is the standard optimal approach under given constraints.

### Decision Tree for Item Selection

```
For each item i (weight=wi, value=vi):
    │
    └─ For each weight wt (from W down to wi):
        │
        ├─ Can we include item i?
        │   │
        │   ├─ Check if dp[wt-wi] is reachable
        │   │   │
        │   │   ├─ YES: Consider two options
        │   │   │   │
        │   │   │   ├─ Option A: Include item i
        │   │   │   │   new_value = dp[wt-wi] + vi
        │   │   │   │
        │   │   │   └─ Option B: Skip item i
        │   │   │       keep_value = dp[wt]
        │   │   │
        │   │   │   Choose: dp[wt] = max(new_value, keep_value)
        │   │   │
        │   │   └─ NO: Cannot include (previous state unreachable)
        │   │       dp[wt] stays unchanged
        │   │
        │   └─ Loop direction: DESCENDING (W→wi)
        │       (Ensures each item used at most once - 0/1 property)
        │
        └─ After all items processed:
            Find answer = max(dp[R], dp[R+1], ..., dp[W])
            (Maximum value in the required weight range)
```

![Algorithm Visualization](../images/DP-003/algorithm-visualization.png)
![Algorithm Steps](../images/DP-003/algorithm-steps.png)

## 🚫 Why Iteration Order Matters (0/1 vs Unbounded)

This is one of the most common interview traps.

When you compress a 2D knapsack DP to 1D, the direction of the weight loop decides whether you are solving:

- **0/1 knapsack** (each item once), or
- **unbounded knapsack** (same item can be used many times)

### Correct (0/1): loop weight from `W` down to `wi`

When you update `dp[wt]` from `dp[wt-wi]` in descending order, `dp[wt-wi]` still belongs to the “previous item set”, so the current item is not reused.

### Wrong (unbounded): loop weight from `wi` up to `W`

Ascending order makes `dp[wt-wi]` already include the current item’s effect, so you can unintentionally take the same item multiple times.

#### Mini counterexample

One item: `(w=2, v=10)`, `W=4`, `R=4`

- In 0/1 knapsack, you can take it only once ⇒ max weight reachable is 2 ⇒ answer should be `-1`.
- With ascending loop, dp would allow:
  - dp[2] = 10
  - dp[4] = dp[2] + 10 = 20 (same item twice) ❌

So you must use descending order here.

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Extra Example (Impossible Case)

Input:

```
1 5 3
2 10
```

You have one item of weight 2. Even if you take it, total weight = 2 which is still `< R=3`. Since you cannot take the item twice, there is no valid selection.

So output is `-1`.

This example is included as a public testcase for a reason: many submissions incorrectly return dp[W] or forget the minimum weight constraint.

## 🧪 Test Case Walkthrough (Dry Run)

Sample:

```
3 6 5
2 4
3 5
4 6
```

### State Evolution Table

| Item | Weight | Value | Selected? | Current Weight | Current Value | dp State Update |
|------|--------|-------|-----------|----------------|---------------|-----------------|
| - | - | - | - | 0 | 0 | dp[0]=0, others=-INF |
| 1 | 2 | 4 | Consider | - | - | dp[2]=4 |
| 2 | 3 | 5 | Consider | - | - | dp[3]=5, dp[5]=dp[2]+5=9 |
| 3 | 4 | 6 | Consider | - | - | dp[4]=6, dp[6]=dp[2]+6=10 |

### Final DP Array State

```
Weight:  0    1    2    3    4    5    6
dp:      0   -INF  4    5    6    9   10
         ^                          ^    ^
         |                          |    |
      base case              R (required) W (capacity)
```

Now required range is weights 5..6:

- dp[5]=9 (items 1+2: weights 2+3=5, values 4+5=9)
- dp[6]=10 (items 1+3: weights 2+4=6, values 4+6=10) ⇒ answer 10 ✓

![Example Visualization](../images/DP-003/example-1.png)

## ✅ Proof of Correctness

### Claim

After processing the first `i` items, `dp[wt]` equals the maximum value achievable using a subset of those `i` items with exact total weight `wt` (or unreachable if no such subset exists).

### Reason

Induction on `i`:

- Base: before any items, only weight 0 is reachable with value 0.
- Step: when adding item `i`:
  - Either we do not take it: dp[wt] stays as before.
  - Or we take it: we must come from weight `wt-w[i]` using previous items, so candidate value is dp[wt-w[i]] + v[i].
  - We take the maximum of these two options.

Descending iteration on `wt` ensures each item is used at most once.

Finally, any valid solution must have weight in `[R..W]`, so taking the maximum over that range gives the correct answer.

## 📊 Complexity Comparison (What to Say in Interviews)

| Approach | Time | Space | Works for n=200, W=5000? |
|---------|------|-------|---------------------------|
| Brute force subsets | `O(2^n)` | `O(n)` | ❌ never |
| 2D DP (classic) | `O(n·W)` | `O(n·W)` | ✅ but memory heavier |
| 1D DP (this solution) | `O(n·W)` | `O(W)` | ✅ best for constraints |

If you are asked “why 1D DP is safe”, the answer is: descending order preserves the 0/1 constraint.

## 💡 Interview Extensions (High-Value Add-ons)

1. **Reconstruct the chosen items**

If the interviewer asks “which items were chosen”, you can:

- keep a parent pointer array (or keep a 2D `take[i][w]` boolean)
- backtrack from the best weight in `[R..W]`

This costs more memory but is straightforward.

2. **If `W` becomes large (e.g., 10^5 or 10^6)**

Then `O(n·W)` may become too slow. You would need:

- meet-in-the-middle (for smaller n), or
- value-based DP if values are small, or
- approximation schemes (FPTAS) in advanced settings

For this problem, `W <= 5000`, so standard DP is correct and optimal.

### Common Mistakes to Avoid

1. **Using ascending weight loop (turns it into unbounded knapsack)**
   - ❌ Ascending loop can reuse the same item multiple times.
   - ✅ Always loop `wt = W .. wi`.

2. **Returning `dp[W]` instead of `max(dp[R..W])`**
   - The best valid solution may not fill the knapsack completely.
   - ✅ Answer is maximum dp within the required weight interval.

3. **Not handling unreachable states properly**
   - If you initialize dp to 0 everywhere, you accidentally allow “free” unreachable weights.
   - ✅ Use `-INF` (or a very negative sentinel) and only transition from reachable states.

4. **Overflow in value sums**
   - Values can be up to `10^9` each, and you might pick many items.
   - ✅ Use 64-bit integers (`long long` / `long`).

5. **Forgetting that `R` can be 0**
   - If `R=0`, the empty set is valid and the problem reduces to classic max-value ≤ W.
   - ✅ Your answer loop over `R..W` already handles this cleanly.


## Related Concepts

- 0/1 knapsack DP
- DP with feasibility constraints
- Extracting answer from a DP table (not always dp[W])
