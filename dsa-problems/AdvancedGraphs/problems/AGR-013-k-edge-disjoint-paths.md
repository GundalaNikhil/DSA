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
        //Implement here
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        int t = sc.nextInt();
        int k = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.hasKEdgeDisjointPaths(n, s, t, k, edges) ? "YES" : "NO");
        sc.close();
    }
}
```

### Python

```python
import sys

sys.setrecursionlimit(300000)

def has_k_edge_disjoint_paths(n: int, s: int, t: int, k: int, edges: list[tuple[int, int]]) -> bool:
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        s = int(next(iterator))
        t = int(next(iterator))
        k = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))
            
        print("YES" if has_k_edge_disjoint_paths(n, s, t, k, edges) else "NO")
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool hasKEdgeDisjointPaths(int n, int s, int t, int k, const vector<pair<int, int>>& edges) {
        //Implement here
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t, k;
    if (!(cin >> n >> m >> s >> t >> k)) return 0;
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution solution;
    cout << (solution.hasKEdgeDisjointPaths(n, s, t, k, edges) ? "YES" : "NO");
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  hasKEdgeDisjointPaths(n, s, t, k, edges) {
    //Implement here
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let data = [];
rl.on("line", (line) => { const parts = line.trim().split(/\s+/); for (const p of parts) if (p) data.push(p); });
rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  const n = parseInt(data[idx++], 10);
  const m = parseInt(data[idx++], 10);
  const s = parseInt(data[idx++], 10);
  const t = parseInt(data[idx++], 10);
  const k = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }

  const solution = new Solution();
  console.log(solution.hasKEdgeDisjointPaths(n, s, t, k, edges) ? "YES" : "NO");
});
```

