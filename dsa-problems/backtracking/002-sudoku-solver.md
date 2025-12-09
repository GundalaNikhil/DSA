# Sudoku Solver

**Problem ID:** BACK-002
**Display ID:** 61
**Question Name:** Sudoku Solver
**Slug:** sudoku-solver
**Title:** Valid Sudoku
**Difficulty:** Medium
**Premium:** No
**Tags:** Backtracking, Array, Matrix, Hash Table

## Problem Description

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

## A Simple Scenario (Daily Life Usage)

You're building a digital newspaper app that includes a daily Sudoku puzzle. Before publishing the puzzle, you need to validate that it's been set up correctly - no duplicate numbers in any row, column, or 3x3 box. This ensures players won't encounter an impossible-to-solve puzzle.

## Your Task

Write a function that takes a 9x9 Sudoku board and returns `true` if it's valid according to Sudoku rules, or `false` if there are any violations. Empty cells are represented by the character '.'.

## Why is it Important?

This problem teaches you how to:

- Work with 2D arrays and matrix traversal
- Implement constraint validation logic
- Use hash sets for duplicate detection
- Handle multiple simultaneous constraints
- Map 2D coordinates to sub-grid indices

## Examples

### Example 1:

**Input:**
```
board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
```
**Output:** `true`
**Explanation:** The board is valid. Each row, column, and 3x3 sub-box follows the rules.

### Example 2:

**Input:**
```
board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
```
**Output:** `false`
**Explanation:** Invalid! The first column has two 8's (positions [0,0] and [3,0]).

### Example 3:

**Input:**
```
board =
[[".",".",".",".","5",".",".","1","."]
,[".","4",".","3",".",".",".",".","."]
,[".",".",".",".",".","3",".",".","1"]
,["8",".",".",".",".",".",".","2","."]
,[".",".","2",".","7",".",".",".","."]
,[".","1","5",".",".",".",".",".","."]
,[".",".",".",".",".","2",".",".","."]
,[".","2",".","9",".",".",".",".","."]
,[".",".","4",".",".",".",".",".","."]]
```
**Output:** `false`
**Explanation:** The second row has two 4's - one at position [1,1] and another causes violation.

## Constraints

- board.length == 9
- board[i].length == 9
- board[i][j] is a digit 1-9 or '.'

## Asked by Companies

- Amazon
- Microsoft
- Apple
- Bloomberg
- Uber
- Google

## Hints

1. Use three sets of hash sets: one for rows, one for columns, one for 3x3 boxes
2. For each filled cell, check if its value already exists in the corresponding row, column, or box
3. The 3x3 box index can be calculated as: `boxIndex = (row / 3) * 3 + (col / 3)`
4. You only need one pass through the board
5. Early return false if you find any duplicate
