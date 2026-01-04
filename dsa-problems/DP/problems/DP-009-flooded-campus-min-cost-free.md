---
problem_id: DP_GRID_FREE_CELL__4415
display_id: DP-009
slug: flooded-campus-min-cost-free
title: "Flooded Campus Min Cost With Free Cells"
difficulty: Medium
difficulty_score: 57
topics:
  - Dynamic Programming
  - Grid DP
  - Shortest Path
tags:
  - dp
  - grid
  - min-cost
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# DP-009: Flooded Campus Min Cost With Free Cells

## Problem Statement

You are given an `m x n` grid of non-negative costs `cost[i][j]`. You start at the top-left cell `(0,0)` and want to reach the bottom-right cell `(m-1, n-1)` by moving only **Right** or **Down**.

You may choose up to `f` cells to traverse **for free** (their cost becomes 0). Each cell’s cost can be discounted at most once.

Find the minimum possible total cost to reach `(m-1, n-1)` if you can pick at most `f` free cells.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513330/dsa/dp/qzdkw5ntxer3zrmnzvke.jpg)

## Input Format

- First line: two integers `m` and `n`
- Next `m` lines: `n` integers each, representing `cost[i][j]`
- Last line: integer `f` (number of free cells allowed)

## Output Format

Print one integer: the minimum cost to reach the bottom-right cell using at most `f` free cells.

## Constraints

- `1 <= m, n <= 200`
- `0 <= cost[i][j] <= 10^4`
- `0 <= f <= 10`

## Example

**Input:**

```
2 2
5 3
4 1
1
```

**Output:**

```
4
```

**Explanation:**

- Without any free cell, cheapest path is `5 -> 3 -> 1` (cost 9) or `5 -> 4 -> 1` (cost 10).
- You can mark one cell free (`f=1`):
  - If you make cell `(0,1)` free, path cost = `5 + 0 + 1 = 6`
  - If you make cell `(1,0)` free, path cost = `5 + 0 + 1 = 6`
  - If you make cell `(0,0)` free, path cost = `0 + 3 + 1 = 4` ✅ minimum

So the minimum achievable cost is 4.

![Example Visualization](../images/DP-009/example-1.png)

## Notes

- You can choose fewer than `f` free cells if that’s better or unnecessary.
- Choosing `(0,0)` or `(m-1,n-1)` as free cells is allowed.
- This is a grid DP with an extra dimension for how many free cells you’ve used so far.

## Related Topics

Dynamic Programming, Grid DP, Min-Cost Path

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long minCost(int m, int n, int[][] costs, int f) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String mnLine = br.readLine();
        if (mnLine == null) return;
        String[] mnParts = mnLine.trim().split("\\s+");
        int m = Integer.parseInt(mnParts[0]);
        int n = Integer.parseInt(mnParts[1]);

        int[][] costs = new int[m][n];
        for (int i = 0; i < m; i++) {
            String[] row = br.readLine().trim().split("\\s+");
            for (int j = 0; j < n; j++) {
                costs[i][j] = Integer.parseInt(row[j]);
            }
        }

        String fLine = br.readLine();
        if (fLine == null) return;
        int f = Integer.parseInt(fLine.trim());

        Solution sol = new Solution();
        System.out.println(sol.minCost(m, n, costs, f));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_cost(self, m, n, costs, f):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    m = int(input_data[0])
    n = int(input_data[1])
    idx = 2
    costs = []
    for _ in range(m):
        costs.append(list(map(int, input_data[idx:idx+n])))
        idx += n

    f = int(input_data[idx])

    sol = Solution()
    print(sol.min_cost(m, n, costs, f))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long minCost(int m, int n, const vector<vector<int>>& costs, int f) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int m, n;
    if (!(cin >> m >> n)) return 0;

    vector<vector<int>> costs(m, vector<int>(n));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> costs[i][j];
        }
    }

    int f;
    cin >> f;

    Solution sol;
    cout << sol.minCost(m, n, costs, f) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minCost(m, n, costs, f) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  const m = parseInt(input[idx++]);
  const n = parseInt(input[idx++]);

  const costs = [];
  for (let i = 0; i < m; i++) {
    const row = [];
    for (let j = 0; j < n; j++) {
      row.push(parseInt(input[idx++]));
    }
    costs.push(row);
  }

  const f = parseInt(input[idx++]);

  const sol = new Solution();
  console.log(sol.minCost(m, n, costs, f).toString());
}

solve();
```
