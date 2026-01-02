---
problem_id: GRB_SHORTEST_PATH_DAG__7291
display_id: GRB-014
slug: shortest-path-dag
title: "Shortest Path in DAG"
difficulty: Easy
difficulty_score: 38
topics:
  - Graphs
  - DAG
  - Shortest Path
tags:
  - graphs-basics
  - dag
  - shortest-path
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# GRB-014: Shortest Path in DAG

## Problem Statement

Given a weighted directed acyclic graph (DAG), compute shortest distances from a source node `s`.

If a node is unreachable, its distance should be `-1`.

![Problem Illustration](../images/GRB-014/problem-illustration.png)

## Input Format

- First line: integers `n`, `m`, and `s`
- Next `m` lines: `u v w` describing a directed edge `u -> v` with weight `w`

## Output Format

- Single line: `n` integers, the distances from `s` to nodes `0..n-1`

## Constraints

- `1 <= n <= 100000`
- `0 <= m <= 200000`
- `-10^9 <= w <= 10^9`
- The graph is a DAG

## Example

**Input:**

```
3 2 0
0 1 1
1 2 2
```

**Output:**

```
0 1 3
```

**Explanation:**

The DAG order is `0,1,2`. Distances relax along this order.

![Example Visualization](../images/GRB-014/example-1.png)

## Notes

- Use topological order and relax edges once.
- Negative weights are allowed in a DAG.
- Use 64-bit integers for distances.

## Related Topics

DAG, Topological Sort, Shortest Path

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public long[] shortestPathDAG(int n, List<List<int[]>> adj, int s) {
        // Implementation here
        return new long[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int s = sc.nextInt();
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            int w = sc.nextInt();
            adj.get(u).add(new int[]{v, w});
        }

        Solution solution = new Solution();
        long[] dist = solution.shortestPathDAG(n, adj, s);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(dist[i]);
        }
        System.out.print(sb.toString());
        sc.close();
    }
}
```

### Python

```python
import sys

def shortest_path_dag(n: int, adj: list[list[tuple[int, int]]], s: int) -> list[int]:
    # Implementation here
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
        s = int(next(iterator))
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            w = int(next(iterator))
            adj[u].append((v, w))
            
        dist = shortest_path_dag(n, adj, s)
        print(" ".join(map(str, dist)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<long long> shortestPathDAG(int n, const vector<vector<pair<int, int>>>& adj, int s) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, s;
    if (!(cin >> n >> m >> s)) return 0;
    vector<vector<pair<int, int>>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    Solution solution;
    vector<long long> dist = solution.shortestPathDAG(n, adj, s);
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << dist[i];
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  shortestPathDAG(n, adj, s) {
    // Implementation here
    return null;
  }
}

class Solution {
  shortestPathDAG(n, adj, s) {
    const visited = new Int8Array(n).fill(0);
    const stack = [];

    const dfs = (u) => {
      visited[u] = 1;
      for (const [v, w] of adj[u]) {
        if (!visited[v]) dfs(v);
      }
      stack.push(u);
    };

    for (let i = 0; i < n; i++) {
      if (!visited[i]) dfs(i);
    }

    // Initialize distances
    // Use BigInt for safety with large weights, though Number is usually fine up to 2^53
    // Problem constraints 10^9 * 10^5 = 10^14, fits in Number.
    const INF = 1e15;
    const dist = new Array(n).fill(INF);
    dist[s] = 0;

    // Process in topological order (reverse of post-order stack)
    while (stack.length > 0) {
      const u = stack.pop();

      if (dist[u] !== INF) {
        for (const [v, w] of adj[u]) {
          if (dist[u] + w < dist[v]) {
            dist[v] = dist[u] + w;
          }
        }
      }
    }

    return dist.map((d) => (d === INF ? -1 : d));
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
  const s = parseInt(data[idx++], 10);
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    const w = parseInt(data[idx++], 10);
    adj[u].push([v, w]);
  }

  const solution = new Solution();
  const dist = solution.shortestPathDAG(n, adj, s);
  console.log(dist.join(" "));
});
```
