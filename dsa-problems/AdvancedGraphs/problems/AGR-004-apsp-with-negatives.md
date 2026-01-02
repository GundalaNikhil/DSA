---
problem_id: AGR_APSP_WITH_NEGATIVES__6027
display_id: AGR-004
slug: apsp-with-negatives
title: "All-Pairs Shortest Path With Negative Edges"
difficulty: Medium
difficulty_score: 58
topics:
  - Graphs
  - APSP
  - Johnson
tags:
  - advanced-graphs
  - apsp
  - johnson
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-004: All-Pairs Shortest Path With Negative Edges

## Problem Statement

Given a directed weighted graph with no negative cycles, compute the shortest path distance between every pair of nodes.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187669/dsa-problems/AGR-004/problem/nii8p5fuu2xwkypthout.jpg)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v w` describing a directed edge `u -> v` with weight `w`

## Output Format

- Print `n` lines, each with `n` entries
- Use `INF` for unreachable pairs

## Constraints

- `1 <= n <= 2000`
- `0 <= m <= 5000`
- `-10^9 <= w <= 10^9`
- The graph has no negative cycles

## Example

**Input:**

```
3 3
0 1 2
1 2 -1
0 2 4
```

**Output:**

```
0 2 1
INF 0 -1
INF INF 0
```

**Explanation:**

The shortest path from 0 to 2 goes through 1 with total cost 1.

![Example Visualization](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767187671/dsa-problems/AGR-004/problem/mpmwtfgxrk0cjmjldfs0.jpg)

## Notes

- Johnson's algorithm runs Bellman-Ford once, then Dijkstra from each node.
- Use 64-bit integers to avoid overflow.
- `INF` is only for unreachable; negative distances can occur.

## Related Topics

APSP, Johnson, Dijkstra

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class Edge {
        int to;
        long weight;
        Edge(int to, long weight) { this.to = to; this.weight = weight; }
    }

    public long[][] allPairsShortestPaths(int n, int[][] edges) {
        return null;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        long[][] dist = solution.allPairsShortestPaths(n, edges);
        long INF = 1_000_000_000_000_000_000L;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j > 0) sb.append(' ');
                if (dist[i][j] >= INF / 2) sb.append("INF");
                else sb.append(dist[i][j]);
            }
            if (i + 1 < n) sb.append('\n');
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys
import heapq

def all_pairs_shortest_paths(n: int, edges: list[tuple[int, int, int]]) -> list[list[int]]:
    return []
def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    iterator = iter(data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            edges.append((u, v, w))
            
        dist = all_pairs_shortest_paths(n, edges)
        INF = 10**18
        out = []
        for i in range(n):
            row = []
            for x in dist[i]:
                if x >= INF // 2:
                    row.append("INF")
                else:
                    row.append(str(x))
            out.append(" ".join(row))
        print("\n".join(out))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <array>
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

const long long INF = 1e18;

class Solution {
public:
    vector<vector<long long>> allPairsShortestPaths(int n, const vector<array<int, 3>>& edges) {
        vector<vector<pair<int, int>>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
        }

        // Bellman-Ford
        vector<long long> h(n + 1, 0); // Virtual source n, connected to all with 0
        // Init h[0..n-1] = 0 is equivalent to 1st iteration of BF from virtual source
        
        for (int i = 0; i < n; i++) {
            bool changed = false;
            for (const auto& e : edges) {
                if (h[e[0]] + e[2] < h[e[1]]) {
                    h[e[1]] = h[e[0]] + e[2];
                    changed = true;
                }
            }
            if (!changed) break;
        }

        vector<vector<long long>> result(n, vector<long long>(n, INF));

        for (int s = 0; s < n; s++) {
            priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
            vector<long long> d(n, INF);

            d[s] = 0;
            pq.push({0, s});

            while (!pq.empty()) {
                long long distU = pq.top().first;
                int u = pq.top().second;
                pq.pop();

                if (distU > d[u]) continue;

                for (const auto& e : adj[u]) {
                    int v = e.first;
                    int w = e.second;
                    long long newWeight = w + h[u] - h[v];
                    if (d[u] + newWeight < d[v]) {
                        d[v] = d[u] + newWeight;
                        pq.push({d[v], v});
                    }
                }
            }

            for (int v = 0; v < n; v++) {
                if (d[v] != INF) {
                    result[s][v] = d[v] - h[s] + h[v];
                }
            }
        }

        return result;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    vector<vector<long long>> dist = solution.allPairsShortestPaths(n, edges);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (j) cout << ' ';
            if (dist[i][j] >= INF / 2) cout << "INF";
            else cout << dist[i][j];
        }
        if (i + 1 < n) cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class PriorityQueue {
  constructor(comparator = (a, b) => a - b) {
    this.heap = [];
    this.comparator = comparator;
  }
  push(val) {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }
  pop() {
    if (this.heap.length === 0) return null;
    const top = this.heap[0];
    const bottom = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = bottom;
      this.bubbleDown(0);
    }
    return top;
  }
  isEmpty() { return this.heap.length === 0; }
  bubbleUp(idx) {
    while (idx > 0) {
      const pIdx = Math.floor((idx - 1) / 2);
      if (this.comparator(this.heap[idx], this.heap[pIdx]) < 0) {
        [this.heap[idx], this.heap[pIdx]] = [this.heap[pIdx], this.heap[idx]];
        idx = pIdx;
      } else break;
    }
  }
  bubbleDown(idx) {
    while (true) {
      const lIdx = 2 * idx + 1;
      const rIdx = 2 * idx + 2;
      let swapIdx = null;
      if (lIdx < this.heap.length && this.comparator(this.heap[lIdx], this.heap[idx]) < 0) swapIdx = lIdx;
      if (rIdx < this.heap.length && this.comparator(this.heap[rIdx], swapIdx === null ? this.heap[idx] : this.heap[swapIdx]) < 0) swapIdx = rIdx;
      if (swapIdx !== null) {
        [this.heap[idx], this.heap[swapIdx]] = [this.heap[swapIdx], this.heap[idx]];
        idx = swapIdx;
      } else break;
    }
  }
}

class Solution {
  allPairsShortestPaths(n, edges) {
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
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    edges.push([u, v, w]);
  }

  const solution = new Solution();
  const dist = solution.allPairsShortestPaths(n, edges);
  const INF = 1e15;
  const out = dist.map((row) => row.map(x => x >= INF / 2 ? "INF" : x).join(" "));
  console.log(out.join("\n"));
});
```

