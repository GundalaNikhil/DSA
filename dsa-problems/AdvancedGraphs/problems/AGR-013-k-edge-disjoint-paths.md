---
problem_id: AGR_K_EDGE_DISJOINT_PATHS__2167
display_id: AGR-013
slug: k-edge-disjoint-paths
title: "K-Edge-Disjoint Paths"
difficulty: Hard
difficulty_score: 68
topics:
  - Graphs
  - Max Flow
  - Disjoint Paths
tags:
  - advanced-graphs
  - disjoint-paths
  - max-flow
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---

# AGR-013: K-Edge-Disjoint Paths

## Problem Statement

Given a directed graph, determine whether there exist at least `k` edge-disjoint paths from `s` to `t`.

![Problem Illustration](../images/AGR-013/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, `s`, `t`, `k`
- Next `m` lines: `u v` describing a directed edge `u -> v`

## Output Format

- Print `YES` if at least `k` edge-disjoint paths exist, otherwise `NO`

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `1 <= k <= 10000`
- `0 <= s, t < n`, `s != t`

## Example

**Input:**

```
4 4 0 3 2
0 1
1 3
0 2
2 3
```

**Output:**

```
YES
```

**Explanation:**

Two edge-disjoint paths exist: 0-1-3 and 0-2-3.

![Example Visualization](../images/AGR-013/example-1.png)

## Notes

- Transform to max flow with unit capacities on edges.
- Answer is YES if max flow >= k.
- Use Dinic for performance on large graphs.

## Related Topics

Edge-Disjoint Paths, Max Flow, Dinic

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public boolean hasKEdgeDisjointPaths(int n, int s, int t, int k, int[][] edges) {
        // Implementation here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt(), m = sc.nextInt(), s = sc.nextInt(), t = sc.nextInt(), k = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) { edges[i][0] = sc.nextInt(); edges[i][1] = sc.nextInt(); }
        System.out.println(new Solution().hasKEdgeDisjointPaths(n, s, t, k, edges) ? "YES" : "NO");
        sc.close();
    }
}
```

### Python

```python
import sys

def has_k_edge_disjoint_paths(n: int, s: int, t: int, k: int, edges: list[tuple[int, int]]) -> bool:
    # Implementation here
    return False

def main():
    data = sys.stdin.read().split()
    if not data: return
    it = iter(data)
    n, m, s, t, k = int(next(it)), int(next(it)), int(next(it)), int(next(it)), int(next(it))
    edges = [(int(next(it)), int(next(it))) for _ in range(m)]
    print("YES" if has_k_edge_disjoint_paths(n, s, t, k, edges) else "NO")

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
    bool hasKEdgeDisjointPaths(int n, int s, int t, int k, const vector<pair<int,int>>& edges) {
        // Implementation here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m, s, t, k;
    if (!(cin >> n >> m >> s >> t >> k)) return 0;
    vector<pair<int,int>> edges(m);
    for (int i = 0; i < m; i++) cin >> edges[i].first >> edges[i].second;
    cout << (Solution().hasKEdgeDisjointPaths(n, s, t, k, edges) ? "YES" : "NO") << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  hasKEdgeDisjointPaths(n, s, t, k, edges) {
    /* Implementation */ return false;
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
    m = parseInt(data[idx++], 10),
    s = parseInt(data[idx++], 10),
    t = parseInt(data[idx++], 10),
    k = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++)
    edges.push([parseInt(data[idx++], 10), parseInt(data[idx++], 10)]);
  console.log(
    new Solution().hasKEdgeDisjointPaths(n, s, t, k, edges) ? "YES" : "NO"
  );
});
```
