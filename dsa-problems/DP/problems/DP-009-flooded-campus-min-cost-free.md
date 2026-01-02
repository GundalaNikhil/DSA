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

![Problem Illustration](../images/DP-009/problem-illustration.png)

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

class Solution {
    public int minCostWithFreeCells(int[][] cost, int f) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        int[][] cost = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                cost[i][j] = sc.nextInt();
            }
        }
        int f = sc.nextInt();
        System.out.println(new Solution().minCostWithFreeCells(cost, f));
        sc.close();
    }
}
```

### Python

```python
import sys

def min_cost_with_free_cells(cost: list[list[int]], f: int) -> int:
    # Implementation here
    return 0

def main():
    m, n = map(int, input().split())
    cost = []
    for _ in range(m):
        row = list(map(int, input().split()))
        cost.append(row)
    f = int(input())
    print(min_cost_with_free_cells(cost, f))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <queue>

using namespace std;

class Solution {
public:
    int minCostWithFreeCells(const vector<vector<int>>& cost, int f) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n;
    cin >> m >> n;
    vector<vector<int>> cost(m, vector<int>(n));
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) cin >> cost[i][j];
    }
    int f;
    cin >> f;

    Solution sol;
    cout << sol.minCostWithFreeCells(cost, f) << '\n';
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minCostWithFreeCells(cost, f) {
    // Implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(line.trim()));
rl.on("close", () => {
  if (data.length === 0) return;

  const tokens = data.join(" ").split(/\s+/);
  let ptr = 0;
  const m = Number(tokens[ptr++]);
  const n = Number(tokens[ptr++]);
  const cost = [];
  for (let i = 0; i < m; i++) {
    const row = [];
    for (let j = 0; j < n; j++) {
      row.push(Number(tokens[ptr++]));
    }
    cost.push(row);
  }
  const f = Number(tokens[ptr++]);

  const solution = new Solution();
  console.log(solution.minCostWithFreeCells(cost, f));
});
```
