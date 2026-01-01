---
problem_id: GMT_STRING_REMOVE__2847
display_id: GMT-010
slug: removal-game-strings
title: "Removal Game on Strings"
difficulty: Medium
difficulty_score: 45
topics:
  - Game Theory
  - Strings
tags:
  - impartial-game
  - sprague-grundy
  - ad-hoc
premium: true
subscription_tier: basic
time_limit: 1000
memory_limit: 256
---

# GMT-010: Removal Game on Strings

## Problem Statement

You are given `n` strings.
Two players take turns making a move.
In each turn, a player must choose one string and perform the following operation:
1.  Select a **contiguous block of identical characters** (e.g., "aaa" in "bbaaac").
2.  Remove this block from the string.
3.  If the removal causes two blocks of the same character to become adjacent, they **merge** into a single block.

For example, in `aaabbbaaccc`:
- Removing `bbb` results in `aaa` and `aa` becoming adjacent.
- They merge to form `aaaaaccc`.

The player who cannot make a valid move loses.
(This happens when all strings are empty).

Determine if the first player has a winning strategy.

![Problem Illustration](../images/GMT-010/problem-illustration.png)

## Input Format

- The first line contains an integer `n`, the number of strings.
- The next `n` lines each contain a string `s`.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= n <= 100`
- `1 <= |s| <= 10^5`
- Strings consist of characters 'a' and 'b'.

## Example

**Input:**
```
2
aaabbbaabbb
aabb
```

**Output:**
```
First
```

**Explanation:**
- String 1: `aaabbbaabbb`.
  - Groups: `a, b, a, b`. Count = 4.
- String 2: `aabb`.
  - Groups: `a, b`. Count = 2.
- Game is equivalent to Nim with pile sizes based on group counts.
- We need to find the Grundy values for group counts 4 and 2.

![Example Visualization](../images/GMT-010/example-1.png)

## Notes

- The actual characters don't matter, only the structure of groups.
- Merging reduces the number of groups by 2 (the removed group is gone, and its two neighbors merge into one).

## Related Topics

Game Theory, Sprague-Grundy Theorem, String Processing

---

## Solution Template

### Java


### Python


### C++


### JavaScript

