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
time_limit: 2000
memory_limit: 256
---

# GRP-011: Library Fire With Exhaustion

## Problem Statement

You are given a 2D grid representing a library where:

- `0` = empty cell
- `1` = wall (impassable)
- `2` = fire source cell

Additionally, you have a parallel stamina grid where each fire source cell has an initial stamina value (between 1 and 10).

Fire spreads as follows:

- Each minute, active fire cells spread to their 4 adjacent neighbors (up, down, left, right)
- When a fire spreads to a neighbor, the stamina value decreases by 1
- A fire cell continues spreading to neighbors while its stamina > 0
- Once stamina reaches 0, that fire cell stops spreading (but remains burning)

Your task: Compute the number of minutes until no new cells ignite. If any empty cell never catches fire, return `-1`.

![Problem Illustration](../images/GRP-011/problem-illustration.png)

## Input Format

- First line: two integers `r c` (number of rows and columns)
- Next `r` lines: `c` space-separated integers representing the grid (0=empty, 1=wall, 2=fire)
- Next `r` lines: `c` space-separated integers representing the stamina grid (positive values for fire sources, 0 elsewhere)

## Output Format

- Single integer: total minutes until no new ignitions occur, or `-1` if some empty cell never burns

## Constraints

- `1 <= r, c <= 200`
- Cell values: 0 (empty), 1 (wall), 2 (fire source)
- Stamina values: 0 to 10
- At least one fire source exists

## Example

**Input:**

```
2 2
2 0
0 0
2 0
0 0
```

**Output:**

```
2
```

**Explanation:**

Initial grid:

```
[2] [0]
[0] [0]
```

Initial stamina:

```
[2] [0]
[0] [0]
```

Minute 0: Fire at (0,0) with stamina 2
Minute 1: Fire spreads to (0,1) and (1,0), stamina becomes 1 at these new cells
Minute 2: Fire spreads from (0,1) to (1,1) and from (1,0) to (1,1), but stamina is now 0, so spreading stops

All cells have been ignited after 2 minutes.

![Example Visualization](../images/GRP-011/example-1.png)

## Notes

- Use multi-source BFS starting from all initial fire sources
- Track remaining stamina for each fire spread
- Only spread to neighbors if current stamina > 0
- Walls cannot burn
- If any empty cell remains unreached, return -1
- Time complexity: O(r × c × max_stamina)

## Related Topics

Multi-Source BFS, Grid Graph, Simulation, State Tracking, Fire Spread

---

## Solution Template

### Java


### Python


### C++


### JavaScript

