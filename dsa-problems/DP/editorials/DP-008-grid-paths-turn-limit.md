---
problem_id: DP_GRID_TURN_LIMIT__4930
display_id: DP-008
slug: grid-paths-turn-limit
title: "Grid Paths With Turn Limit"
difficulty: Medium
difficulty_score: 58
topics:
  - Dynamic Programming
  - Grid DP
  - Counting
tags:
  - dp
  - grid
  - counting
  - medium
premium: true
subscription_tier: basic
---

# DP-008: Grid Paths With Turn Limit

## 📋 Problem Summary

Count the number of paths from `(0,0)` to `(m-1,n-1)` in an `m x n` grid using only Right and Down moves, with the additional constraint that the path uses **at most `T` turns**.

A “turn” is a change in direction between consecutive moves. The first move does not count as a turn. Output the count modulo `1_000_000_007`.

## 🌍 Real-World Scenario

**Scenario Title:** Campus Robot Navigation With Limited Steering

Imagine an autonomous delivery robot moving inside a campus building with a grid-like corridor layout:

- It can move only forward in the two main directions (right/down in our model).
- Turning is expensive: it slows down, wastes battery, and increases chances of collision.

The robot must reach a destination while making **at most T turns**. Your job is to count how many such “low-steering” routes exist.

This shows up in:

- robotics path planning (minimizing steering)
- VLSI routing (limiting bends)
- warehouse automation (turn constraints)

**Why This Problem Matters:**

- Strengthens 2D DP thinking (grid paths)
- Adds an extra dimension for “turns” and “last direction”
- Builds interview skill: design the right state to count paths with constraints

![Real-World Application](../images/DP-008/real-world-scenario.png)

## ✅ Clarifications (Be precise)

- Start: `(0,0)`
- End: `(m-1, n-1)`
- Moves allowed: Right `(r,c)->(r,c+1)` and Down `(r,c)->(r+1,c)`
- Turn happens when direction changes: R→D or D→R
- The first move does not count as a turn (no previous direction)
- We count paths with **at most** `T` turns (not exactly T)
- Use modulo `1_000_000_007` (MOD) for all counts

## Detailed Explanation

### Grid Visualization with Directions and Turns

```
Grid 3x4 with T=1 (1 turn allowed):

Starting at (0,0), ending at (2,3)

Coordinate System:
  (0,0) (0,1) (0,2) (0,3)
  (1,0) (1,1) (1,2) (1,3)
  (2,0) (2,1) (2,2) (2,3)

Valid paths with ≤1 turn:

Path 1: Right → Right → Right → Down → Down  (1 turn from R to D)
  (0,0) → (0,1) → (0,2) → (0,3) → (1,3) → (2,3)
  R       R       R       D       D

Path 2: Down → Down → Right → Right → Right  (1 turn from D to R)
  (0,0) → (1,0) → (2,0) → (2,1) → (2,2) → (2,3)
  D       D       R       R       R

Path 3: Right → Down → Right → Right → Down  (3 turns) ❌ exceeds limit
  (0,0) → (0,1) → (1,1) → (1,2) → (1,3) → (2,3)
  R       D       R       R       D

Grid movement directions:
  U (up):    (r-1, c)
  D (down):  (r+1, c)
  L (left):  (r, c-1)
  R (right): (r, c+1)

Turn occurs when: new_direction ≠ previous_direction

State tracking: dp[row][col][direction][turns_used]
  - row, col: current position
  - direction: last move direction (U/D/L/R or NONE for start)
  - turns_used: number of direction changes so far
```

### State reduction intuition

We add two dimensions (`turns` and `last direction`) because:

- Turn count is necessary to enforce the limit.
- Last direction is necessary to decide whether the next move consumes a turn.

Without the last direction, you cannot know if moving right now creates a turn.

### Why simple combinatorics is not enough

Without turn constraints, number of paths is `C((m-1)+(n-1), m-1)`.

With turn constraints, you must care about the **sequence pattern** of R and D moves, not just how many of each.

