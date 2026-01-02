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
    int R, C, T;
    Long[][][][] memo;

    public long countPaths(int r, int c, int t) {
        return 0;
    }

    private long dfs(int r, int c, int lastDir, int turns) {
        if (r == R - 1 && c == C - 1) return 1;
        if (turns > T) return 0;
        
        if (memo[r][c][lastDir][turns] != null) return memo[r][c][lastDir][turns];

        long count = 0;

        // Dir 0: Right (c+1)
        if (c + 1 < C) {
            int newTurns = turns;
            if (lastDir != 2 && lastDir != 0) newTurns++;
            count += dfs(r, c + 1, 0, newTurns);
        }

        // Dir 1: Down (r+1)
        if (r + 1 < R) {
            int newTurns = turns;
            if (lastDir != 2 && lastDir != 1) newTurns++;
            count += dfs(r + 1, c, 1, newTurns);
        }

        return memo[r][c][lastDir][turns] = count;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int r = sc.nextInt();
        int c = sc.nextInt();
        int T = sc.nextInt();
        
        Solution sol = new Solution();
        System.out.println(sol.countPaths(r, c, T));
        sc.close();
    }
}
```

### Python

```python
def count_paths(r: int, c: int, T: int) -> int:
    return 0
def main():
    import sys
    first_line = sys.stdin.read().strip().split()
    r = int(first_line[0])
    c = int(first_line[1])
    T = int(first_line[2])
    result = count_paths(r, c, T)
    print(result)

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

class Solution {
    int R, C, T;
    long long memo[55][55][4][20]; // r, c, dir, turns. T <= 15 per problem constraints usually? 
    // Python constraints? 
    // If T is large, maybe map? But T usually small for turn limits.
    // Python code handles T dynamically? 
    // Let's use a map or bigger array?
    // r, c usually small?
    // Let's assume R,C <= 50, T <= 50.

public:
    long long countPaths(int r, int c, int t) {
        R = r; C = c; T = t;
        memset(memo, -1, sizeof(memo));
        // Start: 0,0, no last dir (-1), 0 turns
        // lastDir: 0=Right, 1=Down. -1=None.
        // Array index for -1 -> use 2 or something?
        // Map: 0->0, 1->1, -1->2.
        return dfs(0, 0, 2, 0);
    }

    long long dfs(int r, int c, int lastDir, int turns) {
        if (r == R - 1 && c == C - 1) return 1;
        if (turns > T) return 0;
        
        if (memo[r][c][lastDir][turns] != -1) return memo[r][c][lastDir][turns];

        long long count = 0;

        // Dir 0: Right (c+1)
        if (c + 1 < C) {
            int newTurns = turns;
            if (lastDir != 2 && lastDir != 0) newTurns++; // Turn if changing from Down(1) to Right(0)
            count += dfs(r, c + 1, 0, newTurns);
        }

        // Dir 1: Down (r+1)
        if (r + 1 < R) {
            int newTurns = turns;
            if (lastDir != 2 && lastDir != 1) newTurns++; // Turn if changing from Right(0) to Down(1)
            count += dfs(r + 1, c, 1, newTurns);
        }

        return memo[r][c][lastDir][turns] = count;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int r, c, T;
    if (!(cin >> r >> c >> T)) return 0;
    
    Solution sol;
    cout << sol.countPaths(r, c, T) << endl;
    return 0;
}
```

### JavaScript

```javascript
const readline = require('readline');
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
let tokens = [];
rl.on('line', (line) => { tokens.push(...line.trim().split(/\s+/)); });
rl.on('close', () => {
    if(tokens.length===0) return;
    let ptr = 0;
    const r = parseInt(tokens[ptr++]);
    const c = parseInt(tokens[ptr++]);
    const T = parseInt(tokens[ptr++]);
    
    const sol = new Solution();
    console.log(sol.countPaths(r, c, T).toString());
});

class Solution {
    countPaths(r, c, T) {
    return 0;
  }

    dfs(r, c, lastDir, turns) {
    return 0;
  }
}
```

