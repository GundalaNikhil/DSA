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
        // Implementation here
        return new ArrayList<>();
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt(), m = sc.nextInt();
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) { edges[i][0] = sc.nextInt(); edges[i][1] = sc.nextInt(); }
        List<List<Integer>> cycles = new Solution().cycleBasis(n, edges);
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

def cycle_basis(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    # Implementation here
    return []

def main():
    data = sys.stdin.read().split()
    if not data: return
    it = iter(data)
    n, m = int(next(it)), int(next(it))
    edges = [(int(next(it)), int(next(it))) for _ in range(m)]
    cycles = cycle_basis(n, edges)
    out = [str(len(cycles))]
    for cyc in cycles:
        out.append(f"{len(cyc)} " + " ".join(map(str, cyc)))
    print("\n".join(out).strip())

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
    vector<vector<int>> cycleBasis(int n, const vector<pair<int,int>>& edges) {
        // Implementation here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n, m;
    if (!(cin >> n >> m)) return 0;
    vector<pair<int,int>> edges(m);
    for (int i = 0; i < m; i++) cin >> edges[i].first >> edges[i].second;
    auto cycles = Solution().cycleBasis(n, edges);
    cout << cycles.size() << "\n";
    for (auto& cyc : cycles) {
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
    /* Implementation */ return [];
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
    m = parseInt(data[idx++], 10);
  const edges = [];
  for (let i = 0; i < m; i++)
    edges.push([parseInt(data[idx++], 10), parseInt(data[idx++], 10)]);
  const cycles = new Solution().cycleBasis(n, edges);
  const out = [cycles.length.toString()];
  for (const cyc of cycles) out.push(`${cyc.length} ${cyc.join(" ")}`);
  console.log(out.join("\n").trim());
});
```
