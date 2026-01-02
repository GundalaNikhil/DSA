---
problem_id: AGR_SCC_COMPRESSION__2659
display_id: AGR-008
slug: scc-compression
title: "Strongly Connected Components Compression"
difficulty: Easy
difficulty_score: 40
topics:
  - Graphs
  - SCC
  - Condensation Graph
tags:
  - advanced-graphs
  - scc
  - condensation
  - easy
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-008: Strongly Connected Components Compression

## Problem Statement

Find the strongly connected components (SCCs) of a directed graph and build the condensation DAG where each SCC is contracted into a single node.

![Problem Illustration](../images/AGR-008/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` describing a directed edge `u -> v`

## Output Format

- Line 1: integer `k`, number of SCCs
- Line 2: `n` integers `comp[i]` in `[0, k-1]`
- Line 3: integer `e`, number of edges in the condensation DAG
- Next `e` lines: `a b` for each edge `a -> b` between SCCs

## Constraints

- `1 <= n <= 200000`
- `0 <= m <= 200000`
- `0 <= u, v < n`

## Example

**Input:**

```
3 3
0 1
1 0
1 2
```

**Output:**

```
2
0 0 1
1
0 1
```

**Explanation:**

Nodes {0,1} are one SCC, node {2} is another. The condensation graph has one edge.

![Example Visualization](../images/AGR-008/example-1.png)

## Notes

- Use Kosaraju or Tarjan to compute SCCs.
- Avoid duplicate edges in the condensation DAG.
- Any valid component labeling is accepted.

## Related Topics

SCC, Tarjan, Condensation Graph

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    private int timer;
    private int[] tin, low;
    private boolean[] onStack;
    private Stack<Integer> stack;
    private List<List<Integer>> sccs;
    private List<List<Integer>> adj;

    public Object[] sccCompress(int n, List<List<Integer>> adjList) {
        return null;
    }

    private void dfs(int u) {
        tin[u] = low[u] = timer++;
        stack.push(u);
        onStack[u] = true;

        for (int v : adj.get(u)) {
            if (tin[v] == -1) {
                dfs(v);
                low[u] = Math.min(low[u], low[v]);
            } else if (onStack[v]) {
                low[u] = Math.min(low[u], tin[v]);
            }
        }

        if (low[u] == tin[u]) {
            List<Integer> component = new ArrayList<>();
            while (true) {
                int v = stack.pop();
                onStack[v] = false;
                component.add(v);
                if (u == v) break;
            }
            sccs.add(component);
        }
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) adj.add(new ArrayList<>());
        for (int i = 0; i < m; i++) {
            int u = sc.nextInt();
            int v = sc.nextInt();
            adj.get(u).add(v);
        }

        Solution solution = new Solution();
        Object[] res = solution.sccCompress(n, adj);
        int k = (int) res[0];
        int[] comp = (int[]) res[1];
        @SuppressWarnings("unchecked")
        List<int[]> edges = (List<int[]>) res[2];

        StringBuilder sb = new StringBuilder();
        sb.append(k).append('\n');
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(comp[i]);
        }
        sb.append('\n').append(edges.size()).append('\n');
        for (int[] e : edges) sb.append(e[0]).append(' ').append(e[1]).append('\n');
        System.out.print(sb.toString().trim());
        sc.close();
    }
}
```

### Python

```python
import sys

# Increase recursion depth
sys.setrecursionlimit(300000)

def scc_compress(n: int, adj: list[list[int]]):
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
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u = int(next(iterator))
            v = int(next(iterator))
            adj[u].append(v)

        k, comp, edges = scc_compress(n, adj)

        out = [str(k), " ".join(map(str, comp)), str(len(edges))]
        for u, v in edges:
            out.append(f"{u} {v}")

        sys.stdout.write("\n".join(out).strip())
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
#include <set>
#include <tuple>

using namespace std;

class Solution {
    int timer;
    vector<int> tin, low;
    vector<bool> onStack;
    stack<int> st;
    vector<vector<int>> sccs;

    void dfs(int u, const vector<vector<int>>& adj) {
    }

public:
    tuple<int, vector<int>, vector<pair<int, int>>> sccCompress(int n, const vector<vector<int>>& adj) {
        tin.assign(n, -1);
        low.assign(n, -1);
        onStack.assign(n, false);
        while (!st.empty()) st.pop();
        sccs.clear();
        timer = 0;

        for (int i = 0; i < n; i++) {
            if (tin[i] == -1) {
                dfs(i, adj);
            }
        }

        int k = sccs.size();
        vector<int> comp(n);
        for (int i = 0; i < k; i++) {
            for (int node : sccs[i]) {
                comp[node] = i;
            }
        }

        set<pair<int, int>> dagEdges;
        for (int u = 0; u < n; u++) {
            for (int v : adj[u]) {
                if (comp[u] != comp[v]) {
                    dagEdges.insert({comp[u], comp[v]});
                }
            }
        }

        return {k, comp, vector<pair<int, int>>(dagEdges.begin(), dagEdges.end())};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<vector<int>> adj(n);
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
    }

    Solution solution;
    auto [k, comp, edges] = solution.sccCompress(n, adj);

    cout << k << "\n";
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << comp[i];
    }
    cout << "\n" << edges.size() << "\n";
    for (auto& e : edges) {
        cout << e.first << ' ' << e.second << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  sccCompress(n, adj) {
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
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    adj[u].push(v);
  }

  const solution = new Solution();
  const [k, comp, edges] = solution.sccCompress(n, adj);

  const out = [k.toString(), comp.join(" "), edges.length.toString()];
  edges.sort((p, q) => p[0] - q[0] || p[1] - q[1]);
  for (const [a, b] of edges) out.push(`${a} ${b}`);
  console.log(out.join("\n").trim());
});
```

