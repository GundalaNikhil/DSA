---
problem_id: AGR_SCC_COMPRESSION__2659
display_id: AGR-008
slug: scc-compression
title: "Strongly Connected Components Compression"
difficulty: Easy
difficulty_score: 40
topics:
  - Graphs
  - SCC
  - Condensation Graph
tags:
  - advanced-graphs
  - scc
  - condensation
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-008: Strongly Connected Components Compression

## Problem Statement

Find the strongly connected components (SCCs) of a directed graph and build the condensation DAG where each SCC is contracted into a single node.

![Problem Illustration](../images/AGR-008/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` describing a directed edge `u -> v`

## Output Format

- Line 1: integer `k`, number of SCCs
- Line 2: `n` integers `comp[i]` in `[0, k-1]`
- Line 3: integer `e`, number of edges in the condensation DAG
- Next `e` lines: `a b` for each edge `a -> b` between SCCs

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
3 3
0 1
1 0
1 2
```

**Output:**

```
2
0 0 1
1
0 1
```

**Explanation:**

Nodes {0,1} are one SCC, node {2} is another. The condensation graph has one edge.

![Example Visualization](../images/AGR-008/example-1.png)

## Notes

- Use Kosaraju or Tarjan to compute SCCs.
- Avoid duplicate edges in the condensation DAG.
- Any valid component labeling is accepted.

## Related Topics

SCC, Tarjan, Condensation Graph

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    static class Result {
        int numSCC;
        int[] components;
        List<int[]> dagEdges;
        Result(int k, int[] c, List<int[]> e) {
            this.numSCC = k;
            this.components = c;
            this.dagEdges = e;
        }
    }

    public Result solveSCC(int n, int m, int[][] edges) {
        // Implement here
        return new Result(0, new int[0], new ArrayList<>());
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
        Solution.Result res = sol.solveSCC(n, m, edges);

        System.out.println(res.numSCC);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(res.components[i]).append(i == n - 1 ? "" : " ");
        }
        System.out.println(sb);

        System.out.println(res.dagEdges.size());
        for (int[] e : res.dagEdges) {
            System.out.println(e[0] + " " + e[1]);
        }
    }
}
```

### Python

```python
import sys

# Increase recursion depth for deep DFS
sys.setrecursionlimit(200005)

class Solution:
    def solve_scc(self, n, m, edges):
        # Implement here
        return 0, [], []

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
    num_scc, components, dag_edges = sol.solve_scc(n, m, edges)

    print(num_scc)
    print(*(components))
    print(len(dag_edges))
    for u, v in dag_edges:
        print(f"{u} {v}")

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
    int numSCC;
    vector<int> components;
    vector<pair<int, int>> dagEdges;
};

class Solution {
public:
    Result solveSCC(int n, int m, vector<vector<int>>& edges) {
        // Implement here
        return {0, {}, {}};
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
    Result res = sol.solveSCC(n, m, edges);

    cout << res.numSCC << endl;
    for (int i = 0; i < n; i++) {
        cout << res.components[i] << (i == n - 1 ? "" : " ");
    }
    cout << endl;

    cout << res.dagEdges.size() << endl;
    for (const auto& e : res.dagEdges) {
        cout << e.first << " " << e.second << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  solveSCC(n, m, edges) {
    // Implement here
    return { numSCC: 0, components: [], dagEdges: [] };
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
  const res = sol.solveSCC(n, m, edges);

  console.log(res.numSCC);
  console.log(res.components.join(" "));
  console.log(res.dagEdges.length);
  res.dagEdges.forEach((e) => console.log(`${e[0]} ${e[1]}`));
}

solve();
```
