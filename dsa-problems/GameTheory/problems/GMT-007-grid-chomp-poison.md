---
problem_id: GMT_GRID_CHOMP_POISON__7391
display_id: GMT-007
slug: grid-chomp-poisoned
title: "Grid Chomp with Poisoned Cells"
difficulty: Hard
difficulty_score: 60
topics:
  - Game Theory
  - Dynamic Programming
  - Bitmask
tags:
  - impartial-game
  - memoization
  - state-compression
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GMT-007: Grid Chomp with Poisoned Cells

## Problem Statement

You are given an `R x C` grid of chocolate bars.
The cell at `(0, 0)` is poisoned. There may be other poisoned cells as well.
Two players take turns making a move.
In each turn, a player must choose a non-poisoned cell `(r, c)` and eat it, along with all cells `(x, y)` such that `x >= r` and `y >= c` (i.e., the rectangle to the bottom-right of the chosen cell).
However, a player **cannot** choose a cell `(r, c)` if eating it would also consume any poisoned cell.
In other words, the chosen rectangle `[r, R-1] x [c, C-1]` must not contain any poisoned cells.
The player who cannot make a valid move loses.
(This happens when all remaining edible cells would force eating a poisoned cell, or no edible cells are left).

Determine if the first player has a winning strategy.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767539106/dsa/gametheory_simple/mvgdka2blqnzfwxwzt2i.jpg)

## Input Format

- The first line contains two integers `R` and `C`.
- The second line contains an integer `K`, the number of poisoned cells.
- The next `K` lines each contain two integers `r` and `c`, representing a poisoned cell.
- `(0, 0)` is always included in the poisoned cells.

## Output Format

- Return "First" if the first player wins, and "Second" if the second player wins.

## Constraints

- `1 <= R, C <= 8`
- `1 <= K <= R * C`
- `(0, 0)` is always poisoned.

## Example

**Input:**

```
2 2
1
0 0
```

**Output:**

```
First
```

**Explanation:**

- Grid 2x2. Poison at (0,0).
- Valid moves:
  - (0, 1): Removes (0,1), (1,1).
  - (1, 0): Removes (1,0), (1,1).
  - (1, 1): Removes (1,1).
- If P1 picks (1, 1): Grid becomes L-shape (missing (1,1)).
  - P2 can pick (0, 1) or (1, 0).
  - If P2 picks (0, 1), only (1, 0) remains. P1 picks (1, 0). P2 has no moves. P1 wins.
- Thus P1 has a winning strategy.

![Example Visualization](../images/GMT-007/example-1.png)

## Notes

- The state of the game can be represented by the heights of the columns.
- Since we always remove a bottom-right rectangle, the remaining cells always form a "staircase" shape (Young Diagram).
- `h[0] >= h[1] >= ... >= h[C-1]`.

## Related Topics

Game Theory, Memoization, Young Tableaux

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public String determineWinner(int r, int c, int k, int[][] poisoned) {
        // Implement here
        return "";
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String rcLine = br.readLine();
        if (rcLine == null) return;
        String[] rcParts = rcLine.trim().split("\\s+");
        int r = Integer.parseInt(rcParts[0]);
        int c = Integer.parseInt(rcParts[1]);

        String kLine = br.readLine();
        if (kLine == null) return;
        int k = Integer.parseInt(kLine.trim());

        int[][] poisoned = new int[k][2];
        for (int i = 0; i < k; i++) {
            String[] pParts = br.readLine().trim().split("\\s+");
            poisoned[i][0] = Integer.parseInt(pParts[0]);
            poisoned[i][1] = Integer.parseInt(pParts[1]);
        }

        Solution sol = new Solution();
        System.out.println(sol.determineWinner(r, c, k, poisoned));
    }
}
```

### Python

```python
import sys

class Solution:
    def determine_winner(self, r, c, k, poisoned):
        # Implement here
        return ""

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    r = int(input_data[0])
    c = int(input_data[1])
    k = int(input_data[2])

    poisoned = []
    idx = 3
    for _ in range(k):
        poisoned.append([int(input_data[idx]), int(input_data[idx+1])])
        idx += 2

    sol = Solution()
    print(sol.determine_winner(r, c, k, poisoned))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string determineWinner(int r, int c, int k, const vector<pair<int, int>>& poisoned) {
        // Implement here
        return "";
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int r, c, k;
    if (!(cin >> r >> c >> k)) return 0;

    vector<pair<int, int>> poisoned(k);
    for (int i = 0; i < k; i++) {
        cin >> poisoned[i].first >> poisoned[i].second;
    }

    Solution sol;
    cout << sol.determineWinner(r, c, k, poisoned) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  determineWinner(r, c, k, poisoned) {
    // Implement here
    return "";
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  let idx = 0;
  const r = parseInt(input[idx++]);
  const c = parseInt(input[idx++]);
  const k = parseInt(input[idx++]);

  const poisoned = [];
  for (let i = 0; i < k; i++) {
    poisoned.push([parseInt(input[idx++]), parseInt(input[idx++])]);
  }

  const sol = new Solution();
  console.log(sol.determineWinner(r, c, k, poisoned));
}

solve();
```
