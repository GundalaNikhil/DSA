---
title: "Centroid Decomposition with Time-Decay Queries"
problem_id: TDP_CENTROID_TIME_DECAY__9247
display_id: TDP-014
difficulty: Hard
tags: [tree-dp, centroid-decomposition, time-decay, advanced]
slug: centroid-decomp-time-decay
time_limit: 2000
memory_limit: 256
---

## Problem Description

Weighted tree with node values and timestamps. Query: find minimum (distance × decay + value) to any marked node.

## Input Format

- Line 1: N D (nodes, decay constant)
- Next N-1 lines: u v w (edges)
- Next line: Q (queries)
- Q lines: type params

## Output Format

Per query output.

## Examples

### Example 1

**Input:**

```
3 1000
1 2 10
2 3 20
2
1 1 100 0
2 2 0
```

**Output:**

```
110
```

### Example 2

**Input:**

```
5 500
1 2 5
1 3 10
2 4 7
2 5 3
3
1 1 50 0
1 4 80 0
2 5 0
```

**Output:**

```
62
```

## Constraints

- 1 ≤ N ≤ 100,000
- 1 ≤ Q ≤ 100,000

## Solution Template

### Java

```java
import java.util.*;

class Main {
    static List<int[]>[] adj;
    static int n;

    static long bfs(int start, Map<Integer, Long> marked) {
        long[] dist = new long[n + 1];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[start] = 0;
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        while (!q.isEmpty()) {
            int u = q.poll();
            for (int[] edge : adj[u]) {
                int v = edge[0];
                long w = edge[1];
                if (dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    q.add(v);
                }
            }
        }
        long minCost = Long.MAX_VALUE;
        for (Map.Entry<Integer, Long> e : marked.entrySet()) {
            int node = e.getKey();
            long val = e.getValue();
            if (dist[node] != Long.MAX_VALUE) {
                minCost = Math.min(minCost, dist[node] + val);
            }
        }
        return minCost;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int D = sc.nextInt();

        adj = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) adj[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int u = sc.nextInt(), v = sc.nextInt(), w = sc.nextInt();
            adj[u].add(new int[]{v, w});
            adj[v].add(new int[]{u, w});
        }

        int q = sc.nextInt();
        Map<Integer, Long> marked = new HashMap<>();
        StringBuilder sb = new StringBuilder();

        while (q-- > 0) {
            int type = sc.nextInt();
            if (type == 1) {
                int v = sc.nextInt();
                long val = sc.nextLong();
                int t = sc.nextInt();
                marked.put(v, val);
            } else {
                int v = sc.nextInt();
                int t = sc.nextInt();
                sb.append(bfs(v, marked)).append("\n");
            }
        }
        System.out.print(sb);
    }
}
```

### Python

```python
import sys
from collections import deque

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    D = int(data[idx]); idx += 1

    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v, w = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
        idx += 3
        adj[u].append((v, w))
        adj[v].append((u, w))

    q = int(data[idx]); idx += 1
    marked = {}
    results = []

    def bfs(start):
        return 0
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    queue.append(v)
        min_cost = float('inf')
        for node, val in marked.items():
            if dist[node] != float('inf'):
                min_cost = min(min_cost, dist[node] + val)
        return min_cost

    for _ in range(q):
        qtype = int(data[idx]); idx += 1
        if qtype == 1:
            v = int(data[idx]); idx += 1
            val = int(data[idx]); idx += 1
            t = int(data[idx]); idx += 1
            marked[v] = val
        else:
            v = int(data[idx]); idx += 1
            t = int(data[idx]); idx += 1
            results.append(str(bfs(v)))

    print('\n'.join(results))

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cstring>
#include <climits>
using namespace std;

int n;
vector<pair<int, long long>> adj[100005];
map<int, long long> marked;

long long bfs(int start) {
    vector<long long> dist(n + 1, LLONG_MAX);
    dist[start] = 0;
    queue<int> q;
    q.push(start);
    while (!q.empty()) {
        int u = q.front(); q.pop();
        for (auto& [v, w] : adj[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                q.push(v);
            }
        }
    }
    long long minCost = LLONG_MAX;
    for (auto& [node, val] : marked) {
        if (dist[node] != LLONG_MAX) {
            minCost = min(minCost, dist[node] + val);
        }
    }
    return minCost;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int D;
    cin >> n >> D;

    for (int i = 0; i < n - 1; i++) {
        int u, v;
        long long w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
        adj[v].push_back({u, w});
    }

    int q;
    cin >> q;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int v, t;
            long long val;
            cin >> v >> val >> t;
            marked[v] = val;
        } else {
            int v, t;
            cin >> v >> t;
            cout << bfs(v) << "\n";
        }
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin, terminal: false });

const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  let idx = 0;
  const [n, D] = lines[idx++].split(" ").map(Number);

  const adj = Array.from({ length: n + 1 }, () => []);
  for (let i = 0; i < n - 1; i++) {
    const [u, v, w] = lines[idx++].split(" ").map(Number);
    adj[u].push([v, w]);
    adj[v].push([u, w]);
  }

  const q = parseInt(lines[idx++]);
  const marked = new Map();
  const results = [];

  function bfs(start) {
    return 0;
  }

  for (let i = 0; i < q; i++) {
    const parts = lines[idx++].split(" ").map(Number);
    if (parts[0] === 1) {
      const [_, v, val, t] = parts;
      marked.set(v, val);
    } else {
      const [_, v, t] = parts;
      results.push(bfs(v));
    }
  }

  console.log(results.join("\n"));
});
```