So we use DP.

### State design: you must remember direction

If you only track `(r,c,t)`, you cannot know whether the next move creates a new turn, because that depends on the last move direction.

So we track last direction as part of the state:

- `dpR[r][c][t]`: number of ways to reach cell `(r,c)` with exactly `t` turns and the last move was **Right**
- `dpD[r][c][t]`: number of ways to reach cell `(r,c)` with exactly `t` turns and the last move was **Down**

Answer:

`sum_{t=0..T} (dpR[m-1][n-1][t] + dpD[m-1][n-1][t]) mod MOD`

### Transitions

To arrive at `(r,c)` with last move Right, you must come from `(r, c-1)`:

- If you were already moving Right, turn count stays the same.
- If you were moving Down, you add 1 turn (direction change).

So:

`dpR[r][c][t] += dpR[r][c-1][t]`

and for `t>=1`:

`dpR[r][c][t] += dpD[r][c-1][t-1]`

Similarly, to arrive with last move Down, you come from `(r-1, c)`:

`dpD[r][c][t] += dpD[r-1][c][t]`

and for `t>=1`:

`dpD[r][c][t] += dpR[r-1][c][t-1]`

All modulo MOD.

### Decision Tree for Direction and Turn Tracking

```
At position (r, c) with current direction dir and turns_used:
    │
    ├─ Try move RIGHT (to position r, c+1):
    │   │
    │   ├─ Check if c+1 < n (in bounds)?
    │   │   ├─ NO: skip this move
    │   │   └─ YES: continue
    │   │
    │   ├─ Is this a turn? (dir ≠ RIGHT and dir ≠ NONE)
    │   │   ├─ YES: new_turns = turns_used + 1
    │   │   └─ NO:  new_turns = turns_used
    │   │
    │   ├─ Is new_turns ≤ T?
    │   │   ├─ NO: skip this move (exceeds turn limit)
    │   │   └─ YES: add to dpR[r][c+1][new_turns]
    │   │
    │   └─ dpR[r][c+1][new_turns] += dp[r][c][dir][turns_used]
    │
    ├─ Try move DOWN (to position r+1, c):
    │   │
    │   ├─ Check if r+1 < m (in bounds)?
    │   ├─ Is this a turn? (dir ≠ DOWN and dir ≠ NONE)
    │   ├─ Is new_turns ≤ T?
    │   └─ dpD[r+1][c][new_turns] += dp[r][c][dir][turns_used]
    │
    ├─ Try move LEFT (to position r, c-1):
    │   │
    │   ├─ Check if c-1 ≥ 0 (in bounds)?
    │   ├─ Is this a turn? (dir ≠ LEFT and dir ≠ NONE)
    │   ├─ Is new_turns ≤ T?
    │   └─ dpL[r][c-1][new_turns] += dp[r][c][dir][turns_used]
    │
    └─ Try move UP (to position r-1, c):
        │
        ├─ Check if r-1 ≥ 0 (in bounds)?
        ├─ Is this a turn? (dir ≠ UP and dir ≠ NONE)
        ├─ Is new_turns ≤ T?
        └─ dpU[r-1][c][new_turns] += dp[r][c][dir][turns_used]

Final answer: sum of all dp[m-1][n-1][all_dirs][t] for t ∈ [0, T]
```

### Initialization (the common bug zone)

At the start `(0,0)` there is no last direction.

We can initialize by “taking the first move”:

- If `n >= 2`, moving Right once reaches `(0,1)` with 0 turns, last dir Right:
  - `dpR[0][1][0] = 1`
- If `m >= 2`, moving Down once reaches `(1,0)` with 0 turns, last dir Down:
  - `dpD[1][0][0] = 1`

All other dp states start at 0.

Edge case:

- If `(m,n) = (1,1)`, you are already at destination with 0 moves, 0 turns.
  - Answer = 1

## Naive Approach

### Intuition

Enumerate all paths and count those with ≤ T turns.

