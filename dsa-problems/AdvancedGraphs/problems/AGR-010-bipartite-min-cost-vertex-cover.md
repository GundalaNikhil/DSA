---
problem_id: AGR_BIPARTITE_MIN_COST_VERTEX_COVER__3406
display_id: AGR-010
slug: bipartite-min-cost-vertex-cover
title: "Minimum Cost Vertex Cover in Bipartite Graph"
difficulty: Medium
difficulty_score: 56
topics:
  - Graphs
  - Vertex Cover
  - Min Cut
tags:
  - advanced-graphs
  - vertex-cover
  - min-cut
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-010: Minimum Cost Vertex Cover in Bipartite Graph

## Problem Statement

You are given a bipartite graph with left part `U` and right part `V`. Each vertex has a non-negative weight. Find the minimum total weight vertex cover.

A vertex cover is a set of vertices such that every edge has at least one endpoint in the set.

![Problem Illustration](../images/AGR-010/problem-illustration.png)

## Input Format

- First line: integers `nU`, `nV`, and `m`
- Second line: `nU` integers, weights for `U`
- Third line: `nV` integers, weights for `V`
- Next `m` lines: `u v` describing an edge between `u` in `U` and `v` in `V`

## Output Format

- Single integer: minimum total weight of a vertex cover

## Constraints

- `1 <= nU + nV <= 100000`
- `0 <= m <= 200000`
- `0 <= weight <= 10^9`
- `0 <= u < nU`, `0 <= v < nV`

## Example

**Input:**

```
2 2 3
3 1
2 2
0 0
1 0
1 1
```

**Output:**

```
3
```

**Explanation:**

Choosing `U1` (weight 1) and `V0` (weight 2) covers all edges with total weight 3.

![Example Visualization](../images/AGR-010/example-1.png)

## Notes

- Reduce to a min-cut: source->U edges with capacity weight, V->sink edges with capacity weight, U->V edges with capacity INF.
- The minimum cut value equals the minimum vertex cover weight (Kőnig's theorem).
- Use 64-bit integers for capacities.

## Related Topics

Vertex Cover, Min Cut, Bipartite Graphs

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long minCostVertexCover(int nU, int nV, int m, int[] weightU, int[] weightV, int[][] edges) {
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
        int nU = Integer.parseInt(parts[0]);
        int nV = Integer.parseInt(parts[1]);
        int m = Integer.parseInt(parts[2]);

        int[] weightU = new int[nU];
        line = br.readLine();
        if (line != null) {
            parts = line.trim().split("\\s+");
            for (int i = 0; i < nU; i++) {
                weightU[i] = Integer.parseInt(parts[i]);
            }
        }

        int[] weightV = new int[nV];
        line = br.readLine();
        if (line != null) {
            parts = line.trim().split("\\s+");
            for (int i = 0; i < nV; i++) {
                weightV[i] = Integer.parseInt(parts[i]);
            }
        }

        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            line = br.readLine();
            if (line == null) break;
            parts = line.trim().split("\\s+");
            edges[i][0] = Integer.parseInt(parts[0]);
            edges[i][1] = Integer.parseInt(parts[1]);
        }

        Solution sol = new Solution();
        System.out.println(sol.minCostVertexCover(nU, nV, m, weightU, weightV, edges));
    }
}
```

### Python

```python
import sys

class Solution:
    def min_cost_vertex_cover(self, nU, nV, m, weightU, weightV, edges):
        # Implement here
        return 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        nU = int(next(iterator))
        nV = int(next(iterator))
        m = int(next(iterator))

        weightU = []
        for _ in range(nU):
            weightU.append(int(next(iterator)))

        weightV = []
        for _ in range(nV):
            weightV.append(int(next(iterator)))

        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

    except StopIteration:
        pass

    sol = Solution()
    print(sol.min_cost_vertex_cover(nU, nV, m, weightU, weightV, edges))

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
    long long minCostVertexCover(int nU, int nV, int m, vector<int>& weightU, vector<int>& weightV, vector<vector<int>>& edges) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int nU, nV, m;
    if (!(cin >> nU >> nV >> m)) return 0;

    vector<int> weightU(nU);
    for (int i = 0; i < nU; i++) cin >> weightU[i];

    vector<int> weightV(nV);
    for (int i = 0; i < nV; i++) cin >> weightV[i];

    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution sol;
    cout << sol.minCostVertexCover(nU, nV, m, weightU, weightV, edges) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  minCostVertexCover(nU, nV, m, weightU, weightV, edges) {
    // Implement here
    return 0;
  }
}

function solve() {
  const input = fs.readFileSync(0, "utf8").split(/\s+/);
  if (input.length < 3) return;

  let idx = 0;
  function readInt() {
    return parseInt(input[idx++]);
  }

  const nU = readInt();
  const nV = readInt();
  const m = readInt();

  const weightU = [];
  for (let i = 0; i < nU; i++) weightU.push(readInt());

  const weightV = [];
  for (let i = 0; i < nV; i++) weightV.push(readInt());

  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = readInt();
    const v = readInt();
    edges.push([u, v]);
  }

  const sol = new Solution();
  console.log(sol.minCostVertexCover(nU, nV, m, weightU, weightV, edges));
}

solve();
```
