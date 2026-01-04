---
problem_id: AGR_ARTICULATION_AND_BCC__7358
display_id: AGR-006
slug: articulation-and-bcc
title: "Articulation Points and Biconnected Components"
difficulty: Medium
difficulty_score: 60
topics:
  - Graphs
  - Articulation Points
  - Biconnected Components
tags:
  - advanced-graphs
  - articulation-points
  - bcc
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-006: Articulation Points and Biconnected Components

## Problem Statement

Given an undirected graph, find all articulation points and all vertex-biconnected components (BCCs).
A BCC is a maximal set of vertices that remains connected after removing any single vertex from the set.
![Problem Illustration](../images/AGR-006/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` describing an undirected edge

## Output Format

- Line 1: integer `a`, number of articulation points
- Line 2: `a` integers of articulation points in increasing order (or empty line)
- Line 3: integer `b`, number of biconnected components
- Next `b` lines: each BCC as `k v1 v2 ... vk` (vertices in any order)

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
1 3
```

**Output:**

```
1
1
2
3 0 1 2
2 1 3
```

**Explanation:**
Node 1 is an articulation point. The BCCs are {0,1,2} and {1,3}.
![Example Visualization](../images/AGR-006/example-1.png)

## Notes

- Use Tarjan's algorithm with an edge stack to extract BCCs.
- The order of BCCs and vertex order inside each component does not matter.
- The graph may be disconnected.

## Related Topics

## Articulation Points, Biconnected Components, DFS

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    static class Result {
        List<Integer> articulationPoints;
        List<List<Integer>> bccs;

        Result(List<Integer> a, List<List<Integer>> b) {
            this.articulationPoints = a;
            this.bccs = b;
        }
    }

    public Result solveGraph(int n, int m, int[][] edges) {
        // Implement here
        return new Result(new ArrayList<>(), new ArrayList<>());
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

        System.out.println(res.articulationPoints.size());
        StringBuilder sbAP = new StringBuilder();
        for (int i = 0; i < res.articulationPoints.size(); i++) {
            sbAP.append(res.articulationPoints.get(i)).append(i == res.articulationPoints.size() - 1 ? "" : " ");
        }
        System.out.println(sbAP);

        System.out.println(res.bccs.size());
        for (List<Integer> bcc : res.bccs) {
            StringBuilder sbBCC = new StringBuilder();
            sbBCC.append(bcc.size());
            for (int u : bcc) {
                sbBCC.append(" ").append(u);
            }
            System.out.println(sbBCC);
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
    art_points, bccs = sol.solve_graph(n, m, edges)

    print(len(art_points))
    print(*(art_points))

    print(len(bccs))
    for bcc in bccs:
        print(len(bcc), end=" ")
        print(*(bcc))

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
    vector<int> articulationPoints;
    vector<vector<int>> bccs;
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

    cout << res.articulationPoints.size() << endl;
    for (int i = 0; i < res.articulationPoints.size(); i++) {
        cout << res.articulationPoints[i] << (i == res.articulationPoints.size() - 1 ? "" : " ");
    }
    cout << endl;

    cout << res.bccs.size() << endl;
    for (const auto& bcc : res.bccs) {
        cout << bcc.size();
        for (int u : bcc) {
            cout << " " << u;
        }
        cout << endl;
    }

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
    return { articulationPoints: [], bccs: [] };
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

  console.log(res.articulationPoints.length);
  console.log(res.articulationPoints.join(" "));

  console.log(res.bccs.length);
  res.bccs.forEach((bcc) => {
    console.log(bcc.length + " " + bcc.join(" "));
  });
}

solve();
```
