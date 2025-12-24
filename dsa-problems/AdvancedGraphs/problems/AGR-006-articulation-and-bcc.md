---
problem_id: AGR_ARTICULATION_AND_BCC__7358
display_id: AGR-006
slug: articulation-and-bcc
title: "Articulation Points and Biconnected Components"
difficulty: Medium
difficulty_score: 60
topics:
  - Graphs
  - Articulation Points
  - Biconnected Components
tags:
  - advanced-graphs
  - articulation-points
  - bcc
  - medium
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-006: Articulation Points and Biconnected Components
## Problem Statement
Given an undirected graph, find all articulation points and all vertex-biconnected components (BCCs).
A BCC is a maximal set of vertices that remains connected after removing any single vertex from the set.
![Problem Illustration](../images/AGR-006/problem-illustration.png)
## Input Format
- First line: integers `n` and `m`
- Next `m` lines: `u v` describing an undirected edge
## Output Format
- Line 1: integer `a`, number of articulation points
- Line 2: `a` integers of articulation points in increasing order (or empty line)
- Line 3: integer `b`, number of biconnected components
- Next `b` lines: each BCC as `k v1 v2 ... vk` (vertices in any order)
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
1 3
```
**Output:**
```
1
1
2
3 0 1 2
2 1 3
```
**Explanation:**
Node 1 is an articulation point. The BCCs are {0,1,2} and {1,3}.
![Example Visualization](../images/AGR-006/example-1.png)
## Notes
- Use Tarjan's algorithm with an edge stack to extract BCCs.
- The order of BCCs and vertex order inside each component does not matter.
- The graph may be disconnected.
## Related Topics
Articulation Points, Biconnected Components, DFS
---
## Solution Template
### Java
```java
import java.util.*;
class Solution {
    public Object[] articulationAndBcc(int n, int[][] edges) {
        // Your implementation here
        return new Object[]{new int[0], new ArrayList<List<Integer>>()};
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
        Object[] res = solution.articulationAndBcc(n, edges);
        int[] aps = (int[]) res[0];
        @SuppressWarnings("unchecked")
        List<List<Integer>> bccs = (List<List<Integer>>) res[1];
        StringBuilder sb = new StringBuilder();
        sb.append(aps.length).append('\n');
        for (int i = 0; i < aps.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(aps[i]);
        }
        sb.append('\n').append(bccs.size()).append('\n');
        for (List<Integer> bcc : bccs) {
            sb.append(bcc.size());
            for (int v : bcc) sb.append(' ').append(v);
            sb.append('\n');
        }
        System.out.print(sb.toString().trim());
        sc.close();
    }
}
```
### Python
```python
def articulation_and_bcc(n: int, edges: list[tuple[int, int]]):
    # Your implementation here
    return [], []
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
    aps, bccs = articulation_and_bcc(n, edges)
    out = [str(len(aps)), " ".join(str(x) for x in aps), str(len(bccs))]
    for b in bccs:
        out.append(str(len(b)) + " " + " ".join(str(x) for x in b))
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
    pair<vector<int>, vector<vector<int>>> articulationAndBcc(int n, const vector<pair<int, int>>& edges) {
        // Your implementation here
        return {{}, {}};
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
    auto res = solution.articulationAndBcc(n, edges);
    const vector<int>& aps = res.first;
    const vector<vector<int>>& bccs = res.second;
    cout << aps.size() << "\n";
    for (int i = 0; i < (int)aps.size(); i++) {
        if (i) cout << ' ';
        cout << aps[i];
    }
    cout << "\n" << bccs.size() << "\n";
    for (const auto& bcc : bccs) {
        cout << bcc.size();
        for (int v : bcc) cout << ' ' << v;
        cout << "\n";
    }
    return 0;
}
```
### JavaScript
```javascript
const readline = require("readline");
class Solution {
  articulationAndBcc(n, edges) {
    // Your implementation here
    return [[], []];
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
  const [aps, bccs] = solution.articulationAndBcc(n, edges);
  const out = [aps.length.toString(), aps.join(" "), bccs.length.toString()];
  for (const b of bccs) {
    out.push(``b.length`{b.join(" ")}`.trim());
  }
  console.log(out.join("\n").trim());
});
```
