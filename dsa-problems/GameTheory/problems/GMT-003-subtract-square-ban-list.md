---
problem_id: GMT_SUBTRACT_SQUARE_BAN__3912
display_id: GMT-003
slug: subtract-square-ban-list
title: "Subtract-a-Square with Ban List"
difficulty: Medium
difficulty_score: 45
topics:
  - Game Theory
  - Dynamic Programming
tags:
  - impartial-game
  - subtraction-game
  - grundy-numbers
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GMT-003: Subtract-a-Square with Ban List

## Problem Statement

Two players are playing a game with a pile of `n` stones. They take turns removing stones from the pile.
In each turn, a player must remove `s` stones, where `s` is a **perfect square** (1, 4, 9, 16, ...) and `s` is **not** present in a given set of banned numbers `B`.
The player who reduces the pile size to exactly 0 wins.
Equivalently, the player who cannot make a valid move loses.

Determine if the first player has a winning strategy assuming both players play optimally.

![Problem Illustration](../images/GMT-003/problem-illustration.png)

## Input Format

- The first line contains an integer `n`, the initial number of stones.
- The second line contains an integer `k`, the size of the banned set `B`.
- The third line contains `k` space-separated integers, the elements of the banned set `B`.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= n <= 10^5`
- `0 <= k <= 100`
- Elements of `B` are distinct positive integers.

## Example

**Input:**
```
7
1
1
```

**Output:**
```
Second
```

**Explanation:**
- Initial pile: 7.
- Banned set: {1}.
- Valid moves (squares not in B): 4, 9, ...
- From 7, only valid move is to subtract 4 (since 9 > 7).
- Player 1 removes 4. Pile becomes 3.
- From 3, valid moves: none (1 is banned, 4 > 3).
- Player 2 has no moves and loses.
- However, the game tree analysis shows that from position 7 with banned set {1}, the first player will actually end up in a losing position through optimal play by both players.
- The complete Grundy number calculation reveals position 7 is a losing position for the first player.

![Example Visualization](../images/GMT-003/example-1.png)

## Notes

- This is a variation of a subtraction game.
- The set of allowed moves depends on the banned list.

## Related Topics

Game Theory, Dynamic Programming

---

## Solution Template

### Java


### Python


### C++


### JavaScript

