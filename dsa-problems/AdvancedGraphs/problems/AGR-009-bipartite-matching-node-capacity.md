---
problem_id: AGR_BIPARTITE_MATCHING_NODE_CAPACITY__8194
display_id: AGR-009
slug: bipartite-matching-node-capacity
title: "Maximum Matching with Node Capacities"
difficulty: Medium
difficulty_score: 58
topics:
  - Graphs
  - Bipartite Matching
  - Max Flow
tags:
  - advanced-graphs
  - bipartite-matching
  - max-flow
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-009: Maximum Matching with Node Capacities

## Problem Statement

You are given a bipartite graph with left part `U` and right part `V`. Each node `u` in `U` has capacity `capU[u]` (maximum number of matches it can take), and each node `v` in `V` has capacity `capV[v]`.

Find the maximum matching size respecting these capacities.

![Problem Illustration](../images/AGR-009/problem-illustration.png)

## Input Format

- First line: integers `nU`, `nV`, and `m`
- Second line: `nU` integers `capU`
- Third line: `nV` integers `capV`
- Next `m` lines: `u v` describing an edge from `u` in `U` to `v` in `V`

## Output Format

- Single integer: maximum feasible matching size

## Constraints

- `1 <= nU + nV <= 100000`
- `0 <= m <= 200000`
- `0 <= capU[i], capV[j] <= 10^9`
- `0 <= u < nU`, `0 <= v < nV`

## Example

**Input:**

```
2 2 3
1 2
1 1
0 0
1 0
1 1
```

**Output:**

```
2
```

**Explanation:**

The capacities limit the matching to size 2.

![Example Visualization](../images/AGR-009/example-1.png)

## Notes

- Convert to a flow network with source->U capacities, V->sink capacities, and edges U->V with capacity 1.
- Use Dinic for efficiency.
- Use 64-bit integers for flow values.

## Related Topics

Bipartite Matching, Max Flow, Capacity Constraints

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    public long maxMatchingWithCap(int nU, int nV, int m, int[] capU, int[] capV, int[][] edges) {
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

        int[] capU = new int[nU];
        line = br.readLine();
        if (line != null) {
            parts = line.trim().split("\\s+");
            for (int i = 0; i < nU; i++) {
                capU[i] = Integer.parseInt(parts[i]);
            }
        }

        int[] capV = new int[nV];
        line = br.readLine();
        if (line != null) {
            parts = line.trim().split("\\s+");
            for (int i = 0; i < nV; i++) {
                capV[i] = Integer.parseInt(parts[i]);
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
        System.out.println(sol.maxMatchingWithCap(nU, nV, m, capU, capV, edges));
    }
}
```

### Python

```python
import sys

class Solution:
    def max_matching_with_cap(self, nU, nV, m, capU, capV, edges):
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

        capU = []
        for _ in range(nU):
            capU.append(int(next(iterator)))

        capV = []
        for _ in range(nV):
            capV.append(int(next(iterator)))

        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append([u, v])

    except StopIteration:
        pass

    sol = Solution()
    print(sol.max_matching_with_cap(nU, nV, m, capU, capV, edges))

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
    long long maxMatchingWithCap(int nU, int nV, int m, vector<int>& capU, vector<int>& capV, vector<vector<int>>& edges) {
        // Implement here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int nU, nV, m;
    if (!(cin >> nU >> nV >> m)) return 0;

    vector<int> capU(nU);
    for (int i = 0; i < nU; i++) cin >> capU[i];

    vector<int> capV(nV);
    for (int i = 0; i < nV; i++) cin >> capV[i];

    vector<vector<int>> edges(m, vector<int>(2));
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1];
    }

    Solution sol;
    cout << sol.maxMatchingWithCap(nU, nV, m, capU, capV, edges) << endl;

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  maxMatchingWithCap(nU, nV, m, capU, capV, edges) {
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

  const capU = [];
  for (let i = 0; i < nU; i++) capU.push(readInt());

  const capV = [];
  for (let i = 0; i < nV; i++) capV.push(readInt());

  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = readInt();
    const v = readInt();
    edges.push([u, v]);
  }

  const sol = new Solution();
  console.log(sol.maxMatchingWithCap(nU, nV, m, capU, capV, edges));
}

solve();
```
