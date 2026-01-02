---
problem_id: AGR_MAX_FLOW_VERTEX_CAPACITY__5913
display_id: AGR-002
slug: max-flow-vertex-capacity
title: "Max Flow With Vertex Capacities"
difficulty: Medium
difficulty_score: 58
topics:
  - Graphs
  - Max Flow
  - Vertex Capacities
tags:
  - advanced-graphs
  - max-flow
  - vertex-capacity
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-002: Max Flow With Vertex Capacities

## Problem Statement

You are given a directed graph with edge capacities and **vertex capacities**. Compute the maximum flow from source `s` to sink `t` while respecting both edge and vertex limits.

A vertex with capacity `C` can carry at most `C` units of flow through it. The source and sink have unlimited capacity.

![Problem Illustration](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186940/dsa-problems/AGR-002/problem/cunfjp4k77gbrhhghgms.jpg)

## Input Format

- First line: integers `n`, `m`, `s`, `t`
- Second line: `n` integers `cap[i]` (`-1` means infinite capacity)
- Next `m` lines: `u v c` describing a directed edge `u -> v` with capacity `c`

## Output Format

- Single integer: maximum flow from `s` to `t`

## Constraints

- `2 <= n <= 2000`
- `0 <= m <= 5000`
- `0 <= c <= 10^9`
- `cap[i] = -1` or `0 <= cap[i] <= 10^9`
- `0 <= s, t < n`, `s != t`

## Example

**Input:**

```
4 3 0 3
-1 3 2 -1
0 1 3
1 2 2
2 3 3
```

**Output:**

```
2
```

**Explanation:**

Vertex 2 limits the flow to 2, so the max flow is 2.

![Example Visualization](https://res.cloudinary.com/dy4dvna3t/image/upload/v1767186943/dsa-problems/AGR-002/problem/zssufeqz99vcroa175c6.jpg)

## Notes

- Split each vertex into `in` and `out` with an edge of its capacity.
- Use a max flow algorithm like Dinic on the transformed graph.
- Treat `cap[s]` and `cap[t]` as infinite.

## Related Topics

Max Flow, Vertex Capacities, Dinic

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    static class Edge {
        int to;
        long capacity;
        long flow;
        int rev; // index of reverse edge

        Edge(int to, long capacity, int rev) {
            this.to = to;
            this.capacity = capacity;
            this.rev = rev;
            this.flow = 0;
        }
    }

    private List<List<Edge>> adj;
    private int[] level;
    private int[] ptr;

    public long maxFlowVertexCap(int n, int s, int t, long[] cap, int[][] edges) {
        return 0;
    }

    private void addEdge(int from, int to, long cap) {
    }

    private boolean bfs(int s, int t, int n) {
        return false;
    }

    private long dfs(int u, int t, long pushed) {
        return 0;
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
        long[] cap = new long[n];
        for (int i = 0; i < n; i++) cap[i] = sc.nextLong();
        int[][] edges = new int[m][3];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
            edges[i][2] = sc.nextInt();
        }

        Solution solution = new Solution();
        System.out.println(solution.maxFlowVertexCap(n, s, t, cap, edges));
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth for DFS
sys.setrecursionlimit(200000)

class Dinic:
    def __init__(self, n):
        return 0
    def add_edge(self, u, v, capacity):
        return 0
    def bfs(self, s, t):
        return 0
    def dfs(self, u, t, pushed, ptr):
        return 0
    def max_flow(self, s, t):
        return 0
def max_flow_vertex_cap(n: int, s: int, t: int, cap: list[int], edges: list[tuple[int, int, int]]) -> int:
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
        cap = [int(next(iterator)) for _ in range(n)]
        edges = []
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            c = int(next(iterator))
            edges.append((u, v, c))
        print(max_flow_vertex_cap(n, s, t, cap, edges))
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

class Solution {
    struct Edge {
        int to;
        long long capacity;
        long long flow;
        int rev;
    };

    vector<vector<Edge>> adj;
    vector<int> level;
    vector<int> ptr;

    void addEdge(int from, int to, long long cap) {
    }

    bool bfs(int s, int t) {
        return false;
    }

    long long dfs(int u, int t, long long pushed) {
        return 0;
    }

public:
    long long maxFlowVertexCap(int n, int s, int t, const vector<long long>& cap,
                               const vector<array<int, 3>>& edges) {
        int numNodes = 2 * n;
        adj.assign(numNodes, vector<Edge>());
        level.resize(numNodes);
        ptr.resize(numNodes);

        long long INF = 1e15;

        for (int i = 0; i < n; i++) {
            long long c = (cap[i] == -1 || i == s || i == t) ? INF : cap[i];
            addEdge(2 * i, 2 * i + 1, c);
        }

        for (const auto& e : edges) {
            addEdge(2 * e[0] + 1, 2 * e[1], e[2]);
        }

        int sNode = 2 * s;
        int tNode = 2 * t + 1;
        long long maxFlow = 0;

        while (bfs(sNode, tNode)) {
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(sNode, tNode, INF)) {
                maxFlow += pushed;
            }
        }

        return maxFlow;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s, t;
    if (!(cin >> n >> m >> s >> t)) return 0;
    vector<long long> cap(n);
    for (int i = 0; i < n; i++) cin >> cap[i];
    vector<array<int, 3>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
    }

    Solution solution;
    cout << solution.maxFlowVertexCap(n, s, t, cap, edges) << "\n";
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  maxFlowVertexCap(n, s, t, cap, edges) {
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
  const cap = [];
  for (let i = 0; i < n; i++) cap.push(parseInt(data[idx++], 10));
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const c = parseInt(data[idx++], 10);
    edges.push([u, v, c]);
  }

  const solution = new Solution();
  console.log(solution.maxFlowVertexCap(n, s, t, cap, edges).toString());
});
```

