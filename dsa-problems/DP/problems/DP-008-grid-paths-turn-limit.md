---
problem_id: DP_GRID_TURN_LIMIT__4930
display_id: DP-008
slug: grid-paths-turn-limit
title: "Grid Paths With Turn Limit"
difficulty: Medium
difficulty_score: 58
topics:
  - Dynamic Programming
  - Grid DP
  - Counting
tags:
  - dp
  - grid
  - counting
  - medium
premium: true
subscription_tier: basic
time_limit: 2500
memory_limit: 256
---

# DP-008: Grid Paths With Turn Limit

## Problem Statement

You are in an `m x n` grid, starting at the top-left cell `(0,0)` and wanting to reach the bottom-right cell `(m-1, n-1)`.

You may move only:

- **Right** (increase column by 1), or
- **Down** (increase row by 1)

A **turn** occurs when your move direction changes between consecutive moves (Right→Down or Down→Right). The first move does **not** count as a turn because there is no previous direction.

Given an integer `T`, count the number of valid paths that use **at most `T` turns**.

Because the count can be huge, output the answer modulo `1_000_000_007`.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767513330/dsa/dp/tfm7flidt5znphiuzh9p.jpg)

## Input Format

- First line: three integers `m`, `n`, `T`

## Output Format

Print one integer: number of paths from `(0,0)` to `(m-1,n-1)` using at most `T` turns, modulo `1_000_000_007`.

## Constraints

- `1 <= m, n <= 100`
- `0 <= T <= 50`

## Example

**Input:**

```
2 3 1
```

**Output:**

```
2
```

**Explanation:**

Grid is 2 rows and 3 columns. We need 2 Rights and 1 Down in some order.

All possible paths:

- `R R D` (1 turn: R→D)
- `R D R` (2 turns: R→D→R)
- `D R R` (1 turn: D→R)

With at most `T=1` turns, valid paths are `RRD` and `DRR` ⇒ answer is `2`.

![Example Visualization](../images/DP-008/example-1.png)

## Notes

- If `m=1` or `n=1`, there is only one path and it uses 0 turns.
- The first move does not count as a turn.
- Use modulo arithmetic throughout.

## Related Topics

Dynamic Programming, Grid DP, Counting

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public int countPaths(int m, int n, int t) {
        // Implement here
        return 0;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        String[] parts = line.trim().split("\\s+");
        if (parts.length < 3) return;
        int m = Integer.parseInt(parts[0]);
        int n = Integer.parseInt(parts[1]);
        int t = Integer.parseInt(parts[2]);

        Solution sol = new Solution();
        System.out.println(sol.countPaths(m, n, t));
    }
}
```

### Python

```python
import sys

class Solution:
    def count_paths(self, m, n, t):
        # Implement here
        return 0

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    parts = list(map(int, line.split()))
    if len(parts) < 3:
        return
    m, n, t = parts

    sol = Solution()
    print(sol.count_paths(m, n, t))

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
    int countPaths(int m, int n, int t) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int m, n, t;
    if (!(cin >> m >> n >> t)) return 0;

    Solution sol;
    cout << sol.countPaths(m, n, t) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  countPaths(m, n, t) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  const m = parseInt(input[0]);
  const n = parseInt(input[1]);
  const t = parseInt(input[2]);

  const sol = new Solution();
  console.log(sol.countPaths(m, n, t));
}

solve();
```
