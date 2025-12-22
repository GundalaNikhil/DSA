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
    public List<int[]> findPath(int[][] grid, int T) {
        // Your implementation here
        return new ArrayList<>();
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        int c = sc.nextInt();
        int T = sc.nextInt();
        int[][] grid = new int[r][c];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                grid[i][j] = sc.nextInt();
            }
        }

        Solution solution = new Solution();
        List<int[]> path = solution.findPath(grid, T);
        if (path.isEmpty()) {
            System.out.println("NONE");
        } else {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < path.size(); i++) {
                if (i > 0) sb.append(' ');
                sb.append(path.get(i)[0]).append(',').append(path.get(i)[1]);
            }
            System.out.println(sb.toString());
        }
        sc.close();
    }
}
```

### Python

```python
def find_path(grid: list[list[int]], T: int) -> list[tuple[int, int]]:
    # Your implementation here
    return []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    r = int(next(it))
    c = int(next(it))
    T = int(next(it))
    grid = [[int(next(it)) for _ in range(c)] for _ in range(r)]

    path = find_path(grid, T)
    if not path:
        print("NONE")
    else:
        print(" ".join(f"{r},{c}" for r, c in path))

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
    vector<pair<int,int>> findPath(const vector<vector<int>>& grid, int T) {
        // Your implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int r, c, T;
    if (!(cin >> r >> c >> T)) return 0;
    vector<vector<int>> grid(r, vector<int>(c));
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) cin >> grid[i][j];
    }

    Solution solution;
    vector<pair<int,int>> path = solution.findPath(grid, T);
    if (path.empty()) {
        cout << "NONE\n";
    } else {
        for (int i = 0; i < (int)path.size(); i++) {
            if (i) cout << ' ';
            cout << path[i].first << ',' << path[i].second;
        }
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  findPath(grid, T) {
    // Your implementation here
    return [];
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
  const T = parseInt(data[idx++], 10);
  const grid = [];
  for (let i = 0; i < r; i++) {
    const row = [];
    for (let j = 0; j < c; j++) row.push(parseInt(data[idx++], 10));
    grid.push(row);
  }

  const solution = new Solution();
  const path = solution.findPath(grid, T);
  if (path.length === 0) {
    console.log("NONE");
  } else {
    console.log(path.map((p) => `${p[0]},${p[1]}`).join(" "));
  }
});
```
