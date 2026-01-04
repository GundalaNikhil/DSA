---
problem_id: REC_ROBOT_ROUTE_TURNS__7405
display_id: REC-005
slug: robot-route-turns
title: "Robot Route With Turns"
difficulty: Medium
difficulty_score: 52
topics:
  - Recursion
  - Backtracking
  - Grid
tags:
  - recursion
  - backtracking
  - grid
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# REC-005: Robot Route With Turns

## Problem Statement

A robot must move from the top-left cell `(0,0)` to the bottom-right cell `(r-1,c-1)` on a grid. You may move up, down, left, or right, but cannot enter blocked cells (`1`).

Find any valid path that uses at most `T` turns, where a turn is a change in movement direction between consecutive steps. If no path exists, output `NONE`.

![Problem Illustration](../images/REC-005/problem-illustration.png)

## Input Format

- First line: integers `r`, `c`, and `T`
- Next `r` lines: `c` space-separated integers (0 = open, 1 = blocked)

## Output Format

- One line with the path as coordinates `row,col` separated by spaces
- If no valid path exists, output `NONE`

## Constraints

- `1 <= r, c <= 8`
- `0 <= T <= 6`
- Grid values are `0` or `1`

## Example

**Input:**

```
3 3 2
0 0 0
1 1 0
0 0 0
```

**Output:**

```
0,0 0,1 0,2 1,2 2,2
```

**Explanation:**

The path goes right, right, down, down. It has one turn (right to down).

![Example Visualization](../images/REC-005/example-1.png)

## Notes

- Track the previous direction to count turns
- Use a visited grid to avoid cycles
- Stop early when turns exceed `T`
- Any valid path is acceptable

## Related Topics

Backtracking, Grid Search, Pruning

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public void findPath(int r, int c, int t, int[][] grid) {
        // Implement here
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int r = sc.nextInt();
        int c = sc.nextInt();
        int t = sc.nextInt();
        int[][] grid = new int[r][c];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                grid[i][j] = sc.nextInt();
            }
        }
        Solution sol = new Solution();
        sol.findPath(r, c, t, grid);
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def find_path(self, r, c, t, grid):
        # Implement here
        pass

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    r = int(input_data[0])
    c = int(input_data[1])
    t = int(input_data[2])
    grid = []
    idx = 3
    for i in range(r):
        grid.append([int(x) for x in input_data[idx:idx+c]])
        idx += c
    sol = Solution()
    sol.find_path(r, c, t, grid)

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    void findPath(int r, int c, int t, vector<vector<int>>& grid) {
        // Implement here
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int r, c, t;
    if (!(cin >> r >> c >> t)) return 0;
    vector<vector<int>> grid(r, vector<int>(c));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            cin >> grid[i][j];
        }
    }
    Solution sol;
    sol.findPath(r, c, t, grid);
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  findPath(r, c, t, grid) {
    // Implement here
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;
  let idx = 0;
  const r = parseInt(input[idx++]);
  const c = parseInt(input[idx++]);
  const t = parseInt(input[idx++]);
  const grid = [];
  for (let i = 0; i < r; i++) {
    const row = [];
    for (let j = 0; j < c; j++) {
      row.push(parseInt(input[idx++]));
    }
    grid.push(row);
  }
  const sol = new Solution();
  sol.findPath(r, c, t, grid);
}

solve();
```
