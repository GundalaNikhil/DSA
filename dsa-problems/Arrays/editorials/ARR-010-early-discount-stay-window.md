---
problem_id: ARR_EARLY_DISCOUNT_WINDOW__9051
display_id: ARR-010
slug: early-discount-stay-window
title: "Early Discount With Stay Window and Ceiling"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
  - Sliding Window
  - Greedy
tags:
  - arrays
  - sliding-window
  - greedy
  - medium
premium: true
subscription_tier: basic
---

# ARR-010: Early Discount With Stay Window and Ceiling

## 📋 Problem Summary

Find the maximum profit from a single buy and sell transaction.
Two constraints:

1. You must hold the item for a duration `d` such that `dMin <= d <= dMax`.
2. The selling price is effectively `min(actual_price, C)`.

## 🌍 Real-World Scenario

**Scenario Title:** The Hotel Booking Arbitrage

You are booking a hotel room for a conference. You want to reserve a room early (buy) and transfer the reservation to a colleague later (sell).

- **Stay Window**: University rules say you must hold the reservation for at least `dMin` days to be valid, but no more than `dMax` days before the event (to ensure freshness).
- **Price Cap**: The university will reimburse you for the selling price, but only up to a cap `C`. If the market price is higher, you only pocket `C`.
  You have a chart of daily prices. When should you reserve and when should you transfer to maximize your reimbursement difference?

**Why This Problem Matters:**

- **Sliding Window Minimum**: A fundamental technique used in stream processing (e.g., "min value in last k seconds").
- **Constraint Windows**: Processing data where validity depends on relative distance (offsets).
- **Monotonic Queues**: The standard optimal structure for sliding window range queries.

