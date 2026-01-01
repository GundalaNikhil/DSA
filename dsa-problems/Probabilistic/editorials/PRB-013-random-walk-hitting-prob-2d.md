---
problem_id: PRB_RANDOM_WALK_HITTING_PROB_2D__5274
display_id: PRB-013
slug: random-walk-hitting-prob-2d
title: "Random Walk Hitting Probability 2D"
difficulty: Hard
difficulty_score: 70
topics:
  - Probability
  - Random Walk
  - Dynamic Programming
tags:
  - probability
  - random-walk
  - dp
  - hard
premium: true
subscription_tier: basic
---

# PRB-013: Random Walk Hitting Probability 2D

## 📋 Problem Summary

Calculate the probability that a 2D symmetric random walk starting at `(0,0)` reaches a target `(a,b)` within T steps.

| | |
|---|---|
| **Moves** | N, S, E, W with prob 0.25 each |
| **Input** | a, b, T |
| **Output** | Probability (float) |

## 🌍 Real-World Scenario

**Scenario Title:** The Lost Drone

A drone loses its GPS signal at coordinates `(0,0)`.
- It enters a "search mode" where it moves randomly in a grid pattern to try and re-establish connection with a base station located at `(a,b)`.
- The drone has limited battery life, allowing only T moves.
- You need to calculate the probability that the drone flies over the base station at least once before the battery dies.
- This helps in designing emergency protocols: if the probability is too low, the drone should perhaps land immediately instead.

**Why This Problem Matters:**

- **Biology:** Animal foraging patterns (Levy flights).
- **Physics:** Diffusion of particles hitting a sensor.
- **Finance:** Asset price hitting a barrier (Barrier Options).

![Real-World Application](../images/PRB-013/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Grid Walk

Target `(1,1)`, T = 2. Start (0,0)$.

```
(0,1) -- (1,1) Target
  |        |
(0,0) -- (1,0)
Start
```

Paths of length 2:
1. `(0,0) -> (0,1) -> (1,1)`: Hit. Prob `1/4 x 1/4 = 1/16`.
2. `(0,0) -> (1,0) -> (1,1)`: Hit. Prob `1/4 x 1/4 = 1/16`.
3. `(0,0) -> (0,1) -> (0,2)`: Miss.
...
Total paths `4^2 = 16`.
Hits: 2. Probability `2/16 = 0.125`.

Path `(0,0) -> (0,1) -> (1,1) -> (1,2)` counts as a hit at step 2.
We need "at least once".
Equivalent to: Walk stops upon hitting `(a,b)`.

### ✅ Input/Output Clarifications (Read This Before Coding)

- **Absorbing State:** Treat the target `(a,b)` as absorbing. Once reached, the walk stays there (or we just count it as a success and stop tracking).
- **Bounded Grid:** Since max steps is T, the walk cannot go beyond coordinates `[-T, T]`.
- **Constraints:** T \le 500`. Grid size roughly`1000 \times 1000$.
- **DP State:** `dp[t][x][y]` = Prob of being at `(x,y)` at time t without having hit target earlier?
  -   - If `(x,y) == (a,b)`, we make it absorbing: `dp[t+1][a][b] += dp[t][a][b] * 1.0`.
  - Or just accumulate "new hits" at each step.
- **Space Optimization:** We only need `dp[t]` and `dp[t-1]`.
- **Coordinate Shift:** Map indices to array: `x` from `-T` to T maps to `0` to `2T`. Offset by T.

### Core Concept: Dynamic Programming on Grid

Iterate t from 1 to T.
Update probabilities for all reachable `(x,y)`.
Special handling for target `(a,b)`: it acts as a sink.
Total probability = `dp[T][a][b]` (if we make it absorbing).

## Naive Approach

### Intuition

DFS/BFS simulation of all `4^T` paths.

### Algorithm

Recursion.

### Time Complexity

- **O(4^T)**. Impossible for T = 500$.

## Optimal Approach

### Key Insight

DP with coordinate bounding.
The walk can range from `-T` to T in both dimensions.
Grid size `(2T+1) x (2T+1)`.
T = 500 \implies 1000 \times 1000 = 10^6$ cells.
Total ops T \times 10^6 = 5 \cdot 10^8$.
This might be tight for 2 seconds in Python/JS, but fine for C++/Java.
However, at step t, we only need to check range `[-t, t]`.
Sum of squares `sum_t=1^T (2t)^2 ~= frac43 T^3`.
`500^3 = 1.25 * 10^8`. This is acceptable.

### Algorithm

1. Offset coordinates by T to handle negatives. Start at `(T, T)`. Target `(a+T, b+T)`.
2. `dp[x][y]` stores prob at current step.
3. Initialize `dp[T][T] = 1.0`.
4. Loop `step` from 1 to T:
   - Create `new_dp`.
   - Loop `x` from T - step`to T + step`.
   - Loop `y` from T - step`to T + step`.
   - If `(x, y) == target`: `new_dp[x][y] += dp[x][y]` (Absorbing).
   - Else if `dp[x][y] > 0`:
     - Distribute `0.25 * dp[x][y]` to neighbors.
     - Neighbors: `(x+1, y), (x-1, y), (x, y+1), (x, y-1)`.
     - If a neighbor is target, add to target in `new_dp`.
     - Else add to neighbor in `new_dp`.
   - Update `dp = new_dp`.
5. Return `dp[target_x][target_y]`.

### Time Complexity

- **O(T^3)**.

### Space Complexity

- **O(T^2)**.

![Algorithm Visualization](../images/PRB-013/algorithm-visualization.png)
![Algorithm Steps](../images/PRB-013/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Input: `1 0 1`.
1. Start `dp[1][1] = 1` (offset 1). Target `(2, 1)`.
2. Step 1:
   - `(1,1)` spreads 0.25 to `(2,1), (0,1), (1,2), (1,0)`.
   - `(2,1)` is target. `nextDp[2][1] = 0.25`.
3. Result 0.25.
Matches example.

## ✅ Proof of Correctness

### Invariant
`dp[x][y]` holds the probability of being at `(x,y)` at time t without having been absorbed previously (except for the target state which accumulates).

### Why the approach is correct
Standard DP for Markov Chains on a finite grid.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** 1D Case.
  - *Hint:* Reflection Principle (Catalan numbers).
- **Extension 2:** Expected Hitting Time.
  - *Hint:* Solve linear equations (Dirichlet problem).
- **Extension 3:** Infinite T.
  - *Hint:* Polya's Recurrence Theorem (Prob = 1 in 2D).

### Common Mistakes to Avoid

1. **Double Counting**
   - ❌ Wrong: Counting paths that hit target multiple times as separate hits.
   - ✅ Correct: Make target absorbing (stop walking once hit).
2. **Bounds**
   - ❌ Wrong: Array index out of bounds for negative coordinates.
   - ✅ Correct: Use offset.

## Related Concepts

- **Brownian Motion:** Continuous limit.
- **Heat Equation:** Diffusion of probability mass.
