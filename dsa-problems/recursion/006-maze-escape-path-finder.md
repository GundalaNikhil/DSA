# Find All Escape Routes from Maze

**Problem ID:** REC-006
**Display ID:** 107
**Question Name:** Maze Escape Path Finder
**Slug:** maze-escape-path-finder
**Title:** Find All Escape Routes from Maze
**Difficulty:** Hard
**Premium:** No
**Tags:** Recursion, Backtracking, Depth-First Search, Pathfinding

---

**Copyright Notice:** © 2025 NTB DSA Platform. This problem and its description are original content. Unauthorized reproduction or distribution is prohibited.

---

## Problem Description

You are building a game AI pathfinding system. Given a 2D grid maze with walls and open paths, a starting position, and an exit position, find all possible paths from start to exit. You can move up, down, left, or right (not diagonally). Return all valid paths as arrays of coordinates.

## A Simple Scenario (Daily Life Usage)

Video games constantly use pathfinding algorithms. When you're playing a puzzle game like Portal, a maze game like Pac-Man, or a strategy game like Age of Empires, the game needs to calculate possible routes. Game designers might want to know: "How many different ways can the player escape this room?" or "What are all the paths the enemy AI could take to reach the player?" This helps balance difficulty and create interesting gameplay.

## Your Task

Write a recursive function that takes a 2D grid (0 = open path, 1 = wall), a start position, and an exit position. Return all possible paths from start to exit. Each path should be an array of [row, col] coordinates. Use backtracking: mark cells as visited during exploration, then unmark them when backtracking to explore other routes.

## Why is it Important?

This problem teaches you how to:

- Implement backtracking algorithms
- Explore all possible paths in a maze
- Handle visited state during recursion
- Build game AI and pathfinding systems

## Examples

### Example 1:

**Input:**
```javascript
maze = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
]
start = [0, 0]
exit = [2, 2]
```
**Output:**
```javascript
[
  [[0,0], [0,1], [0,2], [1,2], [2,2]],
  [[0,0], [1,0], [2,0], [2,1], [2,2]]
]
```
**Explanation:** Two paths exist: one going right then down, another going down then right, both avoiding the wall at [1,1].

### Example 2:

**Input:**
```javascript
maze = [
  [0, 1, 0],
  [0, 1, 0],
  [0, 0, 0]
]
start = [0, 0]
exit = [0, 2]
```
**Output:**
```javascript
[
  [[0,0], [1,0], [2,0], [2,1], [2,2], [1,2], [0,2]]
]
```
**Explanation:** Only one path exists, going around the wall column by traveling down and around.

### Example 3:

**Input:**
```javascript
maze = [
  [0, 1],
  [1, 0]
]
start = [0, 0]
exit = [1, 1]
```
**Output:**
```javascript
[]
```
**Explanation:** No valid path exists - walls block all routes.

### Example 4:

**Input:**
```javascript
maze = [
  [0, 0],
  [0, 0]
]
start = [0, 0]
exit = [1, 1]
```
**Output:**
```javascript
[
  [[0,0], [0,1], [1,1]],
  [[0,0], [1,0], [1,1]]
]
```
**Explanation:** In an open 2x2 grid with no walls, two paths exist to reach the diagonal exit.

### Example 5:

**Input:**
```javascript
maze = [
  [0, 0, 0, 0],
  [0, 1, 1, 0],
  [0, 0, 0, 0]
]
start = [0, 0]
exit = [2, 3]
```
**Output:**
```javascript
[
  [[0,0], [0,1], [0,2], [0,3], [1,3], [2,3]],
  [[0,0], [1,0], [2,0], [2,1], [2,2], [2,3]]
]
```
**Explanation:** Can go around the wall block via the top or bottom path.

## Constraints

- 2 ≤ maze dimensions ≤ 10 x 10
- 0 represents open path, 1 represents wall
- Start and exit positions are always open paths (value 0)
- Start and exit are different positions
- 0 ≤ number of valid paths ≤ 100
- Can only move up, down, left, right (no diagonal movement)
- Cannot revisit cells within the same path

## Asked by Companies


**Note:** Company names are for illustrative purposes and represent the types of organizations that use similar systems. They do not imply endorsement or partnership.


- Unity Technologies
- Unreal Engine (Epic Games)
- Electronic Arts (EA)
- Ubisoft
- Nintendo
- Riot Games
- Valve

---

**Disclaimer:** While this problem involves classic computer science algorithms and data structures that are part of common knowledge, all problem descriptions, scenarios, examples, and explanations are original content created specifically for this platform.
