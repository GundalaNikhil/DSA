---
problem_id: GRB_BRIDGES_CAPACITY_THRESHOLD__4509
display_id: GRB-011
slug: bridges-capacity-threshold
title: "Bridges With Capacity Threshold"
difficulty: Medium
difficulty_score: 55
topics:
  - Graphs
  - Bridges
  - DFS
tags:
  - graphs-basics
  - bridges
  - dfs
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-011: Bridges With Capacity Threshold

## Problem Statement

You are given an undirected graph where each edge has a capacity `c`. An edge is **critical** if:

1. It is a bridge (removing it increases the number of connected components), and
2. Its capacity is strictly less than a threshold `T`.

Find all such edges.

![Problem Illustration](../images/GRB-011/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, and `T`
- Next `m` lines: `u v c` describing an undirected edge with capacity `c`

## Output Format

- Line 1: integer `k`, number of critical edges
- Next `k` lines: `u v` for each critical edge in the order they appear in input

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `0 <= c <= 10^9`
- `0 <= T <= 10^9`
- `0 <= u, v < n`

## Example

**Input:**

```
4 4 3
0 1 1
1 2 5
2 0 1
1 3 2
```

**Output:**

```
1
1 3
```

**Explanation:**

Edge (1,3) is a bridge and has capacity 2 < 3.

![Example Visualization](../images/GRB-011/example-1.png)

## Notes

- Use DFS low-link to detect bridges.
- The order of output edges must match their input order.
- If no edges qualify, print `0` and nothing else.

## Related Topics

Bridges, DFS, Graph Connectivity

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private int timer;
    private int[] disc, low;
    private List<Integer> criticalIndices;
    
    public List<int[]> criticalEdges(int n, int[][] edges, int T) {
        return null;
    }

    private void dfs(int u, int parentEdgeIdx, List<List<int[]>> adj, int T) {
        disc[u] = low[u] = ++timer;
        
        for (int[] edge : adj.get(u)) {
            int v = edge[0];
            int cap = edge[1];
            int idx = edge[2];
            
            if (idx == parentEdgeIdx) continue; // Don't go back via same edge
            
            if (disc[v] != -1) {
                low[u] = Math.min(low[u], disc[v]);
            } else {
                dfs(v, idx, adj, T);
                low[u] = Math.min(low[u], low[v]);
                
                if (low[v] > disc[u]) {
                    // Bridge found
                    if (cap < T) {
                        criticalIndices.add(idx);
                    }
                }
            }
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int T = sc.nextInt();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<int[]> ans = solution.criticalEdges(n, edges, T);
        StringBuilder sb = new StringBuilder();
        sb.append(ans.size()).append('\n');
        for (int[] e : ans) {
            sb.append(e[0]).append(' ').append(e[1]).append('\n');
        }
        System.out.print(sb.toString().trim());
        sc.close();
    }
}
```

### Python

```python
import sys

sys.setrecursionlimit(200000)

def critical_edges(n: int, edges: list[tuple[int, int, int]], T: int) -> list[tuple[int, int]]:
    return []
def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        T = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            c = int(next(iterator))
            edges.append((u, v, c))
        
        ans = critical_edges(n, edges, T)
        
        out = [str(len(ans))]
        for u, v in ans:
            out.append(f"{u} {v}")
        print("\n".join(out))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <array>

using namespace std;

class Solution {
    int timer;
    vector<int> disc, low;
    vector<int> criticalIndices;
    vector<vector<array<int, 3>>> adj; // {v, cap, idx}

    void dfs(int u, int parentEdgeIdx, int T) {
    }

public:
    vector<pair<int, int>> criticalEdges(int n, const vector<array<int, 3>>& edges, int T) {
        adj.assign(n, vector<array<int, 3>>());
        for (int i = 0; i < edges.size(); i++) {
            if (edges[i][2] < T) {
                adj[edges[i][0]].push_back({edges[i][1], edges[i][2], i});
                adj[edges[i][1]].push_back({edges[i][0], edges[i][2], i});
            }
        }

        disc.assign(n, -1);
        low.assign(n, -1);
        criticalIndices.clear();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (disc[i] == -1) {
                dfs(i, -1, T);
            }
        }

        sort(criticalIndices.begin(), criticalIndices.end());

        vector<pair<int, int>> result;
        for (int idx : criticalIndices) {
            result.push_back({edges[idx][0], edges[idx][1]});
        }
        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, T;
    if (!(cin >> n >> m >> T)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    vector<pair<int, int>> ans = solution.criticalEdges(n, edges, T);
    cout << ans.size() << "\n";
    for (auto& e : ans) {
        cout << e.first << ' ' << e.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  criticalEdges(n, edges, T) {
    return 0;
  }
}

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

let data = [];
rl.on("line", (line) => {
    if (line.trim() !== '') {
        const parts = line.trim().split(/\s+/);
        for(const p of parts) data.push(p);
    }
});

rl.on("close", () => {
  if (data.length === 0) return;
  
  let idx = 0;
  function nextInt() {
      return parseInt(data[idx++], 10);
  }
  
  const n = nextInt();
  const m = nextInt();
  const T = nextInt();
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = nextInt();
    const v = nextInt();
    const c = nextInt();
    edges.push([u, v, c]);
  }

  const solution = new Solution();
  const ans = solution.criticalEdges(n, edges, T);
  console.log(ans.length.toString());
  for(const e of ans) {
      console.log(`${e[0]} ${e[1]}`);
  }
});
```

