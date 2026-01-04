---
problem_id: QUE_FESTIVAL_LANTERN_SPREAD__8461
display_id: QUE-015
slug: festival-lantern-spread
title: "Festival Lantern Spread"
difficulty: Medium
difficulty_score: 52
topics:
  - BFS
  - Queue
  - Grid
tags:
  - bfs
  - grid
  - queue
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# QUE-015: Festival Lantern Spread

## Problem Statement

A festival grid uses `0` for unlit cells and `1` for lit lanterns. Every minute, each lit lantern lights its four neighboring cells (up, down, left, right).

Compute the minimum number of minutes required to light the entire grid. If it is impossible, output `-1`.

![Problem Illustration](../images/QUE-015/problem-illustration.png)

## Input Format

- First line: two integers `r` and `c`
- Next `r` lines: `c` space-separated integers (`0` or `1`)

## Output Format

- Single integer: minutes to light all cells, or `-1`

## Constraints

- `1 <= r, c <= 200`
- `r * c <= 40000`
- Grid values are `0` or `1`

## Example

**Input:**

```
4 4
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 1
```

**Output:**

```
3
```

**Explanation:**

The farthest cell from a lit lantern is at Manhattan distance 3, so it takes 3 minutes to light the entire grid.

![Example Visualization](../images/QUE-015/example-1.png)

## Notes

- Use multi-source BFS starting from all `1` cells
- Track the number of unlit cells to detect impossible cases
- Each BFS layer corresponds to one minute
- Time complexity: O(r \* c)

## Related Topics

BFS, Grid, Queue

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minMinutes(int r, int c, int[][] grid) {
        // Implement here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int r = sc.nextInt();
        int c = sc.nextInt();
        int[][] grid = new int[r][c];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                grid[i][j] = sc.nextInt();
            }
        }
        Solution sol = new Solution();
        System.out.println(sol.minMinutes(r, c, grid));
        sc.close();
    }
}
```

### Python

```python
import sys

class Solution:
    def min_minutes(self, r, c, grid):
        # Implement here
        return -1

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    r = int(input_data[0])
    c = int(input_data[1])
    grid = []
    idx = 2
    for i in range(r):
        grid.append([int(x) for x in input_data[idx:idx+c]])
        idx += c
    sol = Solution()
    print(sol.min_minutes(r, c, grid))

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
    int minMinutes(int r, int c, vector<vector<int>>& grid) {
        // Implement here
        return -1;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int r, c;
    if (!(cin >> r >> c)) return 0;
    vector<vector<int>> grid(r, vector<int>(c));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) cin >> grid[i][j];
    }
    Solution sol;
    cout << sol.minMinutes(r, c, grid) << endl;
    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minMinutes(r, c, grid) {
    // Implement here
    return -1;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;
  const r = parseInt(input[0]);
  const c = parseInt(input[1]);
  const grid = [];
  let idx = 2;
  for (let i = 0; i < r; i++) {
    const row = [];
    for (let j = 0; j < c; j++) row.push(parseInt(input[idx++]));
    grid.push(row);
  }
  const sol = new Solution();
  console.log(sol.minMinutes(r, c, grid));
}

solve();
```
