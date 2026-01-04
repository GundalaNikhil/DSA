---
problem_id: AGR_DINIC_WITH_SCALING__5083
display_id: AGR-011
slug: dinic-with-scaling
title: "Dinic With Scaling"
difficulty: Medium
difficulty_score: 56
topics:
  - Graphs
  - Max Flow
  - Scaling
tags:
  - advanced-graphs
  - max-flow
  - dinic
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-011: Dinic With Scaling

## Problem Statement

Compute the maximum flow in a directed graph using Dinic's algorithm with capacity scaling.

![Problem Illustration](../images/AGR-011/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, `s`, `t`
- Next `m` lines: `u v c` describing a directed edge `u -> v` with capacity `c`

## Output Format

- Single integer: maximum flow from `s` to `t`

## Constraints

- `2 <= n <= 5000`
- `0 <= m <= 20000`
- `0 <= c <= 10^9`
- `0 <= s, t < n`, `s != t`

## Example

**Input:**

```
4 4 0 3
0 1 10
0 2 5
1 3 7
2 3 8
```

**Output:**

```
12
```

**Explanation:**

The maximum flow sends 7 through node 1 and 5 through node 2.

![Example Visualization](../images/AGR-011/example-1.png)

## Notes

- Capacity scaling improves performance on large capacities.
- Use 64-bit integers for flow values.
- Dinic still works without scaling; scaling is an optimization.

## Related Topics

Max Flow, Dinic, Capacity Scaling

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long maxFlow(int n, int m, int s, int t, int[][] edges) {
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
        int n = Integer.parseInt(parts[0]);
        int m = Integer.parseInt(parts[1]);
        int s = Integer.parseInt(parts[2]);
        int t = Integer.parseInt(parts[3]);

        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            line = br.readLine();
            if (line == null) break;
            parts = line.trim().split("\\s+");
            edges[i][0] = Integer.parseInt(parts[0]);
            edges[i][1] = Integer.parseInt(parts[1]);
            edges[i][2] = Integer.parseInt(parts[2]);
        }

        Solution sol = new Solution();
        System.out.println(sol.maxFlow(n, m, s, t, edges));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_flow(self, n, m, s, t, edges):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        s = int(next(iterator))
        t = int(next(iterator))

        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            c = int(next(iterator))
            edges.append([u, v, c])

    except StopIteration:
        pass

    sol = Solution()
    print(sol.max_flow(n, m, s, t, edges))

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
    long long maxFlow(int n, int m, int s, int t, vector<vector<int>>& edges) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;

    vector<vector<int>> edges(m, vector<int>(3));
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution sol;
    cout << sol.maxFlow(n, m, s, t, edges) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxFlow(n, m, s, t, edges) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 4) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }

  const n = readInt();
  const m = readInt();
  const s = readInt();
  const t = readInt();

  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = readInt();
    const v = readInt();
    const c = readInt();
    edges.push([u, v, c]);
  }

  const sol = new Solution();
  console.log(sol.maxFlow(n, m, s, t, edges));
}

solve();
```
