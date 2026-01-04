---
problem_id: AGR_K_EDGE_DISJOINT_PATHS__2167
display_id: AGR-013
slug: k-edge-disjoint-paths
title: "K-Edge-Disjoint Paths"
difficulty: Hard
difficulty_score: 68
topics:
  - Graphs
  - Max Flow
  - Disjoint Paths
tags:
  - advanced-graphs
  - disjoint-paths
  - max-flow
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-013: K-Edge-Disjoint Paths

## Problem Statement

Given a directed graph, determine whether there exist at least `k` edge-disjoint paths from `s` to `t`.

![Problem Illustration](../images/AGR-013/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, `s`, `t`, `k`
- Next `m` lines: `u v` describing a directed edge `u -> v`

## Output Format

- Print `YES` if at least `k` edge-disjoint paths exist, otherwise `NO`

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `1 <= k <= 10000`
- `0 <= s, t < n`, `s != t`

## Example

**Input:**

```
4 4 0 3 2
0 1
1 3
0 2
2 3
```

**Output:**

```
YES
```

**Explanation:**

Two edge-disjoint paths exist: 0-1-3 and 0-2-3.

![Example Visualization](../images/AGR-013/example-1.png)

## Notes

- Transform to max flow with unit capacities on edges.
- Answer is YES if max flow >= k.
- Use Dinic for performance on large graphs.

## Related Topics

Edge-Disjoint Paths, Max Flow, Dinic

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public boolean solve(int n, int m, int s, int t, int k, int[][] edges) {
        // Implement here
        return false;
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        if (line == null) return;
        String[] parts = line.trim().split("\\s+");
        int n = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);
        int s = Integer.parseInt(parts[2]);
        int t = Integer.parseInt(parts[3]);
        int k = Integer.parseInt(parts[4]);

        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            line = br.readLine();
            if (line == null) break;
            parts = line.trim().split("\\s+");
            edges[i][0] = Integer.parseInt(parts[0]);
            edges[i][1] = Integer.parseInt(parts[1]);
        }

        Solution sol = new Solution();
        if (sol.solve(n, m, s, t, k, edges)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}
```

### Python

```python
import sys

class Solution:
    def solve(self, n, m, s, t, k, edges):
        # Implement here
        return False

def run_program():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        s = int(next(iterator))
        t = int(next(iterator))
        k = int(next(iterator))

        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

    except StopIteration:
        pass

    sol = Solution()
    if sol.solve(n, m, s, t, k, edges):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    run_program()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool solve(int n, int m, int s, int t, int k, vector<vector<int>>& edges) {
        // Implement here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, s, t, k;
    if (!(cin >> n >> m >> s >> t >> k)) return 0;

    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution sol;
    if (sol.solve(n, m, s, t, k, edges)) {
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  solve(n, m, s, t, k, edges) {
    // Implement here
    return false;
  }
}

function runProgram() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 5) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }

  const n = readInt();
  const m = readInt();
  const s = readInt();
  const t = readInt();
  const k = readInt();

  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = readInt();
    const v = readInt();
    edges.push([u, v]);
  }

  const sol = new Solution();
  if (sol.solve(n, m, s, t, k, edges)) {
    console.log("YES");
  } else {
    console.log("NO");
  }
}

runProgram();
```
