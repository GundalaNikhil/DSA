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
    public Object[] sccCompress(int n, List<List<Integer>> adj) {
        // Your implementation here
        return new Object[]{0, new int[n], new ArrayList<int[]>()};
    }
}

public class Main {
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
def scc_compress(n: int, adj: list[list[int]]):
    # Your implementation here
    return 0, [0] * n, []

def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
    k, comp, edges = scc_compress(n, adj)
    out = [str(k), " ".join(str(x) for x in comp), str(len(edges))]
    out += [f"{a} {b}" for (a, b) in edges]
    sys.stdout.write("\n".join(out).strip())

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
    tuple<int, vector<int>, vector<pair<int, int>>> sccCompress(int n, const vector<vector<int>>& adj) {
        // Your implementation here
        return {0, vector<int>(n, 0), {}};
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
    // Your implementation here
    return [0, new Array(n).fill(0), []];
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
  const adj = Array.from({ length: n }, () => []);
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    adj[u].push(v);
  }

  const solution = new Solution();
  const [k, comp, edges] = solution.sccCompress(n, adj);
  const out = [k.toString(), comp.join(" "), edges.length.toString()];
  for (const [a, b] of edges) out.push(`${a} ${b}`);
  console.log(out.join("\n").trim());
});
```
