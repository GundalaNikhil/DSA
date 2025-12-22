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
        // Your implementation here
        return -1;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        int c = sc.nextInt();
        int[][] grid = new int[r][c];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                grid[i][j] = sc.nextInt();
            }
        }

        Solution solution = new Solution();
        System.out.println(solution.minutesToLight(grid));
        sc.close();
    }
}
```

### Python

```python
from typing import List

def minutes_to_light(grid: List[List[int]]) -> int:
    # Your implementation here
    return -1

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    r = int(next(it))
    c = int(next(it))
    grid = []
    for _ in range(r):
        row = [int(next(it)) for _ in range(c)]
        grid.append(row)

    result = minutes_to_light(grid)
    sys.stdout.write(str(result))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int minutesToLight(const vector<vector<int>>& grid) {
        // Your implementation here
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
        for (int j = 0; j < c; j++) {
            cin >> grid[i][j];
        }
    }

    Solution solution;
    cout << solution.minutesToLight(grid) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minutesToLight(grid) {
    // Your implementation here
    return -1;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const r = parseInt(data[idx++], 10);
  const c = parseInt(data[idx++], 10);
  const grid = [];
  for (let i = 0; i < r; i++) {
    const row = [];
    for (let j = 0; j < c; j++) {
      row.push(parseInt(data[idx++], 10));
    }
    grid.push(row);
  }

  const solution = new Solution();
  const result = solution.minutesToLight(grid);
  console.log(result.toString());
});
```