![Real-World Application](../images/ARR-010/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: The Moving Buy Window

```
Days:     0    1    2    3    4    5
Prices:  [7]  [2]  [5]  [1]  [9]  [4]
          ^
dMin=2, dMax=3

If Sell Day = 5 (Price 4):
Possible Buy Days:
  Min days back: 5 - 2 = 3 (Price 1)
  Max days back: 5 - 3 = 2 (Price 5)
  Window: Indices [2, 3] -> Values [5, 1]

Best Buy in Window: 1
Profit: 4 - 1 = 3
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Profit Definition**: `min(prices[sell], C) - prices[buy]`.
- **Indices**: If you buy at `i` and sell at `j`, then `dMin <= j - i <= dMax`.
- **Capped Sell Price**: Even if `prices[j]` is 1000 and `C` is 10, your revenue is 10. `prices[buy]` is _not_ capped.

Common interpretation mistake:

- ❌ Thinking `j` (sell) must be after `i` (buy) is the ONLY constraint.
- ✅ The holding period `j - i` is strictly bounded. This defines a sliding window for valid `i` relative to `j`.

### Core Concept: Sliding Window Minimum

For a fixed sell day `j`, the valid buy days `i` form a range `[j - dMax, j - dMin]`.
To maximize profit, we want to minimize `prices[i]` within this range.
Since we iterate `j` forward, both the start and end of this range move forward by 1. This is a classic "Fixed Size Sliding Window Minimum" problem (where size is `dMax - dMin + 1`).

### Why Naive Approach is too slow

For each `j`, iterating from `j-dMax` to `j-dMin` takes O(K) where K is the window size. Total O(N\*K).
In worst case, `dMax` approx N, so O(N²).
With N=200,000, 40 billion ops is TLE.

## Naive Approach

### Intuition

For every possible sell day, check all valid buy days loop-by-loop.

### Algorithm

1. `max_profit = 0`
2. Loop `j` from `dMin` to `n-1` (sell day).
   - `sell_val = min(prices[j], C)`
   - Loop `i` from `j-dMax` to `j-dMin`.
     - If `i >= 0`:
       - `profit = sell_val - prices[i]`
       - `max_profit = max(max_profit, profit)`
3. Return `max_profit`.

### Time Complexity

- **O(N \* (dMax - dMin))** -> Worst case O(N²).

### Space Complexity

- **O(1)**.

## Optimal Approach (Monotonic Deque)

### Key Insight

We maintain a Data Structure that holds indices of potential buy days.
When we move to sell day `j`:

1. **Enter Window**: The index `new_buy = j - dMin` becomes a valid option. Add it to our DS.
2. **Leave Window**: The index `old_buy = j - dMax - 1` is no longer valid. Remove it from our DS.
3. **Query**: Ask the DS for the minimum price currently stored.

A **Monotonic Deque** (Double Ended Queue) can do all these in amortized O(1). We keep indices in the deque such that their prices are strictly increasing. The front always holds the minimum.

### Algorithm

1. Initialize `deque` (stores indices).
2. Initialize `ans = 0`.
3. Loop `j` from `dMin` to `n-1` (Sell day):
   - **Add Candidate**: `buy_candidate = j - dMin`.
     - While `deque` not empty AND `prices[deque.back] >= prices[buy_candidate]`:
       - `deque.popBack()` (Remove expensive options that are "younger" than us; they are useless).
     - `deque.pushBack(buy_candidate)`.
   - **Remove Expired**:
     - While `deque` not empty AND `deque.front < j - dMax`:
       - `deque.popFront()`.
   - **Calc Profit**:
     - `best_buy = prices[deque.front]`.
     - `revenue = min(prices[j], C)`.
     - `ans = max(ans, revenue - best_buy)`.
4. Return `ans`.

### Time Complexity

- **O(N)**: Each index is added to deque once and removed once.

### Space Complexity

- **O(N)**: Deque size.

### Why This Is Optimal

We inspect every price exactly constant number of times.

![Algorithm Visualization](../images/ARR-010/algorithm-visualization.png)
![Algorithm Steps](../images/ARR-010/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

**Input**: `prices=[7, 2, 5, 1, 9]`, `dMin=1, dMax=3, C=6`.

1. **j=1 (Sell @ 2)**:

   - `buyCandidate = 1-1 = 0` (Price 7).
   - `dq` = `[0]`.
   - `Range`: `[1-3, 1-1]` -> `[-2, 0]`. Valid: `0`.
   - `BestBuy`: 7. `Sell`: min(2, 6) = 2.
   - `Profit`: 2-7 = -5. Max=0.

2. **j=2 (Sell @ 5)**:

   - `buyCandidate = 2-1 = 1` (Price 2).
   - `dq` pop back (7 > 2). `dq` = `[1]`.
   - `Range`: `[−1, 1]`.
   - `BestBuy`: 2. `Sell`: min(5, 6) = 5.
   - `Profit`: 5-2 = 3. Max=3.

3. **j=3 (Sell @ 1)**:

   - `buyCandidate = 2` (Price 5).
   - `dq` = `[1, 2]` (2 < 5).
   - `Range`: `[0, 2]`.
   - `BestBuy`: 2. `Sell`: 1.
   - `Profit`: 1-2 = -1. Max=3.

4. **j=4 (Sell @ 9)**:
   - `buyCandidate = 3` (Price 1).
   - `dq` pop 2 (5>1), pop 1 (2>1). `dq` = `[3]`.
   - `Range`: `[1, 3]`.
   - `BestBuy`: 1. `Sell`: min(9, 6) = 6.
   - `Profit`: 6-1 = 5. Max=5.

**Result**: 5. Matches Example.

![Example Visualization](../images/ARR-010/example-1.png)

## ✅ Proof of Correctness

### Invariant

The Deque always contains a sorted sequence of indices `i` valid for future accumulation. `prices[i]` is strictly increasing. The front of the deque is the index with the minimum price in the current valid window `[j-dMax, j-dMin]`.

### Why the approach is correct

Optimization of Finding Minimum in Range. The logic covers all sell days and for each, efficiently retrieves the best valid buy day.

## 💡 Interview Extensions (High-Value Add-ons)

- **Profit per day**: Maximize `(Sell - Buy) / days`. (A: Much harder geometry problem).
- **Two transactions**: Buy/Sell twice. (A: DP).

## Common Mistakes to Avoid

1. **Window Size**:

   - ❌ Window is size `dMax`.
   - ✅ Window is valid interval `[j-dMax, j-dMin]`. This offset is key.

2. **Capping**:

   - ❌ Capping the `profit`.
   - ✅ Only limiting the `sell_price`.

3. **Empty Window**:
   - ❌ If `dMin > dMax`. (Problem constraints say `dMin <= dMax`).

## Related Concepts

- **Sliding Window Maximum**: Samedeque logic, just inequality flipped.
- **Stock Span**: Monotonic Stack.
