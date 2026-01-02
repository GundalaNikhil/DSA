---
problem_id: AGR_DIRECTED_CYCLE_BASIS__8240
display_id: AGR-015
slug: directed-cycle-basis
title: "Directed Cycle Basis"
difficulty: Hard
difficulty_score: 72
topics:
  - Graphs
  - Cycle Basis
  - Spanning Forest
tags:
  - advanced-graphs
  - cycle-basis
  - directed
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-015: Directed Cycle Basis

## Problem Statement

Given a directed graph, output a cycle basis of size `m - n + c`, where `c` is the number of connected components in the underlying undirected graph.

Each cycle should be a simple directed cycle. Any valid basis is accepted.

![Problem Illustration](../images/AGR-015/problem-illustration.png)

## Input Format

- First line: integers `n` and `m`
- Next `m` lines: `u v` describing a directed edge `u -> v`

## Output Format

- Line 1: integer `b`, number of cycles output
- Next `b` lines: each cycle as `k v1 v2 ... vk` where `v1 == vk` (cycle closed)

## Constraints

- `1 <= n <= 500`
- `0 <= m <= 2000`
- `0 <= u, v < n`

## Example

**Input:**

```
4 5
0 1
1 2
2 0
1 3
3 1
```

**Output:**

```
2
4 0 1 2 0
3 1 3 1
```

**Explanation:**

Two independent directed cycles are shown. This is a valid basis.

![Example Visualization](../images/AGR-015/example-1.png)

## Notes

- Build a spanning forest on the underlying undirected graph.
- Each non-tree edge creates a fundamental cycle via parent pointers.
- Any valid basis size is accepted.

## Related Topics

Cycle Basis, Spanning Forest, Graph Theory

---

## Solution Template

### Java

```java
import java.util.*;

class Solution {
    public List<List<Integer>> cycleBasis(int n, int[][] edges) {
        return null;
    }
    
    private void dfs(int u, boolean[] visited, List<List<Integer>> adj) {
        visited[u] = true;
        for (int v : adj.get(u)) {
            if (!visited[v]) dfs(v, visited, adj);
        }
    }
    
    private List<Integer> bfs(int start, int target, int n, List<List<int[]>> adj) {
        if (start == target) return new ArrayList<>();
        int[] parentEdge = new int[n];
        int[] parentNode = new int[n];
        Arrays.fill(parentEdge, -1);
        Arrays.fill(parentNode, -1);
        
        Queue<Integer> q = new ArrayDeque<>();
        q.add(start);
        parentNode[start] = start;
        
        while (!q.isEmpty()) {
            int u = q.poll();
            if (u == target) break;
            for (int[] edge : adj.get(u)) {
                int v = edge[0];
                int idx = edge[1];
                if (parentNode[v] == -1) {
                    parentNode[v] = u;
                    parentEdge[v] = idx;
                    q.add(v);
                }
            }
        }
        
        if (parentNode[target] == -1) return null;
        
        List<Integer> path = new ArrayList<>();
        int curr = target;
        while (curr != start) {
            path.add(parentEdge[curr]);
            curr = parentNode[curr];
        }
        Collections.reverse(path);
        return path;
    }
    
    private boolean insert(BitSet[] basis, BitSet vec) {
        for (int i = vec.nextSetBit(0); i >= 0; i = vec.nextSetBit(i + 1)) {
            if (basis[i] == null) {
                basis[i] = (BitSet) vec.clone();
                return true;
            }
            vec.xor(basis[i]);
        }
        return false;
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        List<List<Integer>> cycles = solution.cycleBasis(n, edges);
        StringBuilder sb = new StringBuilder();
        sb.append(cycles.size()).append('\n');
        for (List<Integer> cyc : cycles) {
            sb.append(cyc.size());
            for (int v : cyc) sb.append(' ').append(v);
            sb.append('\n');
        }
        System.out.print(sb.toString().trim());
        sc.close();
    }
}
```

### Python

```python
import sys
from collections import deque

def cycle_basis(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
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
            edges.append((u, v))
            
        cycles = cycle_basis(n, edges)
        out = [str(len(cycles))]
        for cyc in cycles:
            out.append(str(len(cyc)) + " " + " ".join(map(str, cyc)))
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
#include <queue>
#include <bitset>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> cycleBasis(int n, const vector<pair<int, int>>& edges) {
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<pair<int, int>> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    Solution solution;
    vector<vector<int>> cycles = solution.cycleBasis(n, edges);
    cout << cycles.size() << "\n";
    for (const auto& cyc : cycles) {
        cout << cyc.size();
        for (int v : cyc) cout << ' ' << v;
        cout << "\n";
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  cycleBasis(n, edges) {
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
    edges.push([u, v]);
  }

  const solution = new Solution();
  const cycles = solution.cycleBasis(n, edges);
  const out = [cycles.length.toString()];
  for (const cyc of cycles) {
    out.push(`${cyc.length} ${cyc.join(" ")}`.trim());
  }
  console.log(out.join("\n").trim());
});
```

