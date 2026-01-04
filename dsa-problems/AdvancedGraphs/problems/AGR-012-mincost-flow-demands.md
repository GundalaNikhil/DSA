---
problem_id: AGR_MINCOST_FLOW_DEMANDS__7702
display_id: AGR-012
slug: mincost-flow-demands
title: "Minimum-Cost Flow With Demands"
difficulty: Hard
difficulty_score: 70
topics:
  - Graphs
  - Min-Cost Flow
  - Circulation
tags:
  - advanced-graphs
  - min-cost-flow
  - demands
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-012: Minimum-Cost Flow With Demands

## Problem Statement

You are given a directed graph with lower and upper bounds on edges and a supply/demand value at each node. Find a feasible circulation that satisfies all demands and minimizes total cost.

If no feasible flow exists, output `INFEASIBLE`.

![Problem Illustration](../images/AGR-012/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Second line: `n` integers `b[i]` (positive = supply, negative = demand)
- Next `m` lines: `u v low high cost` for edge `u -> v`

## Output Format

- If infeasible: print `INFEASIBLE`
- Otherwise: print `FEASIBLE` and a line with the minimum total cost

## Constraints

- `1 <= n <= 500`
- `0 <= m <= 2000`
- `-10^9 <= b[i] <= 10^9`
- `0 <= low <= high <= 10^9`
- `-10^6 <= cost <= 10^6`

## Example

**Input:**

```
2 1
5 -5
0 1 2 5 1
```

**Output:**

```
FEASIBLE
5
```

**Explanation:**

Send 5 units from 0 to 1. Total cost is 5.

![Example Visualization](../images/AGR-012/example-1.png)

## Notes

- Convert to circulation with a super source and super sink.
- Use potentials and Dijkstra/SPFA for min-cost max-flow.
- Use 64-bit integers for costs and flows.

## Related Topics

Min-Cost Flow, Circulation, Potentials

---

## Solution Template

### Java

```java
import java.util.*;
import java.io.*;

class Solution {
    static class Result {
        boolean feasible;
        long minCost;
        Result(boolean f, long c) {
            this.feasible = f;
            this.minCost = c;
        }
    }

    public Result solveMinCostFlow(int n, int m, int[] b, int[][] edges) {
        // Implement here
        return new Result(false, 0);
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

        int[] b = new int[n];
        line = br.readLine();
        if (line != null) {
            parts = line.trim().split("\\s+");
            for (int i = 0; i < n; i++) {
                b[i] = Integer.parseInt(parts[i]);
            }
        }

        int[][] edges = new int[m][5];
        for (int i = 0; i < m; i++) {
            line = br.readLine();
            if (line == null) break;
            parts = line.trim().split("\\s+");
            edges[i][0] = Integer.parseInt(parts[0]);
            edges[i][1] = Integer.parseInt(parts[1]);
            edges[i][2] = Integer.parseInt(parts[2]);
            edges[i][3] = Integer.parseInt(parts[3]);
            edges[i][4] = Integer.parseInt(parts[4]);
        }

        Solution sol = new Solution();
        Solution.Result res = sol.solveMinCostFlow(n, m, b, edges);

        if (!res.feasible) {
            System.out.println("INFEASIBLE");
        } else {
            System.out.println("FEASIBLE");
            System.out.println(res.minCost);
        }
    }
}
```

### Python

```python
import sys

class Solution:
    def solve_min_cost_flow(self, n, m, b, edges):
        # Implement here
        return False, 0

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))

        b = []
        for _ in range(n):
            b.append(int(next(iterator)))

        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            low = int(next(iterator))
            high = int(next(iterator))
            cost = int(next(iterator))
            edges.append([u, v, low, high, cost])

    except StopIteration:
        pass

    sol = Solution()
    feasible, min_cost = sol.solve_min_cost_flow(n, m, b, edges)

    if not feasible:
        print("INFEASIBLE")
    else:
        print("FEASIBLE")
        print(min_cost)

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
    bool feasible;
    long long minCost;
};

class Solution {
public:
    Result solveMinCostFlow(int n, int m, vector<int>& b, vector<vector<int>>& edges) {
        // Implement here
        return {false, 0};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<int> b(n);
    for (int i = 0; i < n; i++) cin >> b[i];

    vector<vector<int>> edges(m, vector<int>(5));
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2] >> edges[i][3] >> edges[i][4];
    }

    Solution sol;
    Result res = sol.solveMinCostFlow(n, m, b, edges);

    if (!res.feasible) {
        cout << "INFEASIBLE" << endl;
    } else {
        cout << "FEASIBLE" << endl;
        cout << res.minCost << endl;
    }

    return 0;
}
```

### JavaScript

```javascript
"use strict";

const fs = require("fs");

class Solution {
  solveMinCostFlow(n, m, b, edges) {
    // Implement here
    return { feasible: false, minCost: 0 };
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

  const b = [];
  for (let i = 0; i < n; i++) b.push(readInt());

  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = readInt();
    const v = readInt();
    const low = readInt();
    const high = readInt();
    const cost = readInt();
    edges.push([u, v, low, high, cost]);
  }

  const sol = new Solution();
  const res = sol.solveMinCostFlow(n, m, b, edges);

  if (!res.feasible) {
    console.log("INFEASIBLE");
  } else {
    console.log("FEASIBLE");
    console.log(res.minCost);
  }
}

solve();
```
