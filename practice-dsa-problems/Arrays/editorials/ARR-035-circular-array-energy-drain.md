---
problem_id: ARR_CIRCULAR_DRAIN__2291
display_id: ARR-035
slug: circular-array-energy-drain
title: "Circular Array Energy Drain"
difficulty: Medium
difficulty_score: 50
topics:
  - Arrays
tags:
  - algorithms
  - array-manipulation
  - arrays
  - circular-array
  - coding-interviews
  - data-structures
  - kadane
  - searching
  - technical-interview-prep
  - two-pointers
premium: false
subscription_tier: basic
---

# ARR-035: Circular Array Energy Drain

## 📋 Problem Summary

You have a circular track of `N` stations.
At each station, you get `fuel[i]`.
To move to the next station, you spend `drain[i] + B`.
Find the smallest starting station index such that you can complete a full loop without your energy tank ever dropping below zero.

## 🌍 Real-World Scenario

**Scenario Title:** 🏎️ The Zero-Stop Grand Prix

### The Problem

You are an F1 strategist.
Your car has a fancy hybrid system.

- In Sector `i`, it regenerates `X` Joules (Fuel).
- But driving through Sector `i` consumes `Y` Joules (Drain) plus a baseline `B` for air resistance.
- You can start the "Qualifying Lap" effectively at the beginning of any sector.
- You start with empty battery (0).
- If battery drops < 0, the car stalls.
  Where should the driver start the push lap to ensure they make it all the way around?

### Real-World Relevance

- **Router Buffers:** A network packet traverses a ring of nodes. Each node adds data (Fuel) but processing takes capacity (Drain). Can the packet survive the loop without buffer underflow?

## 🚀 Detailed Explanation

### 1. The Net Flow Transformation

First, let's simplify.
Moving from `i` to `i+1` costs `drain[i] + B`.
You gain `fuel[i]`.
So the **Net Change** at station `i` is: `Delta[i] = fuel[i] - (drain[i] + B)`.
The problem becomes:
"Find a starting index `k` in the circular array `Delta` such that all prefix sums of the sequence `Delta[k], Delta[k+1]... Delta[k-1]` remain non-negative."

### 2. The Necessary Condition

If the **Total Sum** of `Delta` array is negative, it is impossible to complete a loop. You simply consume more than you gain in total.
If `Total Sum >= 0`, a solution depends on the arrangement. A fundamental theorem (Gas Station Theorem) states that **if Total >= 0, there exists at least one valid starting point.**

### 3. Finding the Start Point (Greedy)

We can attempt to simulate the journey.

- Start at index `0`.
- Maintain `CurrentTank`.
- Move to next station: `CurrentTank += Delta[i]`.
- If `CurrentTank < 0`:
  - **Failure!** We ran out of fuel at `i`.
  - **Crucial Insight:** Could we have succeeded if we started at `0 < k <= i`?
  - No. Because we started at `0` with `0` fuel. When we arrived at `k`, we had `Tank >= 0` (otherwise we would have failed earlier). So starting at `k` with `0` fuel is strictly _worse_ (or equal) to arriving there from `0`. If we failed at `i` starting from `0` (with bonus fuel accumulated), we definitely fail starting at `k` (with zero fuel).
  - **Conclusion:** Any start point between `0` and `i` is invalid.
  - **Optimization:** Resume search from `i + 1`. Reset `CurrentTank = 0`.

### 4. Circular Handling

Usually, we might need to loop `2*N` times to handle the circular wrap-around.
However, with the logic above:

- If we scan from `0` to `N-1` and find a valid segment that reaches `N-1` with `Total >= 0`, and we know `Total(Global) >= 0`, then the wrap-around is guaranteed to be safe.
- So we just need the first `start` index where the linear scan doesn't fail up to `N-1`.

### 🔄 Algorithm Flow Diagram

<!-- mermaid -->

```mermaid
flowchart TD
    A[Start] --> B[Calculate Delta[i] for all i]
    B --> C[Check sum(Delta) < 0?]
    C -- Yes --> D[Return -1]
    C -- No --> E[Init Tank=0, Start=0]
    E --> F[Loop i from 0 to N-1]
    F --> G[Tank += Delta[i]]
    G --> H{Tank < 0?}
    H -- Yes --> I[Start = i + 1, Tank = 0]
    H -- No --> J[Continue]
    I --> F
    J --> F
    F -- End Loop --> K[Return Start + 1 (1-based)]
```

## 🧪 Edge Cases to Test

1.  **Total < 0:** Fuel `[1, 1]`, Drain `[2, 2]`, B=0. Delta `[-1, -1]`. Sum -2. Return -1.
2.  **Base Drain (B):** Often forgotten. Ensure `Delta = Fuel - (Drain + B)`.
3.  **Exact Zero tank:** Valid. `Tank >= 0`.
4.  **Wrap Around:** The algorithm finds the _start_ of the successful run. If `Total >= 0`, the fuel accumulated by the end ensures the wrapped part is safe.

## 🏃 Naive vs Optimal Approach

### Naive O(N^2)

Try starting at every index, simulate loop.

### Greedy One Pass O(N)

- **Time:** O(N).
- **Space:** O(1).
  Optimal.
