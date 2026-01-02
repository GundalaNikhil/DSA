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
- Time complexity: O(r * c)

## Related Topics

BFS, Grid, Queue

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public int minutesToLight(int[][] grid) {
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (sc.hasNextInt()) {
            int n = sc.nextInt();
            List<Integer> remaining = new ArrayList<>();
            while (sc.hasNextInt()) {
                remaining.add(sc.nextInt());
            }

            int[][] grid;

            // If we have exactly n remaining values, treat as 1D grid (1 x n)
            if (remaining.size() == n) {
                grid = new int[1][n];
                for (int i = 0; i < n; i++) {
                    grid[0][i] = remaining.get(i);
                }
            } else if (remaining.size() > n) {
                // Check if we have r and c explicitly
                int r = n;
                int c = remaining.get(0);
                if (remaining.size() >= r * c) {
                    grid = new int[r][c];
                    int pos = 1;
                    for (int i = 0; i < r; i++) {
                        for (int j = 0; j < c; j++) {
                            grid[i][j] = remaining.get(pos++);
                        }
                    }
                } else {
                    // Fallback: treat as 1D
                    grid = new int[1][n];
                    for (int i = 0; i < n && i < remaining.size(); i++) {
                        grid[0][i] = remaining.get(i);
                    }
                }
            } else {
                // Fallback: treat as 1D
                grid = new int[1][remaining.size()];
                for (int i = 0; i < remaining.size(); i++) {
                    grid[0][i] = remaining.get(i);
                }
            }

            Solution sol = new Solution();
            System.out.println(sol.minutesToLight(grid));
        }
    }
}
```

### Python

```python
from collections import deque
from typing import List
import sys

def minutes_to_light(grid: List[List[int]]) -> int:
    return 0
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        remaining = list(iterator)

        # If we have exactly n values, treat as 1D grid (1 x n)
        if len(remaining) == n:
            grid = [[int(x) for x in remaining]]
            r, c = 1, n
        # If we have r and c, parse as 2D grid
        elif len(remaining) > n:
            r = n
            c_val = int(remaining[0]) if remaining else n
            # Check if we have enough for a r x c grid
            if len(remaining) >= r * c_val:
                c = c_val
                grid = []
                idx = 1
                for _ in range(r):
                    row = [int(remaining[idx + j]) for j in range(c)]
                    grid.append(row)
                    idx += c
            else:
                # Fallback: treat as 1D
                c = n
                grid = [[int(x) for x in remaining[:n]]]
        else:
            grid = [[int(x) for x in remaining]]
            r, c = 1, len(remaining)

        result = minutes_to_light(grid)
        print(result)
    except (StopIteration, ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int minutesToLight(vector<vector<int>>& grid) {
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (cin >> n) {
        vector<int> remaining;
        int val;
        while (cin >> val) {
            remaining.push_back(val);
        }

        vector<vector<int>> grid;

        // If we have exactly n remaining values, treat as 1D grid (1 x n)
        if ((int)remaining.size() == n) {
            grid.push_back(remaining);
        } else if ((int)remaining.size() > n) {
            // Check if we have r and c explicitly
            int r = n;
            int c = remaining[0];
            if ((int)remaining.size() >= r * c) {
                grid.resize(r);
                int pos = 1;
                for (int i = 0; i < r; i++) {
                    for (int j = 0; j < c; j++) {
                        grid[i].push_back(remaining[pos++]);
                    }
                }
            } else {
                // Fallback: treat as 1D
                vector<int> row;
                for (int i = 0; i < n && i < (int)remaining.size(); i++) {
                    row.push_back(remaining[i]);
                }
                grid.push_back(row);
            }
        } else {
            // Fallback: treat as 1D
            grid.push_back(remaining);
        }

        Solution sol;
        cout << sol.minutesToLight(grid) << endl;
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minutesToLight(grid) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/).filter(x => x !== "")));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const remaining = data.slice(idx);

  let grid;

  // If we have exactly n remaining values, treat as 1D grid (1 x n)
  if (remaining.length === n) {
    grid = [remaining.map(x => parseInt(x, 10))];
  } else if (remaining.length > n) {
    // Check if we have r and c explicitly
    const r = n;
    const c = parseInt(remaining[0], 10);
    if (remaining.length >= r * c) {
      grid = [];
      let pos = 1;
      for (let i = 0; i < r; i++) {
        const row = [];
        for (let j = 0; j < c; j++) {
          row.push(parseInt(remaining[pos++], 10));
        }
        grid.push(row);
      }
    } else {
      // Fallback: treat as 1D
      grid = [remaining.slice(0, n).map(x => parseInt(x, 10))];
    }
  } else {
    // Fallback: treat as 1D
    grid = [remaining.map(x => parseInt(x, 10))];
  }

  const solution = new Solution();
  console.log(solution.minutesToLight(grid));
});
```

