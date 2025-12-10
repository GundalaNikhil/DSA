# Island Counter

**Problem ID:** GRP-002
**Display ID:** 49
**Question Name:** Island Counter
**Slug:** island-counter
**Title:** Number of Islands
**Difficulty:** Medium
**Premium:** No
**Tags:** Graph, Depth-First Search, Breadth-First Search

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

Given a 2D grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically.

## A Simple Scenario (Daily Life Usage)

You're looking at a satellite map. Land masses appear as clusters of pixels. Hawaii has multiple islands, so counting them helps in geography. If you see this map:

```
1 1 0 0
1 0 0 1
0 0 1 1
```

You have 3 islands: top-left (2 cells), middle-right (1 cell), bottom-right (2 cells).

## Your Task

Count the number of distinct islands in the grid.

## Why is it Important?

This problem teaches you:

- 2D grid traversal
- DFS/BFS application
- Flood fill algorithm
- Geographic analysis

## Examples

### Example 1:

**Input:**

```
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
```

**Output:** `1`
**Explanation:** One large island in top-left.

### Example 2:

**Input:**

```
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
```

**Output:** `3`
**Explanation:** Three separate islands.

## Constraints

- m == grid.length
- n == grid[i].length
- 1 ≤ m, n ≤ 300
- grid[i][j] is '0' or '1'

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Amazon
- Google
- Microsoft
- Facebook

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
