---
problem_id: GRP_FESTIVAL_MAZE_SHORTEST__7418
display_id: GRP-017
slug: festival-maze-shortest-path
title: "Festival Maze Shortest Path"
difficulty: Medium
difficulty_score: 55
topics:
  - Grid Graph
  - BFS
  - State Space Search
  - Shortest Path
tags:
  - graph
  - grid
  - bfs
  - state-space
  - shortest-path
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# GRP-017: Festival Maze Shortest Path

## Problem Statement

You are given a 2D grid representing a festival maze with the following cells:

- `S`: Start position (exactly one)
- `E`: Exit position (exactly one)
- `F`: Food stall (at least one)
- `#`: Wall (impassable)
- `.`: Open cell (passable)

You can move 4-directionally (up, down, left, right) through non-wall cells.

**Rule**: You must visit at least one food stall (`F`) before reaching the exit (`E`).

Find the minimum number of steps from `S` to `E` while satisfying the food stall visit rule, or return `-1` if impossible.

![Problem Illustration](../images/GRP-017/problem-illustration.png)

## Input Format

- First line: two integers `r c` (number of rows and columns)
- Next `r` lines: strings of length `c` representing the grid

## Output Format

- Single integer: minimum steps from S to E visiting at least one F, or `-1` if impossible

## Constraints

- `1 <= r, c <= 400`
- Total cells `<= 160,000`
- Grid contains exactly one `S`, exactly one `E`, and at least one `F`

## Example

**Input:**

```
3 3
SF.
###E
.F.
```

**Output:**

```
4
```

**Explanation:**

Grid layout:

```
S F .
# # # E
. F .
```

The optimal path demonstrates the constraint requirement:

```
S . F
# . .
. . E
```

Path: S(0,0) → (0,1) → F(0,2) → (1,2) → (2,2)=E: 4 steps ✓

![Example Visualization](../images/GRP-017/example-1.png)

## Notes

- Use BFS with state tracking: (row, col, visited_food_stall)
- State space: (r, c, {0, 1}) where 0 = haven't visited F yet, 1 = have visited F
- Start from S with state (row_S, col_S, 0)
- When you reach a food stall F, flip the visited flag to 1
- Can only reach E when visited_food_stall = 1
- Time complexity: O(r × c × 2) = O(r × c)
- Use a queue with (row, col, has_visited_food, steps)

## Related Topics

Grid Graph, BFS, State Space Search, Shortest Path with Constraints, Multi-State BFS

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int minStepsWithFood(int r, int c, char[][] grid) {
        // Implement here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String rcLine = br.readLine();
        if (rcLine == null) return;
        String[] rc = rcLine.trim().split("\\s+");
        int r = Integer.parseInt(rc[0]);
        int c = Integer.parseInt(rc[1]);

        char[][] grid = new char[r][c];
        for (int i = 0; i < r; i++) {
            String line = br.readLine();
            if (line == null) break;
            grid[i] = line.trim().toCharArray();
        }

        Solution sol = new Solution();
        System.out.println(sol.minStepsWithFood(r, c, grid));
    }
}
```

### Python

```python
import sys
from collections import deque

class Solution:
    def min_steps_with_food(self, r, c, grid):
        # Implement here
        return -1

def solve():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    rc = input_data[0].split()
    r = int(rc[0])
    c = int(rc[1])

    grid = []
    for i in range(1, 1 + r):
        grid.append(input_data[i].strip())

    sol = Solution()
    print(sol.min_steps_with_food(r, c, grid))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

struct State {
    int r, c, f, s;
};

class Solution {
public:
    int minStepsWithFood(int r, int c, vector<string>& grid) {
        // Implement here
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int r, c;
    if (!(cin >> r >> c)) return 0;

    vector<string> grid(r);
    for (int i = 0; i < r; i++) {
        cin >> grid[i];
    }

    Solution sol;
    cout << sol.minStepsWithFood(r, c, grid) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minStepsWithFood(r, c, grid) {
    // Implement here
    return -1;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\r?\n/);
  if (input.length < 2) return;

  const rc = input[0].trim().split(/\s+/);
  const r = parseInt(rc[0]);
  const c = parseInt(rc[1]);

  const grid = [];
  for (let i = 1; i <= r; i++) {
    grid.push(input[i].trim());
  }

  const sol = new Solution();
  console.log(sol.minStepsWithFood(r, c, grid));
}

solve();
```
