---
problem_id: AGR_OFFLINE_LCA_WITH_MODS__9025
display_id: AGR-016
slug: offline-lca-with-mods
title: "Offline Lowest Common Ancestor with Modifications"
difficulty: Hard
difficulty_score: 72
topics:
  - Graphs
  - Trees
  - LCA
tags:
  - advanced-graphs
  - lca
  - offline
  - hard
premium: true
subscription_tier: basic
time_limit: 2000
memory_limit: 256
---
# AGR-016: Offline Lowest Common Ancestor with Modifications
## Problem Statement
You are given an initial tree on `n` nodes rooted at node `0`. Then you must process a sequence of operations:
- `cut u v`: remove the edge between `u` and `v`
- `link u v`: add an edge between `u` and `v`
- `query u v`: output the LCA of `u` and `v` in the current tree
If `u` and `v` are not connected, output `-1`.
All operations are valid, and the active edge set always forms a forest.
![Problem Illustration](../images/AGR-016/problem-illustration.png)
## Input Format
- First line: integer `n`
- Next `n-1` lines: `u v` edges of the initial tree
- Next line: integer `q`
- Next `q` lines: one of the operations above
## Output Format
- For each `query`, print the LCA value on its own line
## Constraints
- `1 <= n <= 200000`
- `1 <= q <= 200000`
- `0 <= u, v < n`
- Operations are valid and keep the active edges acyclic
## Example
**Input:**
```
4
0 1
1 2
1 3
4
query 2 3
cut 1 3
query 2 3
link 1 3
```
**Output:**
```
1
-1
```
**Explanation:**
Initially, LCA(2,3)=1. After removing edge (1,3), nodes 2 and 3 are disconnected.
![Example Visualization](../images/AGR-016/example-1.png)
## Notes
- Solve offline using a segment tree over time for edge activation intervals.
- Use DSU rollback for dynamic connectivity, and binary lifting for LCA in the base tree.
- Treat LCA as undefined if nodes are disconnected.
## Related Topics
LCA, DSU Rollback, Offline Queries
---
## Solution Template
### Java

```java
import java.util.*;

class Solution {
    public int[] offlineLca(int n, int[][] edges, String[] type, int[][] args) {
        //Implement here
        return new int[0];
    }
}

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
        int m = n - 1;
        int[][] edges = new int[m][2];
        for (int i = 0; i < m; i++) {
            edges[i][0] = sc.nextInt();
            edges[i][1] = sc.nextInt();
        }
        int q = sc.nextInt();
        String[] type = new String[q];
        int[][] queryArgs = new int[q][2];
        for (int i = 0; i < q; i++) {
            type[i] = sc.next();
            queryArgs[i][0] = sc.nextInt();
            queryArgs[i][1] = sc.nextInt();
        }

        Solution solution = new Solution();
        int[] results = solution.offlineLca(n, edges, type, queryArgs);

        for (int res : results) {
            System.out.println(res);
        }
        sc.close();
    }
}
```

### Python

```python
import sys

sys.setrecursionlimit(300000)

def offline_lca(n: int, edges: list[tuple[int, int]], ops: list[tuple[str, int, int]]) -> list[int]:
    # //Implement here
    return 0

def main():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return

    iterator = iter(data)
    try:
        n = int(next(iterator))
        edges = []
        for _ in range(n - 1):
            u = int(next(iterator))
            v = int(next(iterator))
            edges.append((u, v))

        q = int(next(iterator))
        ops = []
        for _ in range(q):
            t = next(iterator)
            u = int(next(iterator))
            v = int(next(iterator))
            ops.append((t, u, v))

        out = offline_lca(n, edges, ops)
        sys.stdout.write("\n".join(map(str, out)))
    except StopIteration:
        pass

if __name__ == "__main__":
    main()
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> offlineLca(int n, const vector<pair<int, int>>& edges, const vector<string>& type, const vector<pair<int, int>>& args) {
        //Implement here
        return {};
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    vector<pair<int, int>> edges(n - 1);
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    int q;
    cin >> q;
    vector<string> type(q);
    vector<pair<int, int>> args(q);
    for (int i = 0; i < q; i++) {
        cin >> type[i] >> args[i].first >> args[i].second;
    }

    Solution solution;
    vector<int> out = solution.offlineLca(n, edges, type, args);
    for (int i = 0; i < (int)out.size(); i++) {
        if (i) cout << "\n";
        cout << out[i];
    }
    return 0;
}
```

### JavaScript

```javascript
const readline = require("readline");

class Solution {
  offlineLca(n, edges, ops) {
    //Implement here
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
  const edges = [];
  for (let i = 0; i < n - 1; i++) {
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    edges.push([u, v]);
  }
  const q = parseInt(data[idx++], 10);
  const ops = [];
  for (let i = 0; i < q; i++) {
    const t = data[idx++];
    const u = parseInt(data[idx++], 10);
    const v = parseInt(data[idx++], 10);
    ops.push([t, u, v]);
  }

  const solution = new Solution();
  const out = solution.offlineLca(n, edges, ops);
  console.log(out.join("\n"));
});
```

