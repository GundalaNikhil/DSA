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

class Solution {
    public long minVertexCoverCost(int nU, int nV, long[] wU, long[] wV, int[][] edges) {
        // Implementation here
        return 0;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int nU = sc.nextInt();
        int nV = sc.nextInt();
        int m = sc.nextInt();
        long[] wU = new long[nU];
        long[] wV = new long[nV];
        for (int i = 0; i < nU; i++) wU[i] = sc.nextLong();
        for (int i = 0; i < nV; i++) wV[i] = sc.nextLong();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) { edges[i][0] = sc.nextInt(); edges[i][1] = sc.nextInt(); }
        Solution solution = new Solution();
        System.out.println(solution.minVertexCoverCost(nU, nV, wU, wV, edges));
        sc.close();
    }
}
```

### Python

```python
import sys

def min_vertex_cover_cost(nU: int, nV: int, wU: list[int], wV: list[int], edges: list[tuple[int, int]]) -> int:
    # Implementation here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data: return
    it = iter(data)
    nU, nV, m = int(next(it)), int(next(it)), int(next(it))
    wU = [int(next(it)) for _ in range(nU)]
    wV = [int(next(it)) for _ in range(nV)]
    edges = [(int(next(it)), int(next(it))) for _ in range(m)]
    print(min_vertex_cover_cost(nU, nV, wU, wV, edges))

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
    long long minVertexCoverCost(int nU, int nV, const vector<long long>& wU, const vector<long long>& wV, const vector<pair<int,int>>& edges) {
        // Implementation here
        return 0;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int nU, nV, m;
    if (!(cin >> nU >> nV >> m)) return 0;
    vector<long long> wU(nU), wV(nV);
    for (int i = 0; i < nU; i++) cin >> wU[i];
    for (int i = 0; i < nV; i++) cin >> wV[i];
    vector<pair<int,int>> edges(m);
    for (int i = 0; i < m; i++) cin >> edges[i].first >> edges[i].second;
    Solution solution;
    cout << solution.minVertexCoverCost(nU, nV, wU, wV, edges) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  minVertexCoverCost(nU, nV, wU, wV, edges) {
    /* Implementation */ return 0;
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
  const nU = parseInt(data[idx++], 10),
    nV = parseInt(data[idx++], 10),
    m = parseInt(data[idx++], 10);
  const wU = [];
  for (let i = 0; i < nU; i++) wU.push(parseInt(data[idx++], 10));
  const wV = [];
  for (let i = 0; i < nV; i++) wV.push(parseInt(data[idx++], 10));
  const edges = [];
  for (let i = 0; i < m; i++)
    edges.push([parseInt(data[idx++], 10), parseInt(data[idx++], 10)]);
  console.log(
    new Solution().minVertexCoverCost(nU, nV, wU, wV, edges).toString()
  );
});
```
