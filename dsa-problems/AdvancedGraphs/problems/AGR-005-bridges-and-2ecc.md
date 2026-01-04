---
problem_id: AGR_BRIDGES_AND_2ECC__3471
display_id: AGR-005
slug: bridges-and-2ecc
title: "Bridges and 2-Edge-Connected Components"
difficulty: Medium
difficulty_score: 54
topics:
  - Graphs
  - Bridges
  - Components
tags:
  - advanced-graphs
  - bridges
  - components
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-005: Bridges and 2-Edge-Connected Components

## Problem Statement

Given an undirected graph, find all bridges and compute the 2-edge-connected components (2ECCs). A 2ECC is a maximal set of nodes that stays connected after removing any single edge.
![Problem Illustration](../images/AGR-005/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` describing an undirected edge

## Output Format

- Line 1: integer `b`, number of bridges
- Next `b` lines: each bridge edge `u v` in input order
- Last line: `n` integers `comp[i]` (1-based component id)

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
4 4
0 1
1 2
2 0
2 3
```

**Output:**

```
1
2 3
1 1 1 2
```

**Explanation:**
Edge (2,3) is a bridge. Nodes {0,1,2} form one 2ECC, node {3} is another.
![Example Visualization](../images/AGR-005/example-1.png)

## Notes

- Use DFS low-link to detect bridges.
- Build components by unioning all non-bridge edges.
- Output bridge edges in their input order.

## Related Topics

## Bridges, 2-Edge-Connected Components, DFS

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    static class Result {
        List<int[]> bridges;
        int[] components;
        Result(List<int[]> b, int[] c) {
            this.bridges = b;
            this.components = c;
        }
    }

    public Result solveGraph(int n, int m, int[][] edges) {
        // Implement here
        return new Result(new ArrayList<>(), new int[0]);
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

        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            line = br.readLine();
            if (line == null) break;
            parts = line.trim().split("\\s+");
            edges[i][0] = Integer.parseInt(parts[0]);
            edges[i][1] = Integer.parseInt(parts[1]);
        }

        Solution sol = new Solution();
        Solution.Result res = sol.solveGraph(n, m, edges);

        System.out.println(res.bridges.size());
        for (int[] b : res.bridges) {
            System.out.println(b[0] + " " + b[1]);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(res.components[i]).append(i == n - 1 ? "" : " ");
        }
        System.out.println(sb);
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep DFS
sys.setrecursionlimit(200005)

class Solution:
    def solve_graph(self, n, m, edges):
        # Implement here
        return [], []

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

    except StopIteration:
        pass

    sol = Solution()
    bridges, components = sol.solve_graph(n, m, edges)

    print(len(bridges))
    for u, v in bridges:
        print(f"{u} {v}")

    print(*(components))

if __name__ == "__main__":
    solve()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Result {
    vector<pair<int, int>> bridges;
    vector<int> components;
};

class Solution {
public:
    Result solveGraph(int n, int m, vector<vector<int>>& edges) {
        // Implement here
        return {{}, {}};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution sol;
    Result res = sol.solveGraph(n, m, edges);

    cout << res.bridges.size() << endl;
    for (const auto& p : res.bridges) {
        cout << p.first << " " << p.second << endl;
    }

    for (int i = 0; i < n; i++) {
        cout << res.components[i] << (i == n - 1 ? "" : " ");
    }
    cout << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  solveGraph(n, m, edges) {
    // Implement here
    return { bridges: [], components: [] };
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 2) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }

  const n = readInt();
  const m = readInt();
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = readInt();
    const v = readInt();
    edges.push([u, v]);
  }

  const sol = new Solution();
  const res = sol.solveGraph(n, m, edges);

  console.log(res.bridges.length);
  res.bridges.forEach((b) => console.log(`${b[0]} ${b[1]}`));
  console.log(res.components.join(" "));
}

solve();
```
