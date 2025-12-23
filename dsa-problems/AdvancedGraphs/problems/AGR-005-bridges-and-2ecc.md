---
problem_id: AGR_BRIDGES_AND_2ECC__3471
display_id: AGR-005
slug: bridges-and-2ecc
title: "Bridges and 2-Edge-Connected Components"
difficulty: Medium
difficulty_score: 54
topics:
  - Graphs
  - Bridges
  - Components
tags:
  - advanced-graphs
  - bridges
  - components
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-005: Bridges and 2-Edge-Connected Components
## Problem Statement
Given an undirected graph, find all bridges and compute the 2-edge-connected components (2ECCs). A 2ECC is a maximal set of nodes that stays connected after removing any single edge.
![Problem Illustration](../images/AGR-005/problem-illustration.png)
## Input Format
- First line: integers `n` and `m`
- Next `m` lines: `u v` describing an undirected edge
## Output Format
- Line 1: integer `b`, number of bridges
- Next `b` lines: each bridge edge `u v` in input order
- Last line: `n` integers `comp[i]` (1-based component id)
## Constraints
- `1 <= n <= 200000`
- `0 <= m <= 200000`
- `0 <= u, v < n`
## Example
**Input:**
```
4 4
0 1
1 2
2 0
2 3
```
**Output:**
```
1
2 3
1 1 1 2
```
**Explanation:**
Edge (2,3) is a bridge. Nodes {0,1,2} form one 2ECC, node {3} is another.
![Example Visualization](../images/AGR-005/example-1.png)
## Notes
- Use DFS low-link to detect bridges.
- Build components by unioning all non-bridge edges.
- Output bridge edges in their input order.
## Related Topics
Bridges, 2-Edge-Connected Components, DFS
---
## Solution Template
### Java
```java
import java.util.*;
class Solution {
    public int[][] bridgesAndComponents(int n, int[][] edges) {
        // Your implementation here
        return new int[][]{};
    }
}
public class Main {
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
        int[][] result = solution.bridgesAndComponents(n, edges);
        int[] bridgeFlags = result[0];
        int[] comp = result[1];
        int bridgeCount = 0;
        for (int f : bridgeFlags) bridgeCount += f;
        StringBuilder sb = new StringBuilder();
        sb.append(bridgeCount).append('\n');
        for (int i = 0; i < m; i++) {
            if (bridgeFlags[i] == 1) {
                sb.append(edges[i][0]).append(' ').append(edges[i][1]).append('\n');
            }
        }
        for (int i = 0; i < n; i++) {
            if (i > 0) sb.append(' ');
            sb.append(comp[i]);
        }
        System.out.print(sb.toString().trim());
        sc.close();
    }
}
```
### Python
```python
def bridges_and_components(n: int, edges: list[tuple[int, int]]):
    # Your implementation here
    return [], [0] * n
def main():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))
    edges = []
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        edges.append((u, v))
    bridge_flags, comp = bridges_and_components(n, edges)
    out = [str(sum(bridge_flags))]
    for i, f in enumerate(bridge_flags):
        if f:
            out.append(f"{edges[i][0]} {edges[i][1]}")
    out.append(" ".join(str(x) for x in comp))
    sys.stdout.write("\n".join(out))
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
    pair<vector<int>, vector<int>> bridgesAndComponents(int n, const vector<pair<int, int>>& edges) {
        // Your implementation here
        return {vector<int>(edges.size(), 0), vector<int>(n, 1)};
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
    auto res = solution.bridgesAndComponents(n, edges);
    const vector<int>& bridgeFlags = res.first;
    const vector<int>& comp = res.second;
    int bridgeCount = 0;
    for (int f : bridgeFlags) bridgeCount += f;
    cout << bridgeCount << "\n";
    for (int i = 0; i < m; i++) {
        if (bridgeFlags[i]) {
            cout << edges[i].first << ' ' << edges[i].second << "\n";
        }
    }
    for (int i = 0; i < n; i++) {
        if (i) cout << ' ';
        cout << comp[i];
    }
    return 0;
}
```
### JavaScript
```javascript
const readline = require("readline");
class Solution {
  bridgesAndComponents(n, edges) {
    // Your implementation here
    return [new Array(edges.length).fill(0), new Array(n).fill(1)];
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
  const edges = [];
  for (let i = 0; i < m; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }
  const solution = new Solution();
  const [bridgeFlags, comp] = solution.bridgesAndComponents(n, edges);
  let bridgeCount = 0;
  for (const f of bridgeFlags) bridgeCount += f;
  const out = [bridgeCount.toString()];
  for (let i = 0; i < m; i++) {
    if (bridgeFlags[i]) out.push(``edges[i][0]`{edges[i][1]}`);
  }
  out.push(comp.join(" "));
  console.log(out.join("\n"));
});
```