### Why it fails

Total paths can be enormous even for 100x100. Enumeration is impossible.

## Optimal Approach (DP with 4D state, but bounded)

DP dimensions:

- `m` up to 100
- `n` up to 100
- `T` up to 50
- `dir` = 2

Total states ≈ `100 * 100 * 51 * 2 = 1,020,000`

Each transition is O(1), so total time is about a few million operations, which is safe.

### Complexity

- Time: `O(m * n * T)`
- Space: `O(m * n * T)`

You can optimize space to `O(n * T)` by processing row-by-row, but for these constraints, full DP is acceptable.

![Algorithm Visualization](../images/DP-008/algorithm-visualization.png)
![Algorithm Steps](../images/DP-008/algorithm-steps.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)
Example: `m=2, n=3, T=1`

Paths:

- `RRD` has 1 turn ✅
- `RDR` has 2 turns ❌
- `DRR` has 1 turn ✅

So answer is 2.

### State Evolution Table

Grid: 2×3, need to go from (0,0) to (1,2), T=1

| Step | Position | Direction | Turns | Path So Far | Valid? | Count |
|------|----------|-----------|-------|-------------|--------|-------|
| 0    | (0,0)    | -         | 0     | START       | ✓      | 1     |
| 1a   | (0,1)    | R         | 0     | R           | ✓      | 1     |
| 1b   | (1,0)    | D         | 0     | D           | ✓      | 1     |
| 2a   | (0,2)    | R         | 0     | RR          | ✓      | 1     |
| 2b   | (1,1)    | D         | 1     | RD          | ✓      | 1     |
| 2c   | (1,1)    | R         | 1     | DR          | ✓      | 1     |
| 3a   | (1,2)    | D         | 1     | RRD         | ✓      | 1     |
| 3b   | (1,2)    | R         | 1     | DRR         | ✓      | 1     |
| 3c   | (0,2)    | R         | 2     | RDR         | ✗      | 0     |

Total paths to (1,2) with ≤1 turn: 2

Detailed DP computation:
```
Initialize:
  dpR[0][1][0] = 1  (first move right to (0,1), 0 turns)
  dpD[1][0][0] = 1  (first move down to (1,0), 0 turns)

Process (0,1) with dir=R, turns=0:
  - Move R to (0,2): dpR[0][2][0] = 1
  - Move D to (1,1): dpD[1][1][1] = 1 (turn from R to D)

Process (1,0) with dir=D, turns=0:
  - Move R to (1,1): dpR[1][1][1] = 1 (turn from D to R)
  - Move D to (2,0): out of bounds

Process (0,2) with dir=R, turns=0:
  - Move D to (1,2): dpD[1][2][1] = 1 (turn from R to D)

Process (1,1) with dir=D, turns=1:
  - Move R to (1,2): dpR[1][2][1] += 1 (no turn, same as RD→RDR, but RD already has 1 turn, so this would be 1 turn total)

Process (1,1) with dir=R, turns=1:
  - Move R to (1,2): dpR[1][2][1] += 1

Final count at (1,2):
  dpR[1][2][1] + dpD[1][2][1] = 1 + 1 = 2
```

![Example Visualization](../images/DP-008/example-1.png)

## ✅ Proof of Correctness (Sketch)

We classify paths by:

- destination cell `(r,c)`
- number of turns used `t`
- last direction used

The last direction fully determines whether the next step creates a turn. The recurrence enumerates all ways to reach each state from its valid predecessor cell and correctly increments turns exactly when direction changes.

Summing dpR and dpD at the destination over all `t <= T` counts exactly the valid paths.

### Common Mistakes to Avoid

1. **Counting the first move as a turn**
2. **Forgetting to track the last direction**
3. **Using exactly T turns instead of at most T**
4. **Wrong base initialization for `(0,1)` and `(1,0)`**
5. **Forgetting modulo operations**



## Related Concepts

- DP with extra state dimensions
- Counting paths with constraints
- Direction-aware DP
