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

class Solution {
    public Long minCostFlow(int n, long[] b, int[][] edges) {
        // Your implementation here
        return null;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        long[] b = new long[n];
        for (int i = 0; i < n; i++) b[i] = sc.nextLong();
        int[][] edges = new int[m][5];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
            edges[i][3] = sc.nextInt();
            edges[i][4] = sc.nextInt();
        }

        Solution solution = new Solution();
        Long ans = solution.minCostFlow(n, b, edges);
        if (ans == null) {
            System.out.print("INFEASIBLE");
        } else {
            System.out.print("FEASIBLE\n" + ans);
        }
        sc.close();
    }
}
```

### Python

```python
def min_cost_flow(n: int, b: list[int], edges: list[tuple[int, int, int, int, int]]):
    # Your implementation here
    return None

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    b = [int(next(it)) for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it)); low = int(next(it)); high = int(next(it)); cost = int(next(it))
        edges.append((u, v, low, high, cost))
    ans = min_cost_flow(n, b, edges)
    if ans is None:
        sys.stdout.write("INFEASIBLE")
    else:
        sys.stdout.write("FEASIBLE\n" + str(ans))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <array>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool minCostFlow(int n, const vector<long long>& b, const vector<array<int, 5>>& edges, long long& cost) {
        // Your implementation here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> b(n);
    for (int i = 0; i < n; i++) cin >> b[i];
    vector<array<int, 5>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2] >> edges[i][3] >> edges[i][4];
    }

    Solution solution;
    long long cost = 0;
    bool ok = solution.minCostFlow(n, b, edges, cost);
    if (!ok) {
        cout << "INFEASIBLE";
    } else {
        cout << "FEASIBLE\n" << cost;
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minCostFlow(n, b, edges) {
    // Your implementation here
    return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => data.push(...line.trim().split(/\s+/)));
rl.on("close", () => {
  if (data.length === 0) return;
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const b = new Array(n);
  for (let i = 0; i < n; i++) b[i] = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const low = parseInt(data[idx++], 10);
    const high = parseInt(data[idx++], 10);
    const cost = parseInt(data[idx++], 10);
    edges.push([u, v, low, high, cost]);
  }

  const solution = new Solution();
  const ans = solution.minCostFlow(n, b, edges);
  if (ans === null) {
    console.log("INFEASIBLE");
  } else {
    console.log("FEASIBLE");
    console.log(ans.toString());
  }
});
```
