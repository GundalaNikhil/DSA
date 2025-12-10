# Zombie Infection Spread

**Problem ID:** GRP-006
**Display ID:** 53
**Question Name:** Zombie Infection Spread
**Slug:** zombie-infection-spread
**Title:** Rotting Oranges
**Difficulty:** Medium
**Premium:** No
**Tags:** Graph, Breadth-First Search, Matrix

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

In a grid, 0=empty, 1=fresh orange, 2=rotten orange. Every minute, rotten oranges infect adjacent fresh oranges. Find minimum minutes until no fresh oranges remain, or -1 if impossible.

## A Simple Scenario (Daily Life Usage)

(Imagine oranges, not zombies!) You have a fruit basket. Some oranges are already rotten (2). Each minute, rot spreads to adjacent oranges (up/down/left/right). Grid:

```
2 1 1
1 1 0
0 1 1
```

Minute 0: top-left is rotten. Minute 1: top-middle and middle-left rot. Continue until all fresh oranges rot. How long does it take?

## Your Task

Return minimum minutes for all oranges to rot, or -1 if some can't be reached.

## Why is it Important?

This problem teaches you:

- Multi-source BFS
- Level-order traversal
- Infection/spreading simulation
- Grid-based time tracking

## Examples

### Example 1:

**Input:** `grid = [[2,1,1],[1,1,0],[0,1,1]]`
**Output:** `4`
**Explanation:** Minute 0: (0,0). Minute 1: (0,1),(1,0). Minute 2: (0,2),(1,1). Minute 3: (1,2),(2,1). Minute 4: (2,2).

### Example 2:

**Input:** `grid = [[2,1,1],[0,1,1],[1,0,1]]`
**Output:** `-1`
**Explanation:** Orange at (2,2) can never be reached.

### Example 3:

**Input:** `grid = [[0,2]]`
**Output:** `0`
**Explanation:** No fresh oranges exist.

## Constraints

- m == grid.length
- n == grid[i].length
- 1 ≤ m, n ≤ 10
- grid[i][j] is 0, 1, or 2

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Microsoft
- Bloomberg
- Uber

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
