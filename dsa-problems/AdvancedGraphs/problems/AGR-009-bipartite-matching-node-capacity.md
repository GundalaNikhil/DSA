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

class Solution {
    public long maxMatching(int nU, int nV, int[] capU, int[] capV, int[][] edges) {
        // Your implementation here
        return 0L;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int nU = sc.nextInt();
        int nV = sc.nextInt();
        int m = sc.nextInt();
        int[] capU = new int[nU];
        int[] capV = new int[nV];
        for (int i = 0; i < nU; i++) capU[i] = sc.nextInt();
        for (int i = 0; i < nV; i++) capV[i] = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxMatching(nU, nV, capU, capV, edges));
        sc.close();
    }
}
```

### Python

```python
def max_matching(nU: int, nV: int, capU: list[int], capV: list[int], edges: list[tuple[int, int]]) -> int:
    # Your implementation here
    return 0

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    nU = int(next(it)); nV = int(next(it)); m = int(next(it))
    capU = [int(next(it)) for _ in range(nU)]
    capV = [int(next(it)) for _ in range(nV)]
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        edges.append((u, v))
    print(max_matching(nU, nV, capU, capV, edges))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    long long maxMatching(int nU, int nV, const vector<int>& capU,
                          const vector<int>& capV, const vector<pair<int, int>>& edges) {
        // Your implementation here
        return 0LL;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int nU, nV, m;
    if (!(cin >> nU >> nV >> m)) return 0;
    vector<int> capU(nU), capV(nV);
    for (int i = 0; i < nU; i++) cin >> capU[i];
    for (int i = 0; i < nV; i++) cin >> capV[i];
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution solution;
    cout << solution.maxMatching(nU, nV, capU, capV, edges) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxMatching(nU, nV, capU, capV, edges) {
    // Your implementation here
    return 0;
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
  const nU = parseInt(data[idx++], 10);
  const nV = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const capU = new Array(nU);
  const capV = new Array(nV);
  for (let i = 0; i < nU; i++) capU[i] = parseInt(data[idx++], 10);
  for (let i = 0; i < nV; i++) capV[i] = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.maxMatching(nU, nV, capU, capV, edges).toString());
});
```
