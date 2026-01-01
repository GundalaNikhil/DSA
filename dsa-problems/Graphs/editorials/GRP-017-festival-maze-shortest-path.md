---
problem_id: GRP_FESTIVAL_MAZE_SHORTEST__7418
display_id: GRP-017
slug: festival-maze-shortest-path
title: Festival Maze Shortest Path
difficulty: Medium
difficulty_score: 55
topics:
- State-Space Search
- BFS
- Shortest Path with Constraints
tags:
- graph
- bfs
- state-space
- shortest-path
- constraints
- hard
premium: true
subscription_tier: premium
---
# GRP-017: Festival Maze Shortest Path

## 📋 Problem Summary

Find shortest path in a grid maze where you can pass through at most K walls. Use state-space BFS where each state is (row, col, walls_remaining). Return minimum steps to reach destination or -1 if impossible.

## 🌍 Real-World Scenario

**Scenario Title:** Emergency Route Planning with Obstacles

Imagine planning an emergency evacuation route through a city where you can break through K barriers (walls) if necessary. You need the shortest path considering you have limited barrier-breaking capacity.

State-space BFS models this by tracking position AND remaining capacity. Each state represents a unique situation (location + resources), allowing optimal pathfinding with constraints. This applies to robotics, game AI, and resource-constrained navigation.

**Why This Problem Matters:**

- **Emergency Planning:** Routes with limited obstacle removal
- **Game AI:** Pathfinding with abilities (teleports, wall-breaks)
- **Robotics:** Navigation with limited battery/fuel
- **Network Routing:** Paths with limited relay hops

![Real-World Application](../images/GRP-017/real-world-scenario.png)

## Detailed Explanation

### ASCII Diagram: State-Space BFS

```
Grid (0=empty, 1=wall):
[0] [1] [0]
[0] [1] [0]
[0] [0] [0]

Start: (0,0), End: (2,2), K=1

State space:
(0,0,1) → (1,0,1) → (2,0,1) → (2,1,1) → (2,2,1)
       ↘ (0,1,0) → (0,2,0) → (1,2,0) → (2,2,0)

Shortest path: 4 steps (breaking 1 wall)
```

## ✅ Input/Output Clarifications (Read This Before Coding)

- **State:** (row, col, walls_remaining)
- **Transition:** Move to adjacent cell, decrement walls_remaining if wall
- **Goal:** Reach destination with any walls_remaining ≥ 0
- **BFS guarantee:** First time reaching destination = shortest path

## Optimal Approach

### Algorithm

```
shortest_path_with_walls(grid, k):
    rows, cols = len(grid), len(grid[0])
    if (0,0) == (rows-1, cols-1):
        return 0
    
    queue = [(0, 0, k, 0)]  // (row, col, walls_left, steps)
    visited = {(0, 0, k)}
    
    while queue not empty:
        (r, c, walls, steps) = queue.dequeue()
        
        for (dr, dc) in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r + dr, c + dc
            
            if not valid(nr, nc):
                continue
            
            new_walls = walls - grid[nr][nc]
            
            if new_walls >= 0 and (nr, nc, new_walls) not in visited:
                if (nr, nc) == (rows-1, cols-1):
                    return steps + 1
                
                visited.add((nr, nc, new_walls))
                queue.enqueue((nr, nc, new_walls, steps + 1))
    
    return -1
```

### Time Complexity: **O(rows × cols × K)**
### Space Complexity: **O(rows × cols × K)**

![Algorithm Visualization](../images/GRP-017/algorithm-visualization.png)

## Implementations

### Java


### Python


### C++


### JavaScript


## 🧪 Test Case Walkthrough (Dry Run)

Grid: `[[0,1,0],[0,1,0],[0,0,0]]`, K=1

| Step | Queue | Visited States | Action |
|-----:|:------|:---------------|:-------|
| 0 | [(0,0,1,0)] | {(0,0,1)} | Start |
| 1 | [(1,0,1,1),(0,1,0,1)] | {(0,0,1),(1,0,1),(0,1,0)} | Explore from (0,0) |
| 2 | [(0,1,0,1),(2,0,1,2)] | {(0,0,1),(1,0,1),(0,1,0),(2,0,1)} | Explore from (1,0) |
| 3 | [(2,0,1,2),(0,2,0,2)] | {(0,0,1),(1,0,1),(0,1,0),(2,0,1),(0,2,0)} | Explore from (0,1) |
| 4 | [(0,2,0,2),(2,1,1,3)] | Add (2,1,1) | Explore from (2,0) |
| 5 | [(2,1,1,3),(1,2,0,3)] | Add (1,2,0) | Explore from (0,2) |
| 6 | [(1,2,0,3),(2,2,1,4)] | Reach (2,2)! | Return 4 |

Answer: 4

![Example Visualization](../images/GRP-017/example-1.png)

## ✅ Proof of Correctness

**Theorem:** State-space BFS finds shortest path with constraints.

**Proof:** BFS explores states in increasing order of steps. Each state (r,c,k) is unique. First time reaching destination = shortest path for that state configuration.

## 💡 Interview Extensions (High-Value Add-ons)

- **Extension 1:** Return the actual path, not just length
- **Extension 2:** Handle different costs for breaking walls
- **Extension 3:** Multiple types of obstacles with different K values
- **Extension 4:** Bidirectional BFS for optimization

### Common Mistakes to Avoid

1. **Wrong State Representation**
   - ❌ Wrong: Only tracking (row, col)
   - ✅ Correct: Track (row, col, walls_remaining)
   - **Impact:** Incorrect shortest path

2. **Not Checking Walls Remaining**
   - ❌ Wrong: Allowing negative walls_remaining
   - ✅ Correct: Only proceed if new_walls >= 0
   - **Description:** Violates constraint

3. **Visiting Same State Multiple Times**
   - ❌ Wrong: Only checking (row, col) in visited
   - ✅ Correct: Check (row, col, walls_remaining) in visited
   - **Prevention:** Different wall counts = different states

4. **Early Termination at Wrong State**
   - ❌ Wrong: Returning when reaching destination with any K
   - ✅ Correct: Return first time reaching destination (BFS guarantees shortest)
   - **Description:** BFS naturally finds shortest path

5. **Not Handling Start == End**
   - ❌ Wrong: Not checking if start is destination
   - ✅ Correct: Return 0 if start == destination
   - **Description:** Edge case

## Related Concepts

- **Standard BFS:** Without state tracking
- **Dijkstra with State:** Weighted version
- **A* Search:** Heuristic-guided state-space search
- **Dynamic Programming:** Alternative for some constraint problems
- **Multi-dimensional BFS:** General state-space technique
