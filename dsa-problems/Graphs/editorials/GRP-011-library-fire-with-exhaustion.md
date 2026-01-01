---
problem_id: GRP_LIBRARY_FIRE_EXHAUSTION__6285
display_id: GRP-011
slug: library-fire-with-exhaustion
title: "Library Fire With Exhaustion"
difficulty: Medium
difficulty_score: 55
topics:
  - Grid Graph
  - Multi-Source BFS
  - State Tracking
tags:
  - graph
  - grid
  - bfs
  - multi-source
  - simulation
  - medium
premium: true
subscription_tier: basic
---

# GRP-011: Library Fire With Exhaustion

## 📋 Problem Summary

Simulate fire spread in a grid where fire sources have stamina that decreases with each spread. Compute the number of minutes until no new cells ignite, considering that fire stops spreading when stamina reaches zero.

## 🌍 Real-World Scenario

**Scenario Title:** Wildfire Simulation with Fuel Depletion

Imagine simulating wildfire spread where each fire source has limited fuel (stamina). As the fire spreads, it consumes fuel and eventually burns out. This models real wildfire behavior where fires don't spread indefinitely but are limited by available fuel.

This type of simulation helps firefighters predict fire spread patterns, plan containment strategies, and estimate when fires will naturally subside. The stamina mechanic represents fuel availability, wind strength, or firefighting efforts that gradually reduce fire intensity.

**Why This Problem Matters:**

- **Disaster Management:** Predicting fire/flood spread with decay
- **Epidemic Modeling:** Disease spread with immunity buildup
- **Network Propagation:** Information spread with diminishing reach
- **Game Development:** Spell effects with limited range/duration

![Real-World Application](../images/GRP-011/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: Fire Spread with Stamina

```
Initial grid:
[2] [0]    Fire at (0,0) with stamina 2
[0] [0]

Minute 0: Fire at (0,0), stamina=2
Minute 1: Spread to (0,1) and (1,0), stamina=1
Minute 2: Spread from (0,1) to (1,1), stamina=0
         Spread from (1,0) to (1,1), stamina=0
         Fire exhausted, no more spread

Total: 2 minutes
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **Fire sources:** Cells with value 2 in grid
- **Stamina:** Initial stamina from stamina grid
- **Spread rule:** Fire spreads to 4-adjacent cells, stamina decreases by 1
- **Exhaustion:** Fire stops spreading when stamina reaches 0
- **Return -1:** If any empty cell never catches fire

## Optimal Approach

### Algorithm

```
fire_spread_time(grid, stamina):
    queue = []  // (row, col, remaining_stamina, time)
    ignited = set()
    
    // Initialize with all fire sources
    for i, j in grid:
        if grid[i][j] == 2:
            queue.add((i, j, stamina[i][j], 0))
            ignited.add((i, j))
    
    max_time = 0
    
    while queue not empty:
        (r, c, stam, time) = queue.dequeue()
        max_time = max(max_time, time)
        
        if stam > 0:
            for (dr, dc) in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r + dr, c + dc
                if valid(nr, nc) and grid[nr][nc] == 0 and (nr,nc) not in ignited:
                    ignited.add((nr, nc))
                    queue.enqueue((nr, nc, stam - 1, time + 1))
    
    // Check if all empty cells ignited
    for i, j in grid:
        if grid[i][j] == 0 and (i,j) not in ignited:
            return -1
    
    return max_time
```

### Time Complexity: **O(rows × cols × max_stamina)**
### Space Complexity: **O(rows × cols)**

![Algorithm Visualization](../images/GRP-011/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Grid: `[[2,0],[0,0]]`, Stamina: `[[2,0],[0,0]]`

| Time | Queue | Ignited | Action |
|-----:|:------|:--------|:-------|
| 0 | [(0,0,2,0)] | {(0,0)} | Start |
| 1 | [(0,1,1,1),(1,0,1,1)] | {(0,0),(0,1),(1,0)} | Spread from (0,0) |
| 2 | [(1,0,1,1),(1,1,0,2)] | {(0,0),(0,1),(1,0),(1,1)} | Spread from (0,1) |
| 3 | [(1,1,0,2)] | {(0,0),(0,1),(1,0),(1,1)} | Spread from (1,0) |
| 4 | [] | {(0,0),(0,1),(1,0),(1,1)} | stam=0, no more spread |

All cells ignited, max_time = 2

![Example Visualization](../images/GRP-011/example-1.png)

## ✅ Proof of Correctness

**Theorem:** Multi-source BFS with stamina tracking correctly simulates fire spread.

**Proof:** BFS ensures cells are ignited in chronological order. Stamina tracking ensures fire only spreads while fuel remains. The ignited set prevents duplicate processing.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Add firefighting actions that reduce stamina
- **Extension 2:** Handle different terrain types with varying spread rates
- **Extension 3:** Optimize using priority queue for faster spread paths
- **Extension 4:** Track which fire source ignited each cell

### Common Mistakes to Avoid

1. **Not Tracking Stamina Correctly**
   - ❌ Wrong: Using global stamina instead of per-spread stamina
   - ✅ Correct: Track remaining stamina for each spread
   - **Impact:** Incorrect spread patterns

2. **Forgetting to Check All Empty Cells**
   - ❌ Wrong: Only returning max_time
   - ✅ Correct: Check if all empty cells were ignited, return -1 if not
   - **Description:** Missing the "all cells must ignite" requirement

3. **Duplicate Ignition**
   - ❌ Wrong: Not using ignited set
   - ✅ Correct: Track ignited cells to prevent re-processing
   - **Prevention:** Use set to track ignited cells

4. **Wrong Time Tracking**
   - ❌ Wrong: Incrementing time globally
   - ✅ Correct: Track time per cell in queue
   - **Description:** Cells at same level should have same time

5. **Not Handling Walls**
   - ❌ Wrong: Spreading to wall cells (grid[i][j] == 1)
   - ✅ Correct: Only spread to empty cells (grid[i][j] == 0)
   - **Description:** Walls should block fire spread

## Related Concepts

- **Multi-Source BFS:** Standard pattern for simultaneous sources
- **Rotting Oranges:** Similar problem without stamina
- **Flood Fill:** Related grid traversal problem
- **Dijkstra's Algorithm:** Weighted version of multi-source BFS
- **Cellular Automata:** Simulation of grid-based systems
