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
        // Implementation here
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt(), m = sc.nextInt();
        long[] b = new long[n];
        for (int i = 0; i < n; i++) b[i] = sc.nextLong();
        int[][] edges = new int[m][5];
        for (int i = 0; i < m; i++) { for (int j = 0; j < 5; j++) edges[i][j] = sc.nextInt(); }
        Long ans = new Solution().minCostFlow(n, b, edges);
        System.out.print(ans == null ? "INFEASIBLE" : "FEASIBLE\n" + ans);
        sc.close();
    }
}
```

### Python

```python
import sys

def min_cost_flow(n: int, b: list[int], edges: list[tuple[int, int, int, int, int]]):
    # Implementation here
    return None

def main():
    data = sys.stdin.read().split()
    if not data: return
    it = iter(data)
    n, m = int(next(it)), int(next(it))
    b = [int(next(it)) for _ in range(n)]
    edges = [(int(next(it)), int(next(it)), int(next(it)), int(next(it)), int(next(it))) for _ in range(m)]
    ans = min_cost_flow(n, b, edges)
    print("INFEASIBLE" if ans is None else f"FEASIBLE\n{ans}")

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    pair<bool, long long> minCostFlow(int n, const vector<long long>& b, const vector<array<int, 5>>& edges) {
        // Implementation here
        return {false, 0};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<long long> b(n);
    for (int i = 0; i < n; i++) cin >> b[i];
    vector<array<int, 5>> edges(m);
    for (int i = 0; i < m; i++) for (int j = 0; j < 5; j++) cin >> edges[i][j];
    auto [ok, ans] = Solution().minCostFlow(n, b, edges);
    cout << (ok ? "FEASIBLE\n" + to_string(ans) : "INFEASIBLE");
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minCostFlow(n, b, edges) {
    /* Implementation */ return null;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});
let data = [];
rl.on("line", (line) => {
  for (const p of line.trim().split(/\s+/)) if (p) data.push(p);
});
rl.on("close", () => {
  let idx = 0;
  const n = parseInt(data[idx++], 10),
    m = parseInt(data[idx++], 10);
  const b = [];
  for (let i = 0; i < n; i++) b.push(parseInt(data[idx++], 10));
  const edges = [];
  for (let i = 0; i < m; i++)
    edges.push([
      parseInt(data[idx++], 10),
      parseInt(data[idx++], 10),
      parseInt(data[idx++], 10),
      parseInt(data[idx++], 10),
      parseInt(data[idx++], 10),
    ]);
  const ans = new Solution().minCostFlow(n, b, edges);
  console.log(ans === null ? "INFEASIBLE" : `FEASIBLE\n${ans}`);
});
```
